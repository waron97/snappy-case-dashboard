from odoo_records import MarketCommEventLog
from typing import Any

class MarketCommEventLogExtended(MarketCommEventLog):
    def last(
        self, flow_code: Any = None, service_code: Any = None
    ) -> MarketCommEventLogExtended: ...
