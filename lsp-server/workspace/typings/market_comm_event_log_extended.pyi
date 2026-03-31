from odoo_records import _MarketCommEventLog
from typing import Any

class MarketCommEventLogExtended(_MarketCommEventLog):
    def last(
        self, flow_code: Any = None, service_code: Any = None
    ) -> MarketCommEventLogExtended: ...
