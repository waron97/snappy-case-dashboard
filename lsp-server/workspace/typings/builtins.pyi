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
from helpdesk_ticket_extended import HelpdeskTicket

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

# --- res.partner ---

class ResPartner(Recordset):
    name: str
    display_name: str
    active: bool
    email: str
    phone: str
    mobile: str
    street: str
    street2: str
    zip: str
    city: str
    state_id: Recordset
    country_id: Recordset
    is_company: bool
    company_type: str
    parent_id: "ResPartner"
    child_ids: "ResPartner"
    vat: str
    ref: str
    # symple_contacts additions
    user_sequence: str
    fiscal_code: str
    is_client: bool
    category: str
    gender: str
    birth_date: Optional[_dt.date]
    is_distributor: bool
    pec_email: str
    # symple_pdp additions
    pod_ids: "ResPartnerPod"
    pdr_ids: "ResPartnerPdr"
    def browse(self, ids: Union[int, List[int]]) -> "ResPartner": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartner": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartner": ...
    def filtered(self, func: Any) -> "ResPartner": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartner": ...
    def exists(self) -> "ResPartner": ...
    def sudo(self) -> "ResPartner": ...
    def with_context(
        self, ctx: Dict[str, Any] = ..., **kwargs: Any
    ) -> "ResPartner": ...

# --- res.partner.pod ---

class ResPartnerPod(Recordset):
    name: str
    code: str
    user_sequence: str
    active: bool
    supply_state: str
    state: str
    activation_date: Optional[_dt.date]
    deactivation_date: Optional[_dt.date]
    client_id: "ResPartner"
    distributor_id: Recordset
    service_point_ids: "ServicePoint"
    tension_type: str
    engaged_power: str
    available_power: str
    tariff_code: str
    pod_use: str
    connection_type: str
    is_not_disconnectable: bool
    not_disconnectable_category: str
    declared_annual_usage: float
    technical_street: str
    technical_city_id: Recordset
    technical_zip: str
    technical_state_id: Recordset
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPod": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPod": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPod": ...
    def filtered(self, func: Any) -> "ResPartnerPod": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPod": ...
    def exists(self) -> "ResPartnerPod": ...
    def sudo(self) -> "ResPartnerPod": ...
    def with_context(
        self, ctx: Dict[str, Any] = ..., **kwargs: Any
    ) -> "ResPartnerPod": ...

# --- res.partner.pdr ---

class ResPartnerPdr(Recordset):
    name: str
    code: str
    user_sequence: str
    active: bool
    supply_state: str
    state: str
    activation_date: Optional[_dt.date]
    deactivation_date: Optional[_dt.date]
    client_id: "ResPartner"
    distributor_id: Recordset
    service_point_ids: "ServicePoint"
    pdr_type: str
    thermal_flow: float
    gas_pressure: float
    is_corrector: bool
    is_not_disconnectable: bool
    not_disconnectable_category: str
    declared_annual_usage: float
    technical_street: str
    technical_city_id: Recordset
    technical_zip: str
    technical_state_id: Recordset
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPdr": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPdr": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPdr": ...
    def filtered(self, func: Any) -> "ResPartnerPdr": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPdr": ...
    def exists(self) -> "ResPartnerPdr": ...
    def sudo(self) -> "ResPartnerPdr": ...
    def with_context(
        self, ctx: Dict[str, Any] = ..., **kwargs: Any
    ) -> "ResPartnerPdr": ...

# --- service.point ---

class ServicePoint(Recordset):
    code: str
    active: bool
    state: str
    commodity: str
    client_id: "ResPartner"
    pod_id: "ResPartnerPod"
    pdr_id: "ResPartnerPdr"
    market_type: str
    supply_start_date: Optional[_dt.date]
    supply_end_date: Optional[_dt.date]
    declared_annual_usage: float
    iva_rate: str
    tax_rate: str
    service_street: str
    service_city_id: Recordset
    service_zip: str
    service_state_id: Recordset
    available_power: float
    engaged_power: float
    use_type: str
    use_category: str
    distributor_practice_code: str
    def browse(self, ids: Union[int, List[int]]) -> "ServicePoint": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ServicePoint": ...
    def create(self, vals: Dict[str, Any]) -> "ServicePoint": ...
    def filtered(self, func: Any) -> "ServicePoint": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ServicePoint": ...
    def exists(self) -> "ServicePoint": ...
    def sudo(self) -> "ServicePoint": ...
    def with_context(
        self, ctx: Dict[str, Any] = ..., **kwargs: Any
    ) -> "ServicePoint": ...

# --- symple.workflow ---

class SympleWorkflow(Recordset):
    name: str
    active: bool
    triplet_phase_id: "SympleTripletPhase"
    phase_ids: "SympleTripletPhase"
    detail_ids: "HelpdeskTicketType"
    excluded_phase_ids: "SympleTripletPhase"
    is_tiqv: bool
    process_type: str
    code: str
    execute_code_every_phase: bool
    show_invoice_tab: bool
    commodity_required: bool
    send_sms: bool
    send_sms_case_domain: str
    alternative_phone: bool
    alternative_phone_domain: str
    show_connect_parent_case_button: bool
    connect_parent_case_is_same_client: bool
    connect_parent_case_is_same_point: bool
    connect_parent_case_domain: str
    feature_flag_async_engine: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleWorkflow": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleWorkflow": ...
    def create(self, vals: Dict[str, Any]) -> "SympleWorkflow": ...
    def filtered(self, func: Any) -> "SympleWorkflow": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleWorkflow": ...
    def exists(self) -> "SympleWorkflow": ...
    def sudo(self) -> "SympleWorkflow": ...

# --- symple.triplet.type ---

class SympleTripletType(Recordset):
    name: str
    active: bool
    type_code: str
    subtype_ids: "SympleTripletSubtype"
    is_visible_to_operators: bool
    is_visible_to_anonymous: bool
    is_pods_in_pop_up: bool
    is_service_points_in_pop_up: bool
    visible_to_channel_ids: Recordset
    domain_of_type: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleTripletType": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleTripletType": ...
    def create(self, vals: Dict[str, Any]) -> "SympleTripletType": ...
    def filtered(self, func: Any) -> "SympleTripletType": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleTripletType": ...
    def exists(self) -> "SympleTripletType": ...
    def sudo(self) -> "SympleTripletType": ...

# --- symple.triplet.subtype ---

class SympleTripletSubtype(Recordset):
    name: str
    code: str
    active: bool
    type_id: "SympleTripletType"
    ticket_type_ids: "HelpdeskTicketType"
    is_visible_to_operators: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleTripletSubtype": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleTripletSubtype": ...
    def create(self, vals: Dict[str, Any]) -> "SympleTripletSubtype": ...
    def filtered(self, func: Any) -> "SympleTripletSubtype": ...
    def sorted(
        self, key: Any = None, reverse: bool = False
    ) -> "SympleTripletSubtype": ...
    def exists(self) -> "SympleTripletSubtype": ...
    def sudo(self) -> "SympleTripletSubtype": ...

# --- symple.triplet.phase ---

class SympleTripletPhase(Recordset):
    name: str
    phase_code: str
    active: bool
    workflow_id: "SympleWorkflow"
    process_type: str
    is_tiqv: bool
    is_timeout: bool
    timeout_hours: int
    timeout_days: int
    timeout_months: int
    timeout_years: int
    timeout_time: int
    node_type: str
    is_voidable: bool
    is_checkpoint_phase: bool
    is_process_managed: bool
    is_externally_integrated: bool
    set_result_automatically: str
    send_email: str
    is_execute_code_at_phase_change: bool
    is_run_code_by_cron: bool
    service_code: str
    flow_code: str
    allowed_phase_ids: "SympleTripletPhase"
    allowed_phase_result_ids: "SympleTripletPhaseResult"
    automatic_phase_result_id: "SympleTripletPhaseResult"
    is_needs_child_case: bool
    needs_child_result_id: "SympleTripletPhaseResult"
    supply_state_change_to: str
    helpdesk_stage_id: Recordset
    def browse(self, ids: Union[int, List[int]]) -> "SympleTripletPhase": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleTripletPhase": ...
    def create(self, vals: Dict[str, Any]) -> "SympleTripletPhase": ...
    def filtered(self, func: Any) -> "SympleTripletPhase": ...
    def sorted(
        self, key: Any = None, reverse: bool = False
    ) -> "SympleTripletPhase": ...
    def exists(self) -> "SympleTripletPhase": ...
    def sudo(self) -> "SympleTripletPhase": ...

# --- symple.triplet.phase.result ---

class SympleTripletPhaseResult(Recordset):
    name: str
    active: bool
    next_phase_id: "SympleTripletPhase"
    workflow_id: "SympleWorkflow"
    is_annulment: bool
    wizard_result: str
    state_code: str
    is_hidden: bool
    has_message: bool
    is_quote_expired: bool
    is_dl_solicitation_result: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleTripletPhaseResult": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleTripletPhaseResult": ...
    def create(self, vals: Dict[str, Any]) -> "SympleTripletPhaseResult": ...
    def filtered(self, func: Any) -> "SympleTripletPhaseResult": ...
    def sorted(
        self, key: Any = None, reverse: bool = False
    ) -> "SympleTripletPhaseResult": ...
    def exists(self) -> "SympleTripletPhaseResult": ...
    def sudo(self) -> "SympleTripletPhaseResult": ...

# --- helpdesk.ticket.type ---

class HelpdeskTicketType(Recordset):
    name: str
    active: bool
    code: str
    subtype_id: "SympleTripletSubtype"
    type_id: "SympleTripletType"
    workflow_id: "SympleWorkflow"
    cluster_id: Recordset
    # flags
    is_meter_readings: bool
    is_reminder: bool
    is_reiteration: bool
    is_point_required: bool
    needs_interaction: bool
    is_visible_to_operators: bool
    is_service_points_in_pop_up: bool
    is_select_parent: bool
    parent_case_domain: str
    domain_of_detail: str
    # triplet-specific flags
    is_market_change: bool
    is_cessazione_se3: bool
    is_cessazione_vt4: bool
    is_sdd_cancel: bool
    is_iban_ma29: bool
    is_an_02: bool
    is_an_03: bool
    is_an_04: bool
    is_an_06: bool
    is_an_22: bool
    is_at_01: bool
    is_sb05_1: bool
    is_sb05_2: bool
    is_sb05_3: bool
    is_cc12_1: bool
    # commodity / market (sorgenia_helpdesk_ticket)
    has_alternative_email: bool
    is_for_commodity_required: bool
    is_for_ele_required: bool
    is_for_gas_required: bool
    is_for_fiber_required: bool
    is_commodity_readonly: bool
    commodity_readonly_default: str
    is_triplet_market: bool
    is_market_l: bool
    is_market_t: bool
    # commodity visibility (sorgenia_tools)
    is_for_commodity: bool
    is_for_ele: bool
    is_for_gas: bool
    is_for_fiber: bool
    is_for_commodity_optional: bool
    is_for_ele_optional: bool
    is_for_gas_optional: bool
    is_for_fiber_optional: bool
    is_from_migration: bool
    # integration (sorgenia_ml)
    univocal_code: str
    m2c_ifa: str
    # rcu (symple_rcu)
    is_rcu_ignore_date_check: bool
    # methods
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskTicketType": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskTicketType": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskTicketType": ...
    def filtered(self, func: Any) -> "HelpdeskTicketType": ...
    def sorted(
        self, key: Any = None, reverse: bool = False
    ) -> "HelpdeskTicketType": ...
    def exists(self) -> "HelpdeskTicketType": ...
    def get_triplet(self, code: str) -> Any: ...
    def sudo(self) -> "HelpdeskTicketType": ...

# HelpdeskTicket is imported from helpdesk_ticket_extended.pyi

# --- symple.pb.process.data ---

class SymplePbProcessData(Recordset):
    res_model: str
    res_id: int
    payload: str
    pb_id: str
    process_name: str
    def get_payload(self) -> Any: ...
    def browse(self, ids: Union[int, List[int]]) -> "SymplePbProcessData": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymplePbProcessData": ...
    def create(self, vals: Dict[str, Any]) -> "SymplePbProcessData": ...
    def filtered(self, func: Any) -> "SymplePbProcessData": ...
    def sorted(
        self, key: Any = None, reverse: bool = False
    ) -> "SymplePbProcessData": ...
    def exists(self) -> "SymplePbProcessData": ...
    def sudo(self) -> "SymplePbProcessData": ...

# --- market.comm.event.log ---

class MarketCommEventLog(Recordset):
    ticket_id: "HelpdeskTicket"
    service_code: str
    flow_code: str
    cp_utente: str
    cp_gestore: str
    inner_payload: str
    full_payload: str
    def browse(self, ids: Union[int, List[int]]) -> "MarketCommEventLog": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MarketCommEventLog": ...
    def create(self, vals: Dict[str, Any]) -> "MarketCommEventLog": ...
    def filtered(self, func: Any) -> "MarketCommEventLog": ...
    def sorted(
        self, key: Any = None, reverse: bool = False
    ) -> "MarketCommEventLog": ...
    def exists(self) -> "MarketCommEventLog": ...
    def sudo(self) -> "MarketCommEventLog": ...

# --- case.integration.history ---

class CaseIntegrationHistory(Recordset):
    ticket_id: "HelpdeskTicket"
    name: str
    symphony_request_id: str
    payload: str
    def browse(self, ids: Union[int, List[int]]) -> "CaseIntegrationHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CaseIntegrationHistory": ...
    def create(self, vals: Dict[str, Any]) -> "CaseIntegrationHistory": ...
    def filtered(self, func: Any) -> "CaseIntegrationHistory": ...
    def sorted(
        self, key: Any = None, reverse: bool = False
    ) -> "CaseIntegrationHistory": ...
    def exists(self) -> "CaseIntegrationHistory": ...
    def sudo(self) -> "CaseIntegrationHistory": ...

# --- ir.config_parameter ---

class IrConfigParameter(Recordset):
    # Odoo base (ir_config_parameter.py)
    def get_param(self, key: str, default: Any = False) -> Any: ...
    def set_param(self, key: str, value: Any) -> None: ...
    # symple_pb_connector (B2W asset/contract API)
    def get_b2w_access_token(
        self, show_log_error: bool = True, raise_exception: bool = False
    ) -> Any: ...
    def get_b2w_base_element(self) -> Any: ...
    def get_b2w_asset_url_and_headers(self, additional_headers: Any) -> Any: ...
    def get_assets(
        self,
        asset_id: Any = None,
        additional_params: Any = False,
        additional_headers: Any = False,
    ) -> Any: ...
    def get_contracts(
        self,
        contract_id: Any = None,
        additional_params: Any = False,
        additional_headers: Any = False,
    ) -> Any: ...
    def get_order(
        self,
        order_id: Any = None,
        additional_params: Any = False,
        additional_headers: Any = False,
    ) -> Any: ...
    def get_orderitem(
        self,
        orderitem_id: Any = None,
        additional_params: Any = False,
        additional_headers: Any = False,
    ) -> Any: ...
    def patch_asset(
        self, asset_id: Any, payload: Any, additional_headers: Any = False
    ) -> Any: ...
    # sorgenia_tools/ir_config_parameter.py (orchestration)
    def call_symphony_process(self, payload: Any, process: Any) -> Any: ...
    def check_compatibility_matrix(
        self,
        external_id: Any = None,
        asset_id: Any = None,
        client_id: Any = None,
        billing_id: Any = None,
    ) -> Any: ...
    def _upload_file_to_dms(
        self, attachment_id: Any, file_upload_path: Any, customer_id: Any = None
    ) -> Any: ...
    def _b2w_wake_up_process(self, payload: Any) -> Any: ...
    # sorgenia_tools/ir_config_parameter__m2c.py (M2C payload builder)
    def prepare_m2c_payload(
        self,
        case_id: Any,
        triplet: str,
        is_client: bool = True,
        is_get_client_extended: bool = False,
        is_validity_date: bool = False,
        is_split_payment: bool = False,
        is_contratti_mandato: bool = False,
        service_points: Union[List[Any], bool] = False,
        service_points_billing_profile_array: Union[List[Any], bool] = False,
        is_associazioneContrattoFornitura: bool = False,
        is_domiciliazione: bool = False,
        is_ccr: bool = False,
        is_dpay: bool = False,
        contatti_array: Union[List[Any], bool] = False,
        extra_contract_info: Union[bool, Any] = False,
        extra_forniture_info: Union[bool, Any] = False,
        causale_attivazione: Union[str, bool] = False,
        contrattiDettaglio_array: Union[List[Any], bool] = False,
        forn_contatti_array: Union[List[Any], bool] = False,
        contrattiMandatoDettaglio_array: Union[List[Any], bool] = False,
        is_cCodiceDestinatario: bool = False,
        is_cCodiceUfficioPA: bool = False,
        is_cigCup: bool = False,
        is_contratti: bool = False,
        is_prodotti: bool = False,
        causale_cessazione: Union[str, bool] = False,
        is_oneri: bool = False,
        charge: Union[str, bool] = False,
        charge_type: Union[str, bool] = False,
        charge_description: Union[str, bool] = False,
        fine_contratto: Union[str, bool] = False,
        fine_contratto_fornitura: Union[str, bool] = False,
        cma_array: Union[List[Any], bool] = False,
        is_codice_offerta: bool = False,
        garanzia: Union[str, bool] = False,
        is_contratti_mandato_dInizioValidita: bool = False,
        protocollo: Union[str, bool] = False,
        is_rcu: bool = False,
        oneri_case_type: Union[str, bool] = False,
        isContrattiOLDAsset: Union[Dict[str, Any], bool] = False,
        is_storno: bool = False,
        storno_case_type: Union[str, bool] = False,
        data_storno: Union[str, bool] = False,
        mask: Optional[str] = None,
    ) -> Dict[str, Any]: ...
    def prepare_m2c_passthrough_payload(
        self,
        case_id: Any,
        triplet: str,
        is_client: bool = True,
        is_get_client_extended: bool = False,
        is_validity_date: bool = False,
        is_split_payment: bool = False,
        is_contratti_mandato: bool = False,
        service_points: Union[List[Any], bool] = False,
        service_points_billing_profile_array: Union[List[Any], bool] = False,
        is_associazioneContrattoFornitura: bool = False,
        is_domiciliazione: bool = False,
        is_ccr: bool = False,
        is_dpay: bool = False,
        contatti_array: Union[List[Any], bool] = False,
        extra_contract_info: Union[bool, Any] = False,
        extra_forniture_info: Union[bool, Any] = False,
        causale_attivazione: Union[str, bool] = False,
        contrattiDettaglio_array: Union[List[Any], bool] = False,
        forn_contatti_array: Union[List[Any], bool] = False,
        contrattiMandatoDettaglio_array: Union[List[Any], bool] = False,
        is_cCodiceDestinatario: bool = False,
        is_cCodiceUfficioPA: bool = False,
        is_cigCup: bool = False,
        is_contratti: bool = False,
        is_prodotti: bool = False,
        causale_cessazione: Union[str, bool] = False,
        fine_contratto: Union[str, bool] = False,
        fine_contratto_fornitura: Union[str, bool] = False,
        is_oneri: bool = False,
        charge: Union[str, bool] = False,
        charge_type: Union[str, bool] = False,
        charge_description: Union[str, bool] = False,
        cma_array: Union[List[Any], bool] = False,
        is_codice_offerta: bool = False,
        garanzia: Union[str, bool] = False,
        is_contratti_mandato_dInizioValidita: bool = False,
        protocollo: Union[str, bool] = False,
        is_rcu: bool = False,
        oneri_case_type: Union[str, bool] = False,
        mask: Optional[str] = None,
        is_storno: bool = False,
        data_storno: Union[str, bool] = False,
        storno_case_type: Union[str, bool] = False,
    ) -> str: ...
    def get_contrattiMandato_payload(self, customer_id: Any, **kwargs: Any) -> Any: ...
    def get_contratti_payload(self, bp_sp_dict: Any, **kwargs: Any) -> Any: ...
    def get_client_extended_payload(self, customer_id: Any, case_id: Any) -> Any: ...
    def get_oneri_payload(
        self,
        customer_id: Any,
        triplet: Any,
        case_id: Any,
        charge: Any,
        charge_type: Any,
        charge_description: Any,
        **kwargs: Any,
    ) -> Any: ...
    def get_storno_payload(
        self, customer_id: Any, triplet: Any, case_id: Any, **kwargs: Any
    ) -> Any: ...
    # sorgenia_tools/ir_config_parameter__state_model.py (B2W state machine)
    def get_b2w_statemodel(
        self,
        sm_name: Any,
        sm_version: str = "1",
        force_result: Any = False,
        token: Any = False,
    ) -> Any: ...
    def update_b2w_statemodel(self, destination_state: Any, **kwargs: Any) -> Any: ...
    def find_b2w_state_model_transition_steps(
        self, sm_name: Any, start_state: Any, destination_state: Any, **kwargs: Any
    ) -> Any: ...
    def get_b2w_entity_current_state(self, **kwargs: Any) -> Any: ...
    def get_b2w_statemodel_name(self, **kwargs: Any) -> Any: ...
    def get_b2w_statemodel_endpoint(self, **kwargs: Any) -> Any: ...
    def shortest_path(self, mtx: Any, start: Any, end: Any) -> Any: ...
    # sorgenia_ml_cessazioni (activation)
    def UNSAFE_set_asset_and_contract_active_status(
        self,
        asset_id: Any = None,
        update_statemodel: bool = False,
        update_sm_reason: str = "",
    ) -> Any: ...
    def browse(self, ids: Union[int, List[int]]) -> "IrConfigParameter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrConfigParameter": ...
    def create(self, vals: Dict[str, Any]) -> "IrConfigParameter": ...
    def filtered(self, func: Any) -> "IrConfigParameter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrConfigParameter": ...
    def exists(self) -> "IrConfigParameter": ...
    def sudo(self) -> "IrConfigParameter": ...

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
    def __getitem__(self, model_name: Literal["helpdesk.ticket"]) -> HelpdeskTicket: ...
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
    ) -> IrConfigParameter: ...
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

case_id: HelpdeskTicket
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
