#!/usr/bin/env python3
"""
Generate odoo_records.pyi from Odoo database metadata.

Queries ir_model and ir_model_fields to create typed stub classes for Odoo models.
"""

import psycopg2
import re
import keyword
from typing import Dict, List, Tuple, Set
from collections import defaultdict


# Don't skip any models - generate stubs for all
ALREADY_TYPED = set()

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


def generate_class_stub(model_name: str, fields: List[Tuple[str, str, str]], typed_models: Set[str]) -> str:
    """Generate a Python class stub for a model."""
    class_name = model_to_class_name(model_name)

    lines = [f"# --- {model_name} ---\n"]
    lines.append(f"class {class_name}(Recordset):")

    if not fields:
        lines.append("    pass")
    else:
        # Field annotations
        for field_name, field_type, relation in fields:
            python_type = map_odoo_type_to_python(field_type, relation, typed_models)
            safe_field_name = sanitize_field_name(field_name)
            lines.append(f"    {safe_field_name}: {python_type}")

        # Standard methods
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

    lines.append("")
    return "\n".join(lines)


# Models that have hand-written extended classes — these override the auto-generated ones
EXTENDED_OVERRIDES: Dict[str, Tuple[str, str]] = {
    "helpdesk.ticket":       ("HelpdeskTicketExtended",     "helpdesk_ticket_extended"),
    "ir.config_parameter":   ("IrConfigParameterExtended",  "ir_config_param_extended"),
    "market.comm.event.log": ("MarketCommEventLogExtended", "market_comm_event_log_extended"),
}


def generate_odoo_environment(models: List[str]) -> str:
    """Generate odoo_environment.pyi with OdooEnvironment class and all __getitem__ overloads."""
    class_names = [model_to_class_name(m) for m in models]

    lines = [
        "# AUTO-GENERATED FILE - do not edit manually",
        "# Run lsp-server/generate_stubs.py to regenerate\n",
        "from typing import Any, Dict, List, Literal, Optional, overload",
        "from recordset import Recordset",
    ]

    # Import all generated _-prefixed classes
    import_names = sorted(class_names)
    # Chunk into groups of 6 for readability
    chunk_size = 6
    for i in range(0, len(import_names), chunk_size):
        chunk = import_names[i:i + chunk_size]
        lines.append(f"from odoo_records import {', '.join(chunk)}")

    # Import extended override classes
    lines.append("")
    for class_name, module in EXTENDED_OVERRIDES.values():
        lines.append(f"from {module} import {class_name}")

    lines.append("\n\nclass OdooEnvironment:")
    lines.append("    cr: Any")
    lines.append("    uid: int")
    lines.append("    context: Dict[str, Any]")

    # Extended overrides first (higher priority)
    for model, (class_name, _) in EXTENDED_OVERRIDES.items():
        if len(model) > 30:
            lines.append(f"    @overload")
            lines.append(f"    def __getitem__(")
            lines.append(f"        self, model_name: Literal[\"{model}\"]")
            lines.append(f"    ) -> {class_name}: ...")
        else:
            lines.append(f"    @overload")
            lines.append(f"    def __getitem__(self, model_name: Literal[\"{model}\"]) -> {class_name}: ...")

    # Auto-generated overloads for all models
    for model, class_name in zip(models, class_names):
        if model in EXTENDED_OVERRIDES:
            continue
        if len(model) > 30:
            lines.append(f"    @overload")
            lines.append(f"    def __getitem__(")
            lines.append(f"        self, model_name: Literal[\"{model}\"]")
            lines.append(f"    ) -> {class_name}: ...")
        else:
            lines.append(f"    @overload")
            lines.append(f"    def __getitem__(self, model_name: Literal[\"{model}\"]) -> {class_name}: ...")

    lines.append("    @overload")
    lines.append("    def __getitem__(self, model_name: str) -> Recordset: ...")
    lines.append("    def sudo(self) -> \"OdooEnvironment\": ...")
    lines.append("    def ref(self, xml_id: str) -> Recordset: ...")

    return "\n".join(lines)


def main():
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
        "from recordset import Recordset\n",
    ]

    # Generate classes for each model
    for model in sorted(models_to_process):
        fields = get_model_fields(conn, model)
        output_lines.append(generate_class_stub(model, fields, typed_models))

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
