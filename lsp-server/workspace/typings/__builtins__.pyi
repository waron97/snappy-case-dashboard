from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Literal,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)
import logging
import datetime as _dt

from recordset import Recordset
from odoo_records import *
from helpdesk_ticket_extended import HelpdeskTicketExtended
from ir_config_param_extended import IrConfigParameterExtended

# --- KV Store ---

class KvStore:
    def get(self, key: str) -> Any: ...
    def set(self, key: str, value: Any) -> None: ...
    def get_many(self, *keys: str) -> Tuple[Any, ...]: ...
    def set_many(self, values: Dict[str, Any]) -> None: ...

# --- Process Data ---

class ProcessData:
    payload: str
    process_name: str
    res_id: int
    def get_payload(self) -> Any: ...

# --- Cursor ---

class Cursor:
    def execute(self, query: str, params: Any = None) -> None: ...
    def fetchone(self) -> Optional[Tuple[Any, ...]]: ...
    def fetchall(self) -> List[Tuple[Any, ...]]: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...

# --- Odoo Environment ---

class OdooEnvironment:
    cr: Cursor
    uid: int
    context: Dict[str, Any]
    @overload
    def __getitem__(
        self, model_name: Literal["helpdesk.ticket"]
    ) -> HelpdeskTicketExtended: ...
    @overload
    def __getitem__(self, model_name: Literal["res.partner"]) -> ResPartner: ...
    @overload
    def __getitem__(self, model_name: Literal["res.partner.pod"]) -> ResPartnerPod: ...
    @overload
    def __getitem__(self, model_name: Literal["res.partner.pdr"]) -> ResPartnerPdr: ...
    @overload
    def __getitem__(self, model_name: Literal["service.point"]) -> ServicePoint: ...
    @overload
    def __getitem__(self, model_name: Literal["symple.workflow"]) -> SympleWorkflow: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.triplet.type"]
    ) -> SympleTripletType: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.triplet.subtype"]
    ) -> SympleTripletSubtype: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.triplet.phase"]
    ) -> SympleTripletPhase: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.triplet.phase.result"]
    ) -> SympleTripletPhaseResult: ...
    @overload
    def __getitem__(
        self, model_name: Literal["helpdesk.ticket.type"]
    ) -> HelpdeskTicketType: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.pb.process.data"]
    ) -> SymplePbProcessData: ...
    @overload
    def __getitem__(
        self, model_name: Literal["market.comm.event.log"]
    ) -> MarketCommEventLog: ...
    @overload
    def __getitem__(
        self, model_name: Literal["case.integration.history"]
    ) -> CaseIntegrationHistory: ...
    @overload
    def __getitem__(
        self, model_name: Literal["ir.config_parameter"]
    ) -> IrConfigParameterExtended: ...
    @overload
    def __getitem__(self, model_name: Literal["ir.attachment"]) -> IrAttachment: ...
    @overload
    def __getitem__(self, model_name: Literal["mail.message"]) -> MailMessage: ...
    @overload
    def __getitem__(self, model_name: Literal["res.country"]) -> ResCountry: ...
    @overload
    def __getitem__(
        self, model_name: Literal["res.country.state"]
    ) -> ResCountryState: ...
    @overload
    def __getitem__(self, model_name: Literal["res.users"]) -> ResUsers: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.contracts"]
    ) -> SorgeniaContracts: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.digital.login"]
    ) -> SorgeniaDigitalLogin: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.digital.login.partner"]
    ) -> SorgeniaDigitalLoginPartner: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.invoice.external.service.ftp.pdf.queue"]
    ) -> SorgeniaInvoiceExternalServiceFtpPdfQueue: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.invoice.external.service.ftp.server"]
    ) -> SorgeniaInvoiceExternalServiceFtpServer: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.loyalty.external.service.ftp.server"]
    ) -> SorgeniaLoyaltyExternalServiceFtpServer: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.mdm.gdpr"]
    ) -> SorgeniaMdmGdpr: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.postalizer.document"]
    ) -> SorgeniaPostalizerDocument: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.question.input"]
    ) -> SorgeniaQuestionInput: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.response.input"]
    ) -> SorgeniaResponseInput: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.sms.ftp.server"]
    ) -> SorgeniaSmsFtpServer: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.survey.input"]
    ) -> SorgeniaSurveyInput: ...
    @overload
    def __getitem__(self, model_name: Literal["sorgenia.tisg"]) -> SorgeniaTisg: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.tisg.line"]
    ) -> SorgeniaTisgLine: ...
    @overload
    def __getitem__(self, model_name: Literal["sorgenia.upsa"]) -> SorgeniaUpsa: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.upsa.line"]
    ) -> SorgeniaUpsaLine: ...
    @overload
    def __getitem__(
        self, model_name: Literal["sorgenia.warranty"]
    ) -> SorgeniaWarranty: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.ai.automation"]
    ) -> SympleAiAutomation: ...
    @overload
    def __getitem__(self, model_name: Literal["symple.ai.tag"]) -> SympleAiTag: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.ai.tag.confidence"]
    ) -> SympleAiTagConfidence: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.ai.tag.confidence.history"]
    ) -> SympleAiTagConfidenceHistory: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.ai.tag.mixin"]
    ) -> SympleAiTagMixin: ...
    @overload
    def __getitem__(self, model_name: Literal["symple.cluster"]) -> SympleCluster: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.dms.folder"]
    ) -> SympleDmsFolder: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.dms.server"]
    ) -> SympleDmsServer: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.dms.token"]
    ) -> SympleDmsToken: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.importer.import.case"]
    ) -> SympleImporterImportCase: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.importer.line"]
    ) -> SympleImporterLine: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.inbound.message.registry"]
    ) -> SympleInboundMessageRegistry: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.interaction"]
    ) -> SympleInteraction: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.interaction.cancel.reason"]
    ) -> SympleInteractionCancelReason: ...
    @overload
    def __getitem__(self, model_name: Literal["symple.mail"]) -> SympleMail: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.mail.import.mail.mail"]
    ) -> SympleMailImportMailMail: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.mail.report"]
    ) -> SympleMailReport: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.message.registry"]
    ) -> SympleMessageRegistry: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.message.registry.mixin"]
    ) -> SympleMessageRegistryMixin: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.outbound.message.registry"]
    ) -> SympleOutboundMessageRegistry: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.pb.instance.key"]
    ) -> SymplePbInstanceKey: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.pb.instance.key.mixin"]
    ) -> SymplePbInstanceKeyMixin: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.pb.launcher"]
    ) -> SymplePbLauncher: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.pb.process"]
    ) -> SymplePbProcess: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.pb.process.element"]
    ) -> SymplePbProcessElement: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.pb.summary.launcher"]
    ) -> SymplePbSummaryLauncher: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.pb.webcomponent"]
    ) -> SymplePbWebcomponent: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.pb.webcomponent.event"]
    ) -> SymplePbWebcomponentEvent: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.pdf.utils"]
    ) -> SymplePdfUtils: ...
    @overload
    def __getitem__(self, model_name: Literal["symple.rcu"]) -> SympleRcu: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.cancel.case.wizard"]
    ) -> SympleRcuCancelCaseWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.check.work.wizard"]
    ) -> SympleRcuCheckWorkWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.commodity.operation"]
    ) -> SympleRcuCommodityOperation: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.create.case.wizard"]
    ) -> SympleRcuCreateCaseWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.force_resolved.wizard"]
    ) -> SympleRcuForceResolvedWizard: ...
    @overload
    def __getitem__(self, model_name: Literal["symple.rcu.line"]) -> SympleRcuLine: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.massive.procedure.result.fc.vat.wizard"]
    ) -> SympleRcuMassiveProcedureResultFcVatWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.massive.procedure.wizard"]
    ) -> SympleRcuMassiveProcedureWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.operation"]
    ) -> SympleRcuOperation: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.operation.type"]
    ) -> SympleRcuOperationType: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.operation.type.code"]
    ) -> SympleRcuOperationTypeCode: ...
    @overload
    def __getitem__(self, model_name: Literal["symple.rcu.pmax"]) -> SympleRcuPmax: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.refresh_deactivation.wizard"]
    ) -> SympleRcuRefreshDeactivationWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.resolved.ok.wizard"]
    ) -> SympleRcuResolvedOkWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.resolved.work.wizard"]
    ) -> SympleRcuResolvedWorkWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.sending.resolved.wizard"]
    ) -> SympleRcuSendingResolvedWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.sending.work.wizard"]
    ) -> SympleRcuSendingWorkWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.show_error_message.case.wizard"]
    ) -> SympleRcuShowErrorMessageCaseWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.work.check.wizard"]
    ) -> SympleRcuWorkCheckWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.rcu.work.sending.wizard"]
    ) -> SympleRcuWorkSendingWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.ax"]
    ) -> SympleRefunderAx: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.ax.line"]
    ) -> SympleRefunderAxLine: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.doxee"]
    ) -> SympleRefunderDoxee: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.doxee.line"]
    ) -> SympleRefunderDoxeeLine: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.import.wizard"]
    ) -> SympleRefunderImportWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.line"]
    ) -> SympleRefunderLine: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.line.mixin"]
    ) -> SympleRefunderLineMixin: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.mixin"]
    ) -> SympleRefunderMixin: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.process.wizard"]
    ) -> SympleRefunderProcessWizard: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.result"]
    ) -> SympleRefunderResult: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.update"]
    ) -> SympleRefunderUpdate: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.refunder.update.line"]
    ) -> SympleRefunderUpdateLine: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.slideout.menu"]
    ) -> SympleSlideoutMenu: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.triplet.phase.history"]
    ) -> SympleTripletPhaseHistory: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.triplet.phase.type"]
    ) -> SympleTripletPhaseType: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.triplet.unsuccess.reason"]
    ) -> SympleTripletUnsuccessReason: ...
    @overload
    def __getitem__(
        self, model_name: Literal["symple.triplet_type"]
    ) -> SympleTripletType: ...
    @overload
    def __getitem__(self, model_name: str) -> Recordset: ...
    def sudo(self) -> "OdooEnvironment": ...
    def ref(self, xml_id: str) -> Recordset: ...

# --- HTTP Response (returned by request()) ---

class Response:
    status_code: int
    text: str
    content: bytes
    headers: Dict[str, str]
    ok: bool
    def json(self) -> Any: ...
    def raise_for_status(self) -> None: ...

# --- Globals ---

case_id: HelpdeskTicketExtended
env: OdooEnvironment
body: Dict[str, Any]
args: List[Any]
model: Recordset
logger: logging.Logger

# --- Functions ---

def log(
    message: Any, level: Literal["debug", "info", "warning", "error"] = ...
) -> None: ...
def json_dumps(
    obj: Any,
    *,
    indent: Optional[int] = None,
    sort_keys: bool = False,
    default: Any = None,
    ensure_ascii: bool = True,
) -> str: ...
def json_loads(s: str) -> Any: ...
def make_response(
    status: Tuple[int, int],
    message: Union[str, Dict[str, Any]],
) -> Any: ...
def request(
    method: str,
    url: str,
    *,
    headers: Optional[Dict[str, str]] = None,
    data: Optional[Union[str, bytes]] = None,
    json: Optional[Any] = None,
    params: Optional[Dict[str, Any]] = None,
    timeout: Optional[float] = None,
) -> Response: ...

FirstArg = TypeVar("FirstArg")

def first(recordset: FirstArg) -> FirstArg: ...
def format_exc() -> str: ...

# --- Exceptions ---

class ValidationError(Exception): ...

# --- Datetime types (injected as the datetime module, not bare classes) ---

class _DatetimeModule:
    datetime: Type[_dt.datetime]
    date: Type[_dt.date]
    time: Type[_dt.time]
    timezone: Type[_dt.timezone]
    timedelta: Type[_dt.timedelta]
    MINYEAR: int
    MAXYEAR: int

datetime: _DatetimeModule
date: Type[_dt.date]
time: Type[_dt.time]
timezone: Type[_dt.timezone]
pytz: Any
dateutil: Any
