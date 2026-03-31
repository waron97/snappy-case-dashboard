from odoo_records import _IrConfigParameter
from typing import Any, Optional, Union, List, Dict

# --- ir.config_parameter ---

class IrConfigParameterExtended(_IrConfigParameter):
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
    def browse(self, ids: Union[int, List[int]]) -> "_IrConfigParameter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "_IrConfigParameter": ...
    def create(self, vals: Dict[str, Any]) -> "_IrConfigParameter": ...
    def filtered(self, func: Any) -> "_IrConfigParameter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "_IrConfigParameter": ...
    def exists(self) -> "_IrConfigParameter": ...
    def sudo(self) -> "_IrConfigParameter": ...
