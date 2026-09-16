"""Auto-imported by Python at interpreter startup (standard `sitecustomize` behavior) when
this directory is on PYTHONPATH. instances.py injects it into the odoo-bin subprocess's
environment ONLY when request tracing is enabled for the current attach — never for the
control Flask process, workers, or any other python invocation in this image.

Installs OpenTelemetry tracing around the Odoo ORM method(s) named in ODOO_PROFILE_METHODS
(default: "read"), PLUS a per-field span for every computed field evaluated along the way
(ODOO_PROFILE_COMPUTES, default on — see _wrap_compute_field_value), plus automatic SQL and
outbound-HTTP instrumentation. A model with many compute fields (e.g. helpdesk.ticket) is
exactly the case this per-field breakdown is for: without it, a slow read() shows one opaque
duration with no indication of which compute is actually responsible.

Every span also carries an `odoo.caller` attribute (file:line:function of whoever called it)
— nested wrapped calls already show their trigger via the trace's own parent/child spans, but
each independently-triggered top-level call (no wrapped parent active — e.g. whatever a page
load fires directly) otherwise gives no indication of what Python code asked for it. When the
caller is inside Odoo's own fields.py, the responsible field's technical name is appended too
(`self` there is the Field descriptor, not a recordset) — this is how a slow relational field
read (e.g. a One2many's own internal search()) gets identified without reading fields.py.

Deliberately hooked at the ORM level (odoo.models.BaseModel), not at a specific transport:
the web client's own /web/dataset/call_kw route and external XML-RPC/JSON-RPC calls
(/xmlrpc/2/object, /jsonrpc) both end up calling the same recordset method underneath, so
one hook here catches a slow read() regardless of which of those actually triggered it —
including the "load a form in the browser" case this was built to diagnose.

Every failure here is caught and logged rather than raised: a bug in this module must never
prevent odoo-bin from starting or break a real request.
"""

import logging
import os

log = logging.getLogger("odoo.profiling")

_ENABLED = os.environ.get("ODOO_PROFILE_ENABLED") == "1"


def _install():
    import functools
    import sys

    from opentelemetry import trace
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor
    from opentelemetry.instrumentation.requests import RequestsInstrumentor
    from opentelemetry.instrumentation.urllib3 import URLLib3Instrumentor
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor

    otlp_endpoint = os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT", "http://jaeger:4318")
    provider = TracerProvider(resource=Resource.create({"service.name": "odoo-dev-instance"}))
    # Batched, not synchronous-per-span: "every method" mode below can wrap dozens of
    # methods, some called very frequently, and a per-span blocking HTTP POST to Jaeger
    # would make the instrumentation itself the bottleneck. A short schedule delay keeps it
    # feeling close to live for interactive debugging without that per-call cost.
    provider.add_span_processor(
        BatchSpanProcessor(OTLPSpanExporter(endpoint=f"{otlp_endpoint}/v1/traces"), schedule_delay_millis=1000)
    )
    trace.set_tracer_provider(provider)

    # Auto-spans every SQL query (with statement text + duration) and every outbound HTTP
    # call, nested under whichever ORM span below is active — the two most common places a
    # slow read() is actually spending its time.
    Psycopg2Instrumentor().instrument()
    RequestsInstrumentor().instrument()
    URLLib3Instrumentor().instrument()

    tracer = trace.get_tracer("odoo.orm")
    target_model = os.environ.get("ODOO_PROFILE_MODEL", "")
    methods_raw = os.environ.get("ODOO_PROFILE_METHODS", "read")

    def _format_caller(depth=4):
        # Each independently-triggered call (no wrapped parent span active — e.g. the
        # top-level call a page load fires) otherwise gives no indication of what Python
        # code asked for it. sys._getframe(2): frame 0 is this function, frame 1 is the
        # `wrapped()` closure that calls it, frame 2 is wrapped()'s own caller — the actual
        # call site we want. Cheap (fixed small walk, not a full stack capture), safe to run
        # on every wrapped call including in "every method" mode.
        frame = sys._getframe(2)
        parts = []
        for _ in range(depth):
            if frame is None:
                break
            co = frame.f_code
            label = f"{co.co_filename.rsplit('/', 1)[-1]}:{frame.f_lineno}:{co.co_name}"
            # Inside Odoo's own fields.py, `self` in virtually every method (read, compute,
            # convert_to_*, ...) is the Field descriptor itself, not a recordset — surfacing
            # its technical name turns "some relational field read is slow" from something
            # you'd have to go grep fields.py's source to understand into something visible
            # directly on the span (this is exactly how symphony_case_ids on helpdesk.ticket
            # was identified as the field behind a slow orm.symphony.case.id.search).
            if co.co_filename.endswith("/fields.py"):
                field_name = getattr(frame.f_locals.get("self"), "name", None)
                if field_name:
                    label += f"[field={field_name}]"
            parts.append(label)
            frame = frame.f_back
        return " < ".join(parts)

    # Pure recordset algebra / context-shifting helpers: no I/O of their own, but called an
    # enormous number of times per request (often per-record, in loops) — tracing these adds
    # only noise and per-call overhead, so "every method" mode below skips them regardless of
    # how many other methods it wraps.
    _NO_IO_METHODS = {
        "browse", "new", "sudo", "with_context", "with_env", "with_user", "with_company",
        "with_prefetch", "ensure_one", "exists", "filtered", "filtered_domain", "mapped",
        "sorted", "union", "concat", "get_base_url",
    }

    def _resolve_target_methods(odoo_models):
        explicit = {m.strip() for m in methods_raw.split(",") if m.strip()}
        if explicit:
            return explicit
        # Blank ODOO_PROFILE_METHODS = every public BaseModel method that can plausibly
        # touch the DB or do real work (everything except the zero-IO helpers above).
        return {
            name for name, value in vars(odoo_models.BaseModel).items()
            if callable(value) and not name.startswith("_") and name not in _NO_IO_METHODS
        }

    def _patch_orm(odoo_models):
        target_methods = _resolve_target_methods(odoo_models)

        def _wrap(method_name):
            original = getattr(odoo_models.BaseModel, method_name, None)
            if original is None:
                log.warning("ODOO_PROFILE_METHODS: BaseModel has no method %r, skipping", method_name)
                return

            @functools.wraps(original)
            def wrapped(self, *args, **kwargs):
                if target_model and self._name != target_model:
                    return original(self, *args, **kwargs)
                with tracer.start_as_current_span(
                    f"orm.{self._name}.{method_name}",
                    attributes={
                        "odoo.model": self._name,
                        "odoo.method": method_name,
                        "odoo.record_count": len(self),
                        "odoo.caller": _format_caller(),
                    },
                ):
                    return original(self, *args, **kwargs)

            # functools.wraps copies original.__dict__ onto wrapped, which matters here far
            # beyond cosmetics: Odoo's own call_kw dispatch (odoo/api.py) decides whether to
            # pass a leading `ids` argument by checking method._api == 'model' — an attribute
            # @api.model sets directly on the function object. Without carrying that over, a
            # wrapped @api.model method (e.g. default_get, search, fields_get) gets
            # mis-dispatched as if it expected ids, raising IndexError on the now-shifted
            # argument list. This bit us for real in "every method" mode.
            setattr(odoo_models.BaseModel, method_name, wrapped)

        for name in target_methods:
            _wrap(name)

        computes_traced = False
        if os.environ.get("ODOO_PROFILE_COMPUTES", "1") == "1":
            computes_traced = _wrap_compute_field_value(odoo_models)

        log.info(
            "odoo request tracing enabled -> %s (model=%r methods=%r computes=%r)",
            otlp_endpoint, target_model or "*", sorted(target_methods), computes_traced,
        )

    def _wrap_compute_field_value(odoo_models):
        # Odoo's single universal dispatch point for computing ANY field's value on ANY
        # model, stored or not (see fields.determine(field.compute, self) inside it) — the
        # per-model _compute_<field> methods themselves live on each addon's own model
        # class, never on BaseModel, so there's no way to reach them generically except via
        # this one choke point they all funnel through. This is what actually answers "which
        # of helpdesk.ticket's many compute fields is slow", which wrapping only the public
        # CRUD methods above cannot show — those just see one opaque read() duration with no
        # breakdown of the compute work that happened inside it.
        original = getattr(odoo_models.BaseModel, "_compute_field_value", None)
        if original is None:
            log.warning("BaseModel has no _compute_field_value; compute-field tracing unavailable")
            return False

        @functools.wraps(original)
        def wrapped(self, field):
            if target_model and self._name != target_model:
                return original(self, field)
            with tracer.start_as_current_span(
                f"compute.{self._name}.{field.name}",
                attributes={
                    "odoo.model": self._name,
                    "odoo.field": field.name,
                    "odoo.field.stored": bool(field.store),
                    "odoo.record_count": len(self),
                    "odoo.caller": _format_caller(),
                },
            ):
                return original(self, field)

        odoo_models.BaseModel._compute_field_value = wrapped
        return True

    # `odoo` isn't importable yet at sitecustomize time: it runs during interpreter startup
    # (site initialization), before odoo-bin's own script body has done whatever sys.path
    # setup makes the `odoo` package importable in this image (it isn't a normally
    # pip-installed package here) — `import odoo.models` right here would just raise
    # ModuleNotFoundError. Instead, hook __import__ once and apply the patch the moment
    # odoo.models genuinely gets imported by Odoo's own startup, then remove the hook.
    import builtins
    import threading

    _patch_lock = threading.Lock()
    original_import = builtins.__import__

    def _import_hook(name, *args, **kwargs):
        module = original_import(name, *args, **kwargs)
        odoo_models = sys.modules.get("odoo.models")
        # Check for the BaseModel attribute itself, not just module presence: sys.modules
        # gets an entry for "odoo.models" as soon as its execution *starts* (Python's normal
        # partial-module-during-circular-import behavior), which can be before BaseModel is
        # actually defined in it — patching too early would AttributeError and, since the
        # hook removes itself unconditionally below, never get a second chance.
        if odoo_models is not None and getattr(odoo_models, "BaseModel", None) is not None:
            with _patch_lock:
                if builtins.__import__ is _import_hook:
                    builtins.__import__ = original_import
                    try:
                        _patch_orm(odoo_models)
                    except Exception:
                        log.exception("failed to patch odoo.models.BaseModel; continuing unprofiled")
        return module

    builtins.__import__ = _import_hook


if _ENABLED:
    try:
        _install()
    except Exception:
        log.exception("failed to install odoo request tracing; continuing unprofiled")
