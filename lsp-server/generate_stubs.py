#!/usr/bin/env python3
"""
Generate odoo_records.pyi from Odoo database metadata + Odoo runtime method signatures.

Queries ir_model and ir_model_fields for fields, then bootstraps the Odoo registry
to extract real Python method signatures via inspect.
"""

import sys
import inspect
import psycopg2
import keyword
from typing import Dict, List, Tuple, Set

ODOO_BASE_PATH = "/home/aron/codebase/odoo/15/base"
ODOO_CONF = "/home/aron/codebase/sorgenia/config/odoo.conf"
ODOO_DB = "sorgenia"


# Don't skip any models - generate stubs for all
ALREADY_TYPED = set()

# Override return types for specific (model_name, method_name) pairs.
# Value is the return type annotation string (used verbatim in the stub).
# Use this for methods that return non-Odoo types (e.g. b2w entity wrappers)
# or whose auto-inferred return type (Any / ...) should be more specific.
OVERRIDES: Dict[Tuple[str, str], str] = {
    ("helpdesk.ticket", "kv_store"): '"_SymplePbProcessData"',
    ("service.point", "assets"): "List[Asset]",
    ("service.point", "asset"): "Optional[Asset]",
    ("service.point", "last_order_item"): "Optional[OrderItem]",
    ("res.partner", "assets"): "List[Asset]",
    ("res.partner", "contracts"): "List[Contract]",
}

# Standard models that scripts commonly use (add if referenced)
STANDARD_MODELS_ALLOW_LIST = {
    "sale.order",
    "sale.order.line",
    "account.move",
    "account.move.line",
    "crm.lead",
    "res.users",
    "product.template",
    "product.product",
    "res.country",
    "res.country.state",
    "mail.message",
    "ir.attachment",
}


def connect_db():
    """Connect to Odoo database."""
    return psycopg2.connect(
        host="localhost",
        port=5433,
        database="sorgenia",
        user="odoo",
        password="odoo"
    )


def model_to_class_name(model_name: str) -> str:
    """Convert model name like 'sorgenia.contracts' to class name '_SorgeniaContracts'."""
    base = "".join(word.capitalize() for word in model_name.replace(".", "_").split("_"))
    return f"_{base}"


def sanitize_field_name(field_name: str) -> str:
    """Escape Python keywords used as field names."""
    if keyword.iskeyword(field_name):
        return f"{field_name}_"
    return field_name


def get_all_models(conn) -> List[str]:
    """Get all models from database."""
    cur = conn.cursor()
    cur.execute("""
        SELECT model FROM ir_model
        ORDER BY model
    """)
    return [row[0] for row in cur.fetchall()]


def get_model_fields(conn, model_name: str) -> List[Tuple[str, str, str]]:
    """
    Get fields for a model. Returns list of (field_name, field_type, relation).
    Skips system fields.
    """
    cur = conn.cursor()
    cur.execute("""
        SELECT f.name, f.ttype, f.relation
        FROM ir_model_fields f
        JOIN ir_model m ON m.id = f.model_id
        WHERE m.model = %s
        AND f.name NOT IN ('id', 'create_uid', 'write_uid', 'create_date', 'write_date', '__last_update', 'display_name')
        ORDER BY f.name
    """, (model_name,))
    return [(row[0], row[1], row[2] or "") for row in cur.fetchall()]


def map_odoo_type_to_python(field_type: str, relation: str, typed_models: Set[str]) -> str:
    """Map Odoo field type to Python type annotation."""
    if field_type in ("char", "text", "selection", "html", "serialized"):
        return "str"
    elif field_type == "boolean":
        return "bool"
    elif field_type == "integer":
        return "int"
    elif field_type in ("float", "monetary"):
        return "float"
    elif field_type == "date":
        return "Optional[_dt.date]"
    elif field_type == "datetime":
        return "Optional[_dt.datetime]"
    elif field_type == "binary":
        return "bytes"
    elif field_type == "many2one":
        # If the related model is typed, use its class name
        if relation and relation in typed_models:
            class_name = model_to_class_name(relation)
            return f'"{class_name}"'
        return "Recordset"
    elif field_type in ("one2many", "many2many"):
        # Relations - use typed class if available
        if relation and relation in typed_models:
            class_name = model_to_class_name(relation)
            return f'"{class_name}"'
        return "Recordset"
    else:
        # Unknown type, use Any
        return "Any"


def _safe_default_str(value) -> str:
    """Return a stub-safe string representation of a default value."""
    if value is None:
        return "None"
    if isinstance(value, bool):
        return repr(value)
    if isinstance(value, (int, float, str)):
        return repr(value)
    if isinstance(value, (list, dict, tuple)) and not value:
        return repr(value)
    if isinstance(value, type):
        return value.__name__
    return "..."


def sanitize_sig(sig) -> str:
    """Build a stub-safe signature string, replacing complex defaults with ..."""
    parts = []
    for name, param in sig.parameters.items():
        if param.kind == inspect.Parameter.VAR_POSITIONAL:
            parts.append(f"*{name}")
        elif param.kind == inspect.Parameter.VAR_KEYWORD:
            parts.append(f"**{name}")
        elif param.default is inspect.Parameter.empty:
            parts.append(name)
        else:
            parts.append(f"{name}={_safe_default_str(param.default)}")
    return f"({', '.join(parts)})"


def get_model_methods(model_class, skip: Set[str], model_name: str) -> List[Tuple[str, str]]:
    """Return [(method_name, signature_str)] for methods defined directly on model_class.

    Only includes methods whose defining class has _name == model_name, which
    excludes inherited mixin methods (mail.thread, web.grid, bit2publish, etc.)
    while keeping methods added by the model's own modules.
    """
    results = []
    for name, obj in inspect.getmembers(model_class, predicate=inspect.isroutine):
        if name.startswith("__"):
            continue
        if name in skip:
            continue
        # Walk MRO to find the class that first defines this method
        for cls in model_class.__mro__:
            if name in cls.__dict__:
                # Only keep if defined by a class that "owns" this model
                if getattr(cls, '_name', None) == model_name:
                    try:
                        sig = sanitize_sig(inspect.signature(obj))
                    except (ValueError, TypeError):
                        sig = "(self, *args, **kwargs)"
                    results.append((name, sig))
                break
    return results


def generate_class_stub(
    model_name: str,
    fields: List[Tuple[str, str, str]],
    typed_models: Set[str],
    methods: List[Tuple[str, str]] = [],
) -> str:
    """Generate a Python class stub for a model."""
    class_name = model_to_class_name(model_name)

    lines = [f"# --- {model_name} ---\n"]
    lines.append(f"class {class_name}(Recordset):")

    if not fields and not methods:
        lines.append("    pass")
    else:
        # Field annotations
        for field_name, field_type, relation in fields:
            python_type = map_odoo_type_to_python(field_type, relation, typed_models)
            safe_field_name = sanitize_field_name(field_name)
            lines.append(f"    {safe_field_name}: {python_type}")

        # Standard methods (self-typed returns)
        lines.append(f"    def browse(self, ids: Union[int, List[int]]) -> \"{class_name}\": ...")
        lines.append(f"    def search(")
        lines.append(f"        self,")
        lines.append(f"        domain: List[Any],")
        lines.append(f"        limit: Optional[int] = None,")
        lines.append(f"        order: Optional[str] = None,")
        lines.append(f"        offset: int = 0,")
        lines.append(f"    ) -> \"{class_name}\": ...")
        lines.append(f"    def create(self, vals: Dict[str, Any]) -> \"{class_name}\": ...")
        lines.append(f"    def filtered(self, func: Any) -> \"{class_name}\": ...")
        lines.append(f"    def sorted(self, key: Any = None, reverse: bool = False) -> \"{class_name}\": ...")
        lines.append(f"    def exists(self) -> \"{class_name}\": ...")
        lines.append(f"    def sudo(self) -> \"{class_name}\": ...")
        lines.append(f"    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> \"{class_name}\": ...")

        # Custom business methods extracted from Odoo registry
        for method_name, sig in methods:
            override_return = OVERRIDES.get((model_name, method_name))
            if override_return:
                lines.append(f"    def {method_name}{sig} -> {override_return}: ...")
            else:
                lines.append(f"    def {method_name}{sig}: ...")

    lines.append("")
    return "\n".join(lines)


# Frequently used models — their __getitem__ overloads appear first in OdooEnvironment
# so LSP resolves them faster. Ordered by usage frequency across agrippa-workflows.
PRIORITY_MODELS = [
    "ir.config_parameter",
    "symple.pb.process.data",
    "service.point",
    "helpdesk.ticket",
    "res.partner",
    "billing.profile",
    "helpdesk.ticket.type",
    "payment.method",
    "case.integration.history",
    "symple.pb.launcher",
    "res.toponym",
    "res.city",
    "symple.interaction",
    "res.country.state",
    "res.partner.pod",
    "automatic.insurance.service",
    "symple.triplet.phase",
    "res.partner.pdr",
    "symple.triplet.phase.result",
    "market.comm.event.log",
    "ir.sequence",
    "charge.dispatch",
    "payment.term",
    "result.type",
    "party.relation",
]


def generate_odoo_environment(models: List[str]) -> str:
    """Generate odoo_environment.pyi with OdooEnvironment class and all __getitem__ overloads."""
    class_names = [model_to_class_name(m) for m in models]
    model_to_class = dict(zip(models, class_names))

    lines = [
        "# AUTO-GENERATED FILE - do not edit manually",
        "# Run lsp-server/generate_stubs.py to regenerate\n",
        "from typing import Any, Dict, List, Literal, Optional, overload",
        "from recordset import Recordset",
    ]

    # Import all generated _-prefixed classes
    import_names = sorted(class_names)
    chunk_size = 6
    for i in range(0, len(import_names), chunk_size):
        chunk = import_names[i:i + chunk_size]
        lines.append(f"from odoo_records import {', '.join(chunk)}")

    lines.append("\n\nclass OdooEnvironment:")
    lines.append("    cr: Any")
    lines.append("    uid: int")
    lines.append("    context: Dict[str, Any]")

    def emit_overload(model: str, class_name: str) -> None:
        if len(model) > 30:
            lines.append(f"    @overload")
            lines.append(f"    def __getitem__(")
            lines.append(f"        self, model_name: Literal[\"{model}\"]")
            lines.append(f"    ) -> {class_name}: ...")
        else:
            lines.append(f"    @overload")
            lines.append(f"    def __getitem__(self, model_name: Literal[\"{model}\"]) -> {class_name}: ...")

    # Priority models first
    for model in PRIORITY_MODELS:
        if model in model_to_class:
            emit_overload(model, model_to_class[model])

    # Remaining models in alphabetical order
    priority_set = set(PRIORITY_MODELS)
    for model, class_name in zip(models, class_names):
        if model not in priority_set:
            emit_overload(model, class_name)

    lines.append("    @overload")
    lines.append("    def __getitem__(self, model_name: str) -> Recordset: ...")
    lines.append("    def sudo(self) -> \"OdooEnvironment\": ...")
    lines.append("    def ref(self, xml_id: str) -> Recordset: ...")

    return "\n".join(lines)


def main():
    # Bootstrap Odoo registry for method signature extraction
    print("Bootstrapping Odoo registry...")
    sys.path.insert(0, ODOO_BASE_PATH)
    import odoo
    odoo.tools.config.parse_config(["-c", ODOO_CONF, "-d", ODOO_DB])
    registry = odoo.registry(ODOO_DB)

    # Build the set of methods to skip: BaseModel ORM internals + already-stubbed methods
    base_skip: Set[str] = set(
        name for name, _ in inspect.getmembers(odoo.models.BaseModel, predicate=inspect.isroutine)
    )
    base_skip |= {"browse", "search", "create", "filtered", "sorted", "exists", "sudo", "with_context"}

    conn = connect_db()

    # Get all models
    all_models = get_all_models(conn)
    print(f"Found {len(all_models)} total models in database")

    # Type all models
    models_to_process = all_models
    typed_models = set(all_models)

    print(f"Will type {len(models_to_process)} models")

    # Generate stub file
    output_lines = [
        "# AUTO-GENERATED FILE - do not edit manually",
        "# Run lsp-server/generate_stubs.py to regenerate\n",
        "from typing import Any, Dict, List, Optional, Union, Literal",
        "import datetime as _dt",
        "from recordset import Recordset",
        "from b2w_entities import Asset, Contract, Order, OrderItem, Task\n",
    ]

    # Generate classes for each model
    with registry.cursor() as cr:
        env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})
        for model in sorted(models_to_process):
            fields = get_model_fields(conn, model)

            model_class = env.registry.get(model)
            if model_class is not None:
                methods: List[Tuple[str, str]] = get_model_methods(model_class, base_skip, model)
            else:
                methods = []

            output_lines.append(generate_class_stub(model, fields, typed_models, methods))

    # Write odoo_records.pyi
    stub_content = "\n".join(output_lines)
    with open("workspace/typings/odoo_records.pyi", "w") as f:
        f.write(stub_content)

    print(f"\nWrote workspace/typings/odoo_records.pyi")

    # Generate odoo_environment.pyi with OdooEnvironment class and all overloads
    env_content = generate_odoo_environment(sorted(models_to_process))
    with open("workspace/typings/odoo_environment.pyi", "w") as f:
        f.write(env_content)

    print(f"Wrote workspace/typings/odoo_environment.pyi")

    conn.close()
    print("\nDone!")


if __name__ == "__main__":
    main()
