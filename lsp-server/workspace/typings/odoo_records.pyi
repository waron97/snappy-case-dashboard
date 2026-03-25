# AUTO-GENERATED FILE - do not edit manually
# Run lsp-server/generate_stubs.py to regenerate

from typing import Any, Dict, List, Optional, Union, Literal
import datetime as _dt
from recordset import Recordset

# --- _unknown ---

class Unknown(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "Unknown": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "Unknown": ...
    def create(self, vals: Dict[str, Any]) -> "Unknown": ...
    def filtered(self, func: Any) -> "Unknown": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "Unknown": ...
    def exists(self) -> "Unknown": ...
    def sudo(self) -> "Unknown": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "Unknown": ...

# --- account.account ---

class AccountAccount(Recordset):
    allowed_journal_ids: "AccountJournal"
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    company_id: "ResCompany"
    currency_id: "ResCurrency"
    current_balance: float
    deprecated: bool
    group_id: "AccountGroup"
    has_bit2publish_template: bool
    has_message: bool
    internal_group: str
    internal_type: str
    is_off_balance: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    name: str
    note: str
    opening_balance: float
    opening_credit: float
    opening_debit: float
    reconcile: bool
    related_taxes_amount: int
    root_id: "AccountRoot"
    show_bit2publish_button: bool
    tag_ids: "AccountAccountTag"
    tax_ids: "AccountTax"
    used: bool
    user_type_id: "AccountAccountType"
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "AccountAccount": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAccount": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAccount": ...
    def filtered(self, func: Any) -> "AccountAccount": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAccount": ...
    def exists(self) -> "AccountAccount": ...
    def sudo(self) -> "AccountAccount": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAccount": ...

# --- account.account.tag ---

class AccountAccountTag(Recordset):
    active: bool
    applicability: str
    bit2publish_template_ids: "Bit2publishTemplate"
    color: int
    country_id: "ResCountry"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    tax_negate: bool
    tax_report_line_ids: "AccountTaxReportLine"
    def browse(self, ids: Union[int, List[int]]) -> "AccountAccountTag": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAccountTag": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAccountTag": ...
    def filtered(self, func: Any) -> "AccountAccountTag": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAccountTag": ...
    def exists(self) -> "AccountAccountTag": ...
    def sudo(self) -> "AccountAccountTag": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAccountTag": ...

# --- account.account.template ---

class AccountAccountTemplate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    chart_template_id: "AccountChartTemplate"
    code: str
    currency_id: "ResCurrency"
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    name: str
    nocreate: bool
    note: str
    reconcile: bool
    show_bit2publish_button: bool
    tag_ids: "AccountAccountTag"
    tax_ids: "AccountTaxTemplate"
    user_type_id: "AccountAccountType"
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "AccountAccountTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAccountTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAccountTemplate": ...
    def filtered(self, func: Any) -> "AccountAccountTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAccountTemplate": ...
    def exists(self) -> "AccountAccountTemplate": ...
    def sudo(self) -> "AccountAccountTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAccountTemplate": ...

# --- account.account.type ---

class AccountAccountType(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    include_initial_balance: bool
    internal_group: str
    name: str
    note: str
    show_bit2publish_button: bool
    type: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountAccountType": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAccountType": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAccountType": ...
    def filtered(self, func: Any) -> "AccountAccountType": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAccountType": ...
    def exists(self) -> "AccountAccountType": ...
    def sudo(self) -> "AccountAccountType": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAccountType": ...

# --- account.accrued.orders.wizard ---

class AccountAccruedOrdersWizard(Recordset):
    account_id: "AccountAccount"
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    currency_id: "ResCurrency"
    date: Optional[_dt.date]
    display_amount: bool
    has_bit2publish_template: bool
    journal_id: "AccountJournal"
    preview_data: str
    reversal_date: Optional[_dt.date]
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountAccruedOrdersWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAccruedOrdersWizard": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAccruedOrdersWizard": ...
    def filtered(self, func: Any) -> "AccountAccruedOrdersWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAccruedOrdersWizard": ...
    def exists(self) -> "AccountAccruedOrdersWizard": ...
    def sudo(self) -> "AccountAccruedOrdersWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAccruedOrdersWizard": ...

# --- account.analytic.account ---

class AccountAnalyticAccount(Recordset):
    active: bool
    balance: float
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    company_id: "ResCompany"
    credit: float
    currency_id: "ResCurrency"
    debit: float
    group_id: "AccountAnalyticGroup"
    has_bit2publish_template: bool
    has_message: bool
    invoice_count: int
    line_ids: "AccountAnalyticLine"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    name: str
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    vendor_bill_count: int
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "AccountAnalyticAccount": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAnalyticAccount": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAnalyticAccount": ...
    def filtered(self, func: Any) -> "AccountAnalyticAccount": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAnalyticAccount": ...
    def exists(self) -> "AccountAnalyticAccount": ...
    def sudo(self) -> "AccountAnalyticAccount": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAnalyticAccount": ...

# --- account.analytic.default ---

class AccountAnalyticDefault(Recordset):
    account_id: "AccountAccount"
    analytic_id: "AccountAnalyticAccount"
    analytic_tag_ids: "AccountAnalyticTag"
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    date_start: Optional[_dt.date]
    date_stop: Optional[_dt.date]
    has_bit2publish_template: bool
    partner_id: "ResPartner"
    product_id: "ProductProduct"
    sequence: int
    show_bit2publish_button: bool
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "AccountAnalyticDefault": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAnalyticDefault": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAnalyticDefault": ...
    def filtered(self, func: Any) -> "AccountAnalyticDefault": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAnalyticDefault": ...
    def exists(self) -> "AccountAnalyticDefault": ...
    def sudo(self) -> "AccountAnalyticDefault": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAnalyticDefault": ...

# --- account.analytic.distribution ---

class AccountAnalyticDistribution(Recordset):
    account_id: "AccountAnalyticAccount"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    percentage: float
    show_bit2publish_button: bool
    tag_id: "AccountAnalyticTag"
    def browse(self, ids: Union[int, List[int]]) -> "AccountAnalyticDistribution": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAnalyticDistribution": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAnalyticDistribution": ...
    def filtered(self, func: Any) -> "AccountAnalyticDistribution": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAnalyticDistribution": ...
    def exists(self) -> "AccountAnalyticDistribution": ...
    def sudo(self) -> "AccountAnalyticDistribution": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAnalyticDistribution": ...

# --- account.analytic.group ---

class AccountAnalyticGroup(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    children_ids: "AccountAnalyticGroup"
    company_id: "ResCompany"
    complete_name: str
    description: str
    has_bit2publish_template: bool
    name: str
    parent_id: "AccountAnalyticGroup"
    parent_path: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountAnalyticGroup": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAnalyticGroup": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAnalyticGroup": ...
    def filtered(self, func: Any) -> "AccountAnalyticGroup": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAnalyticGroup": ...
    def exists(self) -> "AccountAnalyticGroup": ...
    def sudo(self) -> "AccountAnalyticGroup": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAnalyticGroup": ...

# --- account.analytic.line ---

class AccountAnalyticLine(Recordset):
    account_id: "AccountAnalyticAccount"
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    category: str
    code: str
    company_id: "ResCompany"
    currency_id: "ResCurrency"
    date: Optional[_dt.date]
    general_account_id: "AccountAccount"
    group_id: "AccountAnalyticGroup"
    has_bit2publish_template: bool
    move_id: "AccountMoveLine"
    name: str
    partner_id: "ResPartner"
    product_id: "ProductProduct"
    product_uom_category_id: "UomCategory"
    product_uom_id: "UomUom"
    ref: str
    show_bit2publish_button: bool
    tag_ids: "AccountAnalyticTag"
    unit_amount: float
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "AccountAnalyticLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAnalyticLine": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAnalyticLine": ...
    def filtered(self, func: Any) -> "AccountAnalyticLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAnalyticLine": ...
    def exists(self) -> "AccountAnalyticLine": ...
    def sudo(self) -> "AccountAnalyticLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAnalyticLine": ...

# --- account.analytic.tag ---

class AccountAnalyticTag(Recordset):
    active: bool
    active_analytic_distribution: bool
    analytic_distribution_ids: "AccountAnalyticDistribution"
    bit2publish_template_ids: "Bit2publishTemplate"
    color: int
    company_id: "ResCompany"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountAnalyticTag": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAnalyticTag": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAnalyticTag": ...
    def filtered(self, func: Any) -> "AccountAnalyticTag": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAnalyticTag": ...
    def exists(self) -> "AccountAnalyticTag": ...
    def sudo(self) -> "AccountAnalyticTag": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAnalyticTag": ...

# --- account.automatic.entry.wizard ---

class AccountAutomaticEntryWizard(Recordset):
    account_type: str
    action: str
    bit2publish_template_ids: "Bit2publishTemplate"
    company_currency_id: "ResCurrency"
    company_id: "ResCompany"
    date: Optional[_dt.date]
    destination_account_id: "AccountAccount"
    display_currency_helper: bool
    expense_accrual_account: "AccountAccount"
    has_bit2publish_template: bool
    journal_id: "AccountJournal"
    move_data: str
    move_line_ids: "AccountMoveLine"
    percentage: float
    preview_move_data: str
    revenue_accrual_account: "AccountAccount"
    show_bit2publish_button: bool
    total_amount: float
    def browse(self, ids: Union[int, List[int]]) -> "AccountAutomaticEntryWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountAutomaticEntryWizard": ...
    def create(self, vals: Dict[str, Any]) -> "AccountAutomaticEntryWizard": ...
    def filtered(self, func: Any) -> "AccountAutomaticEntryWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountAutomaticEntryWizard": ...
    def exists(self) -> "AccountAutomaticEntryWizard": ...
    def sudo(self) -> "AccountAutomaticEntryWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountAutomaticEntryWizard": ...

# --- account.bank.statement ---

class AccountBankStatement(Recordset):
    all_lines_reconciled: bool
    balance_end: float
    balance_end_real: float
    balance_start: float
    bit2publish_template_ids: "Bit2publishTemplate"
    cashbox_end_id: "AccountBankStatementCashbox"
    cashbox_start_id: "AccountBankStatementCashbox"
    company_id: "ResCompany"
    country_code: str
    currency_id: "ResCurrency"
    date: Optional[_dt.date]
    date_done: Optional[_dt.datetime]
    difference: float
    has_bit2publish_template: bool
    has_message: bool
    is_difference_zero: bool
    is_valid_balance_start: bool
    journal_id: "AccountJournal"
    journal_type: str
    line_ids: "AccountBankStatementLine"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    move_line_count: int
    move_line_ids: "AccountMoveLine"
    name: str
    previous_statement_id: "AccountBankStatement"
    reference: str
    sequence_number: int
    sequence_prefix: str
    show_bit2publish_button: bool
    state: str
    total_entry_encoding: float
    user_id: "ResUsers"
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "AccountBankStatement": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountBankStatement": ...
    def create(self, vals: Dict[str, Any]) -> "AccountBankStatement": ...
    def filtered(self, func: Any) -> "AccountBankStatement": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountBankStatement": ...
    def exists(self) -> "AccountBankStatement": ...
    def sudo(self) -> "AccountBankStatement": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountBankStatement": ...

# --- account.bank.statement.cashbox ---

class AccountBankStatementCashbox(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    cashbox_lines_ids: "AccountCashboxLine"
    currency_id: "ResCurrency"
    end_bank_stmt_ids: "AccountBankStatement"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    start_bank_stmt_ids: "AccountBankStatement"
    total: float
    def browse(self, ids: Union[int, List[int]]) -> "AccountBankStatementCashbox": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountBankStatementCashbox": ...
    def create(self, vals: Dict[str, Any]) -> "AccountBankStatementCashbox": ...
    def filtered(self, func: Any) -> "AccountBankStatementCashbox": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountBankStatementCashbox": ...
    def exists(self) -> "AccountBankStatementCashbox": ...
    def sudo(self) -> "AccountBankStatementCashbox": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountBankStatementCashbox": ...

# --- account.bank.statement.closebalance ---

class AccountBankStatementClosebalance(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountBankStatementClosebalance": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountBankStatementClosebalance": ...
    def create(self, vals: Dict[str, Any]) -> "AccountBankStatementClosebalance": ...
    def filtered(self, func: Any) -> "AccountBankStatementClosebalance": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountBankStatementClosebalance": ...
    def exists(self) -> "AccountBankStatementClosebalance": ...
    def sudo(self) -> "AccountBankStatementClosebalance": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountBankStatementClosebalance": ...

# --- account.bank.statement.line ---

class AccountBankStatementLine(Recordset):
    access_token: str
    access_url: str
    access_warning: str
    account_number: str
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    always_tax_exigible: bool
    amount: float
    amount_currency: float
    amount_paid: float
    amount_residual: float
    amount_residual_signed: float
    amount_tax: float
    amount_tax_signed: float
    amount_total: float
    amount_total_in_currency_signed: float
    amount_total_signed: float
    amount_untaxed: float
    amount_untaxed_signed: float
    authorized_transaction_ids: "PaymentTransaction"
    auto_post: bool
    bank_partner_id: "ResPartner"
    bit2publish_template_ids: "Bit2publishTemplate"
    commercial_partner_id: "ResPartner"
    company_currency_id: "ResCurrency"
    company_id: "ResCompany"
    country_code: str
    currency_id: "ResCurrency"
    date: Optional[_dt.date]
    display_inactive_currency_warning: bool
    display_qr_code: bool
    duplicated_vendor_ref: str
    edi_blocking_level: str
    edi_document_ids: "AccountEdiDocument"
    edi_error_count: int
    edi_error_message: str
    edi_show_abandon_cancel_button: bool
    edi_show_cancel_button: bool
    edi_state: str
    edi_web_services_to_process: str
    extract_can_show_resend_button: bool
    extract_can_show_send_button: bool
    extract_error_message: str
    extract_remote_id: int
    extract_state: str
    extract_status_code: int
    extract_word_ids: "AccountInvoiceExtractWords"
    fiscal_position_id: "AccountFiscalPosition"
    foreign_currency_id: "ResCurrency"
    has_bit2publish_template: bool
    has_message: bool
    has_reconciled_entries: bool
    highest_name: str
    inalterable_hash: str
    invoice_cash_rounding_id: "AccountCashRounding"
    invoice_date: Optional[_dt.date]
    invoice_date_due: Optional[_dt.date]
    invoice_filter_type_domain: str
    invoice_has_matching_suspense_amount: bool
    invoice_has_outstanding: bool
    invoice_incoterm_id: "AccountIncoterms"
    invoice_line_ids: "AccountMoveLine"
    invoice_origin: str
    invoice_outstanding_credits_debits_widget: str
    invoice_partner_display_name: str
    invoice_payments_widget: str
    invoice_payment_term_id: "AccountPaymentTerm"
    invoice_source_email: str
    invoice_user_id: "ResUsers"
    invoice_vendor_bill_id: "AccountMove"
    is_move_sent: bool
    is_reconciled: bool
    journal_id: "AccountJournal"
    line_ids: "AccountMoveLine"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    move_id: "AccountMove"
    move_type: str
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    narration: str
    partner_bank_id: "ResPartnerBank"
    partner_id: "ResPartner"
    partner_name: str
    payment_id: "AccountPayment"
    payment_ids: "AccountPayment"
    payment_ref: str
    payment_reference: str
    payment_state: str
    posted_before: bool
    preferred_payment_method_id: "AccountPaymentMethod"
    qr_code_method: str
    ref: str
    restrict_mode_hash_table: bool
    reversal_move_id: "AccountMove"
    reversed_entry_id: "AccountMove"
    secure_sequence_number: int
    sequence: int
    sequence_number: int
    sequence_prefix: str
    show_bit2publish_button: bool
    show_name_warning: bool
    show_reset_to_draft_button: bool
    state: str
    statement_id: "AccountBankStatement"
    statement_line_id: "AccountBankStatementLine"
    string_to_hash: str
    suitable_journal_ids: "AccountJournal"
    tax_cash_basis_created_move_ids: "AccountMove"
    tax_cash_basis_origin_move_id: "AccountMove"
    tax_cash_basis_rec_id: "AccountPartialReconcile"
    tax_country_code: str
    tax_country_id: "ResCountry"
    tax_lock_date_message: str
    tax_totals_json: str
    to_check: bool
    transaction_ids: "PaymentTransaction"
    transaction_type: str
    type_name: str
    user_id: "ResUsers"
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "AccountBankStatementLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountBankStatementLine": ...
    def create(self, vals: Dict[str, Any]) -> "AccountBankStatementLine": ...
    def filtered(self, func: Any) -> "AccountBankStatementLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountBankStatementLine": ...
    def exists(self) -> "AccountBankStatementLine": ...
    def sudo(self) -> "AccountBankStatementLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountBankStatementLine": ...

# --- account.cash.rounding ---

class AccountCashRounding(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    has_bit2publish_template: bool
    loss_account_id: "AccountAccount"
    name: str
    profit_account_id: "AccountAccount"
    rounding: float
    rounding_method: str
    show_bit2publish_button: bool
    strategy: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountCashRounding": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountCashRounding": ...
    def create(self, vals: Dict[str, Any]) -> "AccountCashRounding": ...
    def filtered(self, func: Any) -> "AccountCashRounding": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountCashRounding": ...
    def exists(self) -> "AccountCashRounding": ...
    def sudo(self) -> "AccountCashRounding": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountCashRounding": ...

# --- account.cashbox.line ---

class AccountCashboxLine(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    cashbox_id: "AccountBankStatementCashbox"
    coin_value: float
    currency_id: "ResCurrency"
    has_bit2publish_template: bool
    number: int
    show_bit2publish_button: bool
    subtotal: float
    def browse(self, ids: Union[int, List[int]]) -> "AccountCashboxLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountCashboxLine": ...
    def create(self, vals: Dict[str, Any]) -> "AccountCashboxLine": ...
    def filtered(self, func: Any) -> "AccountCashboxLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountCashboxLine": ...
    def exists(self) -> "AccountCashboxLine": ...
    def sudo(self) -> "AccountCashboxLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountCashboxLine": ...

# --- account.chart.template ---

class AccountChartTemplate(Recordset):
    account_ids: "AccountAccountTemplate"
    account_journal_payment_credit_account_id: "AccountAccountTemplate"
    account_journal_payment_debit_account_id: "AccountAccountTemplate"
    account_journal_suspense_account_id: "AccountAccountTemplate"
    bank_account_code_prefix: str
    bit2publish_template_ids: "Bit2publishTemplate"
    cash_account_code_prefix: str
    code_digits: int
    complete_tax_set: bool
    country_id: "ResCountry"
    currency_id: "ResCurrency"
    default_cash_difference_expense_account_id: "AccountAccountTemplate"
    default_cash_difference_income_account_id: "AccountAccountTemplate"
    default_pos_receivable_account_id: "AccountAccountTemplate"
    expense_currency_exchange_account_id: "AccountAccountTemplate"
    has_bit2publish_template: bool
    income_currency_exchange_account_id: "AccountAccountTemplate"
    name: str
    parent_id: "AccountChartTemplate"
    property_account_expense_categ_id: "AccountAccountTemplate"
    property_account_expense_id: "AccountAccountTemplate"
    property_account_income_categ_id: "AccountAccountTemplate"
    property_account_income_id: "AccountAccountTemplate"
    property_account_payable_id: "AccountAccountTemplate"
    property_account_receivable_id: "AccountAccountTemplate"
    property_advance_tax_payment_account_id: "AccountAccountTemplate"
    property_cash_basis_base_account_id: "AccountAccountTemplate"
    property_stock_account_input_categ_id: "AccountAccountTemplate"
    property_stock_account_output_categ_id: "AccountAccountTemplate"
    property_stock_valuation_account_id: "AccountAccountTemplate"
    property_tax_payable_account_id: "AccountAccountTemplate"
    property_tax_receivable_account_id: "AccountAccountTemplate"
    show_bit2publish_button: bool
    tax_template_ids: "AccountTaxTemplate"
    transfer_account_code_prefix: str
    use_anglo_saxon: bool
    visible: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountChartTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountChartTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "AccountChartTemplate": ...
    def filtered(self, func: Any) -> "AccountChartTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountChartTemplate": ...
    def exists(self) -> "AccountChartTemplate": ...
    def sudo(self) -> "AccountChartTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountChartTemplate": ...

# --- account.common.journal.report ---

class AccountCommonJournalReport(Recordset):
    amount_currency: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    date_from: Optional[_dt.date]
    date_to: Optional[_dt.date]
    has_bit2publish_template: bool
    journal_ids: "AccountJournal"
    show_bit2publish_button: bool
    target_move: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountCommonJournalReport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountCommonJournalReport": ...
    def create(self, vals: Dict[str, Any]) -> "AccountCommonJournalReport": ...
    def filtered(self, func: Any) -> "AccountCommonJournalReport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountCommonJournalReport": ...
    def exists(self) -> "AccountCommonJournalReport": ...
    def sudo(self) -> "AccountCommonJournalReport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountCommonJournalReport": ...

# --- account.common.report ---

class AccountCommonReport(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    date_from: Optional[_dt.date]
    date_to: Optional[_dt.date]
    has_bit2publish_template: bool
    journal_ids: "AccountJournal"
    show_bit2publish_button: bool
    target_move: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountCommonReport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountCommonReport": ...
    def create(self, vals: Dict[str, Any]) -> "AccountCommonReport": ...
    def filtered(self, func: Any) -> "AccountCommonReport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountCommonReport": ...
    def exists(self) -> "AccountCommonReport": ...
    def sudo(self) -> "AccountCommonReport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountCommonReport": ...

# --- account.edi.common ---

class AccountEdiCommon(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountEdiCommon": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountEdiCommon": ...
    def create(self, vals: Dict[str, Any]) -> "AccountEdiCommon": ...
    def filtered(self, func: Any) -> "AccountEdiCommon": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountEdiCommon": ...
    def exists(self) -> "AccountEdiCommon": ...
    def sudo(self) -> "AccountEdiCommon": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountEdiCommon": ...

# --- account.edi.document ---

class AccountEdiDocument(Recordset):
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    blocking_level: str
    edi_content: bytes
    edi_format_id: "AccountEdiFormat"
    edi_format_name: str
    error: str
    has_bit2publish_template: bool
    move_id: "AccountMove"
    name: str
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountEdiDocument": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountEdiDocument": ...
    def create(self, vals: Dict[str, Any]) -> "AccountEdiDocument": ...
    def filtered(self, func: Any) -> "AccountEdiDocument": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountEdiDocument": ...
    def exists(self) -> "AccountEdiDocument": ...
    def sudo(self) -> "AccountEdiDocument": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountEdiDocument": ...

# --- account.edi.format ---

class AccountEdiFormat(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountEdiFormat": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountEdiFormat": ...
    def create(self, vals: Dict[str, Any]) -> "AccountEdiFormat": ...
    def filtered(self, func: Any) -> "AccountEdiFormat": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountEdiFormat": ...
    def exists(self) -> "AccountEdiFormat": ...
    def sudo(self) -> "AccountEdiFormat": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountEdiFormat": ...

# --- account.edi.xml.cii ---

class AccountEdiXmlCii(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountEdiXmlCii": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountEdiXmlCii": ...
    def create(self, vals: Dict[str, Any]) -> "AccountEdiXmlCii": ...
    def filtered(self, func: Any) -> "AccountEdiXmlCii": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountEdiXmlCii": ...
    def exists(self) -> "AccountEdiXmlCii": ...
    def sudo(self) -> "AccountEdiXmlCii": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountEdiXmlCii": ...

# --- account.edi.xml.ubl_20 ---

class AccountEdiXmlUbl20(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountEdiXmlUbl20": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountEdiXmlUbl20": ...
    def create(self, vals: Dict[str, Any]) -> "AccountEdiXmlUbl20": ...
    def filtered(self, func: Any) -> "AccountEdiXmlUbl20": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountEdiXmlUbl20": ...
    def exists(self) -> "AccountEdiXmlUbl20": ...
    def sudo(self) -> "AccountEdiXmlUbl20": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountEdiXmlUbl20": ...

# --- account.edi.xml.ubl_21 ---

class AccountEdiXmlUbl21(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountEdiXmlUbl21": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountEdiXmlUbl21": ...
    def create(self, vals: Dict[str, Any]) -> "AccountEdiXmlUbl21": ...
    def filtered(self, func: Any) -> "AccountEdiXmlUbl21": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountEdiXmlUbl21": ...
    def exists(self) -> "AccountEdiXmlUbl21": ...
    def sudo(self) -> "AccountEdiXmlUbl21": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountEdiXmlUbl21": ...

# --- account.edi.xml.ubl_bis3 ---

class AccountEdiXmlUblBis3(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountEdiXmlUblBis3": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountEdiXmlUblBis3": ...
    def create(self, vals: Dict[str, Any]) -> "AccountEdiXmlUblBis3": ...
    def filtered(self, func: Any) -> "AccountEdiXmlUblBis3": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountEdiXmlUblBis3": ...
    def exists(self) -> "AccountEdiXmlUblBis3": ...
    def sudo(self) -> "AccountEdiXmlUblBis3": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountEdiXmlUblBis3": ...

# --- account.edi.xml.ubl_de ---

class AccountEdiXmlUblDe(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountEdiXmlUblDe": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountEdiXmlUblDe": ...
    def create(self, vals: Dict[str, Any]) -> "AccountEdiXmlUblDe": ...
    def filtered(self, func: Any) -> "AccountEdiXmlUblDe": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountEdiXmlUblDe": ...
    def exists(self) -> "AccountEdiXmlUblDe": ...
    def sudo(self) -> "AccountEdiXmlUblDe": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountEdiXmlUblDe": ...

# --- account.edi.xml.ubl_efff ---

class AccountEdiXmlUblEfff(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountEdiXmlUblEfff": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountEdiXmlUblEfff": ...
    def create(self, vals: Dict[str, Any]) -> "AccountEdiXmlUblEfff": ...
    def filtered(self, func: Any) -> "AccountEdiXmlUblEfff": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountEdiXmlUblEfff": ...
    def exists(self) -> "AccountEdiXmlUblEfff": ...
    def sudo(self) -> "AccountEdiXmlUblEfff": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountEdiXmlUblEfff": ...

# --- account.edi.xml.ubl_nl ---

class AccountEdiXmlUblNl(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountEdiXmlUblNl": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountEdiXmlUblNl": ...
    def create(self, vals: Dict[str, Any]) -> "AccountEdiXmlUblNl": ...
    def filtered(self, func: Any) -> "AccountEdiXmlUblNl": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountEdiXmlUblNl": ...
    def exists(self) -> "AccountEdiXmlUblNl": ...
    def sudo(self) -> "AccountEdiXmlUblNl": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountEdiXmlUblNl": ...

# --- account.edi.xml.ubl_sg ---

class AccountEdiXmlUblSg(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountEdiXmlUblSg": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountEdiXmlUblSg": ...
    def create(self, vals: Dict[str, Any]) -> "AccountEdiXmlUblSg": ...
    def filtered(self, func: Any) -> "AccountEdiXmlUblSg": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountEdiXmlUblSg": ...
    def exists(self) -> "AccountEdiXmlUblSg": ...
    def sudo(self) -> "AccountEdiXmlUblSg": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountEdiXmlUblSg": ...

# --- account.financial.year.op ---

class AccountFinancialYearOp(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    fiscalyear_last_day: int
    fiscalyear_last_month: str
    has_bit2publish_template: bool
    opening_date: Optional[_dt.date]
    opening_move_posted: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountFinancialYearOp": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountFinancialYearOp": ...
    def create(self, vals: Dict[str, Any]) -> "AccountFinancialYearOp": ...
    def filtered(self, func: Any) -> "AccountFinancialYearOp": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountFinancialYearOp": ...
    def exists(self) -> "AccountFinancialYearOp": ...
    def sudo(self) -> "AccountFinancialYearOp": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountFinancialYearOp": ...

# --- account.fiscal.position ---

class AccountFiscalPosition(Recordset):
    account_ids: "AccountFiscalPositionAccount"
    active: bool
    auto_apply: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    company_country_id: "ResCountry"
    company_id: "ResCompany"
    country_group_id: "ResCountryGroup"
    country_id: "ResCountry"
    foreign_vat: str
    foreign_vat_header_mode: str
    has_bit2publish_template: bool
    name: str
    note: str
    sequence: int
    show_bit2publish_button: bool
    state_ids: "ResCountryState"
    states_count: int
    tax_ids: "AccountFiscalPositionTax"
    vat_required: bool
    zip_from: str
    zip_to: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountFiscalPosition": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountFiscalPosition": ...
    def create(self, vals: Dict[str, Any]) -> "AccountFiscalPosition": ...
    def filtered(self, func: Any) -> "AccountFiscalPosition": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountFiscalPosition": ...
    def exists(self) -> "AccountFiscalPosition": ...
    def sudo(self) -> "AccountFiscalPosition": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountFiscalPosition": ...

# --- account.fiscal.position.account ---

class AccountFiscalPositionAccount(Recordset):
    account_dest_id: "AccountAccount"
    account_src_id: "AccountAccount"
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    has_bit2publish_template: bool
    position_id: "AccountFiscalPosition"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountFiscalPositionAccount": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountFiscalPositionAccount": ...
    def create(self, vals: Dict[str, Any]) -> "AccountFiscalPositionAccount": ...
    def filtered(self, func: Any) -> "AccountFiscalPositionAccount": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountFiscalPositionAccount": ...
    def exists(self) -> "AccountFiscalPositionAccount": ...
    def sudo(self) -> "AccountFiscalPositionAccount": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountFiscalPositionAccount": ...

# --- account.fiscal.position.account.template ---

class AccountFiscalPositionAccountTemplate(Recordset):
    account_dest_id: "AccountAccountTemplate"
    account_src_id: "AccountAccountTemplate"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    position_id: "AccountFiscalPositionTemplate"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountFiscalPositionAccountTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountFiscalPositionAccountTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "AccountFiscalPositionAccountTemplate": ...
    def filtered(self, func: Any) -> "AccountFiscalPositionAccountTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountFiscalPositionAccountTemplate": ...
    def exists(self) -> "AccountFiscalPositionAccountTemplate": ...
    def sudo(self) -> "AccountFiscalPositionAccountTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountFiscalPositionAccountTemplate": ...

# --- account.fiscal.position.tax ---

class AccountFiscalPositionTax(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    has_bit2publish_template: bool
    position_id: "AccountFiscalPosition"
    show_bit2publish_button: bool
    tax_dest_active: bool
    tax_dest_id: "AccountTax"
    tax_src_id: "AccountTax"
    def browse(self, ids: Union[int, List[int]]) -> "AccountFiscalPositionTax": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountFiscalPositionTax": ...
    def create(self, vals: Dict[str, Any]) -> "AccountFiscalPositionTax": ...
    def filtered(self, func: Any) -> "AccountFiscalPositionTax": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountFiscalPositionTax": ...
    def exists(self) -> "AccountFiscalPositionTax": ...
    def sudo(self) -> "AccountFiscalPositionTax": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountFiscalPositionTax": ...

# --- account.fiscal.position.tax.template ---

class AccountFiscalPositionTaxTemplate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    position_id: "AccountFiscalPositionTemplate"
    show_bit2publish_button: bool
    tax_dest_id: "AccountTaxTemplate"
    tax_src_id: "AccountTaxTemplate"
    def browse(self, ids: Union[int, List[int]]) -> "AccountFiscalPositionTaxTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountFiscalPositionTaxTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "AccountFiscalPositionTaxTemplate": ...
    def filtered(self, func: Any) -> "AccountFiscalPositionTaxTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountFiscalPositionTaxTemplate": ...
    def exists(self) -> "AccountFiscalPositionTaxTemplate": ...
    def sudo(self) -> "AccountFiscalPositionTaxTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountFiscalPositionTaxTemplate": ...

# --- account.fiscal.position.template ---

class AccountFiscalPositionTemplate(Recordset):
    account_ids: "AccountFiscalPositionAccountTemplate"
    auto_apply: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    chart_template_id: "AccountChartTemplate"
    country_group_id: "ResCountryGroup"
    country_id: "ResCountry"
    has_bit2publish_template: bool
    name: str
    note: str
    sequence: int
    show_bit2publish_button: bool
    state_ids: "ResCountryState"
    tax_ids: "AccountFiscalPositionTaxTemplate"
    vat_required: bool
    zip_from: str
    zip_to: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountFiscalPositionTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountFiscalPositionTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "AccountFiscalPositionTemplate": ...
    def filtered(self, func: Any) -> "AccountFiscalPositionTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountFiscalPositionTemplate": ...
    def exists(self) -> "AccountFiscalPositionTemplate": ...
    def sudo(self) -> "AccountFiscalPositionTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountFiscalPositionTemplate": ...

# --- account.full.reconcile ---

class AccountFullReconcile(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    exchange_move_id: "AccountMove"
    has_bit2publish_template: bool
    name: str
    partial_reconcile_ids: "AccountPartialReconcile"
    reconciled_line_ids: "AccountMoveLine"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountFullReconcile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountFullReconcile": ...
    def create(self, vals: Dict[str, Any]) -> "AccountFullReconcile": ...
    def filtered(self, func: Any) -> "AccountFullReconcile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountFullReconcile": ...
    def exists(self) -> "AccountFullReconcile": ...
    def sudo(self) -> "AccountFullReconcile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountFullReconcile": ...

# --- account.group ---

class AccountGroup(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code_prefix_end: str
    code_prefix_start: str
    company_id: "ResCompany"
    has_bit2publish_template: bool
    name: str
    parent_id: "AccountGroup"
    parent_path: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountGroup": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountGroup": ...
    def create(self, vals: Dict[str, Any]) -> "AccountGroup": ...
    def filtered(self, func: Any) -> "AccountGroup": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountGroup": ...
    def exists(self) -> "AccountGroup": ...
    def sudo(self) -> "AccountGroup": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountGroup": ...

# --- account.group.template ---

class AccountGroupTemplate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    chart_template_id: "AccountChartTemplate"
    code_prefix_end: str
    code_prefix_start: str
    has_bit2publish_template: bool
    name: str
    parent_id: "AccountGroupTemplate"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountGroupTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountGroupTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "AccountGroupTemplate": ...
    def filtered(self, func: Any) -> "AccountGroupTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountGroupTemplate": ...
    def exists(self) -> "AccountGroupTemplate": ...
    def sudo(self) -> "AccountGroupTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountGroupTemplate": ...

# --- account.incoterms ---

class AccountIncoterms(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountIncoterms": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountIncoterms": ...
    def create(self, vals: Dict[str, Any]) -> "AccountIncoterms": ...
    def filtered(self, func: Any) -> "AccountIncoterms": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountIncoterms": ...
    def exists(self) -> "AccountIncoterms": ...
    def sudo(self) -> "AccountIncoterms": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountIncoterms": ...

# --- account.invoice.report ---

class AccountInvoiceReport(Recordset):
    account_id: "AccountAccount"
    analytic_account_id: "AccountAnalyticAccount"
    bit2publish_template_ids: "Bit2publishTemplate"
    commercial_partner_id: "ResPartner"
    company_currency_id: "ResCurrency"
    company_id: "ResCompany"
    country_id: "ResCountry"
    fiscal_position_id: "AccountFiscalPosition"
    has_bit2publish_template: bool
    invoice_date: Optional[_dt.date]
    invoice_date_due: Optional[_dt.date]
    invoice_user_id: "ResUsers"
    journal_id: "AccountJournal"
    move_id: "AccountMove"
    move_type: str
    partner_id: "ResPartner"
    payment_state: str
    price_average: float
    price_subtotal: float
    product_categ_id: "ProductCategory"
    product_id: "ProductProduct"
    product_uom_id: "UomUom"
    quantity: float
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountInvoiceReport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountInvoiceReport": ...
    def create(self, vals: Dict[str, Any]) -> "AccountInvoiceReport": ...
    def filtered(self, func: Any) -> "AccountInvoiceReport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountInvoiceReport": ...
    def exists(self) -> "AccountInvoiceReport": ...
    def sudo(self) -> "AccountInvoiceReport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountInvoiceReport": ...

# --- account.invoice.send ---

class AccountInvoiceSend(Recordset):
    active_domain: str
    add_sign: bool
    attachment_ids: "IrAttachment"
    author_id: "ResPartner"
    auto_delete: bool
    auto_delete_message: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    campaign_id: "UtmCampaign"
    can_edit_body: bool
    composer_id: "MailComposeMessage"
    composition_mode: str
    copyvalue: str
    email_bcc: str
    email_cc: str
    email_from: str
    has_bit2publish_template: bool
    invalid_addresses: int
    invalid_invoices: int
    invalid_partner_ids: "ResPartner"
    invoice_ids: "AccountMove"
    invoice_without_email: str
    is_email: bool
    is_log: bool
    is_mail_template_editor: bool
    is_pec: bool
    is_print: bool
    lang: str
    layout: str
    mail_activity_type_id: "MailActivityType"
    mailing_list_ids: "MailingList"
    mail_server_id: "IrMailServer"
    marketing_activity_id: "MarketingActivity"
    mass_mailing_id: "MailingMailing"
    mass_mailing_name: str
    message_type: str
    model: str
    model_object_field: "IrModelFields"
    move_types: str
    notify: bool
    null_value: str
    parent_id: "MailMessage"
    partner_id: "ResPartner"
    partner_ids: "ResPartner"
    printed: bool
    record_name: str
    render_model: str
    reply_to: str
    reply_to_force_new: bool
    reply_to_mode: str
    res_id: int
    send_immediately: bool
    show_bit2publish_button: bool
    snailmail_cost: float
    snailmail_is_letter: bool
    subject: str
    sub_model_object_field: "IrModelFields"
    sub_object: "IrModel"
    subtype_id: "MailMessageSubtype"
    template_domain: "MailTemplate"
    template_id: "MailTemplate"
    use_active_domain: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountInvoiceSend": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountInvoiceSend": ...
    def create(self, vals: Dict[str, Any]) -> "AccountInvoiceSend": ...
    def filtered(self, func: Any) -> "AccountInvoiceSend": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountInvoiceSend": ...
    def exists(self) -> "AccountInvoiceSend": ...
    def sudo(self) -> "AccountInvoiceSend": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountInvoiceSend": ...

# --- account.invoice_extract.words ---

class AccountInvoiceExtractWords(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    field: str
    has_bit2publish_template: bool
    invoice_id: "AccountMove"
    selected_status: int
    show_bit2publish_button: bool
    user_selected: bool
    word_box_angle: float
    word_box_height: float
    word_box_midX: float
    word_box_midY: float
    word_box_width: float
    word_page: int
    word_text: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountInvoiceExtractWords": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountInvoiceExtractWords": ...
    def create(self, vals: Dict[str, Any]) -> "AccountInvoiceExtractWords": ...
    def filtered(self, func: Any) -> "AccountInvoiceExtractWords": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountInvoiceExtractWords": ...
    def exists(self) -> "AccountInvoiceExtractWords": ...
    def sudo(self) -> "AccountInvoiceExtractWords": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountInvoiceExtractWords": ...

# --- account.journal ---

class AccountJournal(Recordset):
    account_control_ids: "AccountAccount"
    active: bool
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    alias_domain: str
    alias_id: "MailAlias"
    alias_name: str
    available_payment_method_ids: "AccountPaymentMethod"
    bank_acc_number: str
    bank_account_id: "ResPartnerBank"
    bank_id: "ResBank"
    bank_statements_source: str
    bit2publish_template_ids: "Bit2publishTemplate"
    check_manual_sequencing: bool
    check_next_number: str
    check_sequence_id: "IrSequence"
    code: str
    color: int
    company_id: "ResCompany"
    company_partner_id: "ResPartner"
    compatible_edi_ids: "AccountEdiFormat"
    country_code: str
    currency_id: "ResCurrency"
    default_account_id: "AccountAccount"
    default_account_type: "AccountAccountType"
    edi_format_ids: "AccountEdiFormat"
    entries_count: int
    has_bit2publish_template: bool
    has_message: bool
    inbound_payment_method_line_ids: "AccountPaymentMethodLine"
    invoice_reference_model: str
    invoice_reference_type: str
    journal_group_ids: "AccountJournalGroup"
    json_activity_data: str
    kanban_dashboard: str
    kanban_dashboard_graph: str
    loss_account_id: "AccountAccount"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    outbound_payment_method_line_ids: "AccountPaymentMethodLine"
    profit_account_id: "AccountAccount"
    refund_sequence: bool
    restrict_mode_hash_table: bool
    sale_activity_note: str
    sale_activity_type_id: "MailActivityType"
    sale_activity_user_id: "ResUsers"
    secure_sequence_id: "IrSequence"
    selected_payment_method_codes: str
    sequence: int
    sequence_override_regex: str
    show_bit2publish_button: bool
    show_on_dashboard: bool
    suspense_account_id: "AccountAccount"
    type: str
    type_control_ids: "AccountAccountType"
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "AccountJournal": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountJournal": ...
    def create(self, vals: Dict[str, Any]) -> "AccountJournal": ...
    def filtered(self, func: Any) -> "AccountJournal": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountJournal": ...
    def exists(self) -> "AccountJournal": ...
    def sudo(self) -> "AccountJournal": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountJournal": ...

# --- account.journal.group ---

class AccountJournalGroup(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    excluded_journal_ids: "AccountJournal"
    has_bit2publish_template: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountJournalGroup": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountJournalGroup": ...
    def create(self, vals: Dict[str, Any]) -> "AccountJournalGroup": ...
    def filtered(self, func: Any) -> "AccountJournalGroup": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountJournalGroup": ...
    def exists(self) -> "AccountJournalGroup": ...
    def sudo(self) -> "AccountJournalGroup": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountJournalGroup": ...

# --- account.move ---

class AccountMove(Recordset):
    access_token: str
    access_url: str
    access_warning: str
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    always_tax_exigible: bool
    amount_paid: float
    amount_residual: float
    amount_residual_signed: float
    amount_tax: float
    amount_tax_signed: float
    amount_total: float
    amount_total_in_currency_signed: float
    amount_total_signed: float
    amount_untaxed: float
    amount_untaxed_signed: float
    authorized_transaction_ids: "PaymentTransaction"
    auto_post: bool
    bank_partner_id: "ResPartner"
    bit2publish_template_ids: "Bit2publishTemplate"
    commercial_partner_id: "ResPartner"
    company_currency_id: "ResCurrency"
    company_id: "ResCompany"
    country_code: str
    currency_id: "ResCurrency"
    date: Optional[_dt.date]
    display_inactive_currency_warning: bool
    display_qr_code: bool
    duplicated_vendor_ref: str
    edi_blocking_level: str
    edi_document_ids: "AccountEdiDocument"
    edi_error_count: int
    edi_error_message: str
    edi_show_abandon_cancel_button: bool
    edi_show_cancel_button: bool
    edi_state: str
    edi_web_services_to_process: str
    extract_can_show_resend_button: bool
    extract_can_show_send_button: bool
    extract_error_message: str
    extract_remote_id: int
    extract_state: str
    extract_status_code: int
    extract_word_ids: "AccountInvoiceExtractWords"
    fiscal_position_id: "AccountFiscalPosition"
    has_bit2publish_template: bool
    has_message: bool
    has_reconciled_entries: bool
    highest_name: str
    inalterable_hash: str
    invoice_cash_rounding_id: "AccountCashRounding"
    invoice_date: Optional[_dt.date]
    invoice_date_due: Optional[_dt.date]
    invoice_filter_type_domain: str
    invoice_has_matching_suspense_amount: bool
    invoice_has_outstanding: bool
    invoice_incoterm_id: "AccountIncoterms"
    invoice_line_ids: "AccountMoveLine"
    invoice_origin: str
    invoice_outstanding_credits_debits_widget: str
    invoice_partner_display_name: str
    invoice_payments_widget: str
    invoice_payment_term_id: "AccountPaymentTerm"
    invoice_source_email: str
    invoice_user_id: "ResUsers"
    invoice_vendor_bill_id: "AccountMove"
    is_move_sent: bool
    journal_id: "AccountJournal"
    line_ids: "AccountMoveLine"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    move_type: str
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    narration: str
    partner_bank_id: "ResPartnerBank"
    partner_id: "ResPartner"
    payment_id: "AccountPayment"
    payment_reference: str
    payment_state: str
    posted_before: bool
    preferred_payment_method_id: "AccountPaymentMethod"
    qr_code_method: str
    ref: str
    restrict_mode_hash_table: bool
    reversal_move_id: "AccountMove"
    reversed_entry_id: "AccountMove"
    secure_sequence_number: int
    sequence_number: int
    sequence_prefix: str
    show_bit2publish_button: bool
    show_name_warning: bool
    show_reset_to_draft_button: bool
    state: str
    statement_id: "AccountBankStatement"
    statement_line_id: "AccountBankStatementLine"
    string_to_hash: str
    suitable_journal_ids: "AccountJournal"
    tax_cash_basis_created_move_ids: "AccountMove"
    tax_cash_basis_origin_move_id: "AccountMove"
    tax_cash_basis_rec_id: "AccountPartialReconcile"
    tax_country_code: str
    tax_country_id: "ResCountry"
    tax_lock_date_message: str
    tax_totals_json: str
    to_check: bool
    transaction_ids: "PaymentTransaction"
    type_name: str
    user_id: "ResUsers"
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "AccountMove": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountMove": ...
    def create(self, vals: Dict[str, Any]) -> "AccountMove": ...
    def filtered(self, func: Any) -> "AccountMove": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountMove": ...
    def exists(self) -> "AccountMove": ...
    def sudo(self) -> "AccountMove": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountMove": ...

# --- account.move.line ---

class AccountMoveLine(Recordset):
    account_id: "AccountAccount"
    account_internal_group: str
    account_internal_type: str
    account_root_id: "AccountRoot"
    amount_currency: float
    amount_residual: float
    amount_residual_currency: float
    analytic_account_id: "AccountAnalyticAccount"
    analytic_line_ids: "AccountAnalyticLine"
    analytic_tag_ids: "AccountAnalyticTag"
    balance: float
    bit2publish_template_ids: "Bit2publishTemplate"
    blocked: bool
    company_currency_id: "ResCurrency"
    company_id: "ResCompany"
    credit: float
    cumulated_balance: float
    currency_id: "ResCurrency"
    date: Optional[_dt.date]
    date_maturity: Optional[_dt.date]
    debit: float
    discount: float
    display_type: str
    exclude_from_invoice_tab: bool
    full_reconcile_id: "AccountFullReconcile"
    group_tax_id: "AccountTax"
    has_bit2publish_template: bool
    is_rounding_line: bool
    journal_id: "AccountJournal"
    matched_credit_ids: "AccountPartialReconcile"
    matched_debit_ids: "AccountPartialReconcile"
    matching_number: str
    move_id: "AccountMove"
    move_name: str
    name: str
    parent_state: str
    partner_id: "ResPartner"
    payment_id: "AccountPayment"
    price_subtotal: float
    price_total: float
    price_unit: float
    product_id: "ProductProduct"
    product_uom_category_id: "UomCategory"
    product_uom_id: "UomUom"
    quantity: float
    recompute_tax_line: bool
    reconciled: bool
    reconcile_model_id: "AccountReconcileModel"
    ref: str
    sequence: int
    show_bit2publish_button: bool
    statement_id: "AccountBankStatement"
    statement_line_id: "AccountBankStatementLine"
    tax_audit: str
    tax_base_amount: float
    tax_group_id: "AccountTaxGroup"
    tax_ids: "AccountTax"
    tax_line_id: "AccountTax"
    tax_repartition_line_id: "AccountTaxRepartitionLine"
    tax_tag_ids: "AccountAccountTag"
    tax_tag_invert: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountMoveLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountMoveLine": ...
    def create(self, vals: Dict[str, Any]) -> "AccountMoveLine": ...
    def filtered(self, func: Any) -> "AccountMoveLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountMoveLine": ...
    def exists(self) -> "AccountMoveLine": ...
    def sudo(self) -> "AccountMoveLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountMoveLine": ...

# --- account.move.reversal ---

class AccountMoveReversal(Recordset):
    available_journal_ids: "AccountJournal"
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    country_code: str
    currency_id: "ResCurrency"
    date: Optional[_dt.date]
    date_mode: str
    has_bit2publish_template: bool
    journal_id: "AccountJournal"
    move_ids: "AccountMove"
    move_type: str
    new_move_ids: "AccountMove"
    reason: str
    refund_method: str
    residual: float
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountMoveReversal": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountMoveReversal": ...
    def create(self, vals: Dict[str, Any]) -> "AccountMoveReversal": ...
    def filtered(self, func: Any) -> "AccountMoveReversal": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountMoveReversal": ...
    def exists(self) -> "AccountMoveReversal": ...
    def sudo(self) -> "AccountMoveReversal": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountMoveReversal": ...

# --- account.partial.reconcile ---

class AccountPartialReconcile(Recordset):
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    company_currency_id: "ResCurrency"
    company_id: "ResCompany"
    credit_amount_currency: float
    credit_currency_id: "ResCurrency"
    credit_move_id: "AccountMoveLine"
    debit_amount_currency: float
    debit_currency_id: "ResCurrency"
    debit_move_id: "AccountMoveLine"
    full_reconcile_id: "AccountFullReconcile"
    has_bit2publish_template: bool
    max_date: Optional[_dt.date]
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountPartialReconcile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountPartialReconcile": ...
    def create(self, vals: Dict[str, Any]) -> "AccountPartialReconcile": ...
    def filtered(self, func: Any) -> "AccountPartialReconcile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountPartialReconcile": ...
    def exists(self) -> "AccountPartialReconcile": ...
    def sudo(self) -> "AccountPartialReconcile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountPartialReconcile": ...

# --- account.payment ---

class AccountPayment(Recordset):
    access_token: str
    access_url: str
    access_warning: str
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    always_tax_exigible: bool
    amount: float
    amount_available_for_refund: float
    amount_company_currency_signed: float
    amount_paid: float
    amount_residual: float
    amount_residual_signed: float
    amount_signed: float
    amount_tax: float
    amount_tax_signed: float
    amount_total: float
    amount_total_in_currency_signed: float
    amount_total_signed: float
    amount_untaxed: float
    amount_untaxed_signed: float
    authorized_transaction_ids: "PaymentTransaction"
    auto_post: bool
    available_partner_bank_ids: "ResPartnerBank"
    available_payment_method_line_ids: "AccountPaymentMethodLine"
    bank_partner_id: "ResPartner"
    bit2publish_template_ids: "Bit2publishTemplate"
    check_amount_in_words: str
    check_manual_sequencing: bool
    check_number: str
    commercial_partner_id: "ResPartner"
    company_currency_id: "ResCurrency"
    company_id: "ResCompany"
    country_code: str
    currency_id: "ResCurrency"
    date: Optional[_dt.date]
    destination_account_id: "AccountAccount"
    destination_journal_id: "AccountJournal"
    display_inactive_currency_warning: bool
    display_qr_code: bool
    duplicated_vendor_ref: str
    edi_blocking_level: str
    edi_document_ids: "AccountEdiDocument"
    edi_error_count: int
    edi_error_message: str
    edi_show_abandon_cancel_button: bool
    edi_show_cancel_button: bool
    edi_state: str
    edi_web_services_to_process: str
    extract_can_show_resend_button: bool
    extract_can_show_send_button: bool
    extract_error_message: str
    extract_remote_id: int
    extract_state: str
    extract_status_code: int
    extract_word_ids: "AccountInvoiceExtractWords"
    fiscal_position_id: "AccountFiscalPosition"
    has_bit2publish_template: bool
    has_message: bool
    has_reconciled_entries: bool
    hide_payment_method_line: bool
    highest_name: str
    inalterable_hash: str
    invoice_cash_rounding_id: "AccountCashRounding"
    invoice_date: Optional[_dt.date]
    invoice_date_due: Optional[_dt.date]
    invoice_filter_type_domain: str
    invoice_has_matching_suspense_amount: bool
    invoice_has_outstanding: bool
    invoice_incoterm_id: "AccountIncoterms"
    invoice_line_ids: "AccountMoveLine"
    invoice_origin: str
    invoice_outstanding_credits_debits_widget: str
    invoice_partner_display_name: str
    invoice_payments_widget: str
    invoice_payment_term_id: "AccountPaymentTerm"
    invoice_source_email: str
    invoice_user_id: "ResUsers"
    invoice_vendor_bill_id: "AccountMove"
    is_internal_transfer: bool
    is_matched: bool
    is_move_sent: bool
    is_reconciled: bool
    journal_id: "AccountJournal"
    line_ids: "AccountMoveLine"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    move_id: "AccountMove"
    move_type: str
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    narration: str
    outstanding_account_id: "AccountAccount"
    paired_internal_transfer_payment_id: "AccountPayment"
    partner_bank_id: "ResPartnerBank"
    partner_id: "ResPartner"
    partner_type: str
    payment_id: "AccountPayment"
    payment_method_code: str
    payment_method_id: "AccountPaymentMethod"
    payment_method_line_id: "AccountPaymentMethodLine"
    payment_reference: str
    payment_state: str
    payment_token_id: "PaymentToken"
    payment_transaction_id: "PaymentTransaction"
    payment_type: str
    posted_before: bool
    preferred_payment_method_id: "AccountPaymentMethod"
    qr_code: str
    qr_code_method: str
    reconciled_bill_ids: "AccountMove"
    reconciled_bills_count: int
    reconciled_invoice_ids: "AccountMove"
    reconciled_invoices_count: int
    reconciled_invoices_type: str
    reconciled_statement_ids: "AccountBankStatement"
    reconciled_statements_count: int
    ref: str
    refunds_count: int
    require_partner_bank_account: bool
    restrict_mode_hash_table: bool
    reversal_move_id: "AccountMove"
    reversed_entry_id: "AccountMove"
    secure_sequence_number: int
    sequence_number: int
    sequence_prefix: str
    show_bit2publish_button: bool
    show_name_warning: bool
    show_partner_bank_account: bool
    show_reset_to_draft_button: bool
    source_payment_id: "AccountPayment"
    state: str
    statement_id: "AccountBankStatement"
    statement_line_id: "AccountBankStatementLine"
    string_to_hash: str
    suitable_journal_ids: "AccountJournal"
    suitable_payment_token_ids: "PaymentToken"
    tax_cash_basis_created_move_ids: "AccountMove"
    tax_cash_basis_origin_move_id: "AccountMove"
    tax_cash_basis_rec_id: "AccountPartialReconcile"
    tax_country_code: str
    tax_country_id: "ResCountry"
    tax_lock_date_message: str
    tax_totals_json: str
    to_check: bool
    transaction_ids: "PaymentTransaction"
    type_name: str
    use_electronic_payment_method: bool
    user_id: "ResUsers"
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "AccountPayment": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountPayment": ...
    def create(self, vals: Dict[str, Any]) -> "AccountPayment": ...
    def filtered(self, func: Any) -> "AccountPayment": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountPayment": ...
    def exists(self) -> "AccountPayment": ...
    def sudo(self) -> "AccountPayment": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountPayment": ...

# --- account.payment.method ---

class AccountPaymentMethod(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    has_bit2publish_template: bool
    name: str
    payment_type: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountPaymentMethod": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountPaymentMethod": ...
    def create(self, vals: Dict[str, Any]) -> "AccountPaymentMethod": ...
    def filtered(self, func: Any) -> "AccountPaymentMethod": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountPaymentMethod": ...
    def exists(self) -> "AccountPaymentMethod": ...
    def sudo(self) -> "AccountPaymentMethod": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountPaymentMethod": ...

# --- account.payment.method.line ---

class AccountPaymentMethodLine(Recordset):
    available_payment_method_ids: "AccountPaymentMethod"
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    company_id: "ResCompany"
    has_bit2publish_template: bool
    journal_id: "AccountJournal"
    name: str
    payment_account_id: "AccountAccount"
    payment_acquirer_id: "PaymentAcquirer"
    payment_acquirer_state: str
    payment_method_id: "AccountPaymentMethod"
    payment_type: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountPaymentMethodLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountPaymentMethodLine": ...
    def create(self, vals: Dict[str, Any]) -> "AccountPaymentMethodLine": ...
    def filtered(self, func: Any) -> "AccountPaymentMethodLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountPaymentMethodLine": ...
    def exists(self) -> "AccountPaymentMethodLine": ...
    def sudo(self) -> "AccountPaymentMethodLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountPaymentMethodLine": ...

# --- account.payment.register ---

class AccountPaymentRegister(Recordset):
    amount: float
    available_partner_bank_ids: "ResPartnerBank"
    available_payment_method_line_ids: "AccountPaymentMethodLine"
    bit2publish_template_ids: "Bit2publishTemplate"
    can_edit_wizard: bool
    can_group_payments: bool
    communication: str
    company_currency_id: "ResCurrency"
    company_id: "ResCompany"
    country_code: str
    currency_id: "ResCurrency"
    group_payment: bool
    has_bit2publish_template: bool
    hide_payment_method_line: bool
    journal_id: "AccountJournal"
    line_ids: "AccountMoveLine"
    partner_bank_id: "ResPartnerBank"
    partner_id: "ResPartner"
    partner_type: str
    payment_date: Optional[_dt.date]
    payment_difference: float
    payment_difference_handling: str
    payment_method_code: str
    payment_method_line_id: "AccountPaymentMethodLine"
    payment_token_id: "PaymentToken"
    payment_type: str
    require_partner_bank_account: bool
    show_bit2publish_button: bool
    show_partner_bank_account: bool
    source_amount: float
    source_amount_currency: float
    source_currency_id: "ResCurrency"
    suitable_payment_token_ids: "PaymentToken"
    use_electronic_payment_method: bool
    writeoff_account_id: "AccountAccount"
    writeoff_label: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountPaymentRegister": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountPaymentRegister": ...
    def create(self, vals: Dict[str, Any]) -> "AccountPaymentRegister": ...
    def filtered(self, func: Any) -> "AccountPaymentRegister": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountPaymentRegister": ...
    def exists(self) -> "AccountPaymentRegister": ...
    def sudo(self) -> "AccountPaymentRegister": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountPaymentRegister": ...

# --- account.payment.term ---

class AccountPaymentTerm(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    has_bit2publish_template: bool
    line_ids: "AccountPaymentTermLine"
    name: str
    note: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountPaymentTerm": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountPaymentTerm": ...
    def create(self, vals: Dict[str, Any]) -> "AccountPaymentTerm": ...
    def filtered(self, func: Any) -> "AccountPaymentTerm": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountPaymentTerm": ...
    def exists(self) -> "AccountPaymentTerm": ...
    def sudo(self) -> "AccountPaymentTerm": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountPaymentTerm": ...

# --- account.payment.term.line ---

class AccountPaymentTermLine(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    day_of_the_month: int
    days: int
    has_bit2publish_template: bool
    option: str
    payment_id: "AccountPaymentTerm"
    sequence: int
    show_bit2publish_button: bool
    value: str
    value_amount: float
    def browse(self, ids: Union[int, List[int]]) -> "AccountPaymentTermLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountPaymentTermLine": ...
    def create(self, vals: Dict[str, Any]) -> "AccountPaymentTermLine": ...
    def filtered(self, func: Any) -> "AccountPaymentTermLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountPaymentTermLine": ...
    def exists(self) -> "AccountPaymentTermLine": ...
    def sudo(self) -> "AccountPaymentTermLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountPaymentTermLine": ...

# --- account.print.journal ---

class AccountPrintJournal(Recordset):
    amount_currency: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    date_from: Optional[_dt.date]
    date_to: Optional[_dt.date]
    has_bit2publish_template: bool
    journal_ids: "AccountJournal"
    show_bit2publish_button: bool
    sort_selection: str
    target_move: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountPrintJournal": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountPrintJournal": ...
    def create(self, vals: Dict[str, Any]) -> "AccountPrintJournal": ...
    def filtered(self, func: Any) -> "AccountPrintJournal": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountPrintJournal": ...
    def exists(self) -> "AccountPrintJournal": ...
    def sudo(self) -> "AccountPrintJournal": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountPrintJournal": ...

# --- account.reconcile.model ---

class AccountReconcileModel(Recordset):
    active: bool
    allow_payment_tolerance: bool
    auto_reconcile: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    decimal_separator: str
    has_bit2publish_template: bool
    has_message: bool
    line_ids: "AccountReconcileModelLine"
    match_amount: str
    match_amount_max: float
    match_amount_min: float
    matching_order: str
    match_journal_ids: "AccountJournal"
    match_label: str
    match_label_param: str
    match_nature: str
    match_note: str
    match_note_param: str
    match_partner: bool
    match_partner_category_ids: "ResPartnerCategory"
    match_partner_ids: "ResPartner"
    match_same_currency: bool
    match_text_location_label: bool
    match_text_location_note: bool
    match_text_location_reference: bool
    match_transaction_type: str
    match_transaction_type_param: str
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    name: str
    number_entries: int
    partner_mapping_line_ids: "AccountReconcileModelPartnerMapping"
    past_months_limit: int
    payment_tolerance_param: float
    payment_tolerance_type: str
    rule_type: str
    sequence: int
    show_bit2publish_button: bool
    show_decimal_separator: bool
    to_check: bool
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "AccountReconcileModel": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountReconcileModel": ...
    def create(self, vals: Dict[str, Any]) -> "AccountReconcileModel": ...
    def filtered(self, func: Any) -> "AccountReconcileModel": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountReconcileModel": ...
    def exists(self) -> "AccountReconcileModel": ...
    def sudo(self) -> "AccountReconcileModel": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountReconcileModel": ...

# --- account.reconcile.model.line ---

class AccountReconcileModelLine(Recordset):
    account_id: "AccountAccount"
    allow_payment_tolerance: bool
    amount: float
    amount_string: str
    amount_type: str
    analytic_account_id: "AccountAnalyticAccount"
    analytic_tag_ids: "AccountAnalyticTag"
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    force_tax_included: bool
    has_bit2publish_template: bool
    journal_id: "AccountJournal"
    label: str
    model_id: "AccountReconcileModel"
    payment_tolerance_param: float
    rule_type: str
    sequence: int
    show_bit2publish_button: bool
    show_force_tax_included: bool
    tax_ids: "AccountTax"
    def browse(self, ids: Union[int, List[int]]) -> "AccountReconcileModelLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountReconcileModelLine": ...
    def create(self, vals: Dict[str, Any]) -> "AccountReconcileModelLine": ...
    def filtered(self, func: Any) -> "AccountReconcileModelLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountReconcileModelLine": ...
    def exists(self) -> "AccountReconcileModelLine": ...
    def sudo(self) -> "AccountReconcileModelLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountReconcileModelLine": ...

# --- account.reconcile.model.line.template ---

class AccountReconcileModelLineTemplate(Recordset):
    account_id: "AccountAccountTemplate"
    amount_string: str
    amount_type: str
    bit2publish_template_ids: "Bit2publishTemplate"
    force_tax_included: bool
    has_bit2publish_template: bool
    label: str
    model_id: "AccountReconcileModelTemplate"
    sequence: int
    show_bit2publish_button: bool
    tax_ids: "AccountTaxTemplate"
    def browse(self, ids: Union[int, List[int]]) -> "AccountReconcileModelLineTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountReconcileModelLineTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "AccountReconcileModelLineTemplate": ...
    def filtered(self, func: Any) -> "AccountReconcileModelLineTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountReconcileModelLineTemplate": ...
    def exists(self) -> "AccountReconcileModelLineTemplate": ...
    def sudo(self) -> "AccountReconcileModelLineTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountReconcileModelLineTemplate": ...

# --- account.reconcile.model.partner.mapping ---

class AccountReconcileModelPartnerMapping(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    model_id: "AccountReconcileModel"
    narration_regex: str
    partner_id: "ResPartner"
    payment_ref_regex: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountReconcileModelPartnerMapping": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountReconcileModelPartnerMapping": ...
    def create(self, vals: Dict[str, Any]) -> "AccountReconcileModelPartnerMapping": ...
    def filtered(self, func: Any) -> "AccountReconcileModelPartnerMapping": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountReconcileModelPartnerMapping": ...
    def exists(self) -> "AccountReconcileModelPartnerMapping": ...
    def sudo(self) -> "AccountReconcileModelPartnerMapping": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountReconcileModelPartnerMapping": ...

# --- account.reconcile.model.template ---

class AccountReconcileModelTemplate(Recordset):
    allow_payment_tolerance: bool
    auto_reconcile: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    chart_template_id: "AccountChartTemplate"
    decimal_separator: str
    has_bit2publish_template: bool
    line_ids: "AccountReconcileModelLineTemplate"
    match_amount: str
    match_amount_max: float
    match_amount_min: float
    matching_order: str
    match_journal_ids: "AccountJournal"
    match_label: str
    match_label_param: str
    match_nature: str
    match_note: str
    match_note_param: str
    match_partner: bool
    match_partner_category_ids: "ResPartnerCategory"
    match_partner_ids: "ResPartner"
    match_same_currency: bool
    match_text_location_label: bool
    match_text_location_note: bool
    match_text_location_reference: bool
    match_transaction_type: str
    match_transaction_type_param: str
    name: str
    payment_tolerance_param: float
    payment_tolerance_type: str
    rule_type: str
    sequence: int
    show_bit2publish_button: bool
    to_check: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountReconcileModelTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountReconcileModelTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "AccountReconcileModelTemplate": ...
    def filtered(self, func: Any) -> "AccountReconcileModelTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountReconcileModelTemplate": ...
    def exists(self) -> "AccountReconcileModelTemplate": ...
    def sudo(self) -> "AccountReconcileModelTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountReconcileModelTemplate": ...

# --- account.resequence.wizard ---

class AccountResequenceWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    end_date: Optional[_dt.date]
    first_date: Optional[_dt.date]
    first_name: str
    has_bit2publish_template: bool
    move_ids: "AccountMove"
    new_values: str
    ordering: str
    preview_moves: str
    sequence_number_reset: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountResequenceWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountResequenceWizard": ...
    def create(self, vals: Dict[str, Any]) -> "AccountResequenceWizard": ...
    def filtered(self, func: Any) -> "AccountResequenceWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountResequenceWizard": ...
    def exists(self) -> "AccountResequenceWizard": ...
    def sudo(self) -> "AccountResequenceWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountResequenceWizard": ...

# --- account.root ---

class AccountRoot(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    has_bit2publish_template: bool
    name: str
    parent_id: "AccountRoot"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountRoot": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountRoot": ...
    def create(self, vals: Dict[str, Any]) -> "AccountRoot": ...
    def filtered(self, func: Any) -> "AccountRoot": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountRoot": ...
    def exists(self) -> "AccountRoot": ...
    def sudo(self) -> "AccountRoot": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountRoot": ...

# --- account.setup.bank.manual.config ---

class AccountSetupBankManualConfig(Recordset):
    acc_holder_name: str
    acc_number: str
    acc_type: str
    active: bool
    bank_bic: str
    bank_id: "ResBank"
    bank_name: str
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    currency_id: "ResCurrency"
    has_bit2publish_template: bool
    journal_id: "AccountJournal"
    linked_journal_id: "AccountJournal"
    new_journal_name: str
    num_journals_without_account: int
    partner_id: "ResPartner"
    res_partner_bank_id: "ResPartnerBank"
    sanitized_acc_number: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountSetupBankManualConfig": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountSetupBankManualConfig": ...
    def create(self, vals: Dict[str, Any]) -> "AccountSetupBankManualConfig": ...
    def filtered(self, func: Any) -> "AccountSetupBankManualConfig": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountSetupBankManualConfig": ...
    def exists(self) -> "AccountSetupBankManualConfig": ...
    def sudo(self) -> "AccountSetupBankManualConfig": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountSetupBankManualConfig": ...

# --- account.tax ---

class AccountTax(Recordset):
    active: bool
    amount: float
    amount_type: str
    analytic: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    cash_basis_transition_account_id: "AccountAccount"
    children_tax_ids: "AccountTax"
    company_id: "ResCompany"
    country_code: str
    country_id: "ResCountry"
    description: str
    has_bit2publish_template: bool
    hide_tax_exigibility: bool
    include_base_amount: bool
    invoice_repartition_line_ids: "AccountTaxRepartitionLine"
    is_base_affected: bool
    name: str
    price_include: bool
    refund_repartition_line_ids: "AccountTaxRepartitionLine"
    sequence: int
    show_bit2publish_button: bool
    tax_exigibility: str
    tax_group_id: "AccountTaxGroup"
    tax_scope: str
    type_tax_use: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountTax": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountTax": ...
    def create(self, vals: Dict[str, Any]) -> "AccountTax": ...
    def filtered(self, func: Any) -> "AccountTax": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountTax": ...
    def exists(self) -> "AccountTax": ...
    def sudo(self) -> "AccountTax": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountTax": ...

# --- account.tax.carryover.line ---

class AccountTaxCarryoverLine(Recordset):
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    date: Optional[_dt.date]
    foreign_vat_fiscal_position_id: "AccountFiscalPosition"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    tax_report_country_id: "ResCountry"
    tax_report_id: "AccountTaxReport"
    tax_report_line_id: "AccountTaxReportLine"
    def browse(self, ids: Union[int, List[int]]) -> "AccountTaxCarryoverLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountTaxCarryoverLine": ...
    def create(self, vals: Dict[str, Any]) -> "AccountTaxCarryoverLine": ...
    def filtered(self, func: Any) -> "AccountTaxCarryoverLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountTaxCarryoverLine": ...
    def exists(self) -> "AccountTaxCarryoverLine": ...
    def sudo(self) -> "AccountTaxCarryoverLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountTaxCarryoverLine": ...

# --- account.tax.group ---

class AccountTaxGroup(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    country_id: "ResCountry"
    has_bit2publish_template: bool
    name: str
    preceding_subtotal: str
    property_advance_tax_payment_account_id: "AccountAccount"
    property_tax_payable_account_id: "AccountAccount"
    property_tax_receivable_account_id: "AccountAccount"
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountTaxGroup": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountTaxGroup": ...
    def create(self, vals: Dict[str, Any]) -> "AccountTaxGroup": ...
    def filtered(self, func: Any) -> "AccountTaxGroup": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountTaxGroup": ...
    def exists(self) -> "AccountTaxGroup": ...
    def sudo(self) -> "AccountTaxGroup": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountTaxGroup": ...

# --- account.tax.repartition.line ---

class AccountTaxRepartitionLine(Recordset):
    account_id: "AccountAccount"
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    factor: float
    factor_percent: float
    has_bit2publish_template: bool
    invoice_tax_id: "AccountTax"
    refund_tax_id: "AccountTax"
    repartition_type: str
    sequence: int
    show_bit2publish_button: bool
    tag_ids: "AccountAccountTag"
    tag_ids_domain: bytes
    tax_id: "AccountTax"
    use_in_tax_closing: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountTaxRepartitionLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountTaxRepartitionLine": ...
    def create(self, vals: Dict[str, Any]) -> "AccountTaxRepartitionLine": ...
    def filtered(self, func: Any) -> "AccountTaxRepartitionLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountTaxRepartitionLine": ...
    def exists(self) -> "AccountTaxRepartitionLine": ...
    def sudo(self) -> "AccountTaxRepartitionLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountTaxRepartitionLine": ...

# --- account.tax.repartition.line.template ---

class AccountTaxRepartitionLineTemplate(Recordset):
    account_id: "AccountAccountTemplate"
    bit2publish_template_ids: "Bit2publishTemplate"
    factor_percent: float
    has_bit2publish_template: bool
    invoice_tax_id: "AccountTaxTemplate"
    minus_report_line_ids: "AccountTaxReportLine"
    plus_report_line_ids: "AccountTaxReportLine"
    refund_tax_id: "AccountTaxTemplate"
    repartition_type: str
    show_bit2publish_button: bool
    tag_ids: "AccountAccountTag"
    use_in_tax_closing: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountTaxRepartitionLineTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountTaxRepartitionLineTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "AccountTaxRepartitionLineTemplate": ...
    def filtered(self, func: Any) -> "AccountTaxRepartitionLineTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountTaxRepartitionLineTemplate": ...
    def exists(self) -> "AccountTaxRepartitionLineTemplate": ...
    def sudo(self) -> "AccountTaxRepartitionLineTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountTaxRepartitionLineTemplate": ...

# --- account.tax.report ---

class AccountTaxReport(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    country_id: "ResCountry"
    has_bit2publish_template: bool
    line_ids: "AccountTaxReportLine"
    name: str
    root_line_ids: "AccountTaxReportLine"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountTaxReport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountTaxReport": ...
    def create(self, vals: Dict[str, Any]) -> "AccountTaxReport": ...
    def filtered(self, func: Any) -> "AccountTaxReport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountTaxReport": ...
    def exists(self) -> "AccountTaxReport": ...
    def sudo(self) -> "AccountTaxReport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountTaxReport": ...

# --- account.tax.report.line ---

class AccountTaxReportLine(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    carry_over_condition_method: str
    carry_over_destination_line_id: "AccountTaxReportLine"
    carryover_line_ids: "AccountTaxCarryoverLine"
    children_line_ids: "AccountTaxReportLine"
    code: str
    formula: str
    has_bit2publish_template: bool
    is_carryover_persistent: bool
    is_carryover_used_in_balance: bool
    name: str
    parent_id: "AccountTaxReportLine"
    parent_path: str
    report_action_id: "IrActionsActWindow"
    report_id: "AccountTaxReport"
    sequence: int
    show_bit2publish_button: bool
    tag_ids: "AccountAccountTag"
    tag_name: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountTaxReportLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountTaxReportLine": ...
    def create(self, vals: Dict[str, Any]) -> "AccountTaxReportLine": ...
    def filtered(self, func: Any) -> "AccountTaxReportLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountTaxReportLine": ...
    def exists(self) -> "AccountTaxReportLine": ...
    def sudo(self) -> "AccountTaxReportLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountTaxReportLine": ...

# --- account.tax.template ---

class AccountTaxTemplate(Recordset):
    active: bool
    amount: float
    amount_type: str
    analytic: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    cash_basis_transition_account_id: "AccountAccountTemplate"
    chart_template_id: "AccountChartTemplate"
    children_tax_ids: "AccountTaxTemplate"
    description: str
    has_bit2publish_template: bool
    include_base_amount: bool
    invoice_repartition_line_ids: "AccountTaxRepartitionLineTemplate"
    is_base_affected: bool
    name: str
    price_include: bool
    refund_repartition_line_ids: "AccountTaxRepartitionLineTemplate"
    sequence: int
    show_bit2publish_button: bool
    tax_exigibility: str
    tax_group_id: "AccountTaxGroup"
    tax_scope: str
    type_tax_use: str
    def browse(self, ids: Union[int, List[int]]) -> "AccountTaxTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountTaxTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "AccountTaxTemplate": ...
    def filtered(self, func: Any) -> "AccountTaxTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountTaxTemplate": ...
    def exists(self) -> "AccountTaxTemplate": ...
    def sudo(self) -> "AccountTaxTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountTaxTemplate": ...

# --- account.tour.upload.bill ---

class AccountTourUploadBill(Recordset):
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    preview_invoice: str
    selection: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountTourUploadBill": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountTourUploadBill": ...
    def create(self, vals: Dict[str, Any]) -> "AccountTourUploadBill": ...
    def filtered(self, func: Any) -> "AccountTourUploadBill": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountTourUploadBill": ...
    def exists(self) -> "AccountTourUploadBill": ...
    def sudo(self) -> "AccountTourUploadBill": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountTourUploadBill": ...

# --- account.tour.upload.bill.email.confirm ---

class AccountTourUploadBillEmailConfirm(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    email_alias: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountTourUploadBillEmailConfirm": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountTourUploadBillEmailConfirm": ...
    def create(self, vals: Dict[str, Any]) -> "AccountTourUploadBillEmailConfirm": ...
    def filtered(self, func: Any) -> "AccountTourUploadBillEmailConfirm": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountTourUploadBillEmailConfirm": ...
    def exists(self) -> "AccountTourUploadBillEmailConfirm": ...
    def sudo(self) -> "AccountTourUploadBillEmailConfirm": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountTourUploadBillEmailConfirm": ...

# --- account.unreconcile ---

class AccountUnreconcile(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AccountUnreconcile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AccountUnreconcile": ...
    def create(self, vals: Dict[str, Any]) -> "AccountUnreconcile": ...
    def filtered(self, func: Any) -> "AccountUnreconcile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AccountUnreconcile": ...
    def exists(self) -> "AccountUnreconcile": ...
    def sudo(self) -> "AccountUnreconcile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AccountUnreconcile": ...

# --- annulment.reason ---

class AnnulmentReason(Recordset):
    annulment_paperwork: str
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    has_bit2publish_template: bool
    reason_code: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AnnulmentReason": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AnnulmentReason": ...
    def create(self, vals: Dict[str, Any]) -> "AnnulmentReason": ...
    def filtered(self, func: Any) -> "AnnulmentReason": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AnnulmentReason": ...
    def exists(self) -> "AnnulmentReason": ...
    def sudo(self) -> "AnnulmentReason": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AnnulmentReason": ...

# --- ateco.category ---

class AtecoCategory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    child_ids: "AtecoCategory"
    code: str
    description: str
    has_bit2publish_template: bool
    name: str
    parent_id: "AtecoCategory"
    partner_ids: "ResPartner"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AtecoCategory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AtecoCategory": ...
    def create(self, vals: Dict[str, Any]) -> "AtecoCategory": ...
    def filtered(self, func: Any) -> "AtecoCategory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AtecoCategory": ...
    def exists(self) -> "AtecoCategory": ...
    def sudo(self) -> "AtecoCategory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AtecoCategory": ...

# --- auth.saml.attribute.mapping ---

class AuthSamlAttributeMapping(Recordset):
    attribute_name: str
    bit2publish_template_ids: "Bit2publishTemplate"
    field_name: str
    has_bit2publish_template: bool
    provider_id: "AuthSamlProvider"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AuthSamlAttributeMapping": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AuthSamlAttributeMapping": ...
    def create(self, vals: Dict[str, Any]) -> "AuthSamlAttributeMapping": ...
    def filtered(self, func: Any) -> "AuthSamlAttributeMapping": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AuthSamlAttributeMapping": ...
    def exists(self) -> "AuthSamlAttributeMapping": ...
    def sudo(self) -> "AuthSamlAttributeMapping": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AuthSamlAttributeMapping": ...

# --- auth.saml.provider ---

class AuthSamlProvider(Recordset):
    active: bool
    attribute_mapping_ids: "AuthSamlAttributeMapping"
    authn_requests_signed: bool
    autoredirect: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    css_class: str
    entity_id: str
    has_bit2publish_template: bool
    idp_metadata: str
    logout_requests_signed: bool
    matching_attribute: str
    matching_attribute_to_lower: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    sig_alg: str
    sign_authenticate_requests: bool
    sign_metadata: bool
    sp_baseurl: str
    sp_metadata_url: str
    sp_pem_private: bytes
    sp_pem_private_filename: str
    sp_pem_public: bytes
    sp_pem_public_filename: str
    want_assertions_or_response_signed: bool
    want_assertions_signed: bool
    want_response_signed: bool
    def browse(self, ids: Union[int, List[int]]) -> "AuthSamlProvider": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AuthSamlProvider": ...
    def create(self, vals: Dict[str, Any]) -> "AuthSamlProvider": ...
    def filtered(self, func: Any) -> "AuthSamlProvider": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AuthSamlProvider": ...
    def exists(self) -> "AuthSamlProvider": ...
    def sudo(self) -> "AuthSamlProvider": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AuthSamlProvider": ...

# --- auth_saml.request ---

class AuthSamlRequest(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    saml_provider_id: "AuthSamlProvider"
    saml_request_id: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AuthSamlRequest": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AuthSamlRequest": ...
    def create(self, vals: Dict[str, Any]) -> "AuthSamlRequest": ...
    def filtered(self, func: Any) -> "AuthSamlRequest": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AuthSamlRequest": ...
    def exists(self) -> "AuthSamlRequest": ...
    def sudo(self) -> "AuthSamlRequest": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AuthSamlRequest": ...

# --- auth_totp.device ---

class AuthTotpDevice(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    scope: str
    show_bit2publish_button: bool
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "AuthTotpDevice": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AuthTotpDevice": ...
    def create(self, vals: Dict[str, Any]) -> "AuthTotpDevice": ...
    def filtered(self, func: Any) -> "AuthTotpDevice": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AuthTotpDevice": ...
    def exists(self) -> "AuthTotpDevice": ...
    def sudo(self) -> "AuthTotpDevice": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AuthTotpDevice": ...

# --- auth_totp.wizard ---

class AuthTotpWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    has_bit2publish_template: bool
    qrcode: bytes
    secret: str
    show_bit2publish_button: bool
    url: str
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "AuthTotpWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AuthTotpWizard": ...
    def create(self, vals: Dict[str, Any]) -> "AuthTotpWizard": ...
    def filtered(self, func: Any) -> "AuthTotpWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AuthTotpWizard": ...
    def exists(self) -> "AuthTotpWizard": ...
    def sudo(self) -> "AuthTotpWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AuthTotpWizard": ...

# --- automatic.email.selector ---

class AutomaticEmailSelector(Recordset):
    allowed_phase_result_ids: "SympleTripletPhaseResult"
    automatic_template_id: "MailTemplate"
    bit2publish_template_ids: "Bit2publishTemplate"
    domain: str
    has_bit2publish_template: bool
    phase_id: "SympleTripletPhase"
    show_bit2publish_button: bool
    triplet_phase_result_id: "SympleTripletPhaseResult"
    def browse(self, ids: Union[int, List[int]]) -> "AutomaticEmailSelector": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AutomaticEmailSelector": ...
    def create(self, vals: Dict[str, Any]) -> "AutomaticEmailSelector": ...
    def filtered(self, func: Any) -> "AutomaticEmailSelector": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AutomaticEmailSelector": ...
    def exists(self) -> "AutomaticEmailSelector": ...
    def sudo(self) -> "AutomaticEmailSelector": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AutomaticEmailSelector": ...

# --- automatic.insurance.service ---

class AutomaticInsuranceService(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_type: str
    engaged_power_max: float
    engaged_power_min: float
    has_bit2publish_template: bool
    insurance_service: str
    is_vulnerable: bool
    pod_use: str
    sequence: int
    show_bit2publish_button: bool
    tension_type: str
    def browse(self, ids: Union[int, List[int]]) -> "AutomaticInsuranceService": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AutomaticInsuranceService": ...
    def create(self, vals: Dict[str, Any]) -> "AutomaticInsuranceService": ...
    def filtered(self, func: Any) -> "AutomaticInsuranceService": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AutomaticInsuranceService": ...
    def exists(self) -> "AutomaticInsuranceService": ...
    def sudo(self) -> "AutomaticInsuranceService": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AutomaticInsuranceService": ...

# --- automatic.postalizer.selector ---

class AutomaticPostalizerSelector(Recordset):
    automatic_template_id: "PostalizerTemplate"
    bit2publish_template_ids: "Bit2publishTemplate"
    domain: str
    has_bit2publish_template: bool
    phase_id: "SympleTripletPhase"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AutomaticPostalizerSelector": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AutomaticPostalizerSelector": ...
    def create(self, vals: Dict[str, Any]) -> "AutomaticPostalizerSelector": ...
    def filtered(self, func: Any) -> "AutomaticPostalizerSelector": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AutomaticPostalizerSelector": ...
    def exists(self) -> "AutomaticPostalizerSelector": ...
    def sudo(self) -> "AutomaticPostalizerSelector": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AutomaticPostalizerSelector": ...

# --- avatar.mixin ---

class AvatarMixin(Recordset):
    avatar_1024: bytes
    avatar_128: bytes
    avatar_1920: bytes
    avatar_256: bytes
    avatar_512: bytes
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    image_1024: bytes
    image_128: bytes
    image_1920: bytes
    image_256: bytes
    image_512: bytes
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "AvatarMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "AvatarMixin": ...
    def create(self, vals: Dict[str, Any]) -> "AvatarMixin": ...
    def filtered(self, func: Any) -> "AvatarMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "AvatarMixin": ...
    def exists(self) -> "AvatarMixin": ...
    def sudo(self) -> "AvatarMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "AvatarMixin": ...

# --- base ---

class Base(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "Base": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "Base": ...
    def create(self, vals: Dict[str, Any]) -> "Base": ...
    def filtered(self, func: Any) -> "Base": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "Base": ...
    def exists(self) -> "Base": ...
    def sudo(self) -> "Base": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "Base": ...

# --- base.automation ---

class BaseAutomation(Recordset):
    action_server_id: "IrActionsServer"
    active: bool
    activity_date_deadline_range: int
    activity_date_deadline_range_type: str
    activity_note: str
    activity_summary: str
    activity_type_id: "MailActivityType"
    activity_user_field_name: str
    activity_user_id: "ResUsers"
    activity_user_type: str
    binding_model_id: "IrModel"
    binding_type: str
    binding_view_types: str
    bit2publish_template_ids: "Bit2publishTemplate"
    child_ids: "IrActionsServer"
    code: str
    crud_model_id: "IrModel"
    crud_model_name: str
    fields_lines: "IrServerObjectLines"
    filter_domain: str
    filter_pre_domain: str
    groups_id: "ResGroups"
    has_bit2publish_template: bool
    help: str
    last_run: Optional[_dt.datetime]
    least_delay_msg: str
    link_field_id: "IrModelFields"
    model_id: "IrModel"
    model_name: str
    name: str
    on_change_field_ids: "IrModelFields"
    partner_ids: "ResPartner"
    sequence: int
    show_bit2publish_button: bool
    sms_mass_keep_log: bool
    sms_template_id: "SmsTemplate"
    state: str
    template_id: "MailTemplate"
    trg_date_calendar_id: "ResourceCalendar"
    trg_date_id: "IrModelFields"
    trg_date_range: int
    trg_date_range_type: str
    trigger: str
    trigger_field_ids: "IrModelFields"
    type: str
    usage: str
    xml_id: str
    def browse(self, ids: Union[int, List[int]]) -> "BaseAutomation": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseAutomation": ...
    def create(self, vals: Dict[str, Any]) -> "BaseAutomation": ...
    def filtered(self, func: Any) -> "BaseAutomation": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseAutomation": ...
    def exists(self) -> "BaseAutomation": ...
    def sudo(self) -> "BaseAutomation": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseAutomation": ...

# --- base.document.layout ---

class BaseDocumentLayout(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_details: str
    company_id: "ResCompany"
    country_id: "ResCountry"
    custom_colors: bool
    email: str
    external_report_layout_id: "IrUiView"
    font: str
    has_bit2publish_template: bool
    layout_background: str
    layout_background_image: bytes
    logo: bytes
    logo_primary_color: str
    logo_secondary_color: str
    name: str
    paperformat_id: "ReportPaperformat"
    partner_id: "ResPartner"
    phone: str
    preview: str
    preview_logo: bytes
    primary_color: str
    report_footer: str
    report_header: str
    report_layout_id: "ReportLayout"
    secondary_color: str
    show_bit2publish_button: bool
    vat: str
    website: str
    def browse(self, ids: Union[int, List[int]]) -> "BaseDocumentLayout": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseDocumentLayout": ...
    def create(self, vals: Dict[str, Any]) -> "BaseDocumentLayout": ...
    def filtered(self, func: Any) -> "BaseDocumentLayout": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseDocumentLayout": ...
    def exists(self) -> "BaseDocumentLayout": ...
    def sudo(self) -> "BaseDocumentLayout": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseDocumentLayout": ...

# --- base.enable.profiling.wizard ---

class BaseEnableProfilingWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    duration: str
    expiration: Optional[_dt.datetime]
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BaseEnableProfilingWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseEnableProfilingWizard": ...
    def create(self, vals: Dict[str, Any]) -> "BaseEnableProfilingWizard": ...
    def filtered(self, func: Any) -> "BaseEnableProfilingWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseEnableProfilingWizard": ...
    def exists(self) -> "BaseEnableProfilingWizard": ...
    def sudo(self) -> "BaseEnableProfilingWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseEnableProfilingWizard": ...

# --- base.import.module ---

class BaseImportModule(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    force: bool
    has_bit2publish_template: bool
    import_message: str
    module_file: bytes
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportModule": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportModule": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportModule": ...
    def filtered(self, func: Any) -> "BaseImportModule": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportModule": ...
    def exists(self) -> "BaseImportModule": ...
    def sudo(self) -> "BaseImportModule": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportModule": ...

# --- base.language.export ---

class BaseLanguageExport(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    format: str
    has_bit2publish_template: bool
    lang: str
    modules: "IrModuleModule"
    name: str
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "BaseLanguageExport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseLanguageExport": ...
    def create(self, vals: Dict[str, Any]) -> "BaseLanguageExport": ...
    def filtered(self, func: Any) -> "BaseLanguageExport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseLanguageExport": ...
    def exists(self) -> "BaseLanguageExport": ...
    def sudo(self) -> "BaseLanguageExport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseLanguageExport": ...

# --- base.language.import ---

class BaseLanguageImport(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    data: bytes
    filename: str
    has_bit2publish_template: bool
    name: str
    overwrite: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BaseLanguageImport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseLanguageImport": ...
    def create(self, vals: Dict[str, Any]) -> "BaseLanguageImport": ...
    def filtered(self, func: Any) -> "BaseLanguageImport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseLanguageImport": ...
    def exists(self) -> "BaseLanguageImport": ...
    def sudo(self) -> "BaseLanguageImport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseLanguageImport": ...

# --- base.language.install ---

class BaseLanguageInstall(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    lang: str
    overwrite: bool
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "BaseLanguageInstall": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseLanguageInstall": ...
    def create(self, vals: Dict[str, Any]) -> "BaseLanguageInstall": ...
    def filtered(self, func: Any) -> "BaseLanguageInstall": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseLanguageInstall": ...
    def exists(self) -> "BaseLanguageInstall": ...
    def sudo(self) -> "BaseLanguageInstall": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseLanguageInstall": ...

# --- base.module.uninstall ---

class BaseModuleUninstall(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    custom_fields: int
    custom_models: int
    custom_reports: int
    custom_views: int
    has_bit2publish_template: bool
    is_studio: bool
    model_ids: "IrModel"
    module_id: "IrModuleModule"
    module_ids: "IrModuleModule"
    show_all: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BaseModuleUninstall": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseModuleUninstall": ...
    def create(self, vals: Dict[str, Any]) -> "BaseModuleUninstall": ...
    def filtered(self, func: Any) -> "BaseModuleUninstall": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseModuleUninstall": ...
    def exists(self) -> "BaseModuleUninstall": ...
    def sudo(self) -> "BaseModuleUninstall": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseModuleUninstall": ...

# --- base.module.update ---

class BaseModuleUpdate(Recordset):
    added: int
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    state: str
    updated: int
    def browse(self, ids: Union[int, List[int]]) -> "BaseModuleUpdate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseModuleUpdate": ...
    def create(self, vals: Dict[str, Any]) -> "BaseModuleUpdate": ...
    def filtered(self, func: Any) -> "BaseModuleUpdate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseModuleUpdate": ...
    def exists(self) -> "BaseModuleUpdate": ...
    def sudo(self) -> "BaseModuleUpdate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseModuleUpdate": ...

# --- base.module.upgrade ---

class BaseModuleUpgrade(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    module_info: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BaseModuleUpgrade": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseModuleUpgrade": ...
    def create(self, vals: Dict[str, Any]) -> "BaseModuleUpgrade": ...
    def filtered(self, func: Any) -> "BaseModuleUpgrade": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseModuleUpgrade": ...
    def exists(self) -> "BaseModuleUpgrade": ...
    def sudo(self) -> "BaseModuleUpgrade": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseModuleUpgrade": ...

# --- base.partner.merge.automatic.wizard ---

class BasePartnerMergeAutomaticWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    current_line_id: "BasePartnerMergeLine"
    dst_partner_id: "ResPartner"
    exclude_contact: bool
    exclude_journal_item: bool
    group_by_email: bool
    group_by_is_company: bool
    group_by_name: bool
    group_by_parent_id: bool
    group_by_vat: bool
    has_bit2publish_template: bool
    line_ids: "BasePartnerMergeLine"
    maximum_group: int
    number_group: int
    partner_ids: "ResPartner"
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "BasePartnerMergeAutomaticWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BasePartnerMergeAutomaticWizard": ...
    def create(self, vals: Dict[str, Any]) -> "BasePartnerMergeAutomaticWizard": ...
    def filtered(self, func: Any) -> "BasePartnerMergeAutomaticWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BasePartnerMergeAutomaticWizard": ...
    def exists(self) -> "BasePartnerMergeAutomaticWizard": ...
    def sudo(self) -> "BasePartnerMergeAutomaticWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BasePartnerMergeAutomaticWizard": ...

# --- base.partner.merge.line ---

class BasePartnerMergeLine(Recordset):
    aggr_ids: str
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    min_id: int
    show_bit2publish_button: bool
    wizard_id: "BasePartnerMergeAutomaticWizard"
    def browse(self, ids: Union[int, List[int]]) -> "BasePartnerMergeLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BasePartnerMergeLine": ...
    def create(self, vals: Dict[str, Any]) -> "BasePartnerMergeLine": ...
    def filtered(self, func: Any) -> "BasePartnerMergeLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BasePartnerMergeLine": ...
    def exists(self) -> "BasePartnerMergeLine": ...
    def sudo(self) -> "BasePartnerMergeLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BasePartnerMergeLine": ...

# --- base.update.translations ---

class BaseUpdateTranslations(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    lang: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BaseUpdateTranslations": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseUpdateTranslations": ...
    def create(self, vals: Dict[str, Any]) -> "BaseUpdateTranslations": ...
    def filtered(self, func: Any) -> "BaseUpdateTranslations": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseUpdateTranslations": ...
    def exists(self) -> "BaseUpdateTranslations": ...
    def sudo(self) -> "BaseUpdateTranslations": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseUpdateTranslations": ...

# --- base_import.import ---

class BaseImportImport(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    file: bytes
    file_name: str
    file_type: str
    has_bit2publish_template: bool
    res_model: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportImport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportImport": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportImport": ...
    def filtered(self, func: Any) -> "BaseImportImport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportImport": ...
    def exists(self) -> "BaseImportImport": ...
    def sudo(self) -> "BaseImportImport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportImport": ...

# --- base_import.mapping ---

class BaseImportMapping(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    column_name: str
    field_name: str
    has_bit2publish_template: bool
    res_model: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportMapping": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportMapping": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportMapping": ...
    def filtered(self, func: Any) -> "BaseImportMapping": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportMapping": ...
    def exists(self) -> "BaseImportMapping": ...
    def sudo(self) -> "BaseImportMapping": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportMapping": ...

# --- base_import.tests.models.char ---

class BaseImportTestsModelsChar(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsChar": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsChar": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsChar": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsChar": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsChar": ...
    def exists(self) -> "BaseImportTestsModelsChar": ...
    def sudo(self) -> "BaseImportTestsModelsChar": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsChar": ...

# --- base_import.tests.models.char.noreadonly ---

class BaseImportTestsModelsCharNoreadonly(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsCharNoreadonly": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsCharNoreadonly": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsCharNoreadonly": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsCharNoreadonly": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsCharNoreadonly": ...
    def exists(self) -> "BaseImportTestsModelsCharNoreadonly": ...
    def sudo(self) -> "BaseImportTestsModelsCharNoreadonly": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsCharNoreadonly": ...

# --- base_import.tests.models.char.readonly ---

class BaseImportTestsModelsCharReadonly(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsCharReadonly": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsCharReadonly": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsCharReadonly": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsCharReadonly": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsCharReadonly": ...
    def exists(self) -> "BaseImportTestsModelsCharReadonly": ...
    def sudo(self) -> "BaseImportTestsModelsCharReadonly": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsCharReadonly": ...

# --- base_import.tests.models.char.required ---

class BaseImportTestsModelsCharRequired(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsCharRequired": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsCharRequired": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsCharRequired": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsCharRequired": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsCharRequired": ...
    def exists(self) -> "BaseImportTestsModelsCharRequired": ...
    def sudo(self) -> "BaseImportTestsModelsCharRequired": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsCharRequired": ...

# --- base_import.tests.models.char.states ---

class BaseImportTestsModelsCharStates(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsCharStates": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsCharStates": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsCharStates": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsCharStates": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsCharStates": ...
    def exists(self) -> "BaseImportTestsModelsCharStates": ...
    def sudo(self) -> "BaseImportTestsModelsCharStates": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsCharStates": ...

# --- base_import.tests.models.char.stillreadonly ---

class BaseImportTestsModelsCharStillreadonly(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsCharStillreadonly": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsCharStillreadonly": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsCharStillreadonly": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsCharStillreadonly": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsCharStillreadonly": ...
    def exists(self) -> "BaseImportTestsModelsCharStillreadonly": ...
    def sudo(self) -> "BaseImportTestsModelsCharStillreadonly": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsCharStillreadonly": ...

# --- base_import.tests.models.complex ---

class BaseImportTestsModelsComplex(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    c: str
    currency_id: "ResCurrency"
    d: Optional[_dt.date]
    dt: Optional[_dt.datetime]
    f: float
    has_bit2publish_template: bool
    m: float
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsComplex": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsComplex": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsComplex": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsComplex": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsComplex": ...
    def exists(self) -> "BaseImportTestsModelsComplex": ...
    def sudo(self) -> "BaseImportTestsModelsComplex": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsComplex": ...

# --- base_import.tests.models.float ---

class BaseImportTestsModelsFloat(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    currency_id: "ResCurrency"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: float
    value2: float
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsFloat": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsFloat": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsFloat": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsFloat": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsFloat": ...
    def exists(self) -> "BaseImportTestsModelsFloat": ...
    def sudo(self) -> "BaseImportTestsModelsFloat": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsFloat": ...

# --- base_import.tests.models.m2o ---

class BaseImportTestsModelsM2o(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: "BaseImportTestsModelsM2oRelated"
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsM2o": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsM2o": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsM2o": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsM2o": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsM2o": ...
    def exists(self) -> "BaseImportTestsModelsM2o": ...
    def sudo(self) -> "BaseImportTestsModelsM2o": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsM2o": ...

# --- base_import.tests.models.m2o.related ---

class BaseImportTestsModelsM2oRelated(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: int
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsM2oRelated": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsM2oRelated": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsM2oRelated": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsM2oRelated": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsM2oRelated": ...
    def exists(self) -> "BaseImportTestsModelsM2oRelated": ...
    def sudo(self) -> "BaseImportTestsModelsM2oRelated": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsM2oRelated": ...

# --- base_import.tests.models.m2o.required ---

class BaseImportTestsModelsM2oRequired(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: "BaseImportTestsModelsM2oRequiredRelated"
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsM2oRequired": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsM2oRequired": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsM2oRequired": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsM2oRequired": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsM2oRequired": ...
    def exists(self) -> "BaseImportTestsModelsM2oRequired": ...
    def sudo(self) -> "BaseImportTestsModelsM2oRequired": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsM2oRequired": ...

# --- base_import.tests.models.m2o.required.related ---

class BaseImportTestsModelsM2oRequiredRelated(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: int
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsM2oRequiredRelated": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsM2oRequiredRelated": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsM2oRequiredRelated": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsM2oRequiredRelated": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsM2oRequiredRelated": ...
    def exists(self) -> "BaseImportTestsModelsM2oRequiredRelated": ...
    def sudo(self) -> "BaseImportTestsModelsM2oRequiredRelated": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsM2oRequiredRelated": ...

# --- base_import.tests.models.o2m ---

class BaseImportTestsModelsO2m(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    value: "BaseImportTestsModelsO2mChild"
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsO2m": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsO2m": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsO2m": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsO2m": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsO2m": ...
    def exists(self) -> "BaseImportTestsModelsO2m": ...
    def sudo(self) -> "BaseImportTestsModelsO2m": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsO2m": ...

# --- base_import.tests.models.o2m.child ---

class BaseImportTestsModelsO2mChild(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    parent_id: "BaseImportTestsModelsO2m"
    show_bit2publish_button: bool
    value: int
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsO2mChild": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsO2mChild": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsO2mChild": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsO2mChild": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsO2mChild": ...
    def exists(self) -> "BaseImportTestsModelsO2mChild": ...
    def sudo(self) -> "BaseImportTestsModelsO2mChild": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsO2mChild": ...

# --- base_import.tests.models.preview ---

class BaseImportTestsModelsPreview(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    othervalue: int
    show_bit2publish_button: bool
    somevalue: int
    def browse(self, ids: Union[int, List[int]]) -> "BaseImportTestsModelsPreview": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BaseImportTestsModelsPreview": ...
    def create(self, vals: Dict[str, Any]) -> "BaseImportTestsModelsPreview": ...
    def filtered(self, func: Any) -> "BaseImportTestsModelsPreview": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BaseImportTestsModelsPreview": ...
    def exists(self) -> "BaseImportTestsModelsPreview": ...
    def sudo(self) -> "BaseImportTestsModelsPreview": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BaseImportTestsModelsPreview": ...

# --- billing.profile ---

class BillingProfile(Recordset):
    account_owner_name: str
    account_owner_surname: str
    active: bool
    billing_center_code: str
    billing_profile_code: str
    bit2publish_template_ids: "Bit2publishTemplate"
    cc_activation_date: Optional[_dt.date]
    cc_alias: str
    cc_circuit: str
    cc_owner: str
    ccr_card_network: str
    ccr_deactivation_date: Optional[_dt.date]
    ccr_identifier: str
    ccr_status: str
    cf_owner: str
    cig_code: str
    client_id: "ResPartner"
    consolidation: str
    consolidation_group: str
    contact_id: "ResPartner"
    contact_name: str
    contract_commission_code: str
    contract_date: Optional[_dt.date]
    contract_id_docu: str
    contract_item_number: str
    contract_line: float
    cre_curr: str
    credit_card: str
    credit_card_hidden: str
    cup: str
    date_sent_advice: Optional[_dt.datetime]
    doxee_univocal_code: str
    e_invoice: bool
    e_invoice_date: Optional[_dt.date]
    email: str
    end_date: Optional[_dt.date]
    export_digital_payment_filter_timestamp: Optional[_dt.datetime]
    fallback_payment_method_id: "PaymentMethod"
    has_bit2publish_template: bool
    holder_cf_or_vat: str
    holder_company: str
    iban: str
    ignore_unexecuted: bool
    ignore_unexecuted_date: Optional[_dt.date]
    institution_name: str
    invoice_code: str
    invoice_due_date: str
    invoice_frequency: str
    invoice_owner: str
    invoice_type: str
    invoicing_address_id: "ResPartner"
    ipa_code: str
    is_active: bool
    is_commodity_ele: bool
    is_commodity_fiber: bool
    is_commodity_gas: bool
    is_multipoint: bool
    lot_invoicing_slot: str
    market: str
    multipoint_std: str
    multipoint_type: str
    name: str
    number_sequence_group: str
    office_code: str
    order_cig_code: str
    order_commission_code: str
    order_cup_code: str
    order_date: Optional[_dt.date]
    order_docu_id: str
    order_item_number: str
    order_line: str
    payment_method: str
    payment_method_id: "PaymentMethod"
    payment_method_status: str
    payment_term_id: "PaymentTerm"
    paym_sched: str
    postalizer_type: str
    private_e_invoice_recipient_code: str
    recipient_pec: str
    sdd_activation_site: str
    sdd_authorization_code: str
    sdd_date_authorization_code: Optional[_dt.date]
    sdd_deactivation_reason: str
    sdd_request_date: Optional[_dt.date]
    sdd_status: str
    sdi_code: str
    sdi_write_date: Optional[_dt.date]
    second_digital_shipment: str
    sending_via: str
    service_point_ids: "ServicePoint"
    service_point_status: str
    show_bit2publish_button: bool
    sign_location: str
    srg_crm_bil_label_lov: str
    srg_crm_bil_label_lov_detail: str
    start_date: Optional[_dt.date]
    tag: str
    tre_curr: str
    def browse(self, ids: Union[int, List[int]]) -> "BillingProfile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BillingProfile": ...
    def create(self, vals: Dict[str, Any]) -> "BillingProfile": ...
    def filtered(self, func: Any) -> "BillingProfile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BillingProfile": ...
    def exists(self) -> "BillingProfile": ...
    def sudo(self) -> "BillingProfile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BillingProfile": ...

# --- bit2publish.documents.wizard ---

class Bit2publishDocumentsWizard(Recordset):
    bit2publish_template: str
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "Bit2publishDocumentsWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "Bit2publishDocumentsWizard": ...
    def create(self, vals: Dict[str, Any]) -> "Bit2publishDocumentsWizard": ...
    def filtered(self, func: Any) -> "Bit2publishDocumentsWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "Bit2publishDocumentsWizard": ...
    def exists(self) -> "Bit2publishDocumentsWizard": ...
    def sudo(self) -> "Bit2publishDocumentsWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "Bit2publishDocumentsWizard": ...

# --- bit2publish.template ---

class Bit2publishTemplate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    filename: str
    has_bit2publish_template: bool
    identifier: str
    lang: str
    lang_type: str
    model_id: "IrModel"
    model_model: str
    name: str
    output_type: str
    placeholder_map_ids: "Bit2publishTemplateMapping"
    record_domain: str
    show_bit2publish_button: bool
    show_button_on_model: bool
    version: int
    def browse(self, ids: Union[int, List[int]]) -> "Bit2publishTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "Bit2publishTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "Bit2publishTemplate": ...
    def filtered(self, func: Any) -> "Bit2publishTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "Bit2publishTemplate": ...
    def exists(self) -> "Bit2publishTemplate": ...
    def sudo(self) -> "Bit2publishTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "Bit2publishTemplate": ...

# --- bit2publish.template.mapping ---

class Bit2publishTemplateMapping(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    date_format: str
    description: str
    field_id: "IrModelFields"
    field_type: str
    fix_value: str
    has_bit2publish_template: bool
    model_id: "IrModel"
    placeholder: str
    python_code: str
    relation_sub_field: str
    relation_sub_field_ignore_empty_value: bool
    show_bit2publish_button: bool
    template_id: "Bit2publishTemplate"
    value_type: str
    def browse(self, ids: Union[int, List[int]]) -> "Bit2publishTemplateMapping": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "Bit2publishTemplateMapping": ...
    def create(self, vals: Dict[str, Any]) -> "Bit2publishTemplateMapping": ...
    def filtered(self, func: Any) -> "Bit2publishTemplateMapping": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "Bit2publishTemplateMapping": ...
    def exists(self) -> "Bit2publishTemplateMapping": ...
    def sudo(self) -> "Bit2publishTemplateMapping": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "Bit2publishTemplateMapping": ...

# --- bit2publish.test.template ---

class Bit2publishTestTemplate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    id_record: int
    result_ids: "Bit2publishTestTemplateResult"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "Bit2publishTestTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "Bit2publishTestTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "Bit2publishTestTemplate": ...
    def filtered(self, func: Any) -> "Bit2publishTestTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "Bit2publishTestTemplate": ...
    def exists(self) -> "Bit2publishTestTemplate": ...
    def sudo(self) -> "Bit2publishTestTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "Bit2publishTestTemplate": ...

# --- bit2publish.test.template.result ---

class Bit2publishTestTemplateResult(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    placeholder: str
    show_bit2publish_button: bool
    value: str
    wizard_id: "Bit2publishTestTemplate"
    def browse(self, ids: Union[int, List[int]]) -> "Bit2publishTestTemplateResult": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "Bit2publishTestTemplateResult": ...
    def create(self, vals: Dict[str, Any]) -> "Bit2publishTestTemplateResult": ...
    def filtered(self, func: Any) -> "Bit2publishTestTemplateResult": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "Bit2publishTestTemplateResult": ...
    def exists(self) -> "Bit2publishTestTemplateResult": ...
    def sudo(self) -> "Bit2publishTestTemplateResult": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "Bit2publishTestTemplateResult": ...

# --- blacklist.history ---

class BlacklistHistory(Recordset):
    agent_id: "ResPartner"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    is_in_blacklist: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BlacklistHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BlacklistHistory": ...
    def create(self, vals: Dict[str, Any]) -> "BlacklistHistory": ...
    def filtered(self, func: Any) -> "BlacklistHistory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BlacklistHistory": ...
    def exists(self) -> "BlacklistHistory": ...
    def sudo(self) -> "BlacklistHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BlacklistHistory": ...

# --- bonus.line.mixin ---

class BonusLineMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    bonus_id: "BonusMixin"
    has_bit2publish_template: bool
    last_error: str
    month: str
    show_bit2publish_button: bool
    state: str
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "BonusLineMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BonusLineMixin": ...
    def create(self, vals: Dict[str, Any]) -> "BonusLineMixin": ...
    def filtered(self, func: Any) -> "BonusLineMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BonusLineMixin": ...
    def exists(self) -> "BonusLineMixin": ...
    def sudo(self) -> "BonusLineMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BonusLineMixin": ...

# --- bonus.mixin ---

class BonusMixin(Recordset):
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    last_error: str
    last_processed_line: int
    month: str
    show_bit2publish_button: bool
    state: str
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "BonusMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BonusMixin": ...
    def create(self, vals: Dict[str, Any]) -> "BonusMixin": ...
    def filtered(self, func: Any) -> "BonusMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BonusMixin": ...
    def exists(self) -> "BonusMixin": ...
    def sudo(self) -> "BonusMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BonusMixin": ...

# --- bonus.wizard ---

class BonusWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BonusWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BonusWizard": ...
    def create(self, vals: Dict[str, Any]) -> "BonusWizard": ...
    def filtered(self, func: Any) -> "BonusWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BonusWizard": ...
    def exists(self) -> "BonusWizard": ...
    def sudo(self) -> "BonusWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BonusWizard": ...

# --- bpmn.flow ---

class BpmnFlow(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BpmnFlow": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BpmnFlow": ...
    def create(self, vals: Dict[str, Any]) -> "BpmnFlow": ...
    def filtered(self, func: Any) -> "BpmnFlow": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BpmnFlow": ...
    def exists(self) -> "BpmnFlow": ...
    def sudo(self) -> "BpmnFlow": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BpmnFlow": ...

# --- bpmn.flow.line ---

class BpmnFlowLine(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    config_id: "BpmnWorkflowParams"
    flow_type_id: "BpmnFlow"
    has_bit2publish_template: bool
    height: float
    markup: str
    show_bit2publish_button: bool
    width: float
    def browse(self, ids: Union[int, List[int]]) -> "BpmnFlowLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BpmnFlowLine": ...
    def create(self, vals: Dict[str, Any]) -> "BpmnFlowLine": ...
    def filtered(self, func: Any) -> "BpmnFlowLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BpmnFlowLine": ...
    def exists(self) -> "BpmnFlowLine": ...
    def sudo(self) -> "BpmnFlowLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BpmnFlowLine": ...

# --- bpmn.hidden.result.color ---

class BpmnHiddenResultColor(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    hex_color: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BpmnHiddenResultColor": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BpmnHiddenResultColor": ...
    def create(self, vals: Dict[str, Any]) -> "BpmnHiddenResultColor": ...
    def filtered(self, func: Any) -> "BpmnHiddenResultColor": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BpmnHiddenResultColor": ...
    def exists(self) -> "BpmnHiddenResultColor": ...
    def sudo(self) -> "BpmnHiddenResultColor": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BpmnHiddenResultColor": ...

# --- bpmn.workflow.params ---

class BpmnWorkflowParams(Recordset):
    apply_edge_label: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    flow_type_ids: "BpmnFlowLine"
    has_bit2publish_template: bool
    h_edge_len: float
    label_h: float
    label_padding: float
    name: str
    show_bit2publish_button: bool
    v_edge_len: float
    x: float
    y: float
    def browse(self, ids: Union[int, List[int]]) -> "BpmnWorkflowParams": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BpmnWorkflowParams": ...
    def create(self, vals: Dict[str, Any]) -> "BpmnWorkflowParams": ...
    def filtered(self, func: Any) -> "BpmnWorkflowParams": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BpmnWorkflowParams": ...
    def exists(self) -> "BpmnWorkflowParams": ...
    def sudo(self) -> "BpmnWorkflowParams": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BpmnWorkflowParams": ...

# --- bus.bus ---

class BusBus(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    channel: str
    has_bit2publish_template: bool
    message: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "BusBus": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BusBus": ...
    def create(self, vals: Dict[str, Any]) -> "BusBus": ...
    def filtered(self, func: Any) -> "BusBus": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BusBus": ...
    def exists(self) -> "BusBus": ...
    def sudo(self) -> "BusBus": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BusBus": ...

# --- bus.presence ---

class BusPresence(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    guest_id: "MailGuest"
    has_bit2publish_template: bool
    last_poll: Optional[_dt.datetime]
    last_presence: Optional[_dt.datetime]
    show_bit2publish_button: bool
    status: str
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "BusPresence": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "BusPresence": ...
    def create(self, vals: Dict[str, Any]) -> "BusPresence": ...
    def filtered(self, func: Any) -> "BusPresence": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "BusPresence": ...
    def exists(self) -> "BusPresence": ...
    def sudo(self) -> "BusPresence": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "BusPresence": ...

# --- cadastral.info.mixin ---

class CadastralInfoMixin(Recordset):
    administrative_location: str
    bit2publish_template_ids: "Bit2publishTemplate"
    cadastral_code: str
    cadastral_date: Optional[_dt.date]
    cadastral_location: str
    cadastral_map: str
    cadastral_parcel: str
    cadastral_sub: str
    declarant_type: str
    following_parcel: str
    has_bit2publish_template: bool
    house_number: str
    house_street: str
    missing_cadastral_reason: str
    parcel_type: str
    real_estate_unit_type: str
    show_bit2publish_button: bool
    urban_section: str
    def browse(self, ids: Union[int, List[int]]) -> "CadastralInfoMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CadastralInfoMixin": ...
    def create(self, vals: Dict[str, Any]) -> "CadastralInfoMixin": ...
    def filtered(self, func: Any) -> "CadastralInfoMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CadastralInfoMixin": ...
    def exists(self) -> "CadastralInfoMixin": ...
    def sudo(self) -> "CadastralInfoMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CadastralInfoMixin": ...

# --- cadastre.data ---

class CadastreData(Recordset):
    acquisition_status: str
    administrative_location: str
    allowed_result_ids: "SympleTripletPhaseResult"
    bit2publish_template_ids: "Bit2publishTemplate"
    cadastral_code: str
    cadastral_create_date: Optional[_dt.date]
    cadastral_date: Optional[_dt.date]
    cadastral_location: str
    cadastral_map: str
    cadastral_parcel: str
    cadastral_sub: str
    cadastral_write_date: Optional[_dt.date]
    channel: str
    commodity: str
    customer_id: "ResPartner"
    data_overwritten: bool
    declarant_type: str
    following_parcel: str
    has_bit2publish_template: bool
    house_number: str
    house_street: str
    interaction_id: "SympleInteraction"
    is_allow_update: bool
    link_ids: "IrAttachment"
    missing_cadastral_reason: str
    parcel_type: str
    pr_code: str
    real_estate_unit_type: str
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    subscriber_first_name: str
    subscriber_fiscal_code: str
    subscriber_last_name: str
    ticket_dc01_id: "HelpdeskTicket"
    ticket_gd07_id: "HelpdeskTicket"
    triplet_name: str
    urban_section: str
    def browse(self, ids: Union[int, List[int]]) -> "CadastreData": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CadastreData": ...
    def create(self, vals: Dict[str, Any]) -> "CadastreData": ...
    def filtered(self, func: Any) -> "CadastreData": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CadastreData": ...
    def exists(self) -> "CadastreData": ...
    def sudo(self) -> "CadastreData": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CadastreData": ...

# --- cadastre.data.ade.report ---

class CadastreDataAdeReport(Recordset):
    ade_row_ids: "CadastreDataAdeReportRow"
    bit2publish_template_ids: "Bit2publishTemplate"
    caf_registration_number: int
    commitment_date: Optional[_dt.date]
    commitment_transmit: str
    commodity: str
    communication_type: str
    file_ids: "IrAttachment"
    has_bit2publish_template: bool
    intermediary_fiscal_code: str
    is_can_generate_preview: bool
    m2c_record_ids: "CadastreDataRowM2c"
    reference_year: str
    rows_to_generate: "CadastreDataRowM2c"
    show_bit2publish_button: bool
    state: str
    telematic_protocol: int
    def browse(self, ids: Union[int, List[int]]) -> "CadastreDataAdeReport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CadastreDataAdeReport": ...
    def create(self, vals: Dict[str, Any]) -> "CadastreDataAdeReport": ...
    def filtered(self, func: Any) -> "CadastreDataAdeReport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CadastreDataAdeReport": ...
    def exists(self) -> "CadastreDataAdeReport": ...
    def sudo(self) -> "CadastreDataAdeReport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CadastreDataAdeReport": ...

# --- cadastre.data.ade.report.row ---

class CadastreDataAdeReportRow(Recordset):
    activate_modify_date: Optional[_dt.datetime]
    activation_date: Optional[_dt.date]
    address: str
    amount_invoiced: int
    birth_county: str
    birth_date: Optional[_dt.date]
    birth_municipality: str
    bit2publish_template_ids: "Bit2publishTemplate"
    cadastral_code: str
    cadastral_map: str
    cadastral_parcel: str
    cadastral_sub: str
    cadastre_record_id: "CadastreData"
    commodity: str
    contract_type: str
    customer_id: "ResPartner"
    error_reason: str
    extraction_result: str
    fiber_contract_type: str
    final_user_count: int
    first_name: str
    fiscal_code: str
    following_parcel: str
    gender: str
    has_bit2publish_template: bool
    idr_code: str
    initial_user_count: int
    is_company: bool
    kwh_consumption: int
    last_name: str
    m2c_record_id: "CadastreDataRowM2c"
    missing_cadastral_reason: str
    months: str
    name: str
    parcel_type: str
    real_estate_unit_type: str
    recharge_cost: int
    reference_year: str
    report_id: "CadastreDataAdeReport"
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    smc_consumption: int
    tariff_type: str
    tax_domicile_municipality: str
    tax_domicile_province: str
    traffic_cost: int
    urban_section: str
    usage_destination: str
    user_id_code: str
    user_qualification: str
    user_type: str
    utility_type: str
    def browse(self, ids: Union[int, List[int]]) -> "CadastreDataAdeReportRow": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CadastreDataAdeReportRow": ...
    def create(self, vals: Dict[str, Any]) -> "CadastreDataAdeReportRow": ...
    def filtered(self, func: Any) -> "CadastreDataAdeReportRow": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CadastreDataAdeReportRow": ...
    def exists(self) -> "CadastreDataAdeReportRow": ...
    def sudo(self) -> "CadastreDataAdeReportRow": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CadastreDataAdeReportRow": ...

# --- cadastre.data.condo.importer ---

class CadastreDataCondoImporter(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    excel_file: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "CadastreDataCondoImporter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CadastreDataCondoImporter": ...
    def create(self, vals: Dict[str, Any]) -> "CadastreDataCondoImporter": ...
    def filtered(self, func: Any) -> "CadastreDataCondoImporter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CadastreDataCondoImporter": ...
    def exists(self) -> "CadastreDataCondoImporter": ...
    def sudo(self) -> "CadastreDataCondoImporter": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CadastreDataCondoImporter": ...

# --- cadastre.data.row.m2c ---

class CadastreDataRowM2c(Recordset):
    ade_record_id: "CadastreDataAdeReport"
    amount: int
    bit2publish_template_ids: "Bit2publishTemplate"
    cadastre_data_id: "CadastreData"
    commodity: str
    customer_id: "ResPartner"
    error_description: str
    file_id: "CadastreDataRowM2cFile"
    fiscal_code: str
    has_bit2publish_template: bool
    idr_code: str
    is_ade_row_generated: bool
    kwh_consumption: int
    last_error: str
    month: int
    pdr_code: str
    pod_code: str
    processing_date: Optional[_dt.datetime]
    process_is_running: bool
    recharge_cost: int
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    smc_consumption: int
    state: str
    traffic_cost: int
    year: int
    def browse(self, ids: Union[int, List[int]]) -> "CadastreDataRowM2c": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CadastreDataRowM2c": ...
    def create(self, vals: Dict[str, Any]) -> "CadastreDataRowM2c": ...
    def filtered(self, func: Any) -> "CadastreDataRowM2c": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CadastreDataRowM2c": ...
    def exists(self) -> "CadastreDataRowM2c": ...
    def sudo(self) -> "CadastreDataRowM2c": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CadastreDataRowM2c": ...

# --- cadastre.data.row.m2c.file ---

class CadastreDataRowM2cFile(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity: str
    data: bytes
    filename: str
    has_bit2publish_template: bool
    is_processed: bool
    is_processing: bool
    last_error: str
    last_processed_line: int
    line_ids: "CadastreDataRowM2c"
    name: str
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "CadastreDataRowM2cFile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CadastreDataRowM2cFile": ...
    def create(self, vals: Dict[str, Any]) -> "CadastreDataRowM2cFile": ...
    def filtered(self, func: Any) -> "CadastreDataRowM2cFile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CadastreDataRowM2cFile": ...
    def exists(self) -> "CadastreDataRowM2cFile": ...
    def sudo(self) -> "CadastreDataRowM2cFile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CadastreDataRowM2cFile": ...

# --- cadastre.data.row.m2c.importer ---

class CadastreDataRowM2cImporter(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity: str
    data: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "CadastreDataRowM2cImporter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CadastreDataRowM2cImporter": ...
    def create(self, vals: Dict[str, Any]) -> "CadastreDataRowM2cImporter": ...
    def filtered(self, func: Any) -> "CadastreDataRowM2cImporter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CadastreDataRowM2cImporter": ...
    def exists(self) -> "CadastreDataRowM2cImporter": ...
    def sudo(self) -> "CadastreDataRowM2cImporter": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CadastreDataRowM2cImporter": ...

# --- calendar.alarm ---

class CalendarAlarm(Recordset):
    alarm_type: str
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    duration: int
    duration_minutes: int
    has_bit2publish_template: bool
    interval: str
    mail_template_id: "MailTemplate"
    name: str
    show_bit2publish_button: bool
    sms_template_id: "SmsTemplate"
    def browse(self, ids: Union[int, List[int]]) -> "CalendarAlarm": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CalendarAlarm": ...
    def create(self, vals: Dict[str, Any]) -> "CalendarAlarm": ...
    def filtered(self, func: Any) -> "CalendarAlarm": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CalendarAlarm": ...
    def exists(self) -> "CalendarAlarm": ...
    def sudo(self) -> "CalendarAlarm": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CalendarAlarm": ...

# --- calendar.alarm_manager ---

class CalendarAlarmManager(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "CalendarAlarmManager": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CalendarAlarmManager": ...
    def create(self, vals: Dict[str, Any]) -> "CalendarAlarmManager": ...
    def filtered(self, func: Any) -> "CalendarAlarmManager": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CalendarAlarmManager": ...
    def exists(self) -> "CalendarAlarmManager": ...
    def sudo(self) -> "CalendarAlarmManager": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CalendarAlarmManager": ...

# --- calendar.attendee ---

class CalendarAttendee(Recordset):
    access_token: str
    availability: str
    bit2publish_template_ids: "Bit2publishTemplate"
    common_name: str
    email: str
    event_id: "CalendarEvent"
    has_bit2publish_template: bool
    mail_tz: str
    partner_id: "ResPartner"
    phone: str
    recurrence_id: "CalendarRecurrence"
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "CalendarAttendee": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CalendarAttendee": ...
    def create(self, vals: Dict[str, Any]) -> "CalendarAttendee": ...
    def filtered(self, func: Any) -> "CalendarAttendee": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CalendarAttendee": ...
    def exists(self) -> "CalendarAttendee": ...
    def sudo(self) -> "CalendarAttendee": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CalendarAttendee": ...

# --- calendar.event ---

class CalendarEvent(Recordset):
    active: bool
    activity_ids: "MailActivity"
    alarm_ids: "CalendarAlarm"
    allday: bool
    attendee_ids: "CalendarAttendee"
    attendee_status: str
    bit2publish_template_ids: "Bit2publishTemplate"
    byday: str
    categ_ids: "CalendarEventType"
    count: int
    day: int
    description: str
    display_description: bool
    display_time: str
    duration: float
    end_type: str
    event_tz: str
    follow_recurrence: bool
    fri: bool
    has_bit2publish_template: bool
    has_message: bool
    interval: int
    is_highlighted: bool
    is_organizer_alone: bool
    location: str
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    mon: bool
    month_by: str
    name: str
    partner_id: "ResPartner"
    partner_ids: "ResPartner"
    privacy: str
    recurrence_id: "CalendarRecurrence"
    recurrence_update: str
    recurrency: bool
    res_id: int
    res_model: str
    res_model_id: "IrModel"
    rrule: str
    rrule_type: str
    sat: bool
    show_as: str
    show_bit2publish_button: bool
    start: Optional[_dt.datetime]
    start_date: Optional[_dt.date]
    stop: Optional[_dt.datetime]
    stop_date: Optional[_dt.date]
    sun: bool
    thu: bool
    tue: bool
    until: Optional[_dt.date]
    user_id: "ResUsers"
    videocall_location: str
    website_message_ids: "MailMessage"
    wed: bool
    weekday: str
    def browse(self, ids: Union[int, List[int]]) -> "CalendarEvent": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CalendarEvent": ...
    def create(self, vals: Dict[str, Any]) -> "CalendarEvent": ...
    def filtered(self, func: Any) -> "CalendarEvent": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CalendarEvent": ...
    def exists(self) -> "CalendarEvent": ...
    def sudo(self) -> "CalendarEvent": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CalendarEvent": ...

# --- calendar.event.type ---

class CalendarEventType(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    color: int
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "CalendarEventType": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CalendarEventType": ...
    def create(self, vals: Dict[str, Any]) -> "CalendarEventType": ...
    def filtered(self, func: Any) -> "CalendarEventType": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CalendarEventType": ...
    def exists(self) -> "CalendarEventType": ...
    def sudo(self) -> "CalendarEventType": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CalendarEventType": ...

# --- calendar.filters ---

class CalendarFilters(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    partner_checked: bool
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "CalendarFilters": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CalendarFilters": ...
    def create(self, vals: Dict[str, Any]) -> "CalendarFilters": ...
    def filtered(self, func: Any) -> "CalendarFilters": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CalendarFilters": ...
    def exists(self) -> "CalendarFilters": ...
    def sudo(self) -> "CalendarFilters": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CalendarFilters": ...

# --- calendar.recurrence ---

class CalendarRecurrence(Recordset):
    base_event_id: "CalendarEvent"
    bit2publish_template_ids: "Bit2publishTemplate"
    byday: str
    calendar_event_ids: "CalendarEvent"
    count: int
    day: int
    dtstart: Optional[_dt.datetime]
    end_type: str
    event_tz: str
    fri: bool
    has_bit2publish_template: bool
    interval: int
    mon: bool
    month_by: str
    name: str
    rrule: str
    rrule_type: str
    sat: bool
    show_bit2publish_button: bool
    sun: bool
    thu: bool
    tue: bool
    until: Optional[_dt.date]
    wed: bool
    weekday: str
    def browse(self, ids: Union[int, List[int]]) -> "CalendarRecurrence": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CalendarRecurrence": ...
    def create(self, vals: Dict[str, Any]) -> "CalendarRecurrence": ...
    def filtered(self, func: Any) -> "CalendarRecurrence": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CalendarRecurrence": ...
    def exists(self) -> "CalendarRecurrence": ...
    def sudo(self) -> "CalendarRecurrence": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CalendarRecurrence": ...

# --- cancel.case ---

class CancelCase(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    case_id: "HelpdeskTicket"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    triplet_allowed_phase_result_ids: "SympleTripletPhaseResult"
    triplet_phase_result_id: "SympleTripletPhaseResult"
    unsuccess_reason_id: "SympleTripletUnsuccessReason"
    unsuccess_reason_ids: "SympleTripletUnsuccessReason"
    def browse(self, ids: Union[int, List[int]]) -> "CancelCase": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CancelCase": ...
    def create(self, vals: Dict[str, Any]) -> "CancelCase": ...
    def filtered(self, func: Any) -> "CancelCase": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CancelCase": ...
    def exists(self) -> "CancelCase": ...
    def sudo(self) -> "CancelCase": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CancelCase": ...

# --- cancel.interaction ---

class CancelInteraction(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    cancel_reason_id: "SympleInteractionCancelReason"
    has_bit2publish_template: bool
    interaction_id: "SympleInteraction"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "CancelInteraction": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CancelInteraction": ...
    def create(self, vals: Dict[str, Any]) -> "CancelInteraction": ...
    def filtered(self, func: Any) -> "CancelInteraction": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CancelInteraction": ...
    def exists(self) -> "CancelInteraction": ...
    def sudo(self) -> "CancelInteraction": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CancelInteraction": ...

# --- case.integration.history ---

class CaseIntegrationHistory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    payload: str
    show_bit2publish_button: bool
    symphony_request_id: str
    ticket_id: "HelpdeskTicket"
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
    def sorted(self, key: Any = None, reverse: bool = False) -> "CaseIntegrationHistory": ...
    def exists(self) -> "CaseIntegrationHistory": ...
    def sudo(self) -> "CaseIntegrationHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CaseIntegrationHistory": ...

# --- cash.box.out ---

class CashBoxOut(Recordset):
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "CashBoxOut": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CashBoxOut": ...
    def create(self, vals: Dict[str, Any]) -> "CashBoxOut": ...
    def filtered(self, func: Any) -> "CashBoxOut": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CashBoxOut": ...
    def exists(self) -> "CashBoxOut": ...
    def sudo(self) -> "CashBoxOut": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CashBoxOut": ...

# --- change.password.user ---

class ChangePasswordUser(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    new_passwd: str
    show_bit2publish_button: bool
    user_id: "ResUsers"
    user_login: str
    wizard_id: "ChangePasswordWizard"
    def browse(self, ids: Union[int, List[int]]) -> "ChangePasswordUser": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ChangePasswordUser": ...
    def create(self, vals: Dict[str, Any]) -> "ChangePasswordUser": ...
    def filtered(self, func: Any) -> "ChangePasswordUser": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ChangePasswordUser": ...
    def exists(self) -> "ChangePasswordUser": ...
    def sudo(self) -> "ChangePasswordUser": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ChangePasswordUser": ...

# --- change.password.wizard ---

class ChangePasswordWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    user_ids: "ChangePasswordUser"
    def browse(self, ids: Union[int, List[int]]) -> "ChangePasswordWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ChangePasswordWizard": ...
    def create(self, vals: Dict[str, Any]) -> "ChangePasswordWizard": ...
    def filtered(self, func: Any) -> "ChangePasswordWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ChangePasswordWizard": ...
    def exists(self) -> "ChangePasswordWizard": ...
    def sudo(self) -> "ChangePasswordWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ChangePasswordWizard": ...

# --- channel.association ---

class ChannelAssociation(Recordset):
    agency_id: "ResPartner"
    bit2publish_template_ids: "Bit2publishTemplate"
    bus_fiber: str
    can_channel_be_reactivated: bool
    ccq: str
    channel_id: "SaleChannel"
    closed_by_commissioning_date: Optional[_dt.date]
    closed_residential_by_commissioning_date: Optional[_dt.date]
    end_residential_validity_date: Optional[_dt.date]
    end_validity_date: Optional[_dt.date]
    has_bit2publish_template: bool
    instant_call: str
    is_closed_by_commissioning: bool
    is_closed_by_commissioning_submitted: bool
    is_closed_frontend: bool
    is_closed_frontend_submitted: bool
    is_closed_residential_by_commissioning: bool
    is_closed_residential_frontend: bool
    name: str
    no_standard: str
    payment_type: str
    product_change: str
    replay: str
    res_fiber: str
    residential_contract: bool
    residential_status: str
    show_bit2publish_button: bool
    standard: str
    start_residential_validity_date: Optional[_dt.date]
    start_validity_date: Optional[_dt.date]
    status: str
    verify_card: str
    def browse(self, ids: Union[int, List[int]]) -> "ChannelAssociation": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ChannelAssociation": ...
    def create(self, vals: Dict[str, Any]) -> "ChannelAssociation": ...
    def filtered(self, func: Any) -> "ChannelAssociation": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ChannelAssociation": ...
    def exists(self) -> "ChannelAssociation": ...
    def sudo(self) -> "ChannelAssociation": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ChannelAssociation": ...

# --- charge.dispatch ---

class ChargeDispatch(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    charge_amount: float
    charge_type: str
    commodity: str
    currency_id: "ResCurrency"
    customer_care_category: str
    end_date: Optional[_dt.date]
    has_bit2publish_template: bool
    marginality_segment: str
    market_type: str
    show_bit2publish_button: bool
    specificity: int
    start_date: Optional[_dt.date]
    ticket_type_code: str
    def browse(self, ids: Union[int, List[int]]) -> "ChargeDispatch": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ChargeDispatch": ...
    def create(self, vals: Dict[str, Any]) -> "ChargeDispatch": ...
    def filtered(self, func: Any) -> "ChargeDispatch": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ChargeDispatch": ...
    def exists(self) -> "ChargeDispatch": ...
    def sudo(self) -> "ChargeDispatch": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ChargeDispatch": ...

# --- city.zip.geonames.import ---

class CityZipGeonamesImport(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    country_ids: "ResCountry"
    has_bit2publish_template: bool
    letter_case: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "CityZipGeonamesImport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CityZipGeonamesImport": ...
    def create(self, vals: Dict[str, Any]) -> "CityZipGeonamesImport": ...
    def filtered(self, func: Any) -> "CityZipGeonamesImport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CityZipGeonamesImport": ...
    def exists(self) -> "CityZipGeonamesImport": ...
    def sudo(self) -> "CityZipGeonamesImport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CityZipGeonamesImport": ...

# --- client.agency.data ---

class ClientAgencyData(Recordset):
    active: bool
    agency_id: "ResPartner"
    bit2publish_template_ids: "Bit2publishTemplate"
    client_type: str
    end_date: Optional[_dt.date]
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    start_date: Optional[_dt.date]
    def browse(self, ids: Union[int, List[int]]) -> "ClientAgencyData": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ClientAgencyData": ...
    def create(self, vals: Dict[str, Any]) -> "ClientAgencyData": ...
    def filtered(self, func: Any) -> "ClientAgencyData": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ClientAgencyData": ...
    def exists(self) -> "ClientAgencyData": ...
    def sudo(self) -> "ClientAgencyData": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ClientAgencyData": ...

# --- config.ccq ---

class ConfigCcq(Recordset):
    agente: str
    agenzia: str
    bit2publish_template_ids: "Bit2publishTemplate"
    campagna: str
    canale: str
    categoria_cliente: str
    data_fine_validita: Optional[_dt.datetime]
    data_inizio_validita: Optional[_dt.datetime]
    desinenza_contratto: str
    has_bit2publish_template: bool
    prodotto: str
    show_bit2publish_button: bool
    tipo_attivita: str
    tipo_contratto: str
    tipo_operazione: str
    user: str
    def browse(self, ids: Union[int, List[int]]) -> "ConfigCcq": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ConfigCcq": ...
    def create(self, vals: Dict[str, Any]) -> "ConfigCcq": ...
    def filtered(self, func: Any) -> "ConfigCcq": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ConfigCcq": ...
    def exists(self) -> "ConfigCcq": ...
    def sudo(self) -> "ConfigCcq": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ConfigCcq": ...

# --- config.cuscinetto ---

class ConfigCuscinetto(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    canale: str
    cuscinetto: int
    has_bit2publish_template: bool
    listino: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ConfigCuscinetto": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ConfigCuscinetto": ...
    def create(self, vals: Dict[str, Any]) -> "ConfigCuscinetto": ...
    def filtered(self, func: Any) -> "ConfigCuscinetto": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ConfigCuscinetto": ...
    def exists(self) -> "ConfigCuscinetto": ...
    def sudo(self) -> "ConfigCuscinetto": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ConfigCuscinetto": ...

# --- config.metodo_di_pagamento ---

class ConfigMetodoDiPagamento(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    canale: str
    categoria_cliente: str
    flag_attivazione_anticipata: bool
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    tipo_operazione: str
    def browse(self, ids: Union[int, List[int]]) -> "ConfigMetodoDiPagamento": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ConfigMetodoDiPagamento": ...
    def create(self, vals: Dict[str, Any]) -> "ConfigMetodoDiPagamento": ...
    def filtered(self, func: Any) -> "ConfigMetodoDiPagamento": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ConfigMetodoDiPagamento": ...
    def exists(self) -> "ConfigMetodoDiPagamento": ...
    def sudo(self) -> "ConfigMetodoDiPagamento": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ConfigMetodoDiPagamento": ...

# --- config.rivalutazione ---

class ConfigRivalutazione(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    canale: str
    check: bool
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    tipo_contratto: str
    def browse(self, ids: Union[int, List[int]]) -> "ConfigRivalutazione": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ConfigRivalutazione": ...
    def create(self, vals: Dict[str, Any]) -> "ConfigRivalutazione": ...
    def filtered(self, func: Any) -> "ConfigRivalutazione": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ConfigRivalutazione": ...
    def exists(self) -> "ConfigRivalutazione": ...
    def sudo(self) -> "ConfigRivalutazione": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ConfigRivalutazione": ...

# --- config.verifica_carta ---

class ConfigVerificaCarta(Recordset):
    agente: str
    agenzia: str
    bit2publish_template_ids: "Bit2publishTemplate"
    campagna: str
    canale: str
    categoria_cliente: str
    data_fine_validita: Optional[_dt.datetime]
    data_inizio_validita: Optional[_dt.datetime]
    desinenza_contratto: str
    has_bit2publish_template: bool
    numero_punti_cliente: int
    show_bit2publish_button: bool
    tipo_contratto: str
    tipo_operazione: str
    user: str
    def browse(self, ids: Union[int, List[int]]) -> "ConfigVerificaCarta": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ConfigVerificaCarta": ...
    def create(self, vals: Dict[str, Any]) -> "ConfigVerificaCarta": ...
    def filtered(self, func: Any) -> "ConfigVerificaCarta": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ConfigVerificaCarta": ...
    def exists(self) -> "ConfigVerificaCarta": ...
    def sudo(self) -> "ConfigVerificaCarta": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ConfigVerificaCarta": ...

# --- connect.case ---

class ConnectCase(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    customer_id: "ResPartner"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    starting_ticket_id: "HelpdeskTicket"
    ticket_id: "HelpdeskTicket"
    ticket_type_id: "HelpdeskTicketType"
    triplet_subtype_id: "SympleTripletSubtype"
    triplet_subtype_ticket_type_ids: "HelpdeskTicketType"
    triplet_type_id: "SympleTripletType"
    triplet_type_subtype_ids: "SympleTripletSubtype"
    workflow_id: "SympleWorkflow"
    def browse(self, ids: Union[int, List[int]]) -> "ConnectCase": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ConnectCase": ...
    def create(self, vals: Dict[str, Any]) -> "ConnectCase": ...
    def filtered(self, func: Any) -> "ConnectCase": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ConnectCase": ...
    def exists(self) -> "ConnectCase": ...
    def sudo(self) -> "ConnectCase": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ConnectCase": ...

# --- connect.parent.case ---

class ConnectParentCase(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    child_case_id: "HelpdeskTicket"
    has_bit2publish_template: bool
    is_same_client: bool
    is_same_point: bool
    parent_case_domain: str
    selection_case_ids: "HelpdeskTicket"
    show_bit2publish_button: bool
    ticket_id: "HelpdeskTicket"
    def browse(self, ids: Union[int, List[int]]) -> "ConnectParentCase": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ConnectParentCase": ...
    def create(self, vals: Dict[str, Any]) -> "ConnectParentCase": ...
    def filtered(self, func: Any) -> "ConnectParentCase": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ConnectParentCase": ...
    def exists(self) -> "ConnectParentCase": ...
    def sudo(self) -> "ConnectParentCase": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ConnectParentCase": ...

# --- consortiums ---

class Consortiums(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    has_bit2publish_template: bool
    is_valid: bool
    name: str
    show_bit2publish_button: bool
    status: str
    def browse(self, ids: Union[int, List[int]]) -> "Consortiums": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "Consortiums": ...
    def create(self, vals: Dict[str, Any]) -> "Consortiums": ...
    def filtered(self, func: Any) -> "Consortiums": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "Consortiums": ...
    def exists(self) -> "Consortiums": ...
    def sudo(self) -> "Consortiums": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "Consortiums": ...

# --- contract.annulment.reason ---

class ContractAnnulmentReason(Recordset):
    annulment_reason_ids: "AnnulmentReason"
    annulment_reason_type: str
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity: str
    has_bit2publish_template: bool
    request_type: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ContractAnnulmentReason": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ContractAnnulmentReason": ...
    def create(self, vals: Dict[str, Any]) -> "ContractAnnulmentReason": ...
    def filtered(self, func: Any) -> "ContractAnnulmentReason": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ContractAnnulmentReason": ...
    def exists(self) -> "ContractAnnulmentReason": ...
    def sudo(self) -> "ContractAnnulmentReason": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ContractAnnulmentReason": ...

# --- correction.invoice ---

class CorrectionInvoice(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    case_id: "HelpdeskTicket"
    client_id: "ResPartner"
    currency_id: "ResCurrency"
    form_sent: str
    has_bit2publish_template: bool
    invoice_amount: float
    invoice_number: str
    issuing_date: Optional[_dt.date]
    period_of_competence_from: Optional[_dt.date]
    period_of_competence_to: Optional[_dt.date]
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "CorrectionInvoice": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CorrectionInvoice": ...
    def create(self, vals: Dict[str, Any]) -> "CorrectionInvoice": ...
    def filtered(self, func: Any) -> "CorrectionInvoice": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CorrectionInvoice": ...
    def exists(self) -> "CorrectionInvoice": ...
    def sudo(self) -> "CorrectionInvoice": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CorrectionInvoice": ...

# --- create.case ---

class CreateCase(Recordset):
    alternative_email: str
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity: str
    commodity_optional: str
    commodity_readonly_default: str
    commodity_required: str
    complaint_ticket_id: "HelpdeskTicket"
    customer_id: "ResPartner"
    from_res_partner: bool
    has_alternative_email: bool
    has_bit2publish_template: bool
    interaction_id: "SympleInteraction"
    is_commodity_readonly: bool
    is_for_commodity: bool
    is_for_commodity_optional: bool
    is_for_commodity_required: bool
    is_for_ele: bool
    is_for_ele_optional: bool
    is_for_ele_required: bool
    is_for_fiber: bool
    is_for_fiber_optional: bool
    is_for_fiber_required: bool
    is_for_gas: bool
    is_for_gas_optional: bool
    is_for_gas_required: bool
    is_pods_in_pop_up: bool
    is_reiteration: bool
    is_reminder: bool
    is_select_parent: bool
    is_service_points_in_pop_up: bool
    is_tiqv: bool
    parent_case_domain: str
    parent_case_id: "HelpdeskTicket"
    parent_case_ids: "HelpdeskTicket"
    partner_id: "ResPartner"
    pod_ids: "ResPartnerPod"
    reiteration_ticket_id: "HelpdeskTicket"
    selected_fiber_service_point_ids: "ServicePoint"
    selected_pdr_ids: "ResPartnerPdr"
    selected_pod_ids: "ResPartnerPod"
    selected_service_point_ids: "ServicePoint"
    show_bit2publish_button: bool
    ticket_type_id: "HelpdeskTicketType"
    triplet_subtype_id: "SympleTripletSubtype"
    triplet_subtype_ticket_type_ids: "HelpdeskTicketType"
    triplet_type_domain: "SympleTripletType"
    triplet_type_id: "SympleTripletType"
    triplet_type_subtype_ids: "SympleTripletSubtype"
    workflow_id: "SympleWorkflow"
    def browse(self, ids: Union[int, List[int]]) -> "CreateCase": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CreateCase": ...
    def create(self, vals: Dict[str, Any]) -> "CreateCase": ...
    def filtered(self, func: Any) -> "CreateCase": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CreateCase": ...
    def exists(self) -> "CreateCase": ...
    def sudo(self) -> "CreateCase": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CreateCase": ...

# --- create.case.mixin ---

class CreateCaseMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity: str
    commodity_optional: str
    commodity_readonly_default: str
    commodity_required: str
    complaint_ticket_id: "HelpdeskTicket"
    customer_id: "ResPartner"
    has_bit2publish_template: bool
    interaction_id: "SympleInteraction"
    is_commodity_readonly: bool
    is_for_commodity: bool
    is_for_commodity_optional: bool
    is_for_commodity_required: bool
    is_for_ele: bool
    is_for_ele_optional: bool
    is_for_ele_required: bool
    is_for_fiber: bool
    is_for_fiber_optional: bool
    is_for_fiber_required: bool
    is_for_gas: bool
    is_for_gas_optional: bool
    is_for_gas_required: bool
    is_pods_in_pop_up: bool
    is_reiteration: bool
    is_reminder: bool
    is_service_points_in_pop_up: bool
    is_tiqv: bool
    pod_ids: "ResPartnerPod"
    reiteration_ticket_id: "HelpdeskTicket"
    selected_pdr_ids: "ResPartnerPdr"
    selected_pod_ids: "ResPartnerPod"
    selected_service_point_ids: "ServicePoint"
    show_bit2publish_button: bool
    ticket_type_id: "HelpdeskTicketType"
    triplet_subtype_id: "SympleTripletSubtype"
    triplet_subtype_ticket_type_ids: "HelpdeskTicketType"
    triplet_type_domain: "SympleTripletType"
    triplet_type_id: "SympleTripletType"
    triplet_type_subtype_ids: "SympleTripletSubtype"
    workflow_id: "SympleWorkflow"
    def browse(self, ids: Union[int, List[int]]) -> "CreateCaseMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CreateCaseMixin": ...
    def create(self, vals: Dict[str, Any]) -> "CreateCaseMixin": ...
    def filtered(self, func: Any) -> "CreateCaseMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CreateCaseMixin": ...
    def exists(self) -> "CreateCaseMixin": ...
    def sudo(self) -> "CreateCaseMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CreateCaseMixin": ...

# --- create.child.case ---

class CreateChildCase(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity: str
    commodity_optional: str
    commodity_readonly_default: str
    commodity_required: str
    complaint_ticket_id: "HelpdeskTicket"
    customer_id: "ResPartner"
    has_bit2publish_template: bool
    interaction_id: "SympleInteraction"
    is_commodity_readonly: bool
    is_for_commodity: bool
    is_for_commodity_optional: bool
    is_for_commodity_required: bool
    is_for_ele: bool
    is_for_ele_optional: bool
    is_for_ele_required: bool
    is_for_fiber: bool
    is_for_fiber_optional: bool
    is_for_fiber_required: bool
    is_for_gas: bool
    is_for_gas_optional: bool
    is_for_gas_required: bool
    is_pods_in_pop_up: bool
    is_reiteration: bool
    is_reminder: bool
    is_service_points_in_pop_up: bool
    is_tiqv: bool
    parent_case_id: "HelpdeskTicket"
    pod_ids: "ResPartnerPod"
    reiteration_ticket_id: "HelpdeskTicket"
    selected_fiber_service_point_ids: "ServicePoint"
    selected_pdr_ids: "ResPartnerPdr"
    selected_pod_ids: "ResPartnerPod"
    selected_service_point_ids: "ServicePoint"
    show_bit2publish_button: bool
    ticket_type_id: "HelpdeskTicketType"
    triplet_subtype_id: "SympleTripletSubtype"
    triplet_subtype_ticket_type_ids: "HelpdeskTicketType"
    triplet_type_domain: "SympleTripletType"
    triplet_type_id: "SympleTripletType"
    triplet_type_subtype_ids: "SympleTripletSubtype"
    workflow_id: "SympleWorkflow"
    def browse(self, ids: Union[int, List[int]]) -> "CreateChildCase": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CreateChildCase": ...
    def create(self, vals: Dict[str, Any]) -> "CreateChildCase": ...
    def filtered(self, func: Any) -> "CreateChildCase": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CreateChildCase": ...
    def exists(self) -> "CreateChildCase": ...
    def sudo(self) -> "CreateChildCase": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CreateChildCase": ...

# --- create.interaction.client ---

class CreateInteractionClient(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    channel: str
    complaint_start_date: Optional[_dt.datetime]
    customer_id: "ResPartner"
    edu_id: str
    has_bit2publish_template: bool
    mandatory_snailmail_pdf: bytes
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    type: str
    def browse(self, ids: Union[int, List[int]]) -> "CreateInteractionClient": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CreateInteractionClient": ...
    def create(self, vals: Dict[str, Any]) -> "CreateInteractionClient": ...
    def filtered(self, func: Any) -> "CreateInteractionClient": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CreateInteractionClient": ...
    def exists(self) -> "CreateInteractionClient": ...
    def sudo(self) -> "CreateInteractionClient": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CreateInteractionClient": ...

# --- credit.status ---

class CreditStatus(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    id_code: str
    inbound_sorting_color: str
    is_blocking: bool
    is_insolvent: bool
    name: str
    severity_index: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "CreditStatus": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CreditStatus": ...
    def create(self, vals: Dict[str, Any]) -> "CreditStatus": ...
    def filtered(self, func: Any) -> "CreditStatus": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CreditStatus": ...
    def exists(self) -> "CreditStatus": ...
    def sudo(self) -> "CreditStatus": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CreditStatus": ...

# --- credit.wizard ---

class CreditWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "CreditWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CreditWizard": ...
    def create(self, vals: Dict[str, Any]) -> "CreditWizard": ...
    def filtered(self, func: Any) -> "CreditWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CreditWizard": ...
    def exists(self) -> "CreditWizard": ...
    def sudo(self) -> "CreditWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CreditWizard": ...

# --- customer.service.numbers ---

class CustomerServiceNumbers(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    city: str
    city_id: "ResCity"
    commodity_npi: str
    distributor_id: "ResPartner"
    has_bit2publish_template: bool
    istat: str
    modified_by_operator: bool
    phone: str
    province: str
    show_bit2publish_button: bool
    transporter_id: "ResPartnerTransporter"
    def browse(self, ids: Union[int, List[int]]) -> "CustomerServiceNumbers": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "CustomerServiceNumbers": ...
    def create(self, vals: Dict[str, Any]) -> "CustomerServiceNumbers": ...
    def filtered(self, func: Any) -> "CustomerServiceNumbers": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "CustomerServiceNumbers": ...
    def exists(self) -> "CustomerServiceNumbers": ...
    def sudo(self) -> "CustomerServiceNumbers": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "CustomerServiceNumbers": ...

# --- dashboard.permission ---

class DashboardPermission(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "DashboardPermission": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DashboardPermission": ...
    def create(self, vals: Dict[str, Any]) -> "DashboardPermission": ...
    def filtered(self, func: Any) -> "DashboardPermission": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DashboardPermission": ...
    def exists(self) -> "DashboardPermission": ...
    def sudo(self) -> "DashboardPermission": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DashboardPermission": ...

# --- dashboard.permission.table ---

class DashboardPermissionTable(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    has_bit2publish_template: bool
    has_permission: bool
    permission_id: "DashboardPermission"
    role_id: "SecurityRole"
    show_bit2publish_button: bool
    type_id: "DashboardType"
    def browse(self, ids: Union[int, List[int]]) -> "DashboardPermissionTable": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DashboardPermissionTable": ...
    def create(self, vals: Dict[str, Any]) -> "DashboardPermissionTable": ...
    def filtered(self, func: Any) -> "DashboardPermissionTable": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DashboardPermissionTable": ...
    def exists(self) -> "DashboardPermissionTable": ...
    def sudo(self) -> "DashboardPermissionTable": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DashboardPermissionTable": ...

# --- dashboard.tab ---

class DashboardTab(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "DashboardTab": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DashboardTab": ...
    def create(self, vals: Dict[str, Any]) -> "DashboardTab": ...
    def filtered(self, func: Any) -> "DashboardTab": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DashboardTab": ...
    def exists(self) -> "DashboardTab": ...
    def sudo(self) -> "DashboardTab": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DashboardTab": ...

# --- dashboard.type ---

class DashboardType(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "DashboardType": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DashboardType": ...
    def create(self, vals: Dict[str, Any]) -> "DashboardType": ...
    def filtered(self, func: Any) -> "DashboardType": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DashboardType": ...
    def exists(self) -> "DashboardType": ...
    def sudo(self) -> "DashboardType": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DashboardType": ...

# --- dashboard.visibility.table ---

class DashboardVisibilityTable(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    is_readonly: bool
    role_id: "SecurityRole"
    show_bit2publish_button: bool
    tab_id: "DashboardTab"
    def browse(self, ids: Union[int, List[int]]) -> "DashboardVisibilityTable": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DashboardVisibilityTable": ...
    def create(self, vals: Dict[str, Any]) -> "DashboardVisibilityTable": ...
    def filtered(self, func: Any) -> "DashboardVisibilityTable": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DashboardVisibilityTable": ...
    def exists(self) -> "DashboardVisibilityTable": ...
    def sudo(self) -> "DashboardVisibilityTable": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DashboardVisibilityTable": ...

# --- decimal.precision ---

class DecimalPrecision(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    digits: int
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "DecimalPrecision": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DecimalPrecision": ...
    def create(self, vals: Dict[str, Any]) -> "DecimalPrecision": ...
    def filtered(self, func: Any) -> "DecimalPrecision": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DecimalPrecision": ...
    def exists(self) -> "DecimalPrecision": ...
    def sudo(self) -> "DecimalPrecision": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DecimalPrecision": ...

# --- deposits.wizard ---

class DepositsWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "DepositsWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DepositsWizard": ...
    def create(self, vals: Dict[str, Any]) -> "DepositsWizard": ...
    def filtered(self, func: Any) -> "DepositsWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DepositsWizard": ...
    def exists(self) -> "DepositsWizard": ...
    def sudo(self) -> "DepositsWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DepositsWizard": ...

# --- digest.digest ---

class DigestDigest(Recordset):
    available_fields: str
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    currency_id: "ResCurrency"
    has_bit2publish_template: bool
    is_subscribed: bool
    kpi_account_total_revenue: bool
    kpi_account_total_revenue_value: float
    kpi_helpdesk_tickets_closed: bool
    kpi_helpdesk_tickets_closed_value: int
    kpi_mail_message_total: bool
    kpi_mail_message_total_value: int
    kpi_res_users_connected: bool
    kpi_res_users_connected_value: int
    name: str
    next_run_date: Optional[_dt.date]
    periodicity: str
    show_bit2publish_button: bool
    state: str
    user_ids: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "DigestDigest": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DigestDigest": ...
    def create(self, vals: Dict[str, Any]) -> "DigestDigest": ...
    def filtered(self, func: Any) -> "DigestDigest": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DigestDigest": ...
    def exists(self) -> "DigestDigest": ...
    def sudo(self) -> "DigestDigest": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DigestDigest": ...

# --- digest.tip ---

class DigestTip(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    group_id: "ResGroups"
    has_bit2publish_template: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    tip_description: str
    user_ids: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "DigestTip": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DigestTip": ...
    def create(self, vals: Dict[str, Any]) -> "DigestTip": ...
    def filtered(self, func: Any) -> "DigestTip": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DigestTip": ...
    def exists(self) -> "DigestTip": ...
    def sudo(self) -> "DigestTip": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DigestTip": ...

# --- distributor.code ---

class DistributorCode(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    distributor_id: "ResPartner"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "DistributorCode": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DistributorCode": ...
    def create(self, vals: Dict[str, Any]) -> "DistributorCode": ...
    def filtered(self, func: Any) -> "DistributorCode": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DistributorCode": ...
    def exists(self) -> "DistributorCode": ...
    def sudo(self) -> "DistributorCode": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DistributorCode": ...

# --- distributor.dispatch.zone ---

class DistributorDispatchZone(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    dispatch_zone: str
    distributor_id: "ResPartner"
    end_date: Optional[_dt.date]
    has_bit2publish_template: bool
    is_managed: bool
    show_bit2publish_button: bool
    start_date: Optional[_dt.date]
    utility_type: str
    def browse(self, ids: Union[int, List[int]]) -> "DistributorDispatchZone": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DistributorDispatchZone": ...
    def create(self, vals: Dict[str, Any]) -> "DistributorDispatchZone": ...
    def filtered(self, func: Any) -> "DistributorDispatchZone": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DistributorDispatchZone": ...
    def exists(self) -> "DistributorDispatchZone": ...
    def sudo(self) -> "DistributorDispatchZone": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DistributorDispatchZone": ...

# --- distributor.pod.code.history ---

class DistributorPodCodeHistory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    distributor_id: "ResPartner"
    end_date: Optional[_dt.date]
    has_bit2publish_template: bool
    pod_code: str
    show_bit2publish_button: bool
    start_date: Optional[_dt.date]
    def browse(self, ids: Union[int, List[int]]) -> "DistributorPodCodeHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DistributorPodCodeHistory": ...
    def create(self, vals: Dict[str, Any]) -> "DistributorPodCodeHistory": ...
    def filtered(self, func: Any) -> "DistributorPodCodeHistory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DistributorPodCodeHistory": ...
    def exists(self) -> "DistributorPodCodeHistory": ...
    def sudo(self) -> "DistributorPodCodeHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DistributorPodCodeHistory": ...

# --- dl.appointment.exemption ---

class DlAppointmentExemption(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    distributor_id: "ResPartner"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    ticket_type_ids: "HelpdeskTicketType"
    def browse(self, ids: Union[int, List[int]]) -> "DlAppointmentExemption": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DlAppointmentExemption": ...
    def create(self, vals: Dict[str, Any]) -> "DlAppointmentExemption": ...
    def filtered(self, func: Any) -> "DlAppointmentExemption": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DlAppointmentExemption": ...
    def exists(self) -> "DlAppointmentExemption": ...
    def sudo(self) -> "DlAppointmentExemption": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DlAppointmentExemption": ...

# --- dl.request ---

class DlRequest(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    case_id: "HelpdeskTicket"
    has_bit2publish_template: bool
    insertion_type: str
    paperwork_code: str
    reply_date: Optional[_dt.date]
    request_send_date: Optional[_dt.date]
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "DlRequest": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DlRequest": ...
    def create(self, vals: Dict[str, Any]) -> "DlRequest": ...
    def filtered(self, func: Any) -> "DlRequest": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DlRequest": ...
    def exists(self) -> "DlRequest": ...
    def sudo(self) -> "DlRequest": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DlRequest": ...

# --- documents.document ---

class DocumentsDocument(Recordset):
    active: bool
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    attachment_id: "IrAttachment"
    attachment_name: str
    attachment_type: str
    available_rule_ids: "DocumentsWorkflowRule"
    bit2publish_template_ids: "Bit2publishTemplate"
    checksum: str
    company_id: "ResCompany"
    create_share_id: "DocumentsShare"
    datas: bytes
    description: str
    email_cc: str
    favorited_ids: "ResUsers"
    file_size: int
    folder_id: "DocumentsFolder"
    group_ids: "ResGroups"
    handler: str
    has_bit2publish_template: bool
    has_message: bool
    index_content: str
    is_editable_attachment: bool
    is_favorited: bool
    is_locked: bool
    lock_uid: "ResUsers"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    mimetype: str
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    owner_id: "ResUsers"
    partner_id: "ResPartner"
    previous_attachment_ids: "IrAttachment"
    raw: bytes
    request_activity_id: "MailActivity"
    res_id: int
    res_model: str
    res_model_name: str
    res_name: str
    show_bit2publish_button: bool
    spreadsheet_revision_ids: "SpreadsheetRevision"
    spreadsheet_snapshot: bytes
    tag_ids: "DocumentsTag"
    thumbnail: bytes
    type: str
    url: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "DocumentsDocument": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DocumentsDocument": ...
    def create(self, vals: Dict[str, Any]) -> "DocumentsDocument": ...
    def filtered(self, func: Any) -> "DocumentsDocument": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DocumentsDocument": ...
    def exists(self) -> "DocumentsDocument": ...
    def sudo(self) -> "DocumentsDocument": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DocumentsDocument": ...

# --- documents.facet ---

class DocumentsFacet(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    folder_id: "DocumentsFolder"
    has_bit2publish_template: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    tag_ids: "DocumentsTag"
    tooltip: str
    def browse(self, ids: Union[int, List[int]]) -> "DocumentsFacet": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DocumentsFacet": ...
    def create(self, vals: Dict[str, Any]) -> "DocumentsFacet": ...
    def filtered(self, func: Any) -> "DocumentsFacet": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DocumentsFacet": ...
    def exists(self) -> "DocumentsFacet": ...
    def sudo(self) -> "DocumentsFacet": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DocumentsFacet": ...

# --- documents.folder ---

class DocumentsFolder(Recordset):
    action_count: int
    bit2publish_template_ids: "Bit2publishTemplate"
    children_folder_ids: "DocumentsFolder"
    company_id: "ResCompany"
    description: str
    document_count: int
    document_ids: "DocumentsDocument"
    facet_ids: "DocumentsFacet"
    group_ids: "ResGroups"
    has_bit2publish_template: bool
    name: str
    parent_folder_id: "DocumentsFolder"
    read_group_ids: "ResGroups"
    sequence: int
    share_link_ids: "DocumentsShare"
    show_bit2publish_button: bool
    user_specific: bool
    user_specific_write: bool
    def browse(self, ids: Union[int, List[int]]) -> "DocumentsFolder": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DocumentsFolder": ...
    def create(self, vals: Dict[str, Any]) -> "DocumentsFolder": ...
    def filtered(self, func: Any) -> "DocumentsFolder": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DocumentsFolder": ...
    def exists(self) -> "DocumentsFolder": ...
    def sudo(self) -> "DocumentsFolder": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DocumentsFolder": ...

# --- documents.link_to_record_wizard ---

class DocumentsLinkToRecordWizard(Recordset):
    accessible_model_ids: "IrModel"
    bit2publish_template_ids: "Bit2publishTemplate"
    document_ids: "DocumentsDocument"
    has_bit2publish_template: bool
    is_readonly_model: bool
    model_id: "IrModel"
    resource_ref: Any
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "DocumentsLinkToRecordWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DocumentsLinkToRecordWizard": ...
    def create(self, vals: Dict[str, Any]) -> "DocumentsLinkToRecordWizard": ...
    def filtered(self, func: Any) -> "DocumentsLinkToRecordWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DocumentsLinkToRecordWizard": ...
    def exists(self) -> "DocumentsLinkToRecordWizard": ...
    def sudo(self) -> "DocumentsLinkToRecordWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DocumentsLinkToRecordWizard": ...

# --- documents.mixin ---

class DocumentsMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "DocumentsMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DocumentsMixin": ...
    def create(self, vals: Dict[str, Any]) -> "DocumentsMixin": ...
    def filtered(self, func: Any) -> "DocumentsMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DocumentsMixin": ...
    def exists(self) -> "DocumentsMixin": ...
    def sudo(self) -> "DocumentsMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DocumentsMixin": ...

# --- documents.request_wizard ---

class DocumentsRequestWizard(Recordset):
    activity_date_deadline_range: int
    activity_date_deadline_range_type: str
    activity_note: str
    activity_type_id: "MailActivityType"
    bit2publish_template_ids: "Bit2publishTemplate"
    folder_id: "DocumentsFolder"
    has_bit2publish_template: bool
    name: str
    owner_id: "ResUsers"
    partner_id: "ResPartner"
    res_id: int
    res_model: str
    show_bit2publish_button: bool
    tag_ids: "DocumentsTag"
    def browse(self, ids: Union[int, List[int]]) -> "DocumentsRequestWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DocumentsRequestWizard": ...
    def create(self, vals: Dict[str, Any]) -> "DocumentsRequestWizard": ...
    def filtered(self, func: Any) -> "DocumentsRequestWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DocumentsRequestWizard": ...
    def exists(self) -> "DocumentsRequestWizard": ...
    def sudo(self) -> "DocumentsRequestWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DocumentsRequestWizard": ...

# --- documents.share ---

class DocumentsShare(Recordset):
    access_token: str
    action: str
    activity_date_deadline_range: int
    activity_date_deadline_range_type: str
    activity_note: str
    activity_option: bool
    activity_summary: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    alias_bounced_content: str
    alias_contact: str
    alias_defaults: str
    alias_domain: str
    alias_force_thread_id: int
    alias_id: "MailAlias"
    alias_model_id: "IrModel"
    alias_name: str
    alias_parent_model_id: "IrModel"
    alias_parent_thread_id: int
    alias_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    can_upload: bool
    date_deadline: Optional[_dt.date]
    document_ids: "DocumentsDocument"
    domain: str
    email_drop: bool
    folder_id: "DocumentsFolder"
    full_url: str
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    name: str
    owner_id: "ResUsers"
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    state: str
    tag_ids: "DocumentsTag"
    type: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "DocumentsShare": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DocumentsShare": ...
    def create(self, vals: Dict[str, Any]) -> "DocumentsShare": ...
    def filtered(self, func: Any) -> "DocumentsShare": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DocumentsShare": ...
    def exists(self) -> "DocumentsShare": ...
    def sudo(self) -> "DocumentsShare": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DocumentsShare": ...

# --- documents.tag ---

class DocumentsTag(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    facet_id: "DocumentsFacet"
    folder_id: "DocumentsFolder"
    has_bit2publish_template: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "DocumentsTag": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DocumentsTag": ...
    def create(self, vals: Dict[str, Any]) -> "DocumentsTag": ...
    def filtered(self, func: Any) -> "DocumentsTag": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DocumentsTag": ...
    def exists(self) -> "DocumentsTag": ...
    def sudo(self) -> "DocumentsTag": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DocumentsTag": ...

# --- documents.workflow.action ---

class DocumentsWorkflowAction(Recordset):
    action: str
    bit2publish_template_ids: "Bit2publishTemplate"
    facet_id: "DocumentsFacet"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    tag_id: "DocumentsTag"
    workflow_rule_id: "DocumentsWorkflowRule"
    def browse(self, ids: Union[int, List[int]]) -> "DocumentsWorkflowAction": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DocumentsWorkflowAction": ...
    def create(self, vals: Dict[str, Any]) -> "DocumentsWorkflowAction": ...
    def filtered(self, func: Any) -> "DocumentsWorkflowAction": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DocumentsWorkflowAction": ...
    def exists(self) -> "DocumentsWorkflowAction": ...
    def sudo(self) -> "DocumentsWorkflowAction": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DocumentsWorkflowAction": ...

# --- documents.workflow.rule ---

class DocumentsWorkflowRule(Recordset):
    activity_date_deadline_range: int
    activity_date_deadline_range_type: str
    activity_note: str
    activity_option: bool
    activity_summary: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    condition_type: str
    create_model: str
    criteria_owner_id: "ResUsers"
    criteria_partner_id: "ResPartner"
    domain: str
    domain_folder_id: "DocumentsFolder"
    excluded_tag_ids: "DocumentsTag"
    folder_id: "DocumentsFolder"
    has_bit2publish_template: bool
    has_owner_activity: bool
    limited_to_single_record: bool
    link_model: "IrModel"
    name: str
    note: str
    partner_id: "ResPartner"
    remove_activities: bool
    required_tag_ids: "DocumentsTag"
    sequence: int
    show_bit2publish_button: bool
    tag_action_ids: "DocumentsWorkflowAction"
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "DocumentsWorkflowRule": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "DocumentsWorkflowRule": ...
    def create(self, vals: Dict[str, Any]) -> "DocumentsWorkflowRule": ...
    def filtered(self, func: Any) -> "DocumentsWorkflowRule": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "DocumentsWorkflowRule": ...
    def exists(self) -> "DocumentsWorkflowRule": ...
    def sudo(self) -> "DocumentsWorkflowRule": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "DocumentsWorkflowRule": ...

# --- export.menu ---

class ExportMenu(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    group_ids: "ResGroups"
    has_bit2publish_template: bool
    model_id: "IrModel"
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ExportMenu": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ExportMenu": ...
    def create(self, vals: Dict[str, Any]) -> "ExportMenu": ...
    def filtered(self, func: Any) -> "ExportMenu": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ExportMenu": ...
    def exists(self) -> "ExportMenu": ...
    def sudo(self) -> "ExportMenu": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ExportMenu": ...

# --- export.rules ---

class ExportRules(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    condition: str
    group_id: "ResGroups"
    has_bit2publish_template: bool
    model: str
    model_id: "IrModel"
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ExportRules": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ExportRules": ...
    def create(self, vals: Dict[str, Any]) -> "ExportRules": ...
    def filtered(self, func: Any) -> "ExportRules": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ExportRules": ...
    def exists(self) -> "ExportRules": ...
    def sudo(self) -> "ExportRules": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ExportRules": ...

# --- fetchmail.server ---

class FetchmailServer(Recordset):
    active: bool
    attach: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    channel_to_set: "InteractionChannel"
    configuration: str
    date: Optional[_dt.datetime]
    google_gmail_access_token: str
    google_gmail_access_token_expiration: int
    google_gmail_authorization_code: str
    google_gmail_refresh_token: str
    google_gmail_uri: str
    has_bit2publish_template: bool
    is_microsoft_outlook_configured: bool
    is_pec_server: bool
    is_readonly_contact: bool
    is_ssl: bool
    message_ids: "MailMail"
    microsoft_outlook_access_token: str
    microsoft_outlook_access_token_expiration: int
    microsoft_outlook_refresh_token: str
    microsoft_outlook_uri: str
    name: str
    object_id: "IrModel"
    original: bool
    partner_to_set: "ResPartner"
    password: str
    port: int
    priority: int
    record_created: str
    script: str
    server: str
    server_type: str
    show_bit2publish_button: bool
    state: str
    use_google_gmail_service: bool
    use_microsoft_outlook_service: bool
    user: str
    def browse(self, ids: Union[int, List[int]]) -> "FetchmailServer": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "FetchmailServer": ...
    def create(self, vals: Dict[str, Any]) -> "FetchmailServer": ...
    def filtered(self, func: Any) -> "FetchmailServer": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "FetchmailServer": ...
    def exists(self) -> "FetchmailServer": ...
    def sudo(self) -> "FetchmailServer": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "FetchmailServer": ...

# --- fiber.assistance.ticket ---

class FiberAssistanceTicket(Recordset):
    action: str
    action_motivation_code: str
    action_motivation_reason: str
    active: bool
    additional_service_code: str
    additional_service_code1: str
    additional_service_code2: str
    appointment_datetime: Optional[_dt.datetime]
    appointment_notes: str
    bit2publish_template_ids: "Bit2publishTemplate"
    certificate_data_l2: str
    certificate_data_l3: str
    client_notes: str
    close_date: Optional[_dt.datetime]
    customer_signature: str
    device_action: str
    device_delivery_status: str
    device_password: str
    device_type: str
    end_intervention_doc: bytes
    error_code: str
    error_description: str
    error_reason: str
    error_start_date: Optional[_dt.datetime]
    error_technical_description: str
    fix_responsibility: str
    has_bit2publish_template: bool
    id_appointment: str
    id_device: str
    installation_extension: str
    is_appointment_confirmed: bool
    is_holidays_availability: bool
    is_post_provisioning: bool
    issue_description: str
    iv_referent_phone: str
    master_ticket_code: str
    meters_tot: str
    motivation_code: str
    motivation_code_ticket: str
    motivation_reason: str
    motivation_reason_ticket: str
    nack_result: str
    name: str
    new_gpon: str
    notes: str
    olo_pin: str
    priority_reason: str
    report_category: str
    request_datetime: Optional[_dt.datetime]
    service_name_ticket: str
    service_result: str
    service_result_code: str
    service_result_reason: str
    show_bit2publish_button: bool
    site_type: str
    sla_on_demand_fw: bool
    sla_on_demand_of: str
    status: str
    suspension_close_date: Optional[_dt.datetime]
    suspension_start_date: Optional[_dt.datetime]
    test_action: str
    ticket_code_of: str
    ticket_code_olo: str
    ticket_ids: "HelpdeskTicket"
    ticket_reason: str
    ticket_status_change_date: Optional[_dt.datetime]
    time_availability: str
    withdraw_reason: str
    withdraw_reason_code: str
    def browse(self, ids: Union[int, List[int]]) -> "FiberAssistanceTicket": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "FiberAssistanceTicket": ...
    def create(self, vals: Dict[str, Any]) -> "FiberAssistanceTicket": ...
    def filtered(self, func: Any) -> "FiberAssistanceTicket": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "FiberAssistanceTicket": ...
    def exists(self) -> "FiberAssistanceTicket": ...
    def sudo(self) -> "FiberAssistanceTicket": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "FiberAssistanceTicket": ...

# --- fiber.voucher.management ---

class FiberVoucherManagement(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    connection_fee: str
    end_voucher_date: Optional[_dt.datetime]
    has_bit2publish_template: bool
    name: str
    related_ids: "HelpdeskTicket"
    reservation_voucher_date: Optional[_dt.datetime]
    show_bit2publish_button: bool
    start_voucher_date: Optional[_dt.datetime]
    voucher_type: str
    def browse(self, ids: Union[int, List[int]]) -> "FiberVoucherManagement": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "FiberVoucherManagement": ...
    def create(self, vals: Dict[str, Any]) -> "FiberVoucherManagement": ...
    def filtered(self, func: Any) -> "FiberVoucherManagement": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "FiberVoucherManagement": ...
    def exists(self) -> "FiberVoucherManagement": ...
    def sudo(self) -> "FiberVoucherManagement": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "FiberVoucherManagement": ...

# --- format.address.mixin ---

class FormatAddressMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "FormatAddressMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "FormatAddressMixin": ...
    def create(self, vals: Dict[str, Any]) -> "FormatAddressMixin": ...
    def filtered(self, func: Any) -> "FormatAddressMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "FormatAddressMixin": ...
    def exists(self) -> "FormatAddressMixin": ...
    def sudo(self) -> "FormatAddressMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "FormatAddressMixin": ...

# --- google.gmail.mixin ---

class GoogleGmailMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    google_gmail_access_token: str
    google_gmail_access_token_expiration: int
    google_gmail_authorization_code: str
    google_gmail_refresh_token: str
    google_gmail_uri: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    use_google_gmail_service: bool
    def browse(self, ids: Union[int, List[int]]) -> "GoogleGmailMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "GoogleGmailMixin": ...
    def create(self, vals: Dict[str, Any]) -> "GoogleGmailMixin": ...
    def filtered(self, func: Any) -> "GoogleGmailMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "GoogleGmailMixin": ...
    def exists(self) -> "GoogleGmailMixin": ...
    def sudo(self) -> "GoogleGmailMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "GoogleGmailMixin": ...

# --- google.service ---

class GoogleService(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "GoogleService": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "GoogleService": ...
    def create(self, vals: Dict[str, Any]) -> "GoogleService": ...
    def filtered(self, func: Any) -> "GoogleService": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "GoogleService": ...
    def exists(self) -> "GoogleService": ...
    def sudo(self) -> "GoogleService": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "GoogleService": ...

# --- helpdesk.sla ---

class HelpdeskSla(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    description: str
    exclude_stage_ids: "HelpdeskStage"
    has_bit2publish_template: bool
    name: str
    partner_ids: "ResPartner"
    priority: str
    send_email_when_sla_expires: bool
    show_bit2publish_button: bool
    sla_expired_mail_template_id: "MailTemplate"
    stage_id: "HelpdeskStage"
    tag_ids: "HelpdeskTag"
    team_id: "HelpdeskTeam"
    ticket_count: int
    ticket_type_id: "HelpdeskTicketType"
    time: float
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskSla": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskSla": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskSla": ...
    def filtered(self, func: Any) -> "HelpdeskSla": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskSla": ...
    def exists(self) -> "HelpdeskSla": ...
    def sudo(self) -> "HelpdeskSla": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskSla": ...

# --- helpdesk.sla.policy ---

class HelpdeskSlaPolicy(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    description: str
    domain: str
    duration: float
    duration_type: str
    end_date_id: "IrModelFields"
    has_bit2publish_template: bool
    is_dynamic: bool
    is_official: bool
    name: str
    resource_calendar_id: "ResourceCalendar"
    responsibility: str
    send_email_when_sla_expires: bool
    show_bit2publish_button: bool
    sla_case_ids: "HelpdeskTicket"
    sla_expired_mail_template_id: "MailTemplate"
    start_date_id: "IrModelFields"
    tag_ids: "HelpdeskTag"
    ticket_count: int
    triplet_phase_id: "SympleTripletPhase"
    unit: str
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskSlaPolicy": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskSlaPolicy": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskSlaPolicy": ...
    def filtered(self, func: Any) -> "HelpdeskSlaPolicy": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskSlaPolicy": ...
    def exists(self) -> "HelpdeskSlaPolicy": ...
    def sudo(self) -> "HelpdeskSlaPolicy": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskSlaPolicy": ...

# --- helpdesk.sla.policy.status ---

class HelpdeskSlaPolicyStatus(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    color: int
    deadline: Optional[_dt.datetime]
    dl_request_end_id: "DlRequest"
    dl_request_start_id: "DlRequest"
    duration: float
    duration_type: str
    end_date: Optional[_dt.datetime]
    exceeded_days: float
    has_bit2publish_template: bool
    is_dynamic: bool
    is_official: bool
    name: str
    reached_datetime: Optional[_dt.datetime]
    responsibility: str
    show_bit2publish_button: bool
    sla_id: "HelpdeskSlaPolicy"
    start_date: Optional[_dt.datetime]
    status: str
    ticket_id: "HelpdeskTicket"
    triplet_phase_id: "SympleTripletPhase"
    unit: str
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskSlaPolicyStatus": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskSlaPolicyStatus": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskSlaPolicyStatus": ...
    def filtered(self, func: Any) -> "HelpdeskSlaPolicyStatus": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskSlaPolicyStatus": ...
    def exists(self) -> "HelpdeskSlaPolicyStatus": ...
    def sudo(self) -> "HelpdeskSlaPolicyStatus": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskSlaPolicyStatus": ...

# --- helpdesk.sla.report.analysis ---

class HelpdeskSlaReportAnalysis(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    close_date: Optional[_dt.datetime]
    company_id: "ResCompany"
    has_bit2publish_template: bool
    partner_id: "ResPartner"
    priority: str
    show_bit2publish_button: bool
    sla_deadline: Optional[_dt.datetime]
    sla_exceeded_days: int
    sla_id: "HelpdeskSla"
    sla_phase_id: "SympleTripletPhase"
    sla_policy_deadline: Optional[_dt.datetime]
    sla_policy_exceeded_days: int
    sla_policy_id: "HelpdeskSlaPolicy"
    sla_policy_reached_datetime: Optional[_dt.datetime]
    sla_policy_status: str
    sla_policy_status_failed: bool
    sla_policy_status_progress: bool
    sla_policy_status_success: bool
    sla_reached_datetime: Optional[_dt.datetime]
    sla_stage_id: "HelpdeskStage"
    sla_status: str
    sla_status_failed: bool
    team_id: "HelpdeskTeam"
    ticket_assignation_hours: int
    ticket_closed: bool
    ticket_close_hours: int
    ticket_deadline: Optional[_dt.datetime]
    ticket_failed: bool
    ticket_id: "HelpdeskTicket"
    ticket_open_hours: int
    ticket_policy_deadline: Optional[_dt.datetime]
    ticket_policy_failed: bool
    ticket_stage_id: "HelpdeskStage"
    ticket_type_id: "HelpdeskTicketType"
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskSlaReportAnalysis": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskSlaReportAnalysis": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskSlaReportAnalysis": ...
    def filtered(self, func: Any) -> "HelpdeskSlaReportAnalysis": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskSlaReportAnalysis": ...
    def exists(self) -> "HelpdeskSlaReportAnalysis": ...
    def sudo(self) -> "HelpdeskSlaReportAnalysis": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskSlaReportAnalysis": ...

# --- helpdesk.sla.status ---

class HelpdeskSlaStatus(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    color: int
    deadline: Optional[_dt.datetime]
    exceeded_days: float
    has_bit2publish_template: bool
    is_mail_sent: bool
    reached_datetime: Optional[_dt.datetime]
    show_bit2publish_button: bool
    sla_id: "HelpdeskSla"
    sla_stage_id: "HelpdeskStage"
    status: str
    ticket_id: "HelpdeskTicket"
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskSlaStatus": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskSlaStatus": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskSlaStatus": ...
    def filtered(self, func: Any) -> "HelpdeskSlaStatus": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskSlaStatus": ...
    def exists(self) -> "HelpdeskSlaStatus": ...
    def sudo(self) -> "HelpdeskSlaStatus": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskSlaStatus": ...

# --- helpdesk.stage ---

class HelpdeskStage(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    fold: bool
    has_bit2publish_template: bool
    is_canceled: bool
    is_close: bool
    is_ko: bool
    is_processing: bool
    legend_blocked: str
    legend_done: str
    legend_normal: str
    name: str
    sequence: int
    show_bit2publish_button: bool
    stage_code: str
    team_ids: "HelpdeskTeam"
    template_id: "MailTemplate"
    ticket_count: int
    triplet_phase_type_id: "SympleTripletPhaseType"
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskStage": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskStage": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskStage": ...
    def filtered(self, func: Any) -> "HelpdeskStage": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskStage": ...
    def exists(self) -> "HelpdeskStage": ...
    def sudo(self) -> "HelpdeskStage": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskStage": ...

# --- helpdesk.tag ---

class HelpdeskTag(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    color: int
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskTag": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskTag": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskTag": ...
    def filtered(self, func: Any) -> "HelpdeskTag": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskTag": ...
    def exists(self) -> "HelpdeskTag": ...
    def sudo(self) -> "HelpdeskTag": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskTag": ...

# --- helpdesk.team ---

class HelpdeskTeam(Recordset):
    active: bool
    alias_bounced_content: str
    alias_contact: str
    alias_defaults: str
    alias_domain: str
    alias_force_thread_id: int
    alias_id: "MailAlias"
    alias_model_id: "IrModel"
    alias_name: str
    alias_parent_model_id: "IrModel"
    alias_parent_thread_id: int
    alias_user_id: "ResUsers"
    allow_portal_ticket_closing: bool
    assign_method: str
    auto_close_day: int
    auto_close_ticket: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    color: int
    company_id: "ResCompany"
    description: str
    display_alias_name: str
    from_stage_ids: "HelpdeskStage"
    group_member_ids: "ResUsers"
    group_roles_ids: "SecurityRole"
    has_bit2publish_template: bool
    has_external_mail_server: bool
    has_message: bool
    has_motivation_required: bool
    is_service_task: bool
    member_ids: "ResUsers"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    name: str
    open_ticket_count: int
    portal_show_rating: bool
    privacy: str
    rating_count: int
    rating_ids: "RatingRating"
    rating_percentage_satisfaction: int
    resource_calendar_id: "ResourceCalendar"
    sequence: int
    show_bit2publish_button: bool
    sla_policy_count: int
    stage_ids: "HelpdeskStage"
    ticket_ids: "HelpdeskTicket"
    to_stage_id: "HelpdeskStage"
    unassigned_tickets: int
    upcoming_sla_fail_tickets: int
    use_alias: bool
    use_coupons: bool
    use_credit_notes: bool
    use_fsm: bool
    use_helpdesk_sale_timesheet: bool
    use_helpdesk_timesheet: bool
    use_product_repairs: bool
    use_product_returns: bool
    use_rating: bool
    use_sla: bool
    use_twitter: bool
    use_website_helpdesk_form: bool
    use_website_helpdesk_forum: bool
    use_website_helpdesk_livechat: bool
    use_website_helpdesk_slides: bool
    visibility_member_ids: "ResUsers"
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskTeam": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskTeam": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskTeam": ...
    def filtered(self, func: Any) -> "HelpdeskTeam": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskTeam": ...
    def exists(self) -> "HelpdeskTeam": ...
    def sudo(self) -> "HelpdeskTeam": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskTeam": ...

# --- helpdesk.technical.check ---

class HelpdeskTechnicalCheck(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    is_other: bool
    is_other_operations: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskTechnicalCheck": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskTechnicalCheck": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskTechnicalCheck": ...
    def filtered(self, func: Any) -> "HelpdeskTechnicalCheck": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskTechnicalCheck": ...
    def exists(self) -> "HelpdeskTechnicalCheck": ...
    def sudo(self) -> "HelpdeskTechnicalCheck": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskTechnicalCheck": ...

# --- helpdesk.ticket ---

class HelpdeskTicket(Recordset):
    access_token: str
    access_url: str
    access_warning: str
    activation_service: str
    active: bool
    active_phase_note: str
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    administrative_cost: float
    ae10050: str
    ae10100: str
    ae10150: str
    agency_id: "ResPartner"
    agreed_by: str
    alternative_email: str
    alternative_phone: str
    annulment_reason: str
    application_mobile_number: str
    appointment_date: Optional[_dt.date]
    appointment_time_slot: str
    asset_id: str
    assign_date: Optional[_dt.datetime]
    assign_hours: int
    ateco_category_ids: "AtecoCategory"
    attempts_number: int
    attestation_unpaid_amount: float
    automatic_contract_communication_channel: str
    automatic_phase_result_id: "SympleTripletPhaseResult"
    automatic_sms_template_id: "SmsTemplate"
    automatic_template_id: "MailTemplate"
    available_distance: float
    available_power: str
    b2w_contract_channel: str
    b2w_contract_number: str
    b2w_contract_type: str
    billing_refund_amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    bpmn_diagram: str
    cadastral_data_dc01_ids: "CadastreData"
    cadastral_data_gd07_ids: "CadastreData"
    cadastre_data_count: int
    campaign: str
    campaign_id: "UtmCampaign"
    case_code: str
    catalog: str
    change_product_id: str
    change_product_start_date: Optional[_dt.date]
    change_start_date: Optional[_dt.date]
    change_value: str
    channel_id: "InteractionChannel"
    channel_origin: str
    child_case_ids: "HelpdeskTicket"
    close_date: Optional[_dt.datetime]
    closed_by_partner: bool
    close_hours: int
    close_login: str
    cluster_id: "SympleCluster"
    color: int
    commercial_charge: float
    commercial_partner_id: "ResPartner"
    commodity: str
    communication_date: Optional[_dt.datetime]
    company_id: "ResCompany"
    company_type: str
    complaint_end_date: Optional[_dt.datetime]
    complaint_reception_date: Optional[_dt.datetime]
    complaint_start_date: Optional[_dt.datetime]
    complaint_ticket_id: "HelpdeskTicket"
    condition_variation: str
    contract_count: int
    contract_end_date: Optional[_dt.date]
    contract_end_reason: str
    contract_estimated_end_date: Optional[_dt.date]
    contract_ids: "SorgeniaContracts"
    contract_referent_id: "ResPartner"
    contract_signed_date: Optional[_dt.date]
    correction_invoice_ids: "CorrectionInvoice"
    correction_response_date: Optional[_dt.date]
    cost: float
    coupon_code: str
    coupon_redemption_date: Optional[_dt.date]
    create_login: str
    css_for_readonly_mode: str
    currency_id: "ResCurrency"
    customer_code: str
    customer_id: "ResPartner"
    data_overwritten: bool
    date_deactivation_limit: Optional[_dt.datetime]
    date_deactivation_start: Optional[_dt.datetime]
    date_last_stage_update: Optional[_dt.datetime]
    date_sent_advice_autolettura: Optional[_dt.datetime]
    date_sent_advice_digital_payment: Optional[_dt.datetime]
    declared_annual_usage: float
    default_template_ids: "MailTemplate"
    description: str
    disconnect_date: Optional[_dt.date]
    distributor_charge: float
    distributor_code: str
    distributor_id: str
    distributor_notes: str
    dl_reply_date: Optional[_dt.date]
    dl_request_ids: "DlRequest"
    dl_request_send_date: Optional[_dt.date]
    dl_set_date: Optional[_dt.date]
    domain_user_ids: "ResUsers"
    email: str
    email_cc: str
    email_priority: str
    email_unread: bool
    email_wizard: str
    energy_use_type: str
    error_message: str
    estimated_time: str
    expected_closing_date: Optional[_dt.date]
    expected_supply_start_date: Optional[_dt.date]
    expired_balance: float
    export_autolettura_gas_filter_timestamp: Optional[_dt.datetime]
    extraction_class: str
    extra_tirv_account_holder_full_name: str
    extra_tirv_beneficiary_full_name: str
    extra_tirv_refund_address: str
    extra_tirv_refund_iban: str
    extra_tirv_refund_method: str
    extra_tirv_refund_reason: str
    extra_tirv_requested_refund_amount: float
    failed_sla_responsibility: str
    fiber_ticket_id: "FiberAssistanceTicket"
    fiber_voucher_id: "FiberVoucherManagement"
    force_blacklist: bool
    force_credit_check: bool
    force_dl: str
    force_supply_start_date: bool
    fw_ticket_id: str
    group_member_ids: "ResUsers"
    has_bit2publish_template: bool
    hash_create_interaction_case: str
    has_message: bool
    has_sla: bool
    helpdesk_sla_ids: "HelpdeskSlaPolicy"
    i86_ccr_alias: str
    i86_payment_date: Optional[_dt.date]
    i86_payment_id: str
    i86_payment_item_ids: "I86PaymentItem"
    i86_payment_mode: str
    id_vocal_order: str
    incoming_mail_server_id: "FetchmailServer"
    incoming_mail_server_user: str
    incompatible_ticket_ids: "HelpdeskTicket"
    infocamere_watchlist_id: "ResPartnerInfocamere"
    info_message: str
    instance_key_ids: "SymplePbInstanceKey"
    integration_history_ids: "CaseIntegrationHistory"
    interaction_ids: "SympleInteraction"
    intervention_cost: float
    intervention_distance: float
    intervention_type: str
    invoice_correction_date: Optional[_dt.date]
    invoice_date: Optional[_dt.date]
    invoice_id: str
    invoicing_address_id: "ResPartner"
    is_annulment_in_progress: bool
    is_annulment_request: bool
    is_appointment_charged_to_distributor: bool
    is_automated_communication: bool
    is_automatic_case: bool
    is_billing_correction: bool
    is_canceled: bool
    is_check_child_cases: bool
    is_close: bool
    is_compute_refund: bool
    is_contains_inorder_items: bool
    is_document_sent: bool
    is_execute_code_at_phase_change: bool
    is_externally_integrated: bool
    is_fiber_activation: bool
    is_fiber_deactivation: bool
    is_giroconto: bool
    is_happy_customer: bool
    is_ko: bool
    is_logged_user_a_team_member: bool
    is_mail_managed: str
    is_meter_readings: bool
    is_multisito: bool
    is_needs_child_case: bool
    is_no_sla_config: bool
    is_not_disconnectable: bool
    is_notified_tiqv: bool
    is_not_to_solicit: bool
    is_other_technical_check: bool
    is_phone: bool
    is_pick_refund_template: bool
    is_point_suspended: bool
    is_postalizer_visible: bool
    is_process_managed: bool
    is_quote_reminder_sent: bool
    is_refund_child_case_created: bool
    is_reiteration: bool
    is_reminder: bool
    is_remove_oneri: bool
    is_residence: bool
    is_retroactive_voltura: bool
    is_run_code_by_cron: bool
    is_sms_managed: str
    is_split_payment: bool
    is_suspended: bool
    is_technical_check: bool
    is_timeout: bool
    is_tiqv: bool
    is_tiqv_indemnity_done: bool
    is_tisg_received: bool
    is_to_refuse: bool
    is_to_suspend: bool
    is_unexecuted: bool
    is_vsg_ticket: bool
    iva_rate: str
    kanban_state: str
    kanban_state_label: str
    last_phase_update_date: Optional[_dt.datetime]
    latest_correction_invoice_issuing_date: Optional[_dt.date]
    legal_address_id: "ResPartner"
    legal_basis: str
    legal_possession_date: Optional[_dt.date]
    legend_blocked: str
    legend_done: str
    legend_normal: str
    locked_balance: float
    ma26_amount_to_be_refunded: float
    ma26_name: str
    ma26_refund_address: str
    ma26_refund_amount: float
    ma26_refund_channel: str
    ma26_refund_city_id: "ResCity"
    ma26_refund_date: Optional[_dt.date]
    ma26_refund_iban: str
    ma26_refund_method: str
    ma26_refund_state_id: "ResCountryState"
    ma26_refund_zip: str
    ma26_refusal_reason: str
    market: str
    market_change_start_date: Optional[_dt.date]
    market_comm_event_log_ids: "MarketCommEventLog"
    matrix_process_id: str
    max_execution_time: str
    max_requested_power: str
    medium_id: "UtmMedium"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    meter_check_ids: "HelpdeskTechnicalCheck"
    meter_check_other: str
    meter_reading_message: str
    meter_reading_result: str
    meter_readings: str
    migrated: bool
    mkt_comm_atti_autorizzativi: str
    mkt_comm_causal_code: str
    mkt_comm_cod_esito: str
    mkt_comm_cognome_resp_verifica: str
    mkt_comm_costo: float
    mkt_comm_costo_lab: float
    mkt_comm_costo_loco: float
    mkt_comm_cp_gestore: str
    mkt_comm_cp_utente: str
    mkt_comm_data_disattivazione: Optional[_dt.date]
    mkt_comm_dettaglio_esito: str
    mkt_comm_motivazione: str
    mkt_comm_nome_resp_verifica: str
    mkt_comm_note: str
    mkt_comm_request_type: str
    mkt_comm_rif_preventivo: str
    mkt_comm_segn_conv: str
    mkt_comm_segn_mis: str
    mkt_comm_stima_tempi: str
    mkt_comm_tel_1: str
    mkt_comm_tel_2: str
    ml_refund_amount: float
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    needs_child_result_id: "SympleTripletPhaseResult"
    new_asset_id: str
    new_connection_end_date: Optional[_dt.date]
    new_connection_start_date: Optional[_dt.date]
    new_connection_type: str
    no_refund_phase_result_id: "SympleTripletPhaseResult"
    no_refund_template_id: "MailTemplate"
    not_disconnectable_category: str
    notify_cpe_description: str
    offer_code: str
    official_sla_status: str
    of_ticket_code: str
    olo_order_code: str
    olo_ticket_code: str
    olo_ticket_id: str
    open_hours: int
    order_id: str
    origin: str
    original_catalog: str
    origin_practice: str
    other_check_ids: "HelpdeskTechnicalCheck"
    other_interaction_ids: "SympleInteraction"
    outcome_confirmation: str
    parent_case_id: "HelpdeskTicket"
    partner_email: str
    partner_id: "ResPartner"
    partner_name: str
    partner_phone: str
    partner_ticket_count: int
    partner_ticket_ids: "HelpdeskTicket"
    payment_method_id: "PaymentMethod"
    pdf_attachment: bytes
    pdf_attachment_filename: str
    pdf_contract_file: bytes
    pdr_change_value_id: "Unknown"
    pdr_code: str
    pdr_ids: "ResPartnerPdr"
    pdr_type: str
    phase_is_voidable: bool
    phone: str
    physical_bonus_id: "PhysicalBonus"
    physical_bonus_line_cf: str
    physical_bonus_line_data_deco: Optional[_dt.date]
    physical_bonus_line_data_fine: Optional[_dt.date]
    physical_bonus_line_id: "PhysicalBonusLine"
    physical_bonus_line_last_error: str
    physical_bonus_line_tipo_compe: str
    pod_code: str
    pod_ids: "ResPartnerPod"
    postalizer_document_ids: "SorgeniaPostalizerDocument"
    predeterminability_text: str
    priority: str
    process_credit_code: str
    process_distributor_code: str
    product: str
    proposal_code: str
    quote_accepted_date: Optional[_dt.date]
    quote_amount: float
    quote_code: str
    quote_expiration_date: Optional[_dt.date]
    quote_number: str
    quote_received_date: Optional[_dt.date]
    quote_sent_date: Optional[_dt.date]
    rai_fee_id: "RaiFee"
    rai_fee_line_cf: str
    rai_fee_line_error: str
    rai_fee_line_id: "RaiFeeLine"
    rate_plan_market: str
    rating_avg: float
    rating_count: int
    rating_ids: "RatingRating"
    rating_last_feedback: str
    rating_last_image: bytes
    rating_last_value: float
    rcu_line_id: "SympleRcuLine"
    rcu_message_code: str
    reach: str
    reading_estimate_date: Optional[_dt.date]
    refund_amount: float
    refund_payment_date: Optional[_dt.date]
    refund_payment_rr_date: Optional[_dt.date]
    refund_phase_result_id: "SympleTripletPhaseResult"
    refund_template_id: "MailTemplate"
    refusal_reason: str
    reiteration_ticket_id: "HelpdeskTicket"
    relation_type: str
    remi_code: str
    request_date: Optional[_dt.date]
    requested_gas_use_type: str
    requested_pdr_meter_type: str
    requested_pdr_type: str
    requested_thermal_flow: str
    request_type: str
    resolutive_billing_correction: bool
    response_channel_id: "InteractionChannel"
    resultative_case: str
    resultative_case_id: "HelpdeskTicket"
    resultative_dl_request_ids: "DlRequest"
    resultative_refund_amount: float
    resultative_refund_date: Optional[_dt.date]
    rif_preventivo_atti_autorizzativi: str
    sale_document_number: str
    sdd_auth_code: str
    self_reading_is_automatic_case: bool
    send_email: str
    send_email_and_set_result: str
    sending_via: str
    send_sms: bool
    service_point_ids: "ServicePoint"
    set_result_automatically: str
    show_bit2publish_button: bool
    show_connect_parent_case_button: bool
    show_i86_ccr_payment_tab: bool
    show_integration_history_tab: bool
    show_invoice_tab: bool
    show_market_comm_event_logs_tab: bool
    sii_activation: str
    skip_communication: bool
    sla_deadline: Optional[_dt.datetime]
    sla_fail: bool
    sla_ids: "HelpdeskSla"
    sla_policy_deadline: Optional[_dt.datetime]
    sla_reached_late: bool
    sla_status_deadline_ids: "HelpdeskSlaStatus"
    sla_status_deadlines: "HelpdeskSlaPolicyStatus"
    sla_statuses: "HelpdeskSlaPolicyStatus"
    sla_status_ids: "HelpdeskSlaStatus"
    sla_success: bool
    sms_phase_ko_result_id: "SympleTripletPhaseResult"
    sms_phase_result_ok_id: "SympleTripletPhaseResult"
    social_bonus_id: "SocialBonus"
    social_bonus_line_error: str
    social_bonus_line_id: "SocialBonusLine"
    social_bonus_starting_state: str
    source_id: "UtmSource"
    stage_id: "HelpdeskStage"
    start_processing_date: Optional[_dt.datetime]
    subtype_code_1: str
    subtype_code_2: str
    supply_address: str
    symphonie_process: str
    symphony_case_ids: "SymphonyCaseId"
    symple_interaction_id: "SympleInteraction"
    system_transfer_distance: str
    tables: str
    tag_ids: "HelpdeskTag"
    tax_rate: str
    team_id: "HelpdeskTeam"
    tension: str
    tension_check_reason: str
    tension_type: str
    tg_symphonie_process: str
    ticket_rc_history_ids: "HelpdeskTicketRcHistory"
    ticket_type_id: "HelpdeskTicketType"
    tiqv_indemnity_date: Optional[_dt.date]
    tiqv_ml_indemnity_date: Optional[_dt.date]
    tirv_complaint_end_date: Optional[_dt.date]
    tirv_complaint_start_date: Optional[_dt.date]
    tirv_issue_date: Optional[_dt.date]
    tirv_welcome_letter_date: Optional[_dt.date]
    tisg_id: "SorgeniaTisg"
    tisg_line_id: "SorgeniaTisgLine"
    to_not_execute_before: Optional[_dt.date]
    triplet_active_phase_id: "SympleTripletPhase"
    triplet_allowed_phase_ids: "SympleTripletPhase"
    triplet_allowed_phase_result_ids: "SympleTripletPhaseResult"
    triplet_checkpoint_phase_id: "SympleTripletPhase"
    triplet_code: str
    triplet_history_phase_ids: "SympleTripletPhaseHistory"
    triplet_phase_id: "SympleTripletPhase"
    triplet_phase_result_id: "SympleTripletPhaseResult"
    triplet_start_phase_id: "SympleTripletPhase"
    triplet_subtype_id: "SympleTripletSubtype"
    triplet_subtype_ticket_type_ids: "HelpdeskTicketType"
    triplet_type_id: "SympleTripletType"
    triplet_type_subtype_ids: "SympleTripletSubtype"
    type_code: str
    unexecuted_client_payment_id: "ResPartnerPayment"
    unexecuted_invoice_number: str
    unexecuted_reason: str
    unexecuted_record_count: int
    unexecuted_record_ids: "UnexecutedRecord"
    unexecuted_sent_date: Optional[_dt.date]
    unexecuted_server_id: "SorgeniaInvoiceExternalServiceFtpServer"
    unsuccess_reason_id: "SympleTripletUnsuccessReason"
    upsa_id: "SorgeniaUpsa"
    upsa_line_at: Optional[_dt.date]
    upsa_line_from: Optional[_dt.date]
    upsa_line_id: "SorgeniaUpsaLine"
    use_coupons: bool
    use_credit_notes: bool
    use_product_repairs: bool
    use_product_returns: bool
    use_rating: bool
    user_code: str
    user_id: "ResUsers"
    use_sla: bool
    use_type: str
    verifier_first_phone_number: str
    verifier_lastname: str
    verifier_name: str
    verifier_second_phone_number: str
    visible_tab_names: str
    visible_tabs_ids: "TabVisibility"
    voltura_outgoing_client_code: str
    voltura_outgoing_client_id: "ResPartner"
    voltura_outgoing_client_name: str
    voltura_phone_number: str
    voltura_start_date: Optional[_dt.date]
    voltura_type: str
    voltura_use_type: str
    warranty_id: "SorgeniaWarranty"
    website_message_ids: "MailMessage"
    wizard: str
    wizard_address_id: "ResPartner"
    wizard_distributor_notes: str
    work_execution_date: Optional[_dt.date]
    workflow_alternative_phone: bool
    workflow_id: "SympleWorkflow"
    workflow_send_sms: bool
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskTicket": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskTicket": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskTicket": ...
    def filtered(self, func: Any) -> "HelpdeskTicket": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskTicket": ...
    def exists(self) -> "HelpdeskTicket": ...
    def sudo(self) -> "HelpdeskTicket": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskTicket": ...

# --- helpdesk.ticket.amounts ---

class HelpdeskTicketAmounts(Recordset):
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    end_date: Optional[_dt.date]
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    start_date: Optional[_dt.date]
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskTicketAmounts": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskTicketAmounts": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskTicketAmounts": ...
    def filtered(self, func: Any) -> "HelpdeskTicketAmounts": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskTicketAmounts": ...
    def exists(self) -> "HelpdeskTicketAmounts": ...
    def sudo(self) -> "HelpdeskTicketAmounts": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskTicketAmounts": ...

# --- helpdesk.ticket.importer ---

class HelpdeskTicketImporter(Recordset):
    advance_payment: float
    bit2publish_template_ids: "Bit2publishTemplate"
    case_id: "HelpdeskTicket"
    client_code: str
    client_id: "ResPartner"
    error: str
    expiration_date: Optional[_dt.date]
    frequency: str
    has_bit2publish_template: bool
    installments_number: int
    invoice_number: str
    invoice_type: str
    notes: str
    payment_method: str
    plan_result: str
    processing_date: Optional[_dt.datetime]
    show_bit2publish_button: bool
    state: str
    ticket_type_id: "HelpdeskTicketType"
    triplet_subtype_id: "SympleTripletSubtype"
    triplet_type_id: "SympleTripletType"
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskTicketImporter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskTicketImporter": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskTicketImporter": ...
    def filtered(self, func: Any) -> "HelpdeskTicketImporter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskTicketImporter": ...
    def exists(self) -> "HelpdeskTicketImporter": ...
    def sudo(self) -> "HelpdeskTicketImporter": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskTicketImporter": ...

# --- helpdesk.ticket.rc.history ---

class HelpdeskTicketRcHistory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    date: Optional[_dt.datetime]
    has_bit2publish_template: bool
    key: str
    show_bit2publish_button: bool
    ticket_id: "HelpdeskTicket"
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskTicketRcHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskTicketRcHistory": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskTicketRcHistory": ...
    def filtered(self, func: Any) -> "HelpdeskTicketRcHistory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskTicketRcHistory": ...
    def exists(self) -> "HelpdeskTicketRcHistory": ...
    def sudo(self) -> "HelpdeskTicketRcHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskTicketRcHistory": ...

# --- helpdesk.ticket.report.analysis ---

class HelpdeskTicketReportAnalysis(Recordset):
    active: bool
    assign_date: Optional[_dt.datetime]
    bit2publish_template_ids: "Bit2publishTemplate"
    close_date: Optional[_dt.datetime]
    company_id: "ResCompany"
    has_bit2publish_template: bool
    kanban_state: str
    partner_id: "ResPartner"
    priority: str
    rating_last_value: float
    show_bit2publish_button: bool
    sla_fail: bool
    team_id: "HelpdeskTeam"
    ticket_assignation_hours: float
    ticket_close_hours: float
    ticket_deadline: Optional[_dt.datetime]
    ticket_id: "HelpdeskTicket"
    ticket_open_hours: float
    ticket_phase_id: "SympleTripletPhase"
    ticket_policy_deadline: Optional[_dt.datetime]
    ticket_stage_id: "HelpdeskStage"
    ticket_type_id: "HelpdeskTicketType"
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskTicketReportAnalysis": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskTicketReportAnalysis": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskTicketReportAnalysis": ...
    def filtered(self, func: Any) -> "HelpdeskTicketReportAnalysis": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskTicketReportAnalysis": ...
    def exists(self) -> "HelpdeskTicketReportAnalysis": ...
    def sudo(self) -> "HelpdeskTicketReportAnalysis": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskTicketReportAnalysis": ...

# --- helpdesk.ticket.rule ---

class HelpdeskTicketRule(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    case_domain: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "HelpdeskTicketRule": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "HelpdeskTicketRule": ...
    def create(self, vals: Dict[str, Any]) -> "HelpdeskTicketRule": ...
    def filtered(self, func: Any) -> "HelpdeskTicketRule": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskTicketRule": ...
    def exists(self) -> "HelpdeskTicketRule": ...
    def sudo(self) -> "HelpdeskTicketRule": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskTicketRule": ...

# --- helpdesk.ticket.type ---

class HelpdeskTicketType(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    cluster_id: "SympleCluster"
    code: str
    commodity_readonly_default: str
    domain_of_detail: str
    has_alternative_email: bool
    has_bit2publish_template: bool
    is_an_02: bool
    is_an_03: bool
    is_an_04: bool
    is_an_06: bool
    is_an_22: bool
    is_at_01: bool
    is_cc12_1: bool
    is_cessazione_se3: bool
    is_cessazione_vt4: bool
    is_commodity_readonly: bool
    is_for_commodity: bool
    is_for_commodity_optional: bool
    is_for_commodity_required: bool
    is_for_ele: bool
    is_for_ele_optional: bool
    is_for_ele_required: bool
    is_for_fiber: bool
    is_for_fiber_optional: bool
    is_for_fiber_required: bool
    is_for_gas: bool
    is_for_gas_optional: bool
    is_for_gas_required: bool
    is_from_migration: bool
    is_iban_ma29: bool
    is_market_change: bool
    is_market_l: bool
    is_market_t: bool
    is_meter_readings: bool
    is_point_required: bool
    is_rcu_ignore_date_check: bool
    is_reiteration: bool
    is_reminder: bool
    is_sb05_1: bool
    is_sb05_2: bool
    is_sb05_3: bool
    is_sdd_cancel: bool
    is_select_parent: bool
    is_service_points_in_pop_up: bool
    is_triplet_market: bool
    is_visible_to_operators: bool
    m2c_ifa: str
    name: str
    needs_interaction: bool
    parent_case_domain: str
    sequence: int
    show_bit2publish_button: bool
    subtype_id: "SympleTripletSubtype"
    univocal_code: str
    workflow_id: "SympleWorkflow"
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
    def sorted(self, key: Any = None, reverse: bool = False) -> "HelpdeskTicketType": ...
    def exists(self) -> "HelpdeskTicketType": ...
    def sudo(self) -> "HelpdeskTicketType": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "HelpdeskTicketType": ...

# --- i86.payment.item ---

class I86PaymentItem(Recordset):
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    installment_id: str
    invoice_id: str
    payment_slip_id: str
    show_bit2publish_button: bool
    ticket_id: "HelpdeskTicket"
    def browse(self, ids: Union[int, List[int]]) -> "I86PaymentItem": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "I86PaymentItem": ...
    def create(self, vals: Dict[str, Any]) -> "I86PaymentItem": ...
    def filtered(self, func: Any) -> "I86PaymentItem": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "I86PaymentItem": ...
    def exists(self) -> "I86PaymentItem": ...
    def sudo(self) -> "I86PaymentItem": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "I86PaymentItem": ...

# --- iap.account ---

class IapAccount(Recordset):
    account_token: str
    api_auth_cred: str
    api_auth_type: str
    api_content_header: str
    api_endpoint: str
    bit2publish_template_ids: "Bit2publishTemplate"
    company_ids: "ResCompany"
    has_bit2publish_template: bool
    is_active: bool
    name: str
    provider: str
    service_name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IapAccount": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IapAccount": ...
    def create(self, vals: Dict[str, Any]) -> "IapAccount": ...
    def filtered(self, func: Any) -> "IapAccount": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IapAccount": ...
    def exists(self) -> "IapAccount": ...
    def sudo(self) -> "IapAccount": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IapAccount": ...

# --- iap.autocomplete.api ---

class IapAutocompleteApi(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IapAutocompleteApi": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IapAutocompleteApi": ...
    def create(self, vals: Dict[str, Any]) -> "IapAutocompleteApi": ...
    def filtered(self, func: Any) -> "IapAutocompleteApi": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IapAutocompleteApi": ...
    def exists(self) -> "IapAutocompleteApi": ...
    def sudo(self) -> "IapAutocompleteApi": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IapAutocompleteApi": ...

# --- iap.enrich.api ---

class IapEnrichApi(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IapEnrichApi": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IapEnrichApi": ...
    def create(self, vals: Dict[str, Any]) -> "IapEnrichApi": ...
    def filtered(self, func: Any) -> "IapEnrichApi": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IapEnrichApi": ...
    def exists(self) -> "IapEnrichApi": ...
    def sudo(self) -> "IapEnrichApi": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IapEnrichApi": ...

# --- image.mixin ---

class ImageMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    image_1024: bytes
    image_128: bytes
    image_1920: bytes
    image_256: bytes
    image_512: bytes
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImageMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImageMixin": ...
    def create(self, vals: Dict[str, Any]) -> "ImageMixin": ...
    def filtered(self, func: Any) -> "ImageMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImageMixin": ...
    def exists(self) -> "ImageMixin": ...
    def sudo(self) -> "ImageMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImageMixin": ...

# --- imperex.export ---

class ImperexExport(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImperexExport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImperexExport": ...
    def create(self, vals: Dict[str, Any]) -> "ImperexExport": ...
    def filtered(self, func: Any) -> "ImperexExport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImperexExport": ...
    def exists(self) -> "ImperexExport": ...
    def sudo(self) -> "ImperexExport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImperexExport": ...

# --- imperex.export.result.wizard ---

class ImperexExportResultWizard(Recordset):
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    log: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImperexExportResultWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImperexExportResultWizard": ...
    def create(self, vals: Dict[str, Any]) -> "ImperexExportResultWizard": ...
    def filtered(self, func: Any) -> "ImperexExportResultWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImperexExportResultWizard": ...
    def exists(self) -> "ImperexExportResultWizard": ...
    def sudo(self) -> "ImperexExportResultWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImperexExportResultWizard": ...

# --- imperex.export.wizard ---

class ImperexExportWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    export_to: str
    has_bit2publish_template: bool
    language_id: "ResLang"
    manifest_id: "ImperexManifestProfile"
    max_depth: int
    output_type: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImperexExportWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImperexExportWizard": ...
    def create(self, vals: Dict[str, Any]) -> "ImperexExportWizard": ...
    def filtered(self, func: Any) -> "ImperexExportWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImperexExportWizard": ...
    def exists(self) -> "ImperexExportWizard": ...
    def sudo(self) -> "ImperexExportWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImperexExportWizard": ...

# --- imperex.import ---

class ImperexImport(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImperexImport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImperexImport": ...
    def create(self, vals: Dict[str, Any]) -> "ImperexImport": ...
    def filtered(self, func: Any) -> "ImperexImport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImperexImport": ...
    def exists(self) -> "ImperexImport": ...
    def sudo(self) -> "ImperexImport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImperexImport": ...

# --- imperex.import.result.wizard ---

class ImperexImportResultWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    log: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImperexImportResultWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImperexImportResultWizard": ...
    def create(self, vals: Dict[str, Any]) -> "ImperexImportResultWizard": ...
    def filtered(self, func: Any) -> "ImperexImportResultWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImperexImportResultWizard": ...
    def exists(self) -> "ImperexImportResultWizard": ...
    def sudo(self) -> "ImperexImportResultWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImperexImportResultWizard": ...

# --- imperex.import.wizard ---

class ImperexImportWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    clean_before: bool
    file_ids: "ImperexImportWizardFile"
    force_language: bool
    force_update: bool
    has_bit2publish_template: bool
    language_id: "ResLang"
    manifest_id: "ImperexManifestProfile"
    package_file: bytes
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImperexImportWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImperexImportWizard": ...
    def create(self, vals: Dict[str, Any]) -> "ImperexImportWizard": ...
    def filtered(self, func: Any) -> "ImperexImportWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImperexImportWizard": ...
    def exists(self) -> "ImperexImportWizard": ...
    def sudo(self) -> "ImperexImportWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImperexImportWizard": ...

# --- imperex.import.wizard.file ---

class ImperexImportWizardFile(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    datas: bytes
    filename: str
    has_bit2publish_template: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    wizard_id: "ImperexImportWizard"
    def browse(self, ids: Union[int, List[int]]) -> "ImperexImportWizardFile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImperexImportWizardFile": ...
    def create(self, vals: Dict[str, Any]) -> "ImperexImportWizardFile": ...
    def filtered(self, func: Any) -> "ImperexImportWizardFile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImperexImportWizardFile": ...
    def exists(self) -> "ImperexImportWizardFile": ...
    def sudo(self) -> "ImperexImportWizardFile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImperexImportWizardFile": ...

# --- imperex.manifest.profile ---

class ImperexManifestProfile(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    full_yaml_manifest: str
    has_bit2publish_template: bool
    has_errors: str
    inherit_id: "ImperexManifestProfile"
    manifest: str
    name: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImperexManifestProfile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImperexManifestProfile": ...
    def create(self, vals: Dict[str, Any]) -> "ImperexManifestProfile": ...
    def filtered(self, func: Any) -> "ImperexManifestProfile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImperexManifestProfile": ...
    def exists(self) -> "ImperexManifestProfile": ...
    def sudo(self) -> "ImperexManifestProfile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImperexManifestProfile": ...

# --- imperex.xid.mixin ---

class ImperexXidMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    xid: str
    def browse(self, ids: Union[int, List[int]]) -> "ImperexXidMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImperexXidMixin": ...
    def create(self, vals: Dict[str, Any]) -> "ImperexXidMixin": ...
    def filtered(self, func: Any) -> "ImperexXidMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImperexXidMixin": ...
    def exists(self) -> "ImperexXidMixin": ...
    def sudo(self) -> "ImperexXidMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImperexXidMixin": ...

# --- import.distributor.transporter.data ---

class ImportDistributorTransporterData(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity_type: str
    file: bytes
    has_bit2publish_template: bool
    logistic_type: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImportDistributorTransporterData": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImportDistributorTransporterData": ...
    def create(self, vals: Dict[str, Any]) -> "ImportDistributorTransporterData": ...
    def filtered(self, func: Any) -> "ImportDistributorTransporterData": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImportDistributorTransporterData": ...
    def exists(self) -> "ImportDistributorTransporterData": ...
    def sudo(self) -> "ImportDistributorTransporterData": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImportDistributorTransporterData": ...

# --- import.file.tisg.wizard ---

class ImportFileTisgWizard(Recordset):
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImportFileTisgWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImportFileTisgWizard": ...
    def create(self, vals: Dict[str, Any]) -> "ImportFileTisgWizard": ...
    def filtered(self, func: Any) -> "ImportFileTisgWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImportFileTisgWizard": ...
    def exists(self) -> "ImportFileTisgWizard": ...
    def sudo(self) -> "ImportFileTisgWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImportFileTisgWizard": ...

# --- import.file.upsa.wizard ---

class ImportFileUpsaWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    file: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImportFileUpsaWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImportFileUpsaWizard": ...
    def create(self, vals: Dict[str, Any]) -> "ImportFileUpsaWizard": ...
    def filtered(self, func: Any) -> "ImportFileUpsaWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImportFileUpsaWizard": ...
    def exists(self) -> "ImportFileUpsaWizard": ...
    def sudo(self) -> "ImportFileUpsaWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImportFileUpsaWizard": ...

# --- import.helpdesk.ticket ---

class ImportHelpdeskTicket(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImportHelpdeskTicket": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImportHelpdeskTicket": ...
    def create(self, vals: Dict[str, Any]) -> "ImportHelpdeskTicket": ...
    def filtered(self, func: Any) -> "ImportHelpdeskTicket": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImportHelpdeskTicket": ...
    def exists(self) -> "ImportHelpdeskTicket": ...
    def sudo(self) -> "ImportHelpdeskTicket": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImportHelpdeskTicket": ...

# --- import.record.arera ---

class ImportRecordArera(Recordset):
    arera_id: str
    bit2publish_template_ids: "Bit2publishTemplate"
    city: str
    commodity_type: str
    company_name: str
    error_message: str
    full_address: str
    gas_type: str
    has_bit2publish_template: bool
    info_message: str
    legal_fax_number: str
    legal_phone_number: str
    logistic_type: str
    operational_fax_number: str
    operational_phone_number: str
    phone: str
    province: str
    region: str
    show_bit2publish_button: bool
    state: str
    status: str
    vat: str
    website: str
    def browse(self, ids: Union[int, List[int]]) -> "ImportRecordArera": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImportRecordArera": ...
    def create(self, vals: Dict[str, Any]) -> "ImportRecordArera": ...
    def filtered(self, func: Any) -> "ImportRecordArera": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImportRecordArera": ...
    def exists(self) -> "ImportRecordArera": ...
    def sudo(self) -> "ImportRecordArera": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImportRecordArera": ...

# --- import.sii.response ---

class ImportSiiResponse(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImportSiiResponse": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImportSiiResponse": ...
    def create(self, vals: Dict[str, Any]) -> "ImportSiiResponse": ...
    def filtered(self, func: Any) -> "ImportSiiResponse": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImportSiiResponse": ...
    def exists(self) -> "ImportSiiResponse": ...
    def sudo(self) -> "ImportSiiResponse": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImportSiiResponse": ...

# --- import.supervip.line ---

class ImportSupervipLine(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ImportSupervipLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ImportSupervipLine": ...
    def create(self, vals: Dict[str, Any]) -> "ImportSupervipLine": ...
    def filtered(self, func: Any) -> "ImportSupervipLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ImportSupervipLine": ...
    def exists(self) -> "ImportSupervipLine": ...
    def sudo(self) -> "ImportSupervipLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ImportSupervipLine": ...

# --- index.config ---

class IndexConfig(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    index_type: str
    show_bit2publish_button: bool
    ticket_type_ids: "HelpdeskTicketType"
    def browse(self, ids: Union[int, List[int]]) -> "IndexConfig": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IndexConfig": ...
    def create(self, vals: Dict[str, Any]) -> "IndexConfig": ...
    def filtered(self, func: Any) -> "IndexConfig": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IndexConfig": ...
    def exists(self) -> "IndexConfig": ...
    def sudo(self) -> "IndexConfig": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IndexConfig": ...

# --- index.history ---

class IndexHistory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    index_type: str
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "IndexHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IndexHistory": ...
    def create(self, vals: Dict[str, Any]) -> "IndexHistory": ...
    def filtered(self, func: Any) -> "IndexHistory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IndexHistory": ...
    def exists(self) -> "IndexHistory": ...
    def sudo(self) -> "IndexHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IndexHistory": ...

# --- infocamere.actions ---

class InfocamereActions(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    method: str
    name: str
    scope: str
    show_bit2publish_button: bool
    state: str
    subscope: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "InfocamereActions": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "InfocamereActions": ...
    def create(self, vals: Dict[str, Any]) -> "InfocamereActions": ...
    def filtered(self, func: Any) -> "InfocamereActions": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "InfocamereActions": ...
    def exists(self) -> "InfocamereActions": ...
    def sudo(self) -> "InfocamereActions": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "InfocamereActions": ...

# --- infocamere.env ---

class InfocamereEnv(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    password: str
    show_bit2publish_button: bool
    url: str
    username: str
    def browse(self, ids: Union[int, List[int]]) -> "InfocamereEnv": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "InfocamereEnv": ...
    def create(self, vals: Dict[str, Any]) -> "InfocamereEnv": ...
    def filtered(self, func: Any) -> "InfocamereEnv": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "InfocamereEnv": ...
    def exists(self) -> "InfocamereEnv": ...
    def sudo(self) -> "InfocamereEnv": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "InfocamereEnv": ...

# --- infocamere.map.output ---

class InfocamereMapOutput(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    field_id: "IrModelFields"
    has_bit2publish_template: bool
    is_match_condition: bool
    name: str
    send_to_m2c: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "InfocamereMapOutput": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "InfocamereMapOutput": ...
    def create(self, vals: Dict[str, Any]) -> "InfocamereMapOutput": ...
    def filtered(self, func: Any) -> "InfocamereMapOutput": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "InfocamereMapOutput": ...
    def exists(self) -> "InfocamereMapOutput": ...
    def sudo(self) -> "InfocamereMapOutput": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "InfocamereMapOutput": ...

# --- infocamere.rules ---

class InfocamereRules(Recordset):
    action_id: "InfocamereActions"
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    criteria: str
    has_bit2publish_template: bool
    has_message: bool
    log_count: int
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    name: str
    pec_match: str
    pec_update: bool
    service_id: "InfocamereEnv"
    show_bit2publish_button: bool
    subscription: str
    subscription_count: int
    url: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "InfocamereRules": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "InfocamereRules": ...
    def create(self, vals: Dict[str, Any]) -> "InfocamereRules": ...
    def filtered(self, func: Any) -> "InfocamereRules": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "InfocamereRules": ...
    def exists(self) -> "InfocamereRules": ...
    def sudo(self) -> "InfocamereRules": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "InfocamereRules": ...

# --- interaction.channel ---

class InteractionChannel(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    channel: str
    has_bit2publish_template: bool
    internal_name: str
    is_digital: bool
    is_visible: bool
    name: str
    show_bit2publish_button: bool
    ticket_type_ids: "SympleTripletType"
    def browse(self, ids: Union[int, List[int]]) -> "InteractionChannel": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "InteractionChannel": ...
    def create(self, vals: Dict[str, Any]) -> "InteractionChannel": ...
    def filtered(self, func: Any) -> "InteractionChannel": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "InteractionChannel": ...
    def exists(self) -> "InteractionChannel": ...
    def sudo(self) -> "InteractionChannel": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "InteractionChannel": ...

# --- invoices.wizard ---

class InvoicesWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "InvoicesWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "InvoicesWizard": ...
    def create(self, vals: Dict[str, Any]) -> "InvoicesWizard": ...
    def filtered(self, func: Any) -> "InvoicesWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "InvoicesWizard": ...
    def exists(self) -> "InvoicesWizard": ...
    def sudo(self) -> "InvoicesWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "InvoicesWizard": ...

# --- ir.actions.act_url ---

class IrActionsActUrl(Recordset):
    binding_model_id: "IrModel"
    binding_type: str
    binding_view_types: str
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    help: str
    name: str
    show_bit2publish_button: bool
    target: str
    type: str
    url: str
    xml_id: str
    def browse(self, ids: Union[int, List[int]]) -> "IrActionsActUrl": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrActionsActUrl": ...
    def create(self, vals: Dict[str, Any]) -> "IrActionsActUrl": ...
    def filtered(self, func: Any) -> "IrActionsActUrl": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrActionsActUrl": ...
    def exists(self) -> "IrActionsActUrl": ...
    def sudo(self) -> "IrActionsActUrl": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrActionsActUrl": ...

# --- ir.actions.act_window ---

class IrActionsActWindow(Recordset):
    binding_model_id: "IrModel"
    binding_type: str
    binding_view_types: str
    bit2publish_template_ids: "Bit2publishTemplate"
    context: str
    domain: str
    filter: bool
    groups_id: "ResGroups"
    has_bit2publish_template: bool
    help: str
    limit: int
    name: str
    res_id: int
    res_model: str
    search_view: str
    search_view_id: "IrUiView"
    show_bit2publish_button: bool
    target: str
    type: str
    usage: str
    view_id: "IrUiView"
    view_ids: "IrActionsActWindowView"
    view_mode: str
    views: bytes
    xml_id: str
    def browse(self, ids: Union[int, List[int]]) -> "IrActionsActWindow": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrActionsActWindow": ...
    def create(self, vals: Dict[str, Any]) -> "IrActionsActWindow": ...
    def filtered(self, func: Any) -> "IrActionsActWindow": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrActionsActWindow": ...
    def exists(self) -> "IrActionsActWindow": ...
    def sudo(self) -> "IrActionsActWindow": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrActionsActWindow": ...

# --- ir.actions.act_window.view ---

class IrActionsActWindowView(Recordset):
    act_window_id: "IrActionsActWindow"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    multi: bool
    sequence: int
    show_bit2publish_button: bool
    view_id: "IrUiView"
    view_mode: str
    def browse(self, ids: Union[int, List[int]]) -> "IrActionsActWindowView": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrActionsActWindowView": ...
    def create(self, vals: Dict[str, Any]) -> "IrActionsActWindowView": ...
    def filtered(self, func: Any) -> "IrActionsActWindowView": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrActionsActWindowView": ...
    def exists(self) -> "IrActionsActWindowView": ...
    def sudo(self) -> "IrActionsActWindowView": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrActionsActWindowView": ...

# --- ir.actions.act_window_close ---

class IrActionsActWindowClose(Recordset):
    binding_model_id: "IrModel"
    binding_type: str
    binding_view_types: str
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    help: str
    name: str
    show_bit2publish_button: bool
    type: str
    xml_id: str
    def browse(self, ids: Union[int, List[int]]) -> "IrActionsActWindowClose": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrActionsActWindowClose": ...
    def create(self, vals: Dict[str, Any]) -> "IrActionsActWindowClose": ...
    def filtered(self, func: Any) -> "IrActionsActWindowClose": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrActionsActWindowClose": ...
    def exists(self) -> "IrActionsActWindowClose": ...
    def sudo(self) -> "IrActionsActWindowClose": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrActionsActWindowClose": ...

# --- ir.actions.actions ---

class IrActionsActions(Recordset):
    binding_model_id: "IrModel"
    binding_type: str
    binding_view_types: str
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    help: str
    name: str
    show_bit2publish_button: bool
    type: str
    xml_id: str
    def browse(self, ids: Union[int, List[int]]) -> "IrActionsActions": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrActionsActions": ...
    def create(self, vals: Dict[str, Any]) -> "IrActionsActions": ...
    def filtered(self, func: Any) -> "IrActionsActions": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrActionsActions": ...
    def exists(self) -> "IrActionsActions": ...
    def sudo(self) -> "IrActionsActions": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrActionsActions": ...

# --- ir.actions.client ---

class IrActionsClient(Recordset):
    binding_model_id: "IrModel"
    binding_type: str
    binding_view_types: str
    bit2publish_template_ids: "Bit2publishTemplate"
    context: str
    has_bit2publish_template: bool
    help: str
    name: str
    params: bytes
    params_store: bytes
    res_model: str
    show_bit2publish_button: bool
    tag: str
    target: str
    type: str
    xml_id: str
    def browse(self, ids: Union[int, List[int]]) -> "IrActionsClient": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrActionsClient": ...
    def create(self, vals: Dict[str, Any]) -> "IrActionsClient": ...
    def filtered(self, func: Any) -> "IrActionsClient": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrActionsClient": ...
    def exists(self) -> "IrActionsClient": ...
    def sudo(self) -> "IrActionsClient": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrActionsClient": ...

# --- ir.actions.report ---

class IrActionsReport(Recordset):
    asynchronous: bool
    asynchronous_delete_days: int
    asynchronous_mail_template_id: "MailTemplate"
    attachment: str
    attachment_use: bool
    binding_model_id: "IrModel"
    binding_type: str
    binding_view_types: str
    bit2publish_template_ids: "Bit2publishTemplate"
    groups_id: "ResGroups"
    has_bit2publish_template: bool
    help: str
    model: str
    model_id: "IrModel"
    multi: bool
    name: str
    paperformat_id: "ReportPaperformat"
    print_report_name: str
    report_file: str
    report_name: str
    report_type: str
    show_bit2publish_button: bool
    type: str
    xml_declaration: bool
    xml_encoding: str
    xml_id: str
    xsd_schema: bytes
    def browse(self, ids: Union[int, List[int]]) -> "IrActionsReport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrActionsReport": ...
    def create(self, vals: Dict[str, Any]) -> "IrActionsReport": ...
    def filtered(self, func: Any) -> "IrActionsReport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrActionsReport": ...
    def exists(self) -> "IrActionsReport": ...
    def sudo(self) -> "IrActionsReport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrActionsReport": ...

# --- ir.actions.report.asynchronous.queue ---

class IrActionsReportAsynchronousQueue(Recordset):
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    delete_date: Optional[_dt.date]
    has_bit2publish_template: bool
    mail_id: "MailMail"
    record_ids: str
    report_id: "IrActionsReport"
    running: bool
    show_bit2publish_button: bool
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "IrActionsReportAsynchronousQueue": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrActionsReportAsynchronousQueue": ...
    def create(self, vals: Dict[str, Any]) -> "IrActionsReportAsynchronousQueue": ...
    def filtered(self, func: Any) -> "IrActionsReportAsynchronousQueue": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrActionsReportAsynchronousQueue": ...
    def exists(self) -> "IrActionsReportAsynchronousQueue": ...
    def sudo(self) -> "IrActionsReportAsynchronousQueue": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrActionsReportAsynchronousQueue": ...

# --- ir.actions.server ---

class IrActionsServer(Recordset):
    activity_date_deadline_range: int
    activity_date_deadline_range_type: str
    activity_note: str
    activity_summary: str
    activity_type_id: "MailActivityType"
    activity_user_field_name: str
    activity_user_id: "ResUsers"
    activity_user_type: str
    binding_model_id: "IrModel"
    binding_type: str
    binding_view_types: str
    bit2publish_template_ids: "Bit2publishTemplate"
    child_ids: "IrActionsServer"
    code: str
    crud_model_id: "IrModel"
    crud_model_name: str
    fields_lines: "IrServerObjectLines"
    groups_id: "ResGroups"
    has_bit2publish_template: bool
    help: str
    link_field_id: "IrModelFields"
    model_id: "IrModel"
    model_name: str
    name: str
    partner_ids: "ResPartner"
    sequence: int
    show_bit2publish_button: bool
    sms_mass_keep_log: bool
    sms_template_id: "SmsTemplate"
    state: str
    template_id: "MailTemplate"
    type: str
    usage: str
    xml_id: str
    def browse(self, ids: Union[int, List[int]]) -> "IrActionsServer": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrActionsServer": ...
    def create(self, vals: Dict[str, Any]) -> "IrActionsServer": ...
    def filtered(self, func: Any) -> "IrActionsServer": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrActionsServer": ...
    def exists(self) -> "IrActionsServer": ...
    def sudo(self) -> "IrActionsServer": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrActionsServer": ...

# --- ir.actions.todo ---

class IrActionsTodo(Recordset):
    action_id: "IrActionsActions"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "IrActionsTodo": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrActionsTodo": ...
    def create(self, vals: Dict[str, Any]) -> "IrActionsTodo": ...
    def filtered(self, func: Any) -> "IrActionsTodo": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrActionsTodo": ...
    def exists(self) -> "IrActionsTodo": ...
    def sudo(self) -> "IrActionsTodo": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrActionsTodo": ...

# --- ir.asset ---

class IrAsset(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    bundle: str
    directive: str
    has_bit2publish_template: bool
    name: str
    path: str
    sequence: int
    show_bit2publish_button: bool
    target: str
    def browse(self, ids: Union[int, List[int]]) -> "IrAsset": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrAsset": ...
    def create(self, vals: Dict[str, Any]) -> "IrAsset": ...
    def filtered(self, func: Any) -> "IrAsset": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrAsset": ...
    def exists(self) -> "IrAsset": ...
    def sudo(self) -> "IrAsset": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrAsset": ...

# --- ir.attachment ---

class IrAttachment(Recordset):
    access_token: str
    bit2publish_template_ids: "Bit2publishTemplate"
    checksum: str
    company_id: "ResCompany"
    datas: bytes
    db_datas: bytes
    description: str
    dms_link_ids: "IrAttachmentSympleDmsLink"
    file_size: int
    has_bit2publish_template: bool
    image_height: int
    image_src: str
    image_width: int
    index_content: str
    local_url: str
    mimetype: str
    name: str
    original_id: "IrAttachment"
    process_state: str
    public: bool
    raw: bytes
    rcu_processed: bool
    res_field: str
    res_id: Any
    res_model: str
    res_name: str
    show_bit2publish_button: bool
    store_fname: str
    type: str
    url: str
    zip_attachment_id: "IrAttachment"
    def browse(self, ids: Union[int, List[int]]) -> "IrAttachment": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrAttachment": ...
    def create(self, vals: Dict[str, Any]) -> "IrAttachment": ...
    def filtered(self, func: Any) -> "IrAttachment": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrAttachment": ...
    def exists(self) -> "IrAttachment": ...
    def sudo(self) -> "IrAttachment": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrAttachment": ...

# --- ir.attachment.symple.dms.link ---

class IrAttachmentSympleDmsLink(Recordset):
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    folder: str
    has_bit2publish_template: bool
    id_document: str
    remote_delete: bool
    server_id: "SympleDmsServer"
    show_bit2publish_button: bool
    tags: str
    def browse(self, ids: Union[int, List[int]]) -> "IrAttachmentSympleDmsLink": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrAttachmentSympleDmsLink": ...
    def create(self, vals: Dict[str, Any]) -> "IrAttachmentSympleDmsLink": ...
    def filtered(self, func: Any) -> "IrAttachmentSympleDmsLink": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrAttachmentSympleDmsLink": ...
    def exists(self) -> "IrAttachmentSympleDmsLink": ...
    def sudo(self) -> "IrAttachmentSympleDmsLink": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrAttachmentSympleDmsLink": ...

# --- ir.autovacuum ---

class IrAutovacuum(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrAutovacuum": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrAutovacuum": ...
    def create(self, vals: Dict[str, Any]) -> "IrAutovacuum": ...
    def filtered(self, func: Any) -> "IrAutovacuum": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrAutovacuum": ...
    def exists(self) -> "IrAutovacuum": ...
    def sudo(self) -> "IrAutovacuum": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrAutovacuum": ...

# --- ir.config_parameter ---

class IrConfigParameter(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    key: str
    show_bit2publish_button: bool
    value: str
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
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrConfigParameter": ...

# --- ir.cron ---

class IrCron(Recordset):
    active: bool
    activity_date_deadline_range: int
    activity_date_deadline_range_type: str
    activity_note: str
    activity_summary: str
    activity_type_id: "MailActivityType"
    activity_user_field_name: str
    activity_user_id: "ResUsers"
    activity_user_type: str
    binding_model_id: "IrModel"
    binding_type: str
    binding_view_types: str
    bit2publish_template_ids: "Bit2publishTemplate"
    child_ids: "IrActionsServer"
    code: str
    cron_name: str
    crud_model_id: "IrModel"
    crud_model_name: str
    doall: bool
    fields_lines: "IrServerObjectLines"
    groups_id: "ResGroups"
    has_bit2publish_template: bool
    help: str
    interval_number: int
    interval_type: str
    ir_actions_server_id: "IrActionsServer"
    lastcall: Optional[_dt.datetime]
    link_field_id: "IrModelFields"
    model_id: "IrModel"
    model_name: str
    name: str
    nextcall: Optional[_dt.datetime]
    numbercall: int
    partner_ids: "ResPartner"
    priority: int
    sequence: int
    show_bit2publish_button: bool
    sms_mass_keep_log: bool
    sms_template_id: "SmsTemplate"
    state: str
    template_id: "MailTemplate"
    type: str
    usage: str
    user_id: "ResUsers"
    xml_id: str
    def browse(self, ids: Union[int, List[int]]) -> "IrCron": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrCron": ...
    def create(self, vals: Dict[str, Any]) -> "IrCron": ...
    def filtered(self, func: Any) -> "IrCron": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrCron": ...
    def exists(self) -> "IrCron": ...
    def sudo(self) -> "IrCron": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrCron": ...

# --- ir.cron.trigger ---

class IrCronTrigger(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    call_at: Optional[_dt.datetime]
    cron_id: "IrCron"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrCronTrigger": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrCronTrigger": ...
    def create(self, vals: Dict[str, Any]) -> "IrCronTrigger": ...
    def filtered(self, func: Any) -> "IrCronTrigger": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrCronTrigger": ...
    def exists(self) -> "IrCronTrigger": ...
    def sudo(self) -> "IrCronTrigger": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrCronTrigger": ...

# --- ir.default ---

class IrDefault(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    condition: str
    field_id: "IrModelFields"
    has_bit2publish_template: bool
    json_value: str
    show_bit2publish_button: bool
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "IrDefault": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrDefault": ...
    def create(self, vals: Dict[str, Any]) -> "IrDefault": ...
    def filtered(self, func: Any) -> "IrDefault": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrDefault": ...
    def exists(self) -> "IrDefault": ...
    def sudo(self) -> "IrDefault": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrDefault": ...

# --- ir.demo ---

class IrDemo(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrDemo": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrDemo": ...
    def create(self, vals: Dict[str, Any]) -> "IrDemo": ...
    def filtered(self, func: Any) -> "IrDemo": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrDemo": ...
    def exists(self) -> "IrDemo": ...
    def sudo(self) -> "IrDemo": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrDemo": ...

# --- ir.demo_failure ---

class IrDemoFailure(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    error: str
    has_bit2publish_template: bool
    module_id: "IrModuleModule"
    show_bit2publish_button: bool
    wizard_id: "IrDemoFailureWizard"
    def browse(self, ids: Union[int, List[int]]) -> "IrDemoFailure": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrDemoFailure": ...
    def create(self, vals: Dict[str, Any]) -> "IrDemoFailure": ...
    def filtered(self, func: Any) -> "IrDemoFailure": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrDemoFailure": ...
    def exists(self) -> "IrDemoFailure": ...
    def sudo(self) -> "IrDemoFailure": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrDemoFailure": ...

# --- ir.demo_failure.wizard ---

class IrDemoFailureWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    failure_ids: "IrDemoFailure"
    failures_count: int
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrDemoFailureWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrDemoFailureWizard": ...
    def create(self, vals: Dict[str, Any]) -> "IrDemoFailureWizard": ...
    def filtered(self, func: Any) -> "IrDemoFailureWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrDemoFailureWizard": ...
    def exists(self) -> "IrDemoFailureWizard": ...
    def sudo(self) -> "IrDemoFailureWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrDemoFailureWizard": ...

# --- ir.exports ---

class IrExports(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    export_fields: "IrExportsLine"
    has_bit2publish_template: bool
    name: str
    resource: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrExports": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrExports": ...
    def create(self, vals: Dict[str, Any]) -> "IrExports": ...
    def filtered(self, func: Any) -> "IrExports": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrExports": ...
    def exists(self) -> "IrExports": ...
    def sudo(self) -> "IrExports": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrExports": ...

# --- ir.exports.line ---

class IrExportsLine(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    export_id: "IrExports"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrExportsLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrExportsLine": ...
    def create(self, vals: Dict[str, Any]) -> "IrExportsLine": ...
    def filtered(self, func: Any) -> "IrExportsLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrExportsLine": ...
    def exists(self) -> "IrExportsLine": ...
    def sudo(self) -> "IrExportsLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrExportsLine": ...

# --- ir.fields.converter ---

class IrFieldsConverter(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrFieldsConverter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrFieldsConverter": ...
    def create(self, vals: Dict[str, Any]) -> "IrFieldsConverter": ...
    def filtered(self, func: Any) -> "IrFieldsConverter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrFieldsConverter": ...
    def exists(self) -> "IrFieldsConverter": ...
    def sudo(self) -> "IrFieldsConverter": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrFieldsConverter": ...

# --- ir.filters ---

class IrFilters(Recordset):
    action_id: "IrActionsActions"
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    context: str
    domain: str
    has_bit2publish_template: bool
    is_default: bool
    model_id: str
    name: str
    show_bit2publish_button: bool
    sort: str
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "IrFilters": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrFilters": ...
    def create(self, vals: Dict[str, Any]) -> "IrFilters": ...
    def filtered(self, func: Any) -> "IrFilters": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrFilters": ...
    def exists(self) -> "IrFilters": ...
    def sudo(self) -> "IrFilters": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrFilters": ...

# --- ir.http ---

class IrHttp(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrHttp": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrHttp": ...
    def create(self, vals: Dict[str, Any]) -> "IrHttp": ...
    def filtered(self, func: Any) -> "IrHttp": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrHttp": ...
    def exists(self) -> "IrHttp": ...
    def sudo(self) -> "IrHttp": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrHttp": ...

# --- ir.logging ---

class IrLogging(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    dbname: str
    func: str
    has_bit2publish_template: bool
    level: str
    line: str
    message: str
    name: str
    path: str
    show_bit2publish_button: bool
    type: str
    def browse(self, ids: Union[int, List[int]]) -> "IrLogging": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrLogging": ...
    def create(self, vals: Dict[str, Any]) -> "IrLogging": ...
    def filtered(self, func: Any) -> "IrLogging": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrLogging": ...
    def exists(self) -> "IrLogging": ...
    def sudo(self) -> "IrLogging": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrLogging": ...

# --- ir.mail_server ---

class IrMailServer(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    from_filter: str
    google_gmail_access_token: str
    google_gmail_access_token_expiration: int
    google_gmail_authorization_code: str
    google_gmail_refresh_token: str
    google_gmail_uri: str
    has_bit2publish_template: bool
    is_microsoft_outlook_configured: bool
    is_pec_server: bool
    microsoft_outlook_access_token: str
    microsoft_outlook_access_token_expiration: int
    microsoft_outlook_refresh_token: str
    microsoft_outlook_uri: str
    name: str
    sequence: int
    show_bit2publish_button: bool
    smtp_authentication: str
    smtp_debug: bool
    smtp_encryption: str
    smtp_host: str
    smtp_pass: str
    smtp_port: int
    smtp_ssl_certificate: bytes
    smtp_ssl_private_key: bytes
    smtp_user: str
    use_google_gmail_service: bool
    use_microsoft_outlook_service: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrMailServer": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrMailServer": ...
    def create(self, vals: Dict[str, Any]) -> "IrMailServer": ...
    def filtered(self, func: Any) -> "IrMailServer": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrMailServer": ...
    def exists(self) -> "IrMailServer": ...
    def sudo(self) -> "IrMailServer": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrMailServer": ...

# --- ir.model ---

class IrModel(Recordset):
    abstract: bool
    access_ids: "IrModelAccess"
    bit2publish_template_ids: "Bit2publishTemplate"
    count: int
    field_id: "IrModelFields"
    has_bit2publish_template: bool
    info: str
    inherited_model_ids: "IrModel"
    is_mail_activity: bool
    is_mail_blacklist: bool
    is_mailing_enabled: bool
    is_mail_thread: bool
    is_mail_thread_sms: bool
    model: str
    modules: str
    name: str
    order: str
    rule_ids: "IrRule"
    show_bit2publish_button: bool
    state: str
    transient: bool
    view_ids: "IrUiView"
    def browse(self, ids: Union[int, List[int]]) -> "IrModel": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrModel": ...
    def create(self, vals: Dict[str, Any]) -> "IrModel": ...
    def filtered(self, func: Any) -> "IrModel": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrModel": ...
    def exists(self) -> "IrModel": ...
    def sudo(self) -> "IrModel": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrModel": ...

# --- ir.model.access ---

class IrModelAccess(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    group_id: "ResGroups"
    has_bit2publish_template: bool
    model_id: "IrModel"
    name: str
    perm_create: bool
    perm_read: bool
    perm_unlink: bool
    perm_write: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrModelAccess": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrModelAccess": ...
    def create(self, vals: Dict[str, Any]) -> "IrModelAccess": ...
    def filtered(self, func: Any) -> "IrModelAccess": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrModelAccess": ...
    def exists(self) -> "IrModelAccess": ...
    def sudo(self) -> "IrModelAccess": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrModelAccess": ...

# --- ir.model.constraint ---

class IrModelConstraint(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    definition: str
    has_bit2publish_template: bool
    message: str
    model: "IrModel"
    module: "IrModuleModule"
    name: str
    show_bit2publish_button: bool
    type: str
    def browse(self, ids: Union[int, List[int]]) -> "IrModelConstraint": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrModelConstraint": ...
    def create(self, vals: Dict[str, Any]) -> "IrModelConstraint": ...
    def filtered(self, func: Any) -> "IrModelConstraint": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrModelConstraint": ...
    def exists(self) -> "IrModelConstraint": ...
    def sudo(self) -> "IrModelConstraint": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrModelConstraint": ...

# --- ir.model.data ---

class IrModelData(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    complete_name: str
    has_bit2publish_template: bool
    model: str
    module: str
    name: str
    noupdate: bool
    reference: str
    res_id: Any
    show_bit2publish_button: bool
    studio: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrModelData": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrModelData": ...
    def create(self, vals: Dict[str, Any]) -> "IrModelData": ...
    def filtered(self, func: Any) -> "IrModelData": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrModelData": ...
    def exists(self) -> "IrModelData": ...
    def sudo(self) -> "IrModelData": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrModelData": ...

# --- ir.model.fields ---

class IrModelFields(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    column1: str
    column2: str
    complete_name: str
    compute: str
    copied: bool
    depends: str
    domain: str
    field_description: str
    group_expand: bool
    groups: "ResGroups"
    has_bit2publish_template: bool
    help: str
    index: bool
    model: str
    model_id: "IrModel"
    modules: str
    name: str
    on_delete: str
    readonly: bool
    related: str
    related_field_id: "IrModelFields"
    relation: str
    relation_field: str
    relation_field_id: "IrModelFields"
    relation_table: str
    required: bool
    selectable: bool
    selection: str
    selection_ids: "IrModelFieldsSelection"
    show_bit2publish_button: bool
    size: int
    state: str
    store: bool
    tracking: int
    translate: bool
    ttype: str
    def browse(self, ids: Union[int, List[int]]) -> "IrModelFields": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrModelFields": ...
    def create(self, vals: Dict[str, Any]) -> "IrModelFields": ...
    def filtered(self, func: Any) -> "IrModelFields": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrModelFields": ...
    def exists(self) -> "IrModelFields": ...
    def sudo(self) -> "IrModelFields": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrModelFields": ...

# --- ir.model.fields.selection ---

class IrModelFieldsSelection(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    field_id: "IrModelFields"
    has_bit2publish_template: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "IrModelFieldsSelection": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrModelFieldsSelection": ...
    def create(self, vals: Dict[str, Any]) -> "IrModelFieldsSelection": ...
    def filtered(self, func: Any) -> "IrModelFieldsSelection": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrModelFieldsSelection": ...
    def exists(self) -> "IrModelFieldsSelection": ...
    def sudo(self) -> "IrModelFieldsSelection": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrModelFieldsSelection": ...

# --- ir.model.relation ---

class IrModelRelation(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    model: "IrModel"
    module: "IrModuleModule"
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrModelRelation": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrModelRelation": ...
    def create(self, vals: Dict[str, Any]) -> "IrModelRelation": ...
    def filtered(self, func: Any) -> "IrModelRelation": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrModelRelation": ...
    def exists(self) -> "IrModelRelation": ...
    def sudo(self) -> "IrModelRelation": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrModelRelation": ...

# --- ir.module.category ---

class IrModuleCategory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    child_ids: "IrModuleCategory"
    description: str
    exclusive: bool
    has_bit2publish_template: bool
    module_ids: "IrModuleModule"
    module_nr: int
    name: str
    parent_id: "IrModuleCategory"
    sequence: int
    show_bit2publish_button: bool
    visible: bool
    xml_id: str
    def browse(self, ids: Union[int, List[int]]) -> "IrModuleCategory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrModuleCategory": ...
    def create(self, vals: Dict[str, Any]) -> "IrModuleCategory": ...
    def filtered(self, func: Any) -> "IrModuleCategory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrModuleCategory": ...
    def exists(self) -> "IrModuleCategory": ...
    def sudo(self) -> "IrModuleCategory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrModuleCategory": ...

# --- ir.module.module ---

class IrModuleModule(Recordset):
    application: bool
    author: str
    auto_install: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    category_id: "IrModuleCategory"
    contributors: str
    demo: bool
    dependencies_id: "IrModuleModuleDependency"
    description: str
    description_html: str
    exclusion_ids: "IrModuleModuleExclusion"
    has_bit2publish_template: bool
    has_iap: bool
    icon: str
    icon_image: bytes
    imported: bool
    installed_version: str
    latest_version: str
    license: str
    maintainer: str
    menus_by_module: str
    name: str
    published_version: str
    reports_by_module: str
    sequence: int
    shortdesc: str
    show_bit2publish_button: bool
    state: str
    summary: str
    to_buy: bool
    url: str
    views_by_module: str
    website: str
    def browse(self, ids: Union[int, List[int]]) -> "IrModuleModule": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrModuleModule": ...
    def create(self, vals: Dict[str, Any]) -> "IrModuleModule": ...
    def filtered(self, func: Any) -> "IrModuleModule": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrModuleModule": ...
    def exists(self) -> "IrModuleModule": ...
    def sudo(self) -> "IrModuleModule": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrModuleModule": ...

# --- ir.module.module.dependency ---

class IrModuleModuleDependency(Recordset):
    auto_install_required: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    depend_id: "IrModuleModule"
    has_bit2publish_template: bool
    module_id: "IrModuleModule"
    name: str
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "IrModuleModuleDependency": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrModuleModuleDependency": ...
    def create(self, vals: Dict[str, Any]) -> "IrModuleModuleDependency": ...
    def filtered(self, func: Any) -> "IrModuleModuleDependency": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrModuleModuleDependency": ...
    def exists(self) -> "IrModuleModuleDependency": ...
    def sudo(self) -> "IrModuleModuleDependency": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrModuleModuleDependency": ...

# --- ir.module.module.exclusion ---

class IrModuleModuleExclusion(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    exclusion_id: "IrModuleModule"
    has_bit2publish_template: bool
    module_id: "IrModuleModule"
    name: str
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "IrModuleModuleExclusion": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrModuleModuleExclusion": ...
    def create(self, vals: Dict[str, Any]) -> "IrModuleModuleExclusion": ...
    def filtered(self, func: Any) -> "IrModuleModuleExclusion": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrModuleModuleExclusion": ...
    def exists(self) -> "IrModuleModuleExclusion": ...
    def sudo(self) -> "IrModuleModuleExclusion": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrModuleModuleExclusion": ...

# --- ir.profile ---

class IrProfile(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    duration: float
    entry_count: int
    has_bit2publish_template: bool
    init_stack_trace: str
    name: str
    qweb: str
    session: str
    show_bit2publish_button: bool
    speedscope: bytes
    speedscope_url: str
    sql: str
    traces_async: str
    traces_sync: str
    def browse(self, ids: Union[int, List[int]]) -> "IrProfile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrProfile": ...
    def create(self, vals: Dict[str, Any]) -> "IrProfile": ...
    def filtered(self, func: Any) -> "IrProfile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrProfile": ...
    def exists(self) -> "IrProfile": ...
    def sudo(self) -> "IrProfile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrProfile": ...

# --- ir.property ---

class IrProperty(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    fields_id: "IrModelFields"
    has_bit2publish_template: bool
    name: str
    res_id: str
    show_bit2publish_button: bool
    type: str
    value_binary: bytes
    value_datetime: Optional[_dt.datetime]
    value_float: float
    value_integer: int
    value_reference: str
    value_text: str
    def browse(self, ids: Union[int, List[int]]) -> "IrProperty": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrProperty": ...
    def create(self, vals: Dict[str, Any]) -> "IrProperty": ...
    def filtered(self, func: Any) -> "IrProperty": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrProperty": ...
    def exists(self) -> "IrProperty": ...
    def sudo(self) -> "IrProperty": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrProperty": ...

# --- ir.qweb ---

class IrQweb(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQweb": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQweb": ...
    def create(self, vals: Dict[str, Any]) -> "IrQweb": ...
    def filtered(self, func: Any) -> "IrQweb": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQweb": ...
    def exists(self) -> "IrQweb": ...
    def sudo(self) -> "IrQweb": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQweb": ...

# --- ir.qweb.field ---

class IrQwebField(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebField": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebField": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebField": ...
    def filtered(self, func: Any) -> "IrQwebField": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebField": ...
    def exists(self) -> "IrQwebField": ...
    def sudo(self) -> "IrQwebField": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebField": ...

# --- ir.qweb.field.barcode ---

class IrQwebFieldBarcode(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldBarcode": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldBarcode": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldBarcode": ...
    def filtered(self, func: Any) -> "IrQwebFieldBarcode": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldBarcode": ...
    def exists(self) -> "IrQwebFieldBarcode": ...
    def sudo(self) -> "IrQwebFieldBarcode": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldBarcode": ...

# --- ir.qweb.field.contact ---

class IrQwebFieldContact(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldContact": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldContact": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldContact": ...
    def filtered(self, func: Any) -> "IrQwebFieldContact": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldContact": ...
    def exists(self) -> "IrQwebFieldContact": ...
    def sudo(self) -> "IrQwebFieldContact": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldContact": ...

# --- ir.qweb.field.date ---

class IrQwebFieldDate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldDate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldDate": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldDate": ...
    def filtered(self, func: Any) -> "IrQwebFieldDate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldDate": ...
    def exists(self) -> "IrQwebFieldDate": ...
    def sudo(self) -> "IrQwebFieldDate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldDate": ...

# --- ir.qweb.field.datetime ---

class IrQwebFieldDatetime(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldDatetime": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldDatetime": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldDatetime": ...
    def filtered(self, func: Any) -> "IrQwebFieldDatetime": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldDatetime": ...
    def exists(self) -> "IrQwebFieldDatetime": ...
    def sudo(self) -> "IrQwebFieldDatetime": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldDatetime": ...

# --- ir.qweb.field.duration ---

class IrQwebFieldDuration(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldDuration": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldDuration": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldDuration": ...
    def filtered(self, func: Any) -> "IrQwebFieldDuration": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldDuration": ...
    def exists(self) -> "IrQwebFieldDuration": ...
    def sudo(self) -> "IrQwebFieldDuration": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldDuration": ...

# --- ir.qweb.field.float ---

class IrQwebFieldFloat(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldFloat": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldFloat": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldFloat": ...
    def filtered(self, func: Any) -> "IrQwebFieldFloat": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldFloat": ...
    def exists(self) -> "IrQwebFieldFloat": ...
    def sudo(self) -> "IrQwebFieldFloat": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldFloat": ...

# --- ir.qweb.field.float_time ---

class IrQwebFieldFloatTime(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldFloatTime": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldFloatTime": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldFloatTime": ...
    def filtered(self, func: Any) -> "IrQwebFieldFloatTime": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldFloatTime": ...
    def exists(self) -> "IrQwebFieldFloatTime": ...
    def sudo(self) -> "IrQwebFieldFloatTime": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldFloatTime": ...

# --- ir.qweb.field.html ---

class IrQwebFieldHtml(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldHtml": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldHtml": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldHtml": ...
    def filtered(self, func: Any) -> "IrQwebFieldHtml": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldHtml": ...
    def exists(self) -> "IrQwebFieldHtml": ...
    def sudo(self) -> "IrQwebFieldHtml": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldHtml": ...

# --- ir.qweb.field.image ---

class IrQwebFieldImage(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldImage": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldImage": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldImage": ...
    def filtered(self, func: Any) -> "IrQwebFieldImage": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldImage": ...
    def exists(self) -> "IrQwebFieldImage": ...
    def sudo(self) -> "IrQwebFieldImage": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldImage": ...

# --- ir.qweb.field.image_url ---

class IrQwebFieldImageUrl(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldImageUrl": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldImageUrl": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldImageUrl": ...
    def filtered(self, func: Any) -> "IrQwebFieldImageUrl": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldImageUrl": ...
    def exists(self) -> "IrQwebFieldImageUrl": ...
    def sudo(self) -> "IrQwebFieldImageUrl": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldImageUrl": ...

# --- ir.qweb.field.integer ---

class IrQwebFieldInteger(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldInteger": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldInteger": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldInteger": ...
    def filtered(self, func: Any) -> "IrQwebFieldInteger": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldInteger": ...
    def exists(self) -> "IrQwebFieldInteger": ...
    def sudo(self) -> "IrQwebFieldInteger": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldInteger": ...

# --- ir.qweb.field.many2many ---

class IrQwebFieldMany2many(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldMany2many": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldMany2many": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldMany2many": ...
    def filtered(self, func: Any) -> "IrQwebFieldMany2many": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldMany2many": ...
    def exists(self) -> "IrQwebFieldMany2many": ...
    def sudo(self) -> "IrQwebFieldMany2many": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldMany2many": ...

# --- ir.qweb.field.many2one ---

class IrQwebFieldMany2one(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldMany2one": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldMany2one": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldMany2one": ...
    def filtered(self, func: Any) -> "IrQwebFieldMany2one": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldMany2one": ...
    def exists(self) -> "IrQwebFieldMany2one": ...
    def sudo(self) -> "IrQwebFieldMany2one": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldMany2one": ...

# --- ir.qweb.field.monetary ---

class IrQwebFieldMonetary(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldMonetary": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldMonetary": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldMonetary": ...
    def filtered(self, func: Any) -> "IrQwebFieldMonetary": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldMonetary": ...
    def exists(self) -> "IrQwebFieldMonetary": ...
    def sudo(self) -> "IrQwebFieldMonetary": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldMonetary": ...

# --- ir.qweb.field.qweb ---

class IrQwebFieldQweb(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldQweb": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldQweb": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldQweb": ...
    def filtered(self, func: Any) -> "IrQwebFieldQweb": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldQweb": ...
    def exists(self) -> "IrQwebFieldQweb": ...
    def sudo(self) -> "IrQwebFieldQweb": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldQweb": ...

# --- ir.qweb.field.relative ---

class IrQwebFieldRelative(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldRelative": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldRelative": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldRelative": ...
    def filtered(self, func: Any) -> "IrQwebFieldRelative": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldRelative": ...
    def exists(self) -> "IrQwebFieldRelative": ...
    def sudo(self) -> "IrQwebFieldRelative": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldRelative": ...

# --- ir.qweb.field.selection ---

class IrQwebFieldSelection(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldSelection": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldSelection": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldSelection": ...
    def filtered(self, func: Any) -> "IrQwebFieldSelection": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldSelection": ...
    def exists(self) -> "IrQwebFieldSelection": ...
    def sudo(self) -> "IrQwebFieldSelection": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldSelection": ...

# --- ir.qweb.field.text ---

class IrQwebFieldText(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrQwebFieldText": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrQwebFieldText": ...
    def create(self, vals: Dict[str, Any]) -> "IrQwebFieldText": ...
    def filtered(self, func: Any) -> "IrQwebFieldText": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrQwebFieldText": ...
    def exists(self) -> "IrQwebFieldText": ...
    def sudo(self) -> "IrQwebFieldText": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrQwebFieldText": ...

# --- ir.rule ---

class IrRule(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    domain_force: str
    global_: bool
    groups: "ResGroups"
    has_bit2publish_template: bool
    model_id: "IrModel"
    name: str
    perm_create: bool
    perm_read: bool
    perm_unlink: bool
    perm_write: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrRule": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrRule": ...
    def create(self, vals: Dict[str, Any]) -> "IrRule": ...
    def filtered(self, func: Any) -> "IrRule": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrRule": ...
    def exists(self) -> "IrRule": ...
    def sudo(self) -> "IrRule": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrRule": ...

# --- ir.sequence ---

class IrSequence(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    company_id: "ResCompany"
    date_range_ids: "IrSequenceDateRange"
    has_bit2publish_template: bool
    implementation: str
    name: str
    number_increment: int
    number_next: int
    number_next_actual: int
    padding: int
    prefix: str
    show_bit2publish_button: bool
    suffix: str
    use_date_range: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrSequence": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrSequence": ...
    def create(self, vals: Dict[str, Any]) -> "IrSequence": ...
    def filtered(self, func: Any) -> "IrSequence": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrSequence": ...
    def exists(self) -> "IrSequence": ...
    def sudo(self) -> "IrSequence": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrSequence": ...

# --- ir.sequence.date_range ---

class IrSequenceDateRange(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    date_from: Optional[_dt.date]
    date_to: Optional[_dt.date]
    has_bit2publish_template: bool
    number_next: int
    number_next_actual: int
    sequence_id: "IrSequence"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IrSequenceDateRange": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrSequenceDateRange": ...
    def create(self, vals: Dict[str, Any]) -> "IrSequenceDateRange": ...
    def filtered(self, func: Any) -> "IrSequenceDateRange": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrSequenceDateRange": ...
    def exists(self) -> "IrSequenceDateRange": ...
    def sudo(self) -> "IrSequenceDateRange": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrSequenceDateRange": ...

# --- ir.server.object.lines ---

class IrServerObjectLines(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    col1: "IrModelFields"
    evaluation_type: str
    has_bit2publish_template: bool
    resource_ref: Any
    server_id: "IrActionsServer"
    show_bit2publish_button: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "IrServerObjectLines": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrServerObjectLines": ...
    def create(self, vals: Dict[str, Any]) -> "IrServerObjectLines": ...
    def filtered(self, func: Any) -> "IrServerObjectLines": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrServerObjectLines": ...
    def exists(self) -> "IrServerObjectLines": ...
    def sudo(self) -> "IrServerObjectLines": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrServerObjectLines": ...

# --- ir.translation ---

class IrTranslation(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    comments: str
    has_bit2publish_template: bool
    lang: str
    module: str
    name: str
    res_id: int
    show_bit2publish_button: bool
    src: str
    state: str
    type: str
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "IrTranslation": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrTranslation": ...
    def create(self, vals: Dict[str, Any]) -> "IrTranslation": ...
    def filtered(self, func: Any) -> "IrTranslation": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrTranslation": ...
    def exists(self) -> "IrTranslation": ...
    def sudo(self) -> "IrTranslation": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrTranslation": ...

# --- ir.ui.menu ---

class IrUiMenu(Recordset):
    action: Any
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    child_id: "IrUiMenu"
    complete_name: str
    groups_id: "ResGroups"
    has_bit2publish_template: bool
    is_studio_configuration: bool
    name: str
    parent_id: "IrUiMenu"
    parent_path: str
    sequence: int
    show_bit2publish_button: bool
    web_icon: str
    web_icon_data: bytes
    def browse(self, ids: Union[int, List[int]]) -> "IrUiMenu": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrUiMenu": ...
    def create(self, vals: Dict[str, Any]) -> "IrUiMenu": ...
    def filtered(self, func: Any) -> "IrUiMenu": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrUiMenu": ...
    def exists(self) -> "IrUiMenu": ...
    def sudo(self) -> "IrUiMenu": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrUiMenu": ...

# --- ir.ui.view ---

class IrUiView(Recordset):
    active: bool
    arch: str
    arch_base: str
    arch_db: str
    arch_fs: str
    arch_prev: str
    arch_updated: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    customize_show: bool
    field_parent: str
    groups_id: "ResGroups"
    has_bit2publish_template: bool
    inherit_children_ids: "IrUiView"
    inherit_id: "IrUiView"
    key: str
    mode: str
    model: str
    model_data_id: "IrModelData"
    name: str
    priority: int
    show_bit2publish_button: bool
    type: str
    xml_id: str
    def browse(self, ids: Union[int, List[int]]) -> "IrUiView": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrUiView": ...
    def create(self, vals: Dict[str, Any]) -> "IrUiView": ...
    def filtered(self, func: Any) -> "IrUiView": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrUiView": ...
    def exists(self) -> "IrUiView": ...
    def sudo(self) -> "IrUiView": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrUiView": ...

# --- ir.ui.view.custom ---

class IrUiViewCustom(Recordset):
    arch: str
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    ref_id: "IrUiView"
    show_bit2publish_button: bool
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "IrUiViewCustom": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IrUiViewCustom": ...
    def create(self, vals: Dict[str, Any]) -> "IrUiViewCustom": ...
    def filtered(self, func: Any) -> "IrUiViewCustom": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IrUiViewCustom": ...
    def exists(self) -> "IrUiViewCustom": ...
    def sudo(self) -> "IrUiViewCustom": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IrUiViewCustom": ...

# --- iva.type.history ---

class IvaTypeHistory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    client_id: "ResPartner"
    has_bit2publish_template: bool
    new_value: str
    original_value: str
    origin_id: "HelpdeskTicket"
    process_type: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "IvaTypeHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "IvaTypeHistory": ...
    def create(self, vals: Dict[str, Any]) -> "IvaTypeHistory": ...
    def filtered(self, func: Any) -> "IvaTypeHistory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "IvaTypeHistory": ...
    def exists(self) -> "IvaTypeHistory": ...
    def sudo(self) -> "IvaTypeHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "IvaTypeHistory": ...

# --- job.titles ---

class JobTitles(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    has_bit2publish_template: bool
    is_from_migration: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "JobTitles": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "JobTitles": ...
    def create(self, vals: Dict[str, Any]) -> "JobTitles": ...
    def filtered(self, func: Any) -> "JobTitles": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "JobTitles": ...
    def exists(self) -> "JobTitles": ...
    def sudo(self) -> "JobTitles": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "JobTitles": ...

# --- jolly.index.import.wizard ---

class JollyIndexImportWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "JollyIndexImportWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "JollyIndexImportWizard": ...
    def create(self, vals: Dict[str, Any]) -> "JollyIndexImportWizard": ...
    def filtered(self, func: Any) -> "JollyIndexImportWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "JollyIndexImportWizard": ...
    def exists(self) -> "JollyIndexImportWizard": ...
    def sudo(self) -> "JollyIndexImportWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "JollyIndexImportWizard": ...

# --- jolly.index.line ---

class JollyIndexLine(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    error_message: str
    has_bit2publish_template: bool
    jolly_index: str
    record_code: str
    show_bit2publish_button: bool
    status: str
    user_sequence: str
    def browse(self, ids: Union[int, List[int]]) -> "JollyIndexLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "JollyIndexLine": ...
    def create(self, vals: Dict[str, Any]) -> "JollyIndexLine": ...
    def filtered(self, func: Any) -> "JollyIndexLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "JollyIndexLine": ...
    def exists(self) -> "JollyIndexLine": ...
    def sudo(self) -> "JollyIndexLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "JollyIndexLine": ...

# --- jolly.index.revision.wizard ---

class JollyIndexRevisionWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "JollyIndexRevisionWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "JollyIndexRevisionWizard": ...
    def create(self, vals: Dict[str, Any]) -> "JollyIndexRevisionWizard": ...
    def filtered(self, func: Any) -> "JollyIndexRevisionWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "JollyIndexRevisionWizard": ...
    def exists(self) -> "JollyIndexRevisionWizard": ...
    def sudo(self) -> "JollyIndexRevisionWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "JollyIndexRevisionWizard": ...

# --- letter.of.intent ---

class LetterOfIntent(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    client_id: "ResPartner"
    has_bit2publish_template: bool
    letter_of_intent_date: Optional[_dt.date]
    name: str
    plafond_amount: float
    residual_plafond: float
    show_bit2publish_button: bool
    telematic_receipt_date: Optional[_dt.date]
    user_sequence: str
    validity_end_date: Optional[_dt.date]
    validity_start_date: Optional[_dt.date]
    vat: str
    def browse(self, ids: Union[int, List[int]]) -> "LetterOfIntent": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "LetterOfIntent": ...
    def create(self, vals: Dict[str, Any]) -> "LetterOfIntent": ...
    def filtered(self, func: Any) -> "LetterOfIntent": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "LetterOfIntent": ...
    def exists(self) -> "LetterOfIntent": ...
    def sudo(self) -> "LetterOfIntent": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "LetterOfIntent": ...

# --- link.tracker ---

class LinkTracker(Recordset):
    absolute_url: str
    bit2publish_template_ids: "Bit2publishTemplate"
    campaign_id: "UtmCampaign"
    code: str
    count: int
    has_bit2publish_template: bool
    label: str
    link_click_ids: "LinkTrackerClick"
    link_code_ids: "LinkTrackerCode"
    mass_mailing_id: "MailingMailing"
    medium_id: "UtmMedium"
    redirected_url: str
    short_url: str
    short_url_host: str
    show_bit2publish_button: bool
    source_id: "UtmSource"
    title: str
    url: str
    def browse(self, ids: Union[int, List[int]]) -> "LinkTracker": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "LinkTracker": ...
    def create(self, vals: Dict[str, Any]) -> "LinkTracker": ...
    def filtered(self, func: Any) -> "LinkTracker": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "LinkTracker": ...
    def exists(self) -> "LinkTracker": ...
    def sudo(self) -> "LinkTracker": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "LinkTracker": ...

# --- link.tracker.click ---

class LinkTrackerClick(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    campaign_id: "UtmCampaign"
    country_id: "ResCountry"
    has_bit2publish_template: bool
    ip: str
    link_id: "LinkTracker"
    mailing_trace_id: "MailingTrace"
    mass_mailing_id: "MailingMailing"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "LinkTrackerClick": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "LinkTrackerClick": ...
    def create(self, vals: Dict[str, Any]) -> "LinkTrackerClick": ...
    def filtered(self, func: Any) -> "LinkTrackerClick": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "LinkTrackerClick": ...
    def exists(self) -> "LinkTrackerClick": ...
    def sudo(self) -> "LinkTrackerClick": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "LinkTrackerClick": ...

# --- link.tracker.code ---

class LinkTrackerCode(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    has_bit2publish_template: bool
    link_id: "LinkTracker"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "LinkTrackerCode": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "LinkTrackerCode": ...
    def create(self, vals: Dict[str, Any]) -> "LinkTrackerCode": ...
    def filtered(self, func: Any) -> "LinkTrackerCode": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "LinkTrackerCode": ...
    def exists(self) -> "LinkTrackerCode": ...
    def sudo(self) -> "LinkTrackerCode": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "LinkTrackerCode": ...

# --- mail.activity ---

class MailActivity(Recordset):
    activity_category: str
    activity_decoration: str
    activity_type_id: "MailActivityType"
    automated: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    calendar_event_id: "CalendarEvent"
    can_write: bool
    chaining_type: str
    date_deadline: Optional[_dt.date]
    has_bit2publish_template: bool
    has_recommended_activities: bool
    icon: str
    mail_template_ids: "MailTemplate"
    note: str
    previous_activity_type_id: "MailActivityType"
    recommended_activity_type_id: "MailActivityType"
    request_partner_id: "ResPartner"
    res_id: Any
    res_model: str
    res_model_id: "IrModel"
    res_name: str
    show_bit2publish_button: bool
    state: str
    summary: str
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "MailActivity": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailActivity": ...
    def create(self, vals: Dict[str, Any]) -> "MailActivity": ...
    def filtered(self, func: Any) -> "MailActivity": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailActivity": ...
    def exists(self) -> "MailActivity": ...
    def sudo(self) -> "MailActivity": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailActivity": ...

# --- mail.activity.mixin ---

class MailActivityMixin(Recordset):
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    my_activity_date_deadline: Optional[_dt.date]
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailActivityMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailActivityMixin": ...
    def create(self, vals: Dict[str, Any]) -> "MailActivityMixin": ...
    def filtered(self, func: Any) -> "MailActivityMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailActivityMixin": ...
    def exists(self) -> "MailActivityMixin": ...
    def sudo(self) -> "MailActivityMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailActivityMixin": ...

# --- mail.activity.type ---

class MailActivityType(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    category: str
    chaining_type: str
    decoration_type: str
    default_note: str
    default_user_id: "ResUsers"
    delay_count: int
    delay_from: str
    delay_label: str
    delay_unit: str
    folder_id: "DocumentsFolder"
    has_bit2publish_template: bool
    icon: str
    initial_res_model: str
    mail_template_ids: "MailTemplate"
    name: str
    previous_type_ids: "MailActivityType"
    res_model: str
    res_model_change: bool
    sequence: int
    show_bit2publish_button: bool
    suggested_next_type_ids: "MailActivityType"
    summary: str
    tag_ids: "DocumentsTag"
    triggered_next_type_id: "MailActivityType"
    def browse(self, ids: Union[int, List[int]]) -> "MailActivityType": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailActivityType": ...
    def create(self, vals: Dict[str, Any]) -> "MailActivityType": ...
    def filtered(self, func: Any) -> "MailActivityType": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailActivityType": ...
    def exists(self) -> "MailActivityType": ...
    def sudo(self) -> "MailActivityType": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailActivityType": ...

# --- mail.alias ---

class MailAlias(Recordset):
    alias_bounced_content: str
    alias_contact: str
    alias_defaults: str
    alias_domain: str
    alias_force_thread_id: int
    alias_model_id: "IrModel"
    alias_name: str
    alias_parent_model_id: "IrModel"
    alias_parent_thread_id: int
    alias_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailAlias": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailAlias": ...
    def create(self, vals: Dict[str, Any]) -> "MailAlias": ...
    def filtered(self, func: Any) -> "MailAlias": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailAlias": ...
    def exists(self) -> "MailAlias": ...
    def sudo(self) -> "MailAlias": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailAlias": ...

# --- mail.alias.mixin ---

class MailAliasMixin(Recordset):
    alias_id: "MailAlias"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailAliasMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailAliasMixin": ...
    def create(self, vals: Dict[str, Any]) -> "MailAliasMixin": ...
    def filtered(self, func: Any) -> "MailAliasMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailAliasMixin": ...
    def exists(self) -> "MailAliasMixin": ...
    def sudo(self) -> "MailAliasMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailAliasMixin": ...

# --- mail.blacklist ---

class MailBlacklist(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    email: str
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    show_bit2publish_button: bool
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "MailBlacklist": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailBlacklist": ...
    def create(self, vals: Dict[str, Any]) -> "MailBlacklist": ...
    def filtered(self, func: Any) -> "MailBlacklist": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailBlacklist": ...
    def exists(self) -> "MailBlacklist": ...
    def sudo(self) -> "MailBlacklist": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailBlacklist": ...

# --- mail.blacklist.remove ---

class MailBlacklistRemove(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    email: str
    has_bit2publish_template: bool
    reason: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailBlacklistRemove": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailBlacklistRemove": ...
    def create(self, vals: Dict[str, Any]) -> "MailBlacklistRemove": ...
    def filtered(self, func: Any) -> "MailBlacklistRemove": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailBlacklistRemove": ...
    def exists(self) -> "MailBlacklistRemove": ...
    def sudo(self) -> "MailBlacklistRemove": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailBlacklistRemove": ...

# --- mail.bot ---

class MailBot(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailBot": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailBot": ...
    def create(self, vals: Dict[str, Any]) -> "MailBot": ...
    def filtered(self, func: Any) -> "MailBot": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailBot": ...
    def exists(self) -> "MailBot": ...
    def sudo(self) -> "MailBot": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailBot": ...

# --- mail.channel ---

class MailChannel(Recordset):
    active: bool
    alias_bounced_content: str
    alias_contact: str
    alias_defaults: str
    alias_domain: str
    alias_force_thread_id: int
    alias_id: "MailAlias"
    alias_model_id: "IrModel"
    alias_name: str
    alias_parent_model_id: "IrModel"
    alias_parent_thread_id: int
    alias_user_id: "ResUsers"
    avatar_128: bytes
    bit2publish_template_ids: "Bit2publishTemplate"
    channel_last_seen_partner_ids: "MailChannelPartner"
    channel_partner_ids: "ResPartner"
    channel_type: str
    default_display_mode: str
    description: str
    group_ids: "ResGroups"
    group_public_id: "ResGroups"
    has_bit2publish_template: bool
    has_message: bool
    image_128: bytes
    is_chat: bool
    is_member: bool
    member_count: int
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    name: str
    public: str
    rtc_session_ids: "MailChannelRtcSession"
    show_bit2publish_button: bool
    uuid: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "MailChannel": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailChannel": ...
    def create(self, vals: Dict[str, Any]) -> "MailChannel": ...
    def filtered(self, func: Any) -> "MailChannel": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailChannel": ...
    def exists(self) -> "MailChannel": ...
    def sudo(self) -> "MailChannel": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailChannel": ...

# --- mail.channel.partner ---

class MailChannelPartner(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    channel_id: "MailChannel"
    custom_channel_name: str
    fetched_message_id: "MailMessage"
    fold_state: str
    guest_id: "MailGuest"
    has_bit2publish_template: bool
    is_minimized: bool
    is_pinned: bool
    last_interest_dt: Optional[_dt.datetime]
    partner_email: str
    partner_id: "ResPartner"
    rtc_inviting_session_id: "MailChannelRtcSession"
    rtc_session_ids: "MailChannelRtcSession"
    seen_message_id: "MailMessage"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailChannelPartner": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailChannelPartner": ...
    def create(self, vals: Dict[str, Any]) -> "MailChannelPartner": ...
    def filtered(self, func: Any) -> "MailChannelPartner": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailChannelPartner": ...
    def exists(self) -> "MailChannelPartner": ...
    def sudo(self) -> "MailChannelPartner": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailChannelPartner": ...

# --- mail.channel.rtc.session ---

class MailChannelRtcSession(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    channel_id: "MailChannel"
    channel_partner_id: "MailChannelPartner"
    guest_id: "MailGuest"
    has_bit2publish_template: bool
    is_camera_on: bool
    is_deaf: bool
    is_muted: bool
    is_screen_sharing_on: bool
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailChannelRtcSession": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailChannelRtcSession": ...
    def create(self, vals: Dict[str, Any]) -> "MailChannelRtcSession": ...
    def filtered(self, func: Any) -> "MailChannelRtcSession": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailChannelRtcSession": ...
    def exists(self) -> "MailChannelRtcSession": ...
    def sudo(self) -> "MailChannelRtcSession": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailChannelRtcSession": ...

# --- mail.compose.message ---

class MailComposeMessage(Recordset):
    active_domain: str
    add_sign: bool
    attachment_ids: "IrAttachment"
    author_id: "ResPartner"
    auto_delete: bool
    auto_delete_message: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    campaign_id: "UtmCampaign"
    can_edit_body: bool
    composition_mode: str
    copyvalue: str
    email_bcc: str
    email_cc: str
    email_from: str
    has_bit2publish_template: bool
    is_log: bool
    is_mail_template_editor: bool
    is_pec: bool
    lang: str
    layout: str
    mail_activity_type_id: "MailActivityType"
    mailing_list_ids: "MailingList"
    mail_server_id: "IrMailServer"
    marketing_activity_id: "MarketingActivity"
    mass_mailing_id: "MailingMailing"
    mass_mailing_name: str
    message_type: str
    model: str
    model_object_field: "IrModelFields"
    notify: bool
    null_value: str
    parent_id: "MailMessage"
    partner_ids: "ResPartner"
    record_name: str
    render_model: str
    reply_to: str
    reply_to_force_new: bool
    reply_to_mode: str
    res_id: int
    send_immediately: bool
    show_bit2publish_button: bool
    subject: str
    sub_model_object_field: "IrModelFields"
    sub_object: "IrModel"
    subtype_id: "MailMessageSubtype"
    template_domain: "MailTemplate"
    template_id: "MailTemplate"
    use_active_domain: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailComposeMessage": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailComposeMessage": ...
    def create(self, vals: Dict[str, Any]) -> "MailComposeMessage": ...
    def filtered(self, func: Any) -> "MailComposeMessage": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailComposeMessage": ...
    def exists(self) -> "MailComposeMessage": ...
    def sudo(self) -> "MailComposeMessage": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailComposeMessage": ...

# --- mail.composer.mixin ---

class MailComposerMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    can_edit_body: bool
    copyvalue: str
    has_bit2publish_template: bool
    is_mail_template_editor: bool
    lang: str
    model_object_field: "IrModelFields"
    null_value: str
    render_model: str
    show_bit2publish_button: bool
    subject: str
    sub_model_object_field: "IrModelFields"
    sub_object: "IrModel"
    template_id: "MailTemplate"
    def browse(self, ids: Union[int, List[int]]) -> "MailComposerMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailComposerMixin": ...
    def create(self, vals: Dict[str, Any]) -> "MailComposerMixin": ...
    def filtered(self, func: Any) -> "MailComposerMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailComposerMixin": ...
    def exists(self) -> "MailComposerMixin": ...
    def sudo(self) -> "MailComposerMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailComposerMixin": ...

# --- mail.followers ---

class MailFollowers(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    email: str
    has_bit2publish_template: bool
    is_active: bool
    name: str
    partner_id: "ResPartner"
    res_id: Any
    res_model: str
    show_bit2publish_button: bool
    subtype_ids: "MailMessageSubtype"
    def browse(self, ids: Union[int, List[int]]) -> "MailFollowers": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailFollowers": ...
    def create(self, vals: Dict[str, Any]) -> "MailFollowers": ...
    def filtered(self, func: Any) -> "MailFollowers": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailFollowers": ...
    def exists(self) -> "MailFollowers": ...
    def sudo(self) -> "MailFollowers": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailFollowers": ...

# --- mail.guest ---

class MailGuest(Recordset):
    access_token: str
    avatar_1024: bytes
    avatar_128: bytes
    avatar_1920: bytes
    avatar_256: bytes
    avatar_512: bytes
    bit2publish_template_ids: "Bit2publishTemplate"
    channel_ids: "MailChannel"
    country_id: "ResCountry"
    has_bit2publish_template: bool
    image_1024: bytes
    image_128: bytes
    image_1920: bytes
    image_256: bytes
    image_512: bytes
    lang: str
    name: str
    show_bit2publish_button: bool
    timezone: str
    def browse(self, ids: Union[int, List[int]]) -> "MailGuest": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailGuest": ...
    def create(self, vals: Dict[str, Any]) -> "MailGuest": ...
    def filtered(self, func: Any) -> "MailGuest": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailGuest": ...
    def exists(self) -> "MailGuest": ...
    def sudo(self) -> "MailGuest": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailGuest": ...

# --- mail.ice.server ---

class MailIceServer(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    credential: str
    has_bit2publish_template: bool
    server_type: str
    show_bit2publish_button: bool
    uri: str
    username: str
    def browse(self, ids: Union[int, List[int]]) -> "MailIceServer": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailIceServer": ...
    def create(self, vals: Dict[str, Any]) -> "MailIceServer": ...
    def filtered(self, func: Any) -> "MailIceServer": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailIceServer": ...
    def exists(self) -> "MailIceServer": ...
    def sudo(self) -> "MailIceServer": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailIceServer": ...

# --- mail.mail ---

class MailMail(Recordset):
    add_sign: bool
    attachment_ids: "IrAttachment"
    author_avatar: bytes
    author_guest_id: "MailGuest"
    author_id: "ResPartner"
    auto_delete: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    body_html: str
    canned_response_ids: "MailShortcode"
    child_ids: "MailMessage"
    date: Optional[_dt.datetime]
    description: str
    email_cc: str
    email_from: str
    email_layout_xmlid: str
    email_to: str
    failure_reason: str
    failure_type: str
    fetchmail_server_id: "FetchmailServer"
    has_bit2publish_template: bool
    has_error: bool
    has_sms_error: bool
    headers: str
    interaction_id: "SympleInteraction"
    is_current_user_or_guest_author: bool
    is_internal: bool
    is_notification: bool
    letter_ids: "SnailmailLetter"
    mail_activity_type_id: "MailActivityType"
    mail_ids: "MailMail"
    mailing_id: "MailingMailing"
    mailing_trace_ids: "MailingTrace"
    mail_message_id: "MailMessage"
    mail_server_id: "IrMailServer"
    message_id: str
    message_type: str
    migrate_in_symple_mail_error: str
    migrate_in_symple_mail_mail_id: "SympleMail"
    migrate_in_symple_mail_state: str
    model: str
    needaction: bool
    notification_ids: "MailNotification"
    notified_partner_ids: "ResPartner"
    parent_id: "MailMessage"
    partner_ids: "ResPartner"
    rating_ids: "RatingRating"
    rating_value: float
    reaction_ids: "MailMessageReaction"
    recipient_ids: "ResPartner"
    record_name: str
    references: str
    reply_to: str
    reply_to_force_new: bool
    res_id: Any
    scheduled_date: str
    show_bit2publish_button: bool
    snailmail_error: bool
    starred: bool
    starred_partner_ids: "ResPartner"
    state: str
    subject: str
    subtype_id: "MailMessageSubtype"
    symple_mail_id: "SympleMail"
    tracking_value_ids: "MailTrackingValue"
    def browse(self, ids: Union[int, List[int]]) -> "MailMail": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailMail": ...
    def create(self, vals: Dict[str, Any]) -> "MailMail": ...
    def filtered(self, func: Any) -> "MailMail": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailMail": ...
    def exists(self) -> "MailMail": ...
    def sudo(self) -> "MailMail": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailMail": ...

# --- mail.message ---

class MailMessage(Recordset):
    add_sign: bool
    attachment_ids: "IrAttachment"
    author_avatar: bytes
    author_guest_id: "MailGuest"
    author_id: "ResPartner"
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    canned_response_ids: "MailShortcode"
    child_ids: "MailMessage"
    date: Optional[_dt.datetime]
    description: str
    email_from: str
    email_layout_xmlid: str
    has_bit2publish_template: bool
    has_error: bool
    has_sms_error: bool
    interaction_id: "SympleInteraction"
    is_current_user_or_guest_author: bool
    is_internal: bool
    letter_ids: "SnailmailLetter"
    mail_activity_type_id: "MailActivityType"
    mail_ids: "MailMail"
    mail_server_id: "IrMailServer"
    message_id: str
    message_type: str
    model: str
    needaction: bool
    notification_ids: "MailNotification"
    notified_partner_ids: "ResPartner"
    parent_id: "MailMessage"
    partner_ids: "ResPartner"
    rating_ids: "RatingRating"
    rating_value: float
    reaction_ids: "MailMessageReaction"
    record_name: str
    reply_to: str
    reply_to_force_new: bool
    res_id: Any
    show_bit2publish_button: bool
    snailmail_error: bool
    starred: bool
    starred_partner_ids: "ResPartner"
    subject: str
    subtype_id: "MailMessageSubtype"
    tracking_value_ids: "MailTrackingValue"
    def browse(self, ids: Union[int, List[int]]) -> "MailMessage": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailMessage": ...
    def create(self, vals: Dict[str, Any]) -> "MailMessage": ...
    def filtered(self, func: Any) -> "MailMessage": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailMessage": ...
    def exists(self) -> "MailMessage": ...
    def sudo(self) -> "MailMessage": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailMessage": ...

# --- mail.message.reaction ---

class MailMessageReaction(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    content: str
    guest_id: "MailGuest"
    has_bit2publish_template: bool
    message_id: "MailMessage"
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailMessageReaction": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailMessageReaction": ...
    def create(self, vals: Dict[str, Any]) -> "MailMessageReaction": ...
    def filtered(self, func: Any) -> "MailMessageReaction": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailMessageReaction": ...
    def exists(self) -> "MailMessageReaction": ...
    def sudo(self) -> "MailMessageReaction": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailMessageReaction": ...

# --- mail.message.subtype ---

class MailMessageSubtype(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    default: bool
    description: str
    has_bit2publish_template: bool
    hidden: bool
    internal: bool
    name: str
    parent_id: "MailMessageSubtype"
    relation_field: str
    res_model: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailMessageSubtype": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailMessageSubtype": ...
    def create(self, vals: Dict[str, Any]) -> "MailMessageSubtype": ...
    def filtered(self, func: Any) -> "MailMessageSubtype": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailMessageSubtype": ...
    def exists(self) -> "MailMessageSubtype": ...
    def sudo(self) -> "MailMessageSubtype": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailMessageSubtype": ...

# --- mail.notification ---

class MailNotification(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    failure_reason: str
    failure_type: str
    has_bit2publish_template: bool
    is_read: bool
    letter_id: "SnailmailLetter"
    mail_mail_id: "MailMail"
    mail_message_id: "MailMessage"
    notification_status: str
    notification_type: str
    read_date: Optional[_dt.datetime]
    res_partner_id: "ResPartner"
    show_bit2publish_button: bool
    sms_id: "SmsSms"
    sms_number: str
    def browse(self, ids: Union[int, List[int]]) -> "MailNotification": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailNotification": ...
    def create(self, vals: Dict[str, Any]) -> "MailNotification": ...
    def filtered(self, func: Any) -> "MailNotification": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailNotification": ...
    def exists(self) -> "MailNotification": ...
    def sudo(self) -> "MailNotification": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailNotification": ...

# --- mail.render.mixin ---

class MailRenderMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    copyvalue: str
    has_bit2publish_template: bool
    lang: str
    model_object_field: "IrModelFields"
    null_value: str
    render_model: str
    show_bit2publish_button: bool
    sub_model_object_field: "IrModelFields"
    sub_object: "IrModel"
    def browse(self, ids: Union[int, List[int]]) -> "MailRenderMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailRenderMixin": ...
    def create(self, vals: Dict[str, Any]) -> "MailRenderMixin": ...
    def filtered(self, func: Any) -> "MailRenderMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailRenderMixin": ...
    def exists(self) -> "MailRenderMixin": ...
    def sudo(self) -> "MailRenderMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailRenderMixin": ...

# --- mail.resend.cancel ---

class MailResendCancel(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    help_message: str
    model: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailResendCancel": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailResendCancel": ...
    def create(self, vals: Dict[str, Any]) -> "MailResendCancel": ...
    def filtered(self, func: Any) -> "MailResendCancel": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailResendCancel": ...
    def exists(self) -> "MailResendCancel": ...
    def sudo(self) -> "MailResendCancel": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailResendCancel": ...

# --- mail.resend.message ---

class MailResendMessage(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    has_cancel: bool
    mail_message_id: "MailMessage"
    notification_ids: "MailNotification"
    partner_ids: "MailResendPartner"
    partner_readonly: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailResendMessage": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailResendMessage": ...
    def create(self, vals: Dict[str, Any]) -> "MailResendMessage": ...
    def filtered(self, func: Any) -> "MailResendMessage": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailResendMessage": ...
    def exists(self) -> "MailResendMessage": ...
    def sudo(self) -> "MailResendMessage": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailResendMessage": ...

# --- mail.resend.partner ---

class MailResendPartner(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    email: str
    has_bit2publish_template: bool
    message: str
    name: str
    partner_id: "ResPartner"
    resend: bool
    resend_wizard_id: "MailResendMessage"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailResendPartner": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailResendPartner": ...
    def create(self, vals: Dict[str, Any]) -> "MailResendPartner": ...
    def filtered(self, func: Any) -> "MailResendPartner": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailResendPartner": ...
    def exists(self) -> "MailResendPartner": ...
    def sudo(self) -> "MailResendPartner": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailResendPartner": ...

# --- mail.shortcode ---

class MailShortcode(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    has_bit2publish_template: bool
    message_ids: "MailMessage"
    show_bit2publish_button: bool
    source: str
    substitution: str
    def browse(self, ids: Union[int, List[int]]) -> "MailShortcode": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailShortcode": ...
    def create(self, vals: Dict[str, Any]) -> "MailShortcode": ...
    def filtered(self, func: Any) -> "MailShortcode": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailShortcode": ...
    def exists(self) -> "MailShortcode": ...
    def sudo(self) -> "MailShortcode": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailShortcode": ...

# --- mail.template ---

class MailTemplate(Recordset):
    attachment_config_ids: "MailTemplateAttachment"
    attachment_ids: "IrAttachment"
    auto_delete: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    body_html: str
    can_write: bool
    copyvalue: str
    dynamic_attachment: str
    email_bcc: str
    email_cc: str
    email_from: str
    email_to: str
    has_bit2publish_template: bool
    is_dynamic_attachment: bool
    lang: str
    mail_server_id: "IrMailServer"
    model: str
    model_id: "IrModel"
    model_object_field: "IrModelFields"
    name: str
    null_value: str
    partner_to: str
    ref_ir_act_window: "IrActionsActWindow"
    render_model: str
    reply_to: str
    report_name: str
    report_template: "IrActionsReport"
    scheduled_date: str
    send_immediately: bool
    show_bit2publish_button: bool
    subject: str
    sub_model_object_field: "IrModelFields"
    sub_object: "IrModel"
    template_code: str
    use_default_to: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "MailTemplate": ...
    def filtered(self, func: Any) -> "MailTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailTemplate": ...
    def exists(self) -> "MailTemplate": ...
    def sudo(self) -> "MailTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailTemplate": ...

# --- mail.template.attachment ---

class MailTemplateAttachment(Recordset):
    binary_field_id: "IrModelFields"
    bit2publish_template_ids: "Bit2publishTemplate"
    filename_field_id: "IrModelFields"
    file_type: str
    forced_filename: str
    has_bit2publish_template: bool
    model_id: "IrModel"
    show_bit2publish_button: bool
    template_id: "MailTemplate"
    use_forced_filename: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailTemplateAttachment": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailTemplateAttachment": ...
    def create(self, vals: Dict[str, Any]) -> "MailTemplateAttachment": ...
    def filtered(self, func: Any) -> "MailTemplateAttachment": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailTemplateAttachment": ...
    def exists(self) -> "MailTemplateAttachment": ...
    def sudo(self) -> "MailTemplateAttachment": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailTemplateAttachment": ...

# --- mail.template.attachment.wizard ---

class MailTemplateAttachmentWizard(Recordset):
    binary_field_id: "IrModelFields"
    bit2publish_template_ids: "Bit2publishTemplate"
    filename_field_id: "IrModelFields"
    file_type: str
    forced_filename: str
    has_bit2publish_template: bool
    model_id: "IrModel"
    show_bit2publish_button: bool
    template_id: "MailTemplate"
    use_forced_filename: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailTemplateAttachmentWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailTemplateAttachmentWizard": ...
    def create(self, vals: Dict[str, Any]) -> "MailTemplateAttachmentWizard": ...
    def filtered(self, func: Any) -> "MailTemplateAttachmentWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailTemplateAttachmentWizard": ...
    def exists(self) -> "MailTemplateAttachmentWizard": ...
    def sudo(self) -> "MailTemplateAttachmentWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailTemplateAttachmentWizard": ...

# --- mail.template.preview ---

class MailTemplatePreview(Recordset):
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    body_html: str
    email_bcc: str
    email_cc: str
    email_from: str
    email_to: str
    error_msg: str
    has_bit2publish_template: bool
    lang: str
    mail_template_id: "MailTemplate"
    model_id: "IrModel"
    no_record: bool
    partner_ids: "ResPartner"
    reply_to: str
    resource_ref: Any
    scheduled_date: str
    show_bit2publish_button: bool
    subject: str
    def browse(self, ids: Union[int, List[int]]) -> "MailTemplatePreview": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailTemplatePreview": ...
    def create(self, vals: Dict[str, Any]) -> "MailTemplatePreview": ...
    def filtered(self, func: Any) -> "MailTemplatePreview": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailTemplatePreview": ...
    def exists(self) -> "MailTemplatePreview": ...
    def sudo(self) -> "MailTemplatePreview": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailTemplatePreview": ...

# --- mail.thread ---

class MailThread(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    show_bit2publish_button: bool
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "MailThread": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailThread": ...
    def create(self, vals: Dict[str, Any]) -> "MailThread": ...
    def filtered(self, func: Any) -> "MailThread": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailThread": ...
    def exists(self) -> "MailThread": ...
    def sudo(self) -> "MailThread": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailThread": ...

# --- mail.thread.blacklist ---

class MailThreadBlacklist(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    email_normalized: str
    has_bit2publish_template: bool
    has_message: bool
    is_blacklisted: bool
    message_attachment_count: int
    message_bounce: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    show_bit2publish_button: bool
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "MailThreadBlacklist": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailThreadBlacklist": ...
    def create(self, vals: Dict[str, Any]) -> "MailThreadBlacklist": ...
    def filtered(self, func: Any) -> "MailThreadBlacklist": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailThreadBlacklist": ...
    def exists(self) -> "MailThreadBlacklist": ...
    def sudo(self) -> "MailThreadBlacklist": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailThreadBlacklist": ...

# --- mail.thread.cc ---

class MailThreadCc(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    email_cc: str
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    show_bit2publish_button: bool
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "MailThreadCc": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailThreadCc": ...
    def create(self, vals: Dict[str, Any]) -> "MailThreadCc": ...
    def filtered(self, func: Any) -> "MailThreadCc": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailThreadCc": ...
    def exists(self) -> "MailThreadCc": ...
    def sudo(self) -> "MailThreadCc": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailThreadCc": ...

# --- mail.thread.phone ---

class MailThreadPhone(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    mobile_blacklisted: bool
    phone_blacklisted: bool
    phone_mobile_search: str
    phone_sanitized: str
    phone_sanitized_blacklisted: bool
    show_bit2publish_button: bool
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "MailThreadPhone": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailThreadPhone": ...
    def create(self, vals: Dict[str, Any]) -> "MailThreadPhone": ...
    def filtered(self, func: Any) -> "MailThreadPhone": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailThreadPhone": ...
    def exists(self) -> "MailThreadPhone": ...
    def sudo(self) -> "MailThreadPhone": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailThreadPhone": ...

# --- mail.tracking.value ---

class MailTrackingValue(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    currency_id: "ResCurrency"
    field: "IrModelFields"
    field_desc: str
    field_groups: str
    field_type: str
    has_bit2publish_template: bool
    mail_message_id: "MailMessage"
    new_value_boolean: bool
    new_value_char: str
    new_value_datetime: Optional[_dt.datetime]
    new_value_float: float
    new_value_integer: int
    new_value_monetary: float
    new_value_text: str
    old_value_boolean: bool
    old_value_char: str
    old_value_datetime: Optional[_dt.datetime]
    old_value_float: float
    old_value_integer: int
    old_value_monetary: float
    old_value_text: str
    show_bit2publish_button: bool
    tracking_sequence: int
    def browse(self, ids: Union[int, List[int]]) -> "MailTrackingValue": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailTrackingValue": ...
    def create(self, vals: Dict[str, Any]) -> "MailTrackingValue": ...
    def filtered(self, func: Any) -> "MailTrackingValue": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailTrackingValue": ...
    def exists(self) -> "MailTrackingValue": ...
    def sudo(self) -> "MailTrackingValue": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailTrackingValue": ...

# --- mail.wizard.invite ---

class MailWizardInvite(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    message: str
    partner_ids: "ResPartner"
    res_id: int
    res_model: str
    send_mail: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailWizardInvite": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailWizardInvite": ...
    def create(self, vals: Dict[str, Any]) -> "MailWizardInvite": ...
    def filtered(self, func: Any) -> "MailWizardInvite": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailWizardInvite": ...
    def exists(self) -> "MailWizardInvite": ...
    def sudo(self) -> "MailWizardInvite": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailWizardInvite": ...

# --- mailing.contact ---

class MailingContact(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_name: str
    country_id: "ResCountry"
    email: str
    email_normalized: str
    has_bit2publish_template: bool
    has_message: bool
    is_blacklisted: bool
    list_ids: "MailingList"
    message_attachment_count: int
    message_bounce: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    mobile: str
    mobile_blacklisted: bool
    name: str
    opt_out: bool
    phone_blacklisted: bool
    phone_mobile_search: str
    phone_sanitized: str
    phone_sanitized_blacklisted: bool
    show_bit2publish_button: bool
    subscription_list_ids: "MailingContactSubscription"
    tag_ids: "ResPartnerCategory"
    title_id: "ResPartnerTitle"
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "MailingContact": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailingContact": ...
    def create(self, vals: Dict[str, Any]) -> "MailingContact": ...
    def filtered(self, func: Any) -> "MailingContact": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailingContact": ...
    def exists(self) -> "MailingContact": ...
    def sudo(self) -> "MailingContact": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailingContact": ...

# --- mailing.contact.subscription ---

class MailingContactSubscription(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    contact_id: "MailingContact"
    has_bit2publish_template: bool
    is_blacklisted: bool
    list_id: "MailingList"
    message_bounce: int
    opt_out: bool
    show_bit2publish_button: bool
    unsubscription_date: Optional[_dt.datetime]
    def browse(self, ids: Union[int, List[int]]) -> "MailingContactSubscription": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailingContactSubscription": ...
    def create(self, vals: Dict[str, Any]) -> "MailingContactSubscription": ...
    def filtered(self, func: Any) -> "MailingContactSubscription": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailingContactSubscription": ...
    def exists(self) -> "MailingContactSubscription": ...
    def sudo(self) -> "MailingContactSubscription": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailingContactSubscription": ...

# --- mailing.contact.to.list ---

class MailingContactToList(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    contact_ids: "MailingContact"
    has_bit2publish_template: bool
    mailing_list_id: "MailingList"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailingContactToList": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailingContactToList": ...
    def create(self, vals: Dict[str, Any]) -> "MailingContactToList": ...
    def filtered(self, func: Any) -> "MailingContactToList": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailingContactToList": ...
    def exists(self) -> "MailingContactToList": ...
    def sudo(self) -> "MailingContactToList": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailingContactToList": ...

# --- mailing.list ---

class MailingList(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    contact_count: int
    contact_count_blacklisted: int
    contact_count_email: int
    contact_count_opt_out: int
    contact_count_sms: int
    contact_ids: "MailingContact"
    contact_pct_blacklisted: float
    contact_pct_bounce: float
    contact_pct_opt_out: float
    has_bit2publish_template: bool
    is_public: bool
    mailing_count: int
    mailing_ids: "MailingMailing"
    name: str
    show_bit2publish_button: bool
    subscription_ids: "MailingContactSubscription"
    def browse(self, ids: Union[int, List[int]]) -> "MailingList": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailingList": ...
    def create(self, vals: Dict[str, Any]) -> "MailingList": ...
    def filtered(self, func: Any) -> "MailingList": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailingList": ...
    def exists(self) -> "MailingList": ...
    def sudo(self) -> "MailingList": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailingList": ...

# --- mailing.list.merge ---

class MailingListMerge(Recordset):
    archive_src_lists: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    dest_list_id: "MailingList"
    has_bit2publish_template: bool
    merge_options: str
    new_list_name: str
    show_bit2publish_button: bool
    src_list_ids: "MailingList"
    def browse(self, ids: Union[int, List[int]]) -> "MailingListMerge": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailingListMerge": ...
    def create(self, vals: Dict[str, Any]) -> "MailingListMerge": ...
    def filtered(self, func: Any) -> "MailingListMerge": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailingListMerge": ...
    def exists(self) -> "MailingListMerge": ...
    def sudo(self) -> "MailingListMerge": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailingListMerge": ...

# --- mailing.mailing ---

class MailingMailing(Recordset):
    ab_testing_completed: bool
    ab_testing_description: str
    ab_testing_enabled: bool
    ab_testing_mailings_count: int
    ab_testing_pc: int
    ab_testing_schedule_datetime: Optional[_dt.datetime]
    ab_testing_sms_winner_selection: str
    ab_testing_winner_selection: str
    active: bool
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    body_arch: str
    body_html: str
    body_plaintext: str
    bounced: int
    bounced_ratio: int
    calendar_date: Optional[_dt.datetime]
    campaign_id: "UtmCampaign"
    canceled: int
    clicked: int
    clicks_ratio: int
    color: int
    contact_list_ids: "MailingList"
    copyvalue: str
    delivered: int
    email_from: str
    expected: int
    failed: int
    has_bit2publish_template: bool
    has_message: bool
    is_body_empty: bool
    keep_archives: bool
    kpi_mail_required: bool
    lang: str
    mailing_domain: str
    mailing_model_id: "IrModel"
    mailing_model_name: str
    mailing_model_real: str
    mailing_trace_ids: "MailingTrace"
    mailing_type: str
    mailing_type_description: str
    mail_server_available: bool
    mail_server_id: "IrMailServer"
    marketing_activity_ids: "MarketingActivity"
    medium_id: "UtmMedium"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    model_object_field: "IrModelFields"
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    next_departure: Optional[_dt.datetime]
    null_value: str
    opened: int
    opened_ratio: int
    preview: str
    received_ratio: int
    render_model: str
    replied: int
    replied_ratio: int
    reply_to: str
    reply_to_mode: str
    scheduled: int
    schedule_date: Optional[_dt.datetime]
    schedule_type: str
    sent: int
    sent_date: Optional[_dt.datetime]
    show_bit2publish_button: bool
    sms_allow_unsubscribe: bool
    sms_force_send: bool
    sms_has_insufficient_credit: bool
    sms_has_unregistered_account: bool
    sms_subject: str
    sms_template_id: "SmsTemplate"
    source_id: "UtmSource"
    state: str
    subject: str
    sub_model_object_field: "IrModelFields"
    sub_object: "IrModel"
    total: int
    use_in_marketing_automation: bool
    user_id: "ResUsers"
    warning_message: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "MailingMailing": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailingMailing": ...
    def create(self, vals: Dict[str, Any]) -> "MailingMailing": ...
    def filtered(self, func: Any) -> "MailingMailing": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailingMailing": ...
    def exists(self) -> "MailingMailing": ...
    def sudo(self) -> "MailingMailing": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailingMailing": ...

# --- mailing.mailing.schedule.date ---

class MailingMailingScheduleDate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    mass_mailing_id: "MailingMailing"
    schedule_date: Optional[_dt.datetime]
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailingMailingScheduleDate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailingMailingScheduleDate": ...
    def create(self, vals: Dict[str, Any]) -> "MailingMailingScheduleDate": ...
    def filtered(self, func: Any) -> "MailingMailingScheduleDate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailingMailingScheduleDate": ...
    def exists(self) -> "MailingMailingScheduleDate": ...
    def sudo(self) -> "MailingMailingScheduleDate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailingMailingScheduleDate": ...

# --- mailing.mailing.test ---

class MailingMailingTest(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    email_to: str
    has_bit2publish_template: bool
    mass_mailing_id: "MailingMailing"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailingMailingTest": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailingMailingTest": ...
    def create(self, vals: Dict[str, Any]) -> "MailingMailingTest": ...
    def filtered(self, func: Any) -> "MailingMailingTest": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailingMailingTest": ...
    def exists(self) -> "MailingMailingTest": ...
    def sudo(self) -> "MailingMailingTest": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailingMailingTest": ...

# --- mailing.sms.test ---

class MailingSmsTest(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    mailing_id: "MailingMailing"
    numbers: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MailingSmsTest": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailingSmsTest": ...
    def create(self, vals: Dict[str, Any]) -> "MailingSmsTest": ...
    def filtered(self, func: Any) -> "MailingSmsTest": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailingSmsTest": ...
    def exists(self) -> "MailingSmsTest": ...
    def sudo(self) -> "MailingSmsTest": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailingSmsTest": ...

# --- mailing.trace ---

class MailingTrace(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    campaign_id: "UtmCampaign"
    email: str
    failure_type: str
    has_bit2publish_template: bool
    links_click_datetime: Optional[_dt.datetime]
    links_click_ids: "LinkTrackerClick"
    mail_mail_id: "MailMail"
    mail_mail_id_int: int
    marketing_trace_id: "MarketingTrace"
    mass_mailing_id: "MailingMailing"
    medium_id: "UtmMedium"
    message_id: str
    model: str
    open_datetime: Optional[_dt.datetime]
    reply_datetime: Optional[_dt.datetime]
    res_id: Any
    sent_datetime: Optional[_dt.datetime]
    show_bit2publish_button: bool
    sms_code: str
    sms_number: str
    sms_sms_id: "SmsSms"
    sms_sms_id_int: int
    source_id: "UtmSource"
    trace_status: str
    trace_type: str
    def browse(self, ids: Union[int, List[int]]) -> "MailingTrace": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailingTrace": ...
    def create(self, vals: Dict[str, Any]) -> "MailingTrace": ...
    def filtered(self, func: Any) -> "MailingTrace": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailingTrace": ...
    def exists(self) -> "MailingTrace": ...
    def sudo(self) -> "MailingTrace": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailingTrace": ...

# --- mailing.trace.report ---

class MailingTraceReport(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    bounced: int
    campaign: str
    canceled: int
    clicked: int
    delivered: int
    email_from: str
    error: int
    has_bit2publish_template: bool
    mailing_type: str
    name: str
    opened: int
    replied: int
    scheduled: int
    scheduled_date: Optional[_dt.datetime]
    sent: int
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "MailingTraceReport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MailingTraceReport": ...
    def create(self, vals: Dict[str, Any]) -> "MailingTraceReport": ...
    def filtered(self, func: Any) -> "MailingTraceReport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MailingTraceReport": ...
    def exists(self) -> "MailingTraceReport": ...
    def sudo(self) -> "MailingTraceReport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MailingTraceReport": ...

# --- market.comm.event.log ---

class MarketCommEventLog(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    cp_gestore: str
    cp_utente: str
    flow_code: str
    full_payload: str
    has_bit2publish_template: bool
    inner_payload: str
    service_code: str
    show_bit2publish_button: bool
    ticket_id: "HelpdeskTicket"
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
    def sorted(self, key: Any = None, reverse: bool = False) -> "MarketCommEventLog": ...
    def exists(self) -> "MarketCommEventLog": ...
    def sudo(self) -> "MarketCommEventLog": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MarketCommEventLog": ...

# --- market.comm.event.log.cp.utente.filter ---

class MarketCommEventLogCpUtenteFilter(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    file: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MarketCommEventLogCpUtenteFilter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MarketCommEventLogCpUtenteFilter": ...
    def create(self, vals: Dict[str, Any]) -> "MarketCommEventLogCpUtenteFilter": ...
    def filtered(self, func: Any) -> "MarketCommEventLogCpUtenteFilter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MarketCommEventLogCpUtenteFilter": ...
    def exists(self) -> "MarketCommEventLogCpUtenteFilter": ...
    def sudo(self) -> "MarketCommEventLogCpUtenteFilter": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MarketCommEventLogCpUtenteFilter": ...

# --- market.comm.event.log.distinct ---

class MarketCommEventLogDistinct(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    cp_utente: str
    has_bit2publish_template: bool
    service_code: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MarketCommEventLogDistinct": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MarketCommEventLogDistinct": ...
    def create(self, vals: Dict[str, Any]) -> "MarketCommEventLogDistinct": ...
    def filtered(self, func: Any) -> "MarketCommEventLogDistinct": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MarketCommEventLogDistinct": ...
    def exists(self) -> "MarketCommEventLogDistinct": ...
    def sudo(self) -> "MarketCommEventLogDistinct": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MarketCommEventLogDistinct": ...

# --- marketing.activity ---

class MarketingActivity(Recordset):
    activity_domain: str
    activity_type: str
    allowed_parent_ids: "MarketingActivity"
    bit2publish_template_ids: "Bit2publishTemplate"
    campaign_id: "MarketingCampaign"
    child_ids: "MarketingActivity"
    domain: str
    has_bit2publish_template: bool
    interval_number: int
    interval_standardized: int
    interval_type: str
    mail_template_id: "MailTemplate"
    mass_mailing_id: "MailingMailing"
    mass_mailing_id_mailing_type: str
    model_id: "IrModel"
    model_name: str
    name: str
    parent_id: "MarketingActivity"
    postalizer_template_id: "PostalizerTemplate"
    processed: int
    rejected: int
    require_sync: bool
    server_action_id: "IrActionsServer"
    show_bit2publish_button: bool
    sms_template_id: "SmsTemplate"
    statistics_graph_data: str
    total_bounce: int
    total_click: int
    total_open: int
    total_reply: int
    total_sent: int
    trace_ids: "MarketingTrace"
    trigger_category: str
    trigger_type: str
    utm_campaign_id: "UtmCampaign"
    utm_source_id: "UtmSource"
    validity_duration: bool
    validity_duration_number: int
    validity_duration_type: str
    def browse(self, ids: Union[int, List[int]]) -> "MarketingActivity": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MarketingActivity": ...
    def create(self, vals: Dict[str, Any]) -> "MarketingActivity": ...
    def filtered(self, func: Any) -> "MarketingActivity": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MarketingActivity": ...
    def exists(self) -> "MarketingActivity": ...
    def sudo(self) -> "MarketingActivity": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MarketingActivity": ...

# --- marketing.campaign ---

class MarketingCampaign(Recordset):
    ab_testing_completed: bool
    ab_testing_mailings_count: int
    ab_testing_schedule_datetime: Optional[_dt.datetime]
    ab_testing_sms_winner_selection: str
    ab_testing_total_pc: int
    ab_testing_winner_selection: str
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    bounced_ratio: int
    click_count: int
    color: int
    completed_participant_count: int
    domain: str
    has_bit2publish_template: bool
    is_auto_campaign: bool
    last_sync_date: Optional[_dt.datetime]
    link_tracker_click_count: int
    mailing_mail_count: int
    mailing_mail_ids: "MailingMailing"
    mailing_sms_count: int
    mailing_sms_ids: "MailingMailing"
    marketing_activity_ids: "MarketingActivity"
    mass_mailing_count: int
    model_id: "IrModel"
    model_name: str
    name: str
    opened_ratio: int
    participant_ids: "MarketingParticipant"
    received_ratio: int
    replied_ratio: int
    require_sync: bool
    running_participant_count: int
    show_bit2publish_button: bool
    stage_id: "UtmStage"
    state: str
    tag_ids: "UtmTag"
    test_participant_count: int
    total_participant_count: int
    unique_field_id: "IrModelFields"
    user_id: "ResUsers"
    utm_campaign_id: "UtmCampaign"
    def browse(self, ids: Union[int, List[int]]) -> "MarketingCampaign": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MarketingCampaign": ...
    def create(self, vals: Dict[str, Any]) -> "MarketingCampaign": ...
    def filtered(self, func: Any) -> "MarketingCampaign": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MarketingCampaign": ...
    def exists(self) -> "MarketingCampaign": ...
    def sudo(self) -> "MarketingCampaign": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MarketingCampaign": ...

# --- marketing.campaign.test ---

class MarketingCampaignTest(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    campaign_id: "MarketingCampaign"
    has_bit2publish_template: bool
    model_id: "IrModel"
    model_name: str
    res_id: int
    resource_ref: Any
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MarketingCampaignTest": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MarketingCampaignTest": ...
    def create(self, vals: Dict[str, Any]) -> "MarketingCampaignTest": ...
    def filtered(self, func: Any) -> "MarketingCampaignTest": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MarketingCampaignTest": ...
    def exists(self) -> "MarketingCampaignTest": ...
    def sudo(self) -> "MarketingCampaignTest": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MarketingCampaignTest": ...

# --- marketing.event ---

class MarketingEvent(Recordset):
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    description: str
    email: str
    external_id: str
    flag_insurance: bool
    has_bit2publish_template: bool
    has_message: bool
    marketing_event_type_id: "MarketingEventType"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    partner_id: "ResPartner"
    phone: str
    process: str
    product_code: str
    reference: str
    repricing_type: str
    res_id: Any
    res_model: str
    res_model_display_name: str
    res_partner_address_id: "ResPartner"
    show_bit2publish_button: bool
    sym_process_ref_id: str
    sym_process_ref_name: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "MarketingEvent": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MarketingEvent": ...
    def create(self, vals: Dict[str, Any]) -> "MarketingEvent": ...
    def filtered(self, func: Any) -> "MarketingEvent": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MarketingEvent": ...
    def exists(self) -> "MarketingEvent": ...
    def sudo(self) -> "MarketingEvent": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MarketingEvent": ...

# --- marketing.event.type ---

class MarketingEventType(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    external_name: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MarketingEventType": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MarketingEventType": ...
    def create(self, vals: Dict[str, Any]) -> "MarketingEventType": ...
    def filtered(self, func: Any) -> "MarketingEventType": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MarketingEventType": ...
    def exists(self) -> "MarketingEventType": ...
    def sudo(self) -> "MarketingEventType": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MarketingEventType": ...

# --- marketing.participant ---

class MarketingParticipant(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    campaign_id: "MarketingCampaign"
    has_bit2publish_template: bool
    is_test: bool
    model_id: "IrModel"
    model_name: str
    res_id: int
    resource_ref: Any
    show_bit2publish_button: bool
    state: str
    trace_ids: "MarketingTrace"
    def browse(self, ids: Union[int, List[int]]) -> "MarketingParticipant": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MarketingParticipant": ...
    def create(self, vals: Dict[str, Any]) -> "MarketingParticipant": ...
    def filtered(self, func: Any) -> "MarketingParticipant": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MarketingParticipant": ...
    def exists(self) -> "MarketingParticipant": ...
    def sudo(self) -> "MarketingParticipant": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MarketingParticipant": ...

# --- marketing.trace ---

class MarketingTrace(Recordset):
    activity_id: "MarketingActivity"
    activity_type: str
    bit2publish_template_ids: "Bit2publishTemplate"
    child_ids: "MarketingTrace"
    has_bit2publish_template: bool
    is_test: bool
    links_click_datetime: Optional[_dt.datetime]
    mailing_trace_ids: "MailingTrace"
    mailing_trace_status: str
    parent_id: "MarketingTrace"
    participant_id: "MarketingParticipant"
    res_id: int
    schedule_date: Optional[_dt.datetime]
    show_bit2publish_button: bool
    state: str
    state_msg: str
    trigger_type: str
    def browse(self, ids: Union[int, List[int]]) -> "MarketingTrace": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MarketingTrace": ...
    def create(self, vals: Dict[str, Any]) -> "MarketingTrace": ...
    def filtered(self, func: Any) -> "MarketingTrace": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MarketingTrace": ...
    def exists(self) -> "MarketingTrace": ...
    def sudo(self) -> "MarketingTrace": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MarketingTrace": ...

# --- meter.readings ---

class MeterReadings(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    client_id: "ResPartner"
    f0_reading: str
    f0_responsive_reading: str
    f0_voltage_reading: str
    f1_reading: str
    f1_responsive_reading: str
    f1_voltage_reading: str
    f2_reading: str
    f2_responsive_reading: str
    f2_voltage_reading: str
    f3_reading: str
    f3_responsive_reading: str
    f3_voltage_reading: str
    has_bit2publish_template: bool
    meter_id: "ResPartnerMeter"
    name: str
    notes: str
    reading_date: Optional[_dt.date]
    reading_type: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MeterReadings": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MeterReadings": ...
    def create(self, vals: Dict[str, Any]) -> "MeterReadings": ...
    def filtered(self, func: Any) -> "MeterReadings": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MeterReadings": ...
    def exists(self) -> "MeterReadings": ...
    def sudo(self) -> "MeterReadings": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MeterReadings": ...

# --- meter.readings.pdr ---

class MeterReadingsPdr(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    client_id: "ResPartner"
    correction_reading: int
    has_bit2publish_template: bool
    meter_id: "ResPartnerMeterPdr"
    meter_reading: int
    name: str
    notes: str
    reading_date: Optional[_dt.date]
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "MeterReadingsPdr": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MeterReadingsPdr": ...
    def create(self, vals: Dict[str, Any]) -> "MeterReadingsPdr": ...
    def filtered(self, func: Any) -> "MeterReadingsPdr": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MeterReadingsPdr": ...
    def exists(self) -> "MeterReadingsPdr": ...
    def sudo(self) -> "MeterReadingsPdr": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MeterReadingsPdr": ...

# --- microsoft.outlook.mixin ---

class MicrosoftOutlookMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    is_microsoft_outlook_configured: bool
    microsoft_outlook_access_token: str
    microsoft_outlook_access_token_expiration: int
    microsoft_outlook_refresh_token: str
    microsoft_outlook_uri: str
    show_bit2publish_button: bool
    use_microsoft_outlook_service: bool
    def browse(self, ids: Union[int, List[int]]) -> "MicrosoftOutlookMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "MicrosoftOutlookMixin": ...
    def create(self, vals: Dict[str, Any]) -> "MicrosoftOutlookMixin": ...
    def filtered(self, func: Any) -> "MicrosoftOutlookMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "MicrosoftOutlookMixin": ...
    def exists(self) -> "MicrosoftOutlookMixin": ...
    def sudo(self) -> "MicrosoftOutlookMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "MicrosoftOutlookMixin": ...

# --- natural.disasters.history ---

class NaturalDisastersHistory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    end_date: Optional[_dt.date]
    has_bit2publish_template: bool
    id_event: str
    reference_year: str
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    start_date: Optional[_dt.date]
    def browse(self, ids: Union[int, List[int]]) -> "NaturalDisastersHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "NaturalDisastersHistory": ...
    def create(self, vals: Dict[str, Any]) -> "NaturalDisastersHistory": ...
    def filtered(self, func: Any) -> "NaturalDisastersHistory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "NaturalDisastersHistory": ...
    def exists(self) -> "NaturalDisastersHistory": ...
    def sudo(self) -> "NaturalDisastersHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "NaturalDisastersHistory": ...

# --- nuts.import ---

class NutsImport(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    current_country_id: "ResCountry"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "NutsImport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "NutsImport": ...
    def create(self, vals: Dict[str, Any]) -> "NutsImport": ...
    def filtered(self, func: Any) -> "NutsImport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "NutsImport": ...
    def exists(self) -> "NutsImport": ...
    def sudo(self) -> "NutsImport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "NutsImport": ...

# --- olo.fiber.codes ---

class OloFiberCodes(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    description: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "OloFiberCodes": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "OloFiberCodes": ...
    def create(self, vals: Dict[str, Any]) -> "OloFiberCodes": ...
    def filtered(self, func: Any) -> "OloFiberCodes": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "OloFiberCodes": ...
    def exists(self) -> "OloFiberCodes": ...
    def sudo(self) -> "OloFiberCodes": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "OloFiberCodes": ...

# --- paperwork ---

class Paperwork(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "Paperwork": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "Paperwork": ...
    def create(self, vals: Dict[str, Any]) -> "Paperwork": ...
    def filtered(self, func: Any) -> "Paperwork": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "Paperwork": ...
    def exists(self) -> "Paperwork": ...
    def sudo(self) -> "Paperwork": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "Paperwork": ...

# --- paperwork.annulment.reason ---

class PaperworkAnnulmentReason(Recordset):
    annulment_paperwork: str
    annulment_reason_ids: "AnnulmentReason"
    annulment_reason_type: str
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    paperwork_id: "Paperwork"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "PaperworkAnnulmentReason": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PaperworkAnnulmentReason": ...
    def create(self, vals: Dict[str, Any]) -> "PaperworkAnnulmentReason": ...
    def filtered(self, func: Any) -> "PaperworkAnnulmentReason": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PaperworkAnnulmentReason": ...
    def exists(self) -> "PaperworkAnnulmentReason": ...
    def sudo(self) -> "PaperworkAnnulmentReason": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PaperworkAnnulmentReason": ...

# --- party.relation ---

class PartyRelation(Recordset):
    a_to_b_string: str
    bit2publish_template_ids: "Bit2publishTemplate"
    b_to_a_string: str
    domain_partner_a: str
    domain_partner_b: str
    end_date: Optional[_dt.date]
    has_bit2publish_template: bool
    is_symmetrical_relation: bool
    name: str
    partner_a_id: "ResPartner"
    partner_b_id: "ResPartner"
    party_type_id: "PartyType"
    relation_string: str
    service_point_codes: str
    service_point_ids: "ServicePoint"
    show_bit2publish_button: bool
    start_date: Optional[_dt.date]
    state: str
    symmetrical_string: str
    def browse(self, ids: Union[int, List[int]]) -> "PartyRelation": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PartyRelation": ...
    def create(self, vals: Dict[str, Any]) -> "PartyRelation": ...
    def filtered(self, func: Any) -> "PartyRelation": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PartyRelation": ...
    def exists(self) -> "PartyRelation": ...
    def sudo(self) -> "PartyRelation": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PartyRelation": ...

# --- party.type ---

class PartyType(Recordset):
    a_relates_to_b_string: str
    bit2publish_template_ids: "Bit2publishTemplate"
    b_relates_to_a_string: str
    has_bit2publish_template: bool
    hide_service_point: bool
    is_from_migration: bool
    is_symmetrical_relation: bool
    name: str
    partner_domain_a: str
    partner_domain_a_ids: "ResPartner"
    partner_domain_b: str
    partner_domain_b_ids: "ResPartner"
    requires_service_point: bool
    show_bit2publish_button: bool
    symmetrical_relation_to_string: str
    def browse(self, ids: Union[int, List[int]]) -> "PartyType": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PartyType": ...
    def create(self, vals: Dict[str, Any]) -> "PartyType": ...
    def filtered(self, func: Any) -> "PartyType": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PartyType": ...
    def exists(self) -> "PartyType": ...
    def sudo(self) -> "PartyType": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PartyType": ...

# --- payment.acquirer ---

class PaymentAcquirer(Recordset):
    allow_tokenization: bool
    auth_msg: str
    bit2publish_template_ids: "Bit2publishTemplate"
    cancel_msg: str
    capture_manually: bool
    color: int
    company_id: "ResCompany"
    country_ids: "ResCountry"
    description: str
    display_as: str
    done_msg: str
    fees_active: bool
    fees_dom_fixed: float
    fees_dom_var: float
    fees_int_fixed: float
    fees_int_var: float
    has_bit2publish_template: bool
    image_128: bytes
    inline_form_view_id: "IrUiView"
    journal_id: "AccountJournal"
    module_id: "IrModuleModule"
    module_state: str
    module_to_buy: bool
    name: str
    payment_icon_ids: "PaymentIcon"
    pending_msg: str
    pre_msg: str
    provider: str
    qr_code: bool
    redirect_form_view_id: "IrUiView"
    sequence: int
    show_allow_tokenization: bool
    show_auth_msg: bool
    show_bit2publish_button: bool
    show_cancel_msg: bool
    show_credentials_page: bool
    show_done_msg: bool
    show_payment_icon_ids: bool
    show_pending_msg: bool
    show_pre_msg: bool
    state: str
    support_authorization: bool
    support_fees_computation: bool
    support_refund: str
    support_tokenization: bool
    def browse(self, ids: Union[int, List[int]]) -> "PaymentAcquirer": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PaymentAcquirer": ...
    def create(self, vals: Dict[str, Any]) -> "PaymentAcquirer": ...
    def filtered(self, func: Any) -> "PaymentAcquirer": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PaymentAcquirer": ...
    def exists(self) -> "PaymentAcquirer": ...
    def sudo(self) -> "PaymentAcquirer": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PaymentAcquirer": ...

# --- payment.acquirer.onboarding.wizard ---

class PaymentAcquirerOnboardingWizard(Recordset):
    acc_number: str
    bit2publish_template_ids: "Bit2publishTemplate"
    _data_fetched: bool
    has_bit2publish_template: bool
    journal_name: str
    manual_name: str
    manual_post_msg: str
    payment_method: str
    paypal_email_account: str
    paypal_pdt_token: str
    paypal_seller_account: str
    paypal_user_type: str
    show_bit2publish_button: bool
    stripe_publishable_key: str
    stripe_secret_key: str
    def browse(self, ids: Union[int, List[int]]) -> "PaymentAcquirerOnboardingWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PaymentAcquirerOnboardingWizard": ...
    def create(self, vals: Dict[str, Any]) -> "PaymentAcquirerOnboardingWizard": ...
    def filtered(self, func: Any) -> "PaymentAcquirerOnboardingWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PaymentAcquirerOnboardingWizard": ...
    def exists(self) -> "PaymentAcquirerOnboardingWizard": ...
    def sudo(self) -> "PaymentAcquirerOnboardingWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PaymentAcquirerOnboardingWizard": ...

# --- payment.icon ---

class PaymentIcon(Recordset):
    acquirer_ids: "PaymentAcquirer"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    image: bytes
    image_payment_form: bytes
    name: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "PaymentIcon": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PaymentIcon": ...
    def create(self, vals: Dict[str, Any]) -> "PaymentIcon": ...
    def filtered(self, func: Any) -> "PaymentIcon": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PaymentIcon": ...
    def exists(self) -> "PaymentIcon": ...
    def sudo(self) -> "PaymentIcon": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PaymentIcon": ...

# --- payment.link.wizard ---

class PaymentLinkWizard(Recordset):
    access_token: str
    acquirer_id: "PaymentAcquirer"
    amount: float
    amount_max: float
    available_acquirer_ids: "PaymentAcquirer"
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    currency_id: "ResCurrency"
    description: str
    has_bit2publish_template: bool
    has_multiple_acquirers: bool
    link: str
    partner_email: str
    partner_id: "ResPartner"
    payment_acquirer_selection: str
    res_id: int
    res_model: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "PaymentLinkWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PaymentLinkWizard": ...
    def create(self, vals: Dict[str, Any]) -> "PaymentLinkWizard": ...
    def filtered(self, func: Any) -> "PaymentLinkWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PaymentLinkWizard": ...
    def exists(self) -> "PaymentLinkWizard": ...
    def sudo(self) -> "PaymentLinkWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PaymentLinkWizard": ...

# --- payment.method ---

class PaymentMethod(Recordset):
    abi: str
    account_owner_name: str
    account_owner_surname: str
    activation_date: Optional[_dt.date]
    active: bool
    alias_pan: str
    auth_code: str
    bank_account: str
    bank_name: str
    billing_profile_ids: "BillingProfile"
    bit2publish_template_ids: "Bit2publishTemplate"
    cab: str
    card_or_iban: str
    cc_activation_date: Optional[_dt.date]
    cc_alias: str
    cc_circuit: str
    cc_owner: str
    ccr_card_network: str
    ccr_deactivation_date: Optional[_dt.date]
    ccr_identifier: str
    ccr_status: str
    cf_owner: str
    checking_account: str
    cin: str
    cin_eu: str
    client_code: str
    client_id: "ResPartner"
    cre_curr: str
    credit_card: str
    credit_card_end_month: str
    credit_card_end_year: int
    credit_card_hidden: str
    dpay_alias: str
    dpay_create_date: Optional[_dt.datetime]
    dpay_end_date: Optional[_dt.datetime]
    dpay_owner: str
    dpay_status: str
    elaboration_phase: str
    end_validity_date: Optional[_dt.date]
    filter_status: str
    has_active_billing_profile: bool
    has_bit2publish_template: bool
    holder_cf_or_vat: str
    holder_company: str
    iban: str
    id_dpay: str
    id_sdd: str
    is_active: bool
    is_foreign_iban: bool
    name: str
    payment_method: str
    payment_method_status: str
    revocation_date: Optional[_dt.date]
    sdd_activation_site: str
    sdd_authorization_code: str
    sdd_authorization_sign_date: Optional[_dt.date]
    sdd_date_authorization_code: Optional[_dt.date]
    sdd_deactivation_date: Optional[_dt.date]
    sdd_deactivation_reason: str
    sdd_deactivation_request_date: Optional[_dt.datetime]
    sdd_deactivation_response_date: Optional[_dt.date]
    sdd_deactivation_sent_date: Optional[_dt.date]
    sdd_request_date: Optional[_dt.date]
    sdd_status: str
    show_bit2publish_button: bool
    sign_location: str
    start_validity_date: Optional[_dt.date]
    state: str
    swift: str
    tre_curr: str
    def browse(self, ids: Union[int, List[int]]) -> "PaymentMethod": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PaymentMethod": ...
    def create(self, vals: Dict[str, Any]) -> "PaymentMethod": ...
    def filtered(self, func: Any) -> "PaymentMethod": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PaymentMethod": ...
    def exists(self) -> "PaymentMethod": ...
    def sudo(self) -> "PaymentMethod": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PaymentMethod": ...

# --- payment.refund.wizard ---

class PaymentRefundWizard(Recordset):
    amount_available_for_refund: float
    amount_to_refund: float
    bit2publish_template_ids: "Bit2publishTemplate"
    currency_id: "ResCurrency"
    has_bit2publish_template: bool
    has_pending_refund: bool
    payment_amount: float
    payment_id: "AccountPayment"
    refunded_amount: float
    show_bit2publish_button: bool
    support_refund: str
    transaction_id: "PaymentTransaction"
    def browse(self, ids: Union[int, List[int]]) -> "PaymentRefundWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PaymentRefundWizard": ...
    def create(self, vals: Dict[str, Any]) -> "PaymentRefundWizard": ...
    def filtered(self, func: Any) -> "PaymentRefundWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PaymentRefundWizard": ...
    def exists(self) -> "PaymentRefundWizard": ...
    def sudo(self) -> "PaymentRefundWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PaymentRefundWizard": ...

# --- payment.term ---

class PaymentTerm(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    id_code: str
    is_locked: bool
    name: str
    short_label: str
    show_bit2publish_button: bool
    term_type: str
    def browse(self, ids: Union[int, List[int]]) -> "PaymentTerm": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PaymentTerm": ...
    def create(self, vals: Dict[str, Any]) -> "PaymentTerm": ...
    def filtered(self, func: Any) -> "PaymentTerm": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PaymentTerm": ...
    def exists(self) -> "PaymentTerm": ...
    def sudo(self) -> "PaymentTerm": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PaymentTerm": ...

# --- payment.token ---

class PaymentToken(Recordset):
    acquirer_id: "PaymentAcquirer"
    acquirer_ref: str
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    has_bit2publish_template: bool
    name: str
    partner_id: "ResPartner"
    provider: str
    show_bit2publish_button: bool
    transaction_ids: "PaymentTransaction"
    verified: bool
    def browse(self, ids: Union[int, List[int]]) -> "PaymentToken": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PaymentToken": ...
    def create(self, vals: Dict[str, Any]) -> "PaymentToken": ...
    def filtered(self, func: Any) -> "PaymentToken": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PaymentToken": ...
    def exists(self) -> "PaymentToken": ...
    def sudo(self) -> "PaymentToken": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PaymentToken": ...

# --- payment.transaction ---

class PaymentTransaction(Recordset):
    acquirer_id: "PaymentAcquirer"
    acquirer_reference: str
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    callback_hash: str
    callback_is_done: bool
    callback_method: str
    callback_model_id: "IrModel"
    callback_res_id: int
    company_id: "ResCompany"
    currency_id: "ResCurrency"
    fees: float
    has_bit2publish_template: bool
    invoice_ids: "AccountMove"
    invoices_count: int
    is_post_processed: bool
    landing_route: str
    last_state_change: Optional[_dt.datetime]
    operation: str
    partner_address: str
    partner_city: str
    partner_country_id: "ResCountry"
    partner_email: str
    partner_id: "ResPartner"
    partner_lang: str
    partner_name: str
    partner_phone: str
    partner_state_id: "ResCountryState"
    partner_zip: str
    payment_id: "AccountPayment"
    provider: str
    reference: str
    refunds_count: int
    show_bit2publish_button: bool
    source_transaction_id: "PaymentTransaction"
    state: str
    state_message: str
    token_id: "PaymentToken"
    tokenize: bool
    def browse(self, ids: Union[int, List[int]]) -> "PaymentTransaction": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PaymentTransaction": ...
    def create(self, vals: Dict[str, Any]) -> "PaymentTransaction": ...
    def filtered(self, func: Any) -> "PaymentTransaction": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PaymentTransaction": ...
    def exists(self) -> "PaymentTransaction": ...
    def sudo(self) -> "PaymentTransaction": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PaymentTransaction": ...

# --- pcs.data.wizard ---

class PcsDataWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    pcs_record_lines: "PcsRecordLine"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "PcsDataWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PcsDataWizard": ...
    def create(self, vals: Dict[str, Any]) -> "PcsDataWizard": ...
    def filtered(self, func: Any) -> "PcsDataWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PcsDataWizard": ...
    def exists(self) -> "PcsDataWizard": ...
    def sudo(self) -> "PcsDataWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PcsDataWizard": ...

# --- pcs.record.line ---

class PcsRecordLine(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    codice_remi: str
    competence: str
    data_competenza_pcs_giornaliera: Optional[_dt.date]
    fonte_pcs_giornaliero: str
    has_bit2publish_template: bool
    pcs_convenzionale: float
    pcs_effettivo: float
    show_bit2publish_button: bool
    valore_pcs: float
    wizard_id: "PcsDataWizard"
    def browse(self, ids: Union[int, List[int]]) -> "PcsRecordLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PcsRecordLine": ...
    def create(self, vals: Dict[str, Any]) -> "PcsRecordLine": ...
    def filtered(self, func: Any) -> "PcsRecordLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PcsRecordLine": ...
    def exists(self) -> "PcsRecordLine": ...
    def sudo(self) -> "PcsRecordLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PcsRecordLine": ...

# --- pcs.wizard.handler ---

class PcsWizardHandler(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "PcsWizardHandler": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PcsWizardHandler": ...
    def create(self, vals: Dict[str, Any]) -> "PcsWizardHandler": ...
    def filtered(self, func: Any) -> "PcsWizardHandler": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PcsWizardHandler": ...
    def exists(self) -> "PcsWizardHandler": ...
    def sudo(self) -> "PcsWizardHandler": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PcsWizardHandler": ...

# --- phase.result.selector ---

class PhaseResultSelector(Recordset):
    allowed_phase_result_ids: "SympleTripletPhaseResult"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    phase_id: "SympleTripletPhase"
    show_bit2publish_button: bool
    state: str
    triplet_phase_result_id: "SympleTripletPhaseResult"
    def browse(self, ids: Union[int, List[int]]) -> "PhaseResultSelector": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PhaseResultSelector": ...
    def create(self, vals: Dict[str, Any]) -> "PhaseResultSelector": ...
    def filtered(self, func: Any) -> "PhaseResultSelector": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PhaseResultSelector": ...
    def exists(self) -> "PhaseResultSelector": ...
    def sudo(self) -> "PhaseResultSelector": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PhaseResultSelector": ...

# --- phone.blacklist ---

class PhoneBlacklist(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    number: str
    show_bit2publish_button: bool
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "PhoneBlacklist": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PhoneBlacklist": ...
    def create(self, vals: Dict[str, Any]) -> "PhoneBlacklist": ...
    def filtered(self, func: Any) -> "PhoneBlacklist": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PhoneBlacklist": ...
    def exists(self) -> "PhoneBlacklist": ...
    def sudo(self) -> "PhoneBlacklist": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PhoneBlacklist": ...

# --- phone.blacklist.remove ---

class PhoneBlacklistRemove(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    phone: str
    reason: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "PhoneBlacklistRemove": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PhoneBlacklistRemove": ...
    def create(self, vals: Dict[str, Any]) -> "PhoneBlacklistRemove": ...
    def filtered(self, func: Any) -> "PhoneBlacklistRemove": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PhoneBlacklistRemove": ...
    def exists(self) -> "PhoneBlacklistRemove": ...
    def sudo(self) -> "PhoneBlacklistRemove": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PhoneBlacklistRemove": ...

# --- physical.bonus ---

class PhysicalBonus(Recordset):
    attachment_ids: "IrAttachment"
    attachment_warning: str
    bit2publish_template_ids: "Bit2publishTemplate"
    bonus_type: str
    commodity: str
    has_bit2publish_template: bool
    last_error: str
    last_processed_line: int
    line_ids: "PhysicalBonusLine"
    month: str
    name: str
    origin: str
    service_type: str
    show_bit2publish_button: bool
    state: str
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "PhysicalBonus": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PhysicalBonus": ...
    def create(self, vals: Dict[str, Any]) -> "PhysicalBonus": ...
    def filtered(self, func: Any) -> "PhysicalBonus": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PhysicalBonus": ...
    def exists(self) -> "PhysicalBonus": ...
    def sudo(self) -> "PhysicalBonus": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PhysicalBonus": ...

# --- physical.bonus.expected.value ---

class PhysicalBonusExpectedValue(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "PhysicalBonusExpectedValue": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PhysicalBonusExpectedValue": ...
    def create(self, vals: Dict[str, Any]) -> "PhysicalBonusExpectedValue": ...
    def filtered(self, func: Any) -> "PhysicalBonusExpectedValue": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PhysicalBonusExpectedValue": ...
    def exists(self) -> "PhysicalBonusExpectedValue": ...
    def sudo(self) -> "PhysicalBonusExpectedValue": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PhysicalBonusExpectedValue": ...

# --- physical.bonus.line ---

class PhysicalBonusLine(Recordset):
    alert_message: bool
    ammontare: float
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    bonus_id: "PhysicalBonus"
    case_ids: "HelpdeskTicket"
    cf: str
    client_code: str
    client_id: "ResPartner"
    cod_pod: str
    cod_prestazione: str
    cognome: str
    data_deco: Optional[_dt.date]
    data_fine: Optional[_dt.date]
    display_is_before_migration_cutoff: str
    has_bit2publish_template: bool
    is_before_migration_cutoff: bool
    last_error: str
    month: str
    name: str
    nome: str
    piva_distr: str
    piva_utente: str
    pod_id: "ResPartnerPod"
    show_bit2publish_button: bool
    state: str
    termine_rinnovo: Optional[_dt.date]
    tipo_compe: str
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "PhysicalBonusLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PhysicalBonusLine": ...
    def create(self, vals: Dict[str, Any]) -> "PhysicalBonusLine": ...
    def filtered(self, func: Any) -> "PhysicalBonusLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PhysicalBonusLine": ...
    def exists(self) -> "PhysicalBonusLine": ...
    def sudo(self) -> "PhysicalBonusLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PhysicalBonusLine": ...

# --- portal.mixin ---

class PortalMixin(Recordset):
    access_token: str
    access_url: str
    access_warning: str
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "PortalMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PortalMixin": ...
    def create(self, vals: Dict[str, Any]) -> "PortalMixin": ...
    def filtered(self, func: Any) -> "PortalMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PortalMixin": ...
    def exists(self) -> "PortalMixin": ...
    def sudo(self) -> "PortalMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PortalMixin": ...

# --- portal.share ---

class PortalShare(Recordset):
    access_warning: str
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    note: str
    partner_ids: "ResPartner"
    res_id: int
    res_model: str
    resource_ref: Any
    share_link: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "PortalShare": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PortalShare": ...
    def create(self, vals: Dict[str, Any]) -> "PortalShare": ...
    def filtered(self, func: Any) -> "PortalShare": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PortalShare": ...
    def exists(self) -> "PortalShare": ...
    def sudo(self) -> "PortalShare": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PortalShare": ...

# --- portal.wizard ---

class PortalWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    partner_ids: "ResPartner"
    show_bit2publish_button: bool
    user_ids: "PortalWizardUser"
    welcome_message: str
    def browse(self, ids: Union[int, List[int]]) -> "PortalWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PortalWizard": ...
    def create(self, vals: Dict[str, Any]) -> "PortalWizard": ...
    def filtered(self, func: Any) -> "PortalWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PortalWizard": ...
    def exists(self) -> "PortalWizard": ...
    def sudo(self) -> "PortalWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PortalWizard": ...

# --- portal.wizard.user ---

class PortalWizardUser(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    email: str
    has_bit2publish_template: bool
    is_internal: bool
    is_portal: bool
    login_date: Optional[_dt.datetime]
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    user_id: "ResUsers"
    wizard_id: "PortalWizard"
    def browse(self, ids: Union[int, List[int]]) -> "PortalWizardUser": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PortalWizardUser": ...
    def create(self, vals: Dict[str, Any]) -> "PortalWizardUser": ...
    def filtered(self, func: Any) -> "PortalWizardUser": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PortalWizardUser": ...
    def exists(self) -> "PortalWizardUser": ...
    def sudo(self) -> "PortalWizardUser": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PortalWizardUser": ...

# --- postalizer.template ---

class PostalizerTemplate(Recordset):
    address: str
    attachment_id: bytes
    attachment_type: str
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    can_edit_body: bool
    case_attachment: "IrModelFields"
    copyvalue: str
    dynamic_attachment: str
    has_bit2publish_template: bool
    is_created_from_marketing_automation: bool
    is_dynamic_attachment: bool
    is_mail_template_editor: bool
    lang: str
    layout: str
    model_id: "IrModel"
    model_object_field: "IrModelFields"
    name: str
    null_value: str
    postalizer_to: str
    render_model: str
    show_bit2publish_button: bool
    subject: str
    sub_model_object_field: "IrModelFields"
    sub_object: "IrModel"
    template_id: "MailTemplate"
    type: str
    def browse(self, ids: Union[int, List[int]]) -> "PostalizerTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PostalizerTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "PostalizerTemplate": ...
    def filtered(self, func: Any) -> "PostalizerTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PostalizerTemplate": ...
    def exists(self) -> "PostalizerTemplate": ...
    def sudo(self) -> "PostalizerTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PostalizerTemplate": ...

# --- print.prenumbered.checks ---

class PrintPrenumberedChecks(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    next_check_number: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "PrintPrenumberedChecks": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PrintPrenumberedChecks": ...
    def create(self, vals: Dict[str, Any]) -> "PrintPrenumberedChecks": ...
    def filtered(self, func: Any) -> "PrintPrenumberedChecks": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PrintPrenumberedChecks": ...
    def exists(self) -> "PrintPrenumberedChecks": ...
    def sudo(self) -> "PrintPrenumberedChecks": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PrintPrenumberedChecks": ...

# --- privacy.history ---

class PrivacyHistory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    consent_type: str
    has_bit2publish_template: bool
    new_value: str
    old_value: str
    origin_id: int
    origin_model: str
    origin_string: str
    partner_id: "ResPartner"
    process_type: str
    show_bit2publish_button: bool
    variation_date: Optional[_dt.datetime]
    def browse(self, ids: Union[int, List[int]]) -> "PrivacyHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PrivacyHistory": ...
    def create(self, vals: Dict[str, Any]) -> "PrivacyHistory": ...
    def filtered(self, func: Any) -> "PrivacyHistory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PrivacyHistory": ...
    def exists(self) -> "PrivacyHistory": ...
    def sudo(self) -> "PrivacyHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PrivacyHistory": ...

# --- product.attribute ---

class ProductAttribute(Recordset):
    attribute_line_ids: "ProductTemplateAttributeLine"
    bit2publish_template_ids: "Bit2publishTemplate"
    create_variant: str
    display_type: str
    has_bit2publish_template: bool
    name: str
    number_related_products: int
    product_tmpl_ids: "ProductTemplate"
    sequence: int
    show_bit2publish_button: bool
    value_ids: "ProductAttributeValue"
    def browse(self, ids: Union[int, List[int]]) -> "ProductAttribute": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductAttribute": ...
    def create(self, vals: Dict[str, Any]) -> "ProductAttribute": ...
    def filtered(self, func: Any) -> "ProductAttribute": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductAttribute": ...
    def exists(self) -> "ProductAttribute": ...
    def sudo(self) -> "ProductAttribute": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductAttribute": ...

# --- product.attribute.custom.value ---

class ProductAttributeCustomValue(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    custom_product_template_attribute_value_id: "ProductTemplateAttributeValue"
    custom_value: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ProductAttributeCustomValue": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductAttributeCustomValue": ...
    def create(self, vals: Dict[str, Any]) -> "ProductAttributeCustomValue": ...
    def filtered(self, func: Any) -> "ProductAttributeCustomValue": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductAttributeCustomValue": ...
    def exists(self) -> "ProductAttributeCustomValue": ...
    def sudo(self) -> "ProductAttributeCustomValue": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductAttributeCustomValue": ...

# --- product.attribute.value ---

class ProductAttributeValue(Recordset):
    attribute_id: "ProductAttribute"
    bit2publish_template_ids: "Bit2publishTemplate"
    color: int
    display_type: str
    has_bit2publish_template: bool
    html_color: str
    is_custom: bool
    is_used_on_products: bool
    name: str
    pav_attribute_line_ids: "ProductTemplateAttributeLine"
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ProductAttributeValue": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductAttributeValue": ...
    def create(self, vals: Dict[str, Any]) -> "ProductAttributeValue": ...
    def filtered(self, func: Any) -> "ProductAttributeValue": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductAttributeValue": ...
    def exists(self) -> "ProductAttributeValue": ...
    def sudo(self) -> "ProductAttributeValue": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductAttributeValue": ...

# --- product.category ---

class ProductCategory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    child_id: "ProductCategory"
    complete_name: str
    has_bit2publish_template: bool
    name: str
    parent_id: "ProductCategory"
    parent_path: str
    product_count: int
    property_account_expense_categ_id: "AccountAccount"
    property_account_income_categ_id: "AccountAccount"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ProductCategory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductCategory": ...
    def create(self, vals: Dict[str, Any]) -> "ProductCategory": ...
    def filtered(self, func: Any) -> "ProductCategory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductCategory": ...
    def exists(self) -> "ProductCategory": ...
    def sudo(self) -> "ProductCategory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductCategory": ...

# --- product.label.layout ---

class ProductLabelLayout(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    columns: int
    custom_quantity: int
    extra_html: str
    has_bit2publish_template: bool
    print_format: str
    product_ids: "ProductProduct"
    product_tmpl_ids: "ProductTemplate"
    rows: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ProductLabelLayout": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductLabelLayout": ...
    def create(self, vals: Dict[str, Any]) -> "ProductLabelLayout": ...
    def filtered(self, func: Any) -> "ProductLabelLayout": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductLabelLayout": ...
    def exists(self) -> "ProductLabelLayout": ...
    def sudo(self) -> "ProductLabelLayout": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductLabelLayout": ...

# --- product.packaging ---

class ProductPackaging(Recordset):
    barcode: str
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    has_bit2publish_template: bool
    name: str
    product_id: "ProductProduct"
    product_uom_id: "UomUom"
    qty: float
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ProductPackaging": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductPackaging": ...
    def create(self, vals: Dict[str, Any]) -> "ProductPackaging": ...
    def filtered(self, func: Any) -> "ProductPackaging": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductPackaging": ...
    def exists(self) -> "ProductPackaging": ...
    def sudo(self) -> "ProductPackaging": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductPackaging": ...

# --- product.pricelist ---

class ProductPricelist(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    country_group_ids: "ResCountryGroup"
    currency_id: "ResCurrency"
    discount_policy: str
    has_bit2publish_template: bool
    item_ids: "ProductPricelistItem"
    name: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ProductPricelist": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductPricelist": ...
    def create(self, vals: Dict[str, Any]) -> "ProductPricelist": ...
    def filtered(self, func: Any) -> "ProductPricelist": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductPricelist": ...
    def exists(self) -> "ProductPricelist": ...
    def sudo(self) -> "ProductPricelist": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductPricelist": ...

# --- product.pricelist.item ---

class ProductPricelistItem(Recordset):
    active: bool
    applied_on: str
    base: str
    base_pricelist_id: "ProductPricelist"
    bit2publish_template_ids: "Bit2publishTemplate"
    categ_id: "ProductCategory"
    company_id: "ResCompany"
    compute_price: str
    currency_id: "ResCurrency"
    date_end: Optional[_dt.datetime]
    date_start: Optional[_dt.datetime]
    fixed_price: float
    has_bit2publish_template: bool
    min_quantity: float
    name: str
    percent_price: float
    price: str
    price_discount: float
    pricelist_id: "ProductPricelist"
    price_max_margin: float
    price_min_margin: float
    price_round: float
    price_surcharge: float
    product_id: "ProductProduct"
    product_tmpl_id: "ProductTemplate"
    rule_tip: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ProductPricelistItem": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductPricelistItem": ...
    def create(self, vals: Dict[str, Any]) -> "ProductPricelistItem": ...
    def filtered(self, func: Any) -> "ProductPricelistItem": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductPricelistItem": ...
    def exists(self) -> "ProductPricelistItem": ...
    def sudo(self) -> "ProductPricelistItem": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductPricelistItem": ...

# --- product.product ---

class ProductProduct(Recordset):
    account_tag_ids: "AccountAccountTag"
    active: bool
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    attribute_line_ids: "ProductTemplateAttributeLine"
    barcode: str
    bit2publish_template_ids: "Bit2publishTemplate"
    can_image_1024_be_zoomed: bool
    can_image_variant_1024_be_zoomed: bool
    categ_id: "ProductCategory"
    code: str
    color: int
    combination_indices: str
    company_id: "ResCompany"
    cost_currency_id: "ResCurrency"
    currency_id: "ResCurrency"
    default_code: str
    description: str
    description_purchase: str
    description_sale: str
    detailed_type: str
    has_bit2publish_template: bool
    has_configurable_attributes: bool
    has_message: bool
    image_1024: bytes
    image_128: bytes
    image_1920: bytes
    image_256: bytes
    image_512: bytes
    image_variant_1024: bytes
    image_variant_128: bytes
    image_variant_1920: bytes
    image_variant_256: bytes
    image_variant_512: bytes
    is_product_variant: bool
    list_price: float
    lst_price: float
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    packaging_ids: "ProductPackaging"
    partner_ref: str
    price: float
    price_extra: float
    pricelist_id: "ProductPricelist"
    pricelist_item_count: int
    priority: str
    product_template_attribute_value_ids: "ProductTemplateAttributeValue"
    product_template_variant_value_ids: "ProductTemplateAttributeValue"
    product_tmpl_id: "ProductTemplate"
    product_tooltip: str
    product_variant_count: int
    product_variant_id: "ProductProduct"
    product_variant_ids: "ProductProduct"
    property_account_expense_id: "AccountAccount"
    property_account_income_id: "AccountAccount"
    purchase_ok: bool
    sale_ok: bool
    seller_ids: "ProductSupplierinfo"
    sequence: int
    show_bit2publish_button: bool
    standard_price: float
    supplier_taxes_id: "AccountTax"
    taxes_id: "AccountTax"
    tax_string: str
    type: str
    uom_id: "UomUom"
    uom_name: str
    uom_po_id: "UomUom"
    valid_product_template_attribute_line_ids: "ProductTemplateAttributeLine"
    variant_seller_ids: "ProductSupplierinfo"
    volume: float
    volume_uom_name: str
    website_message_ids: "MailMessage"
    weight: float
    weight_uom_name: str
    def browse(self, ids: Union[int, List[int]]) -> "ProductProduct": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductProduct": ...
    def create(self, vals: Dict[str, Any]) -> "ProductProduct": ...
    def filtered(self, func: Any) -> "ProductProduct": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductProduct": ...
    def exists(self) -> "ProductProduct": ...
    def sudo(self) -> "ProductProduct": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductProduct": ...

# --- product.supplierinfo ---

class ProductSupplierinfo(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    currency_id: "ResCurrency"
    date_end: Optional[_dt.date]
    date_start: Optional[_dt.date]
    delay: int
    has_bit2publish_template: bool
    min_qty: float
    name: "ResPartner"
    price: float
    product_code: str
    product_id: "ProductProduct"
    product_name: str
    product_tmpl_id: "ProductTemplate"
    product_uom: "UomUom"
    product_variant_count: int
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ProductSupplierinfo": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductSupplierinfo": ...
    def create(self, vals: Dict[str, Any]) -> "ProductSupplierinfo": ...
    def filtered(self, func: Any) -> "ProductSupplierinfo": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductSupplierinfo": ...
    def exists(self) -> "ProductSupplierinfo": ...
    def sudo(self) -> "ProductSupplierinfo": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductSupplierinfo": ...

# --- product.template ---

class ProductTemplate(Recordset):
    account_tag_ids: "AccountAccountTag"
    active: bool
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    attribute_line_ids: "ProductTemplateAttributeLine"
    barcode: str
    bit2publish_template_ids: "Bit2publishTemplate"
    can_image_1024_be_zoomed: bool
    categ_id: "ProductCategory"
    color: int
    company_id: "ResCompany"
    cost_currency_id: "ResCurrency"
    currency_id: "ResCurrency"
    default_code: str
    description: str
    description_purchase: str
    description_sale: str
    detailed_type: str
    has_bit2publish_template: bool
    has_configurable_attributes: bool
    has_message: bool
    image_1024: bytes
    image_128: bytes
    image_1920: bytes
    image_256: bytes
    image_512: bytes
    is_product_variant: bool
    list_price: float
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    packaging_ids: "ProductPackaging"
    price: float
    pricelist_id: "ProductPricelist"
    pricelist_item_count: int
    priority: str
    product_tooltip: str
    product_variant_count: int
    product_variant_id: "ProductProduct"
    product_variant_ids: "ProductProduct"
    property_account_expense_id: "AccountAccount"
    property_account_income_id: "AccountAccount"
    purchase_ok: bool
    sale_ok: bool
    seller_ids: "ProductSupplierinfo"
    sequence: int
    show_bit2publish_button: bool
    standard_price: float
    supplier_taxes_id: "AccountTax"
    taxes_id: "AccountTax"
    tax_string: str
    type: str
    uom_id: "UomUom"
    uom_name: str
    uom_po_id: "UomUom"
    valid_product_template_attribute_line_ids: "ProductTemplateAttributeLine"
    variant_seller_ids: "ProductSupplierinfo"
    volume: float
    volume_uom_name: str
    website_message_ids: "MailMessage"
    weight: float
    weight_uom_name: str
    def browse(self, ids: Union[int, List[int]]) -> "ProductTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "ProductTemplate": ...
    def filtered(self, func: Any) -> "ProductTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductTemplate": ...
    def exists(self) -> "ProductTemplate": ...
    def sudo(self) -> "ProductTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductTemplate": ...

# --- product.template.attribute.exclusion ---

class ProductTemplateAttributeExclusion(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    product_template_attribute_value_id: "ProductTemplateAttributeValue"
    product_tmpl_id: "ProductTemplate"
    show_bit2publish_button: bool
    value_ids: "ProductTemplateAttributeValue"
    def browse(self, ids: Union[int, List[int]]) -> "ProductTemplateAttributeExclusion": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductTemplateAttributeExclusion": ...
    def create(self, vals: Dict[str, Any]) -> "ProductTemplateAttributeExclusion": ...
    def filtered(self, func: Any) -> "ProductTemplateAttributeExclusion": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductTemplateAttributeExclusion": ...
    def exists(self) -> "ProductTemplateAttributeExclusion": ...
    def sudo(self) -> "ProductTemplateAttributeExclusion": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductTemplateAttributeExclusion": ...

# --- product.template.attribute.line ---

class ProductTemplateAttributeLine(Recordset):
    active: bool
    attribute_id: "ProductAttribute"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    product_template_value_ids: "ProductTemplateAttributeValue"
    product_tmpl_id: "ProductTemplate"
    show_bit2publish_button: bool
    value_count: int
    value_ids: "ProductAttributeValue"
    def browse(self, ids: Union[int, List[int]]) -> "ProductTemplateAttributeLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductTemplateAttributeLine": ...
    def create(self, vals: Dict[str, Any]) -> "ProductTemplateAttributeLine": ...
    def filtered(self, func: Any) -> "ProductTemplateAttributeLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductTemplateAttributeLine": ...
    def exists(self) -> "ProductTemplateAttributeLine": ...
    def sudo(self) -> "ProductTemplateAttributeLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductTemplateAttributeLine": ...

# --- product.template.attribute.value ---

class ProductTemplateAttributeValue(Recordset):
    attribute_id: "ProductAttribute"
    attribute_line_id: "ProductTemplateAttributeLine"
    bit2publish_template_ids: "Bit2publishTemplate"
    color: int
    currency_id: "ResCurrency"
    display_type: str
    exclude_for: "ProductTemplateAttributeExclusion"
    has_bit2publish_template: bool
    html_color: str
    is_custom: bool
    name: str
    price_extra: float
    product_attribute_value_id: "ProductAttributeValue"
    product_tmpl_id: "ProductTemplate"
    ptav_active: bool
    ptav_product_variant_ids: "ProductProduct"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ProductTemplateAttributeValue": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ProductTemplateAttributeValue": ...
    def create(self, vals: Dict[str, Any]) -> "ProductTemplateAttributeValue": ...
    def filtered(self, func: Any) -> "ProductTemplateAttributeValue": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ProductTemplateAttributeValue": ...
    def exists(self) -> "ProductTemplateAttributeValue": ...
    def sudo(self) -> "ProductTemplateAttributeValue": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ProductTemplateAttributeValue": ...

# --- publisher_warranty.contract ---

class PublisherWarrantyContract(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "PublisherWarrantyContract": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "PublisherWarrantyContract": ...
    def create(self, vals: Dict[str, Any]) -> "PublisherWarrantyContract": ...
    def filtered(self, func: Any) -> "PublisherWarrantyContract": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "PublisherWarrantyContract": ...
    def exists(self) -> "PublisherWarrantyContract": ...
    def sudo(self) -> "PublisherWarrantyContract": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "PublisherWarrantyContract": ...

# --- rai.fee ---

class RaiFee(Recordset):
    active: bool
    attachment_ids: "IrAttachment"
    attachment_warning: str
    bit2publish_template_ids: "Bit2publishTemplate"
    error: str
    has_bit2publish_template: bool
    is_the_most_recent: bool
    last_processed_line: int
    line_ids: "RaiFeeLine"
    month: str
    name: str
    origin: str
    service_type: str
    show_bit2publish_button: bool
    state: str
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "RaiFee": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RaiFee": ...
    def create(self, vals: Dict[str, Any]) -> "RaiFee": ...
    def filtered(self, func: Any) -> "RaiFee": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RaiFee": ...
    def exists(self) -> "RaiFee": ...
    def sudo(self) -> "RaiFee": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RaiFee": ...

# --- rai.fee.line ---

class RaiFeeLine(Recordset):
    active: bool
    allowed_action: str
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    case_ids: "HelpdeskTicket"
    cf: str
    client_fiscal_code: str
    client_id: "ResPartner"
    cod_importo: str
    cod_istat: str
    cod_pod: str
    cod_prestazione: str
    data_fine: Optional[_dt.date]
    data_inizio: Optional[_dt.date]
    data_inizio_fornitura: Optional[_dt.date]
    display_data_fine: str
    display_data_inizio: str
    error: str
    has_bit2publish_template: bool
    id_addebito: str
    importo: float
    is_part_of_the_most_recent: bool
    month: str
    name: str
    pod_id: "ResPartnerPod"
    pod_tariff_code: str
    rai_fee_id: "RaiFee"
    service_type: str
    show_bit2publish_button: bool
    sii_report_admissibility: str
    sii_report_causal: str
    state: str
    tariffa: str
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "RaiFeeLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RaiFeeLine": ...
    def create(self, vals: Dict[str, Any]) -> "RaiFeeLine": ...
    def filtered(self, func: Any) -> "RaiFeeLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RaiFeeLine": ...
    def exists(self) -> "RaiFeeLine": ...
    def sudo(self) -> "RaiFeeLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RaiFeeLine": ...

# --- rai.fee.wizard ---

class RaiFeeWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    pod_id: "ResPartnerPod"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "RaiFeeWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RaiFeeWizard": ...
    def create(self, vals: Dict[str, Any]) -> "RaiFeeWizard": ...
    def filtered(self, func: Any) -> "RaiFeeWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RaiFeeWizard": ...
    def exists(self) -> "RaiFeeWizard": ...
    def sudo(self) -> "RaiFeeWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RaiFeeWizard": ...

# --- rating.mixin ---

class RatingMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    rating_avg: float
    rating_count: int
    rating_ids: "RatingRating"
    rating_last_feedback: str
    rating_last_image: bytes
    rating_last_value: float
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "RatingMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RatingMixin": ...
    def create(self, vals: Dict[str, Any]) -> "RatingMixin": ...
    def filtered(self, func: Any) -> "RatingMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RatingMixin": ...
    def exists(self) -> "RatingMixin": ...
    def sudo(self) -> "RatingMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RatingMixin": ...

# --- rating.parent.mixin ---

class RatingParentMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    rating_count: int
    rating_ids: "RatingRating"
    rating_percentage_satisfaction: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "RatingParentMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RatingParentMixin": ...
    def create(self, vals: Dict[str, Any]) -> "RatingParentMixin": ...
    def filtered(self, func: Any) -> "RatingParentMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RatingParentMixin": ...
    def exists(self) -> "RatingParentMixin": ...
    def sudo(self) -> "RatingParentMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RatingParentMixin": ...

# --- rating.rating ---

class RatingRating(Recordset):
    access_token: str
    bit2publish_template_ids: "Bit2publishTemplate"
    consumed: bool
    feedback: str
    has_bit2publish_template: bool
    is_internal: bool
    message_id: "MailMessage"
    parent_ref: Any
    parent_res_id: int
    parent_res_model: str
    parent_res_model_id: "IrModel"
    parent_res_name: str
    partner_id: "ResPartner"
    publisher_comment: str
    publisher_datetime: Optional[_dt.datetime]
    publisher_id: "ResPartner"
    rated_partner_id: "ResPartner"
    rated_partner_name: str
    rating: float
    rating_image: bytes
    rating_text: str
    res_id: int
    res_model: str
    res_model_id: "IrModel"
    res_name: str
    resource_ref: Any
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "RatingRating": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RatingRating": ...
    def create(self, vals: Dict[str, Any]) -> "RatingRating": ...
    def filtered(self, func: Any) -> "RatingRating": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RatingRating": ...
    def exists(self) -> "RatingRating": ...
    def sudo(self) -> "RatingRating": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RatingRating": ...

# --- refusal.reason ---

class RefusalReason(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    ticket_type_ids: "HelpdeskTicketType"
    def browse(self, ids: Union[int, List[int]]) -> "RefusalReason": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RefusalReason": ...
    def create(self, vals: Dict[str, Any]) -> "RefusalReason": ...
    def filtered(self, func: Any) -> "RefusalReason": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RefusalReason": ...
    def exists(self) -> "RefusalReason": ...
    def sudo(self) -> "RefusalReason": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RefusalReason": ...

# --- remi.table ---

class RemiTable(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    extraction_type: str
    has_bit2publish_template: bool
    remi_code: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "RemiTable": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RemiTable": ...
    def create(self, vals: Dict[str, Any]) -> "RemiTable": ...
    def filtered(self, func: Any) -> "RemiTable": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RemiTable": ...
    def exists(self) -> "RemiTable": ...
    def sudo(self) -> "RemiTable": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RemiTable": ...

# --- report.account.report_hash_integrity ---

class ReportAccountReportHashIntegrity(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportAccountReportHashIntegrity": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportAccountReportHashIntegrity": ...
    def create(self, vals: Dict[str, Any]) -> "ReportAccountReportHashIntegrity": ...
    def filtered(self, func: Any) -> "ReportAccountReportHashIntegrity": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportAccountReportHashIntegrity": ...
    def exists(self) -> "ReportAccountReportHashIntegrity": ...
    def sudo(self) -> "ReportAccountReportHashIntegrity": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportAccountReportHashIntegrity": ...

# --- report.account.report_invoice ---

class ReportAccountReportInvoice(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportAccountReportInvoice": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportAccountReportInvoice": ...
    def create(self, vals: Dict[str, Any]) -> "ReportAccountReportInvoice": ...
    def filtered(self, func: Any) -> "ReportAccountReportInvoice": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportAccountReportInvoice": ...
    def exists(self) -> "ReportAccountReportInvoice": ...
    def sudo(self) -> "ReportAccountReportInvoice": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportAccountReportInvoice": ...

# --- report.account.report_invoice_with_payments ---

class ReportAccountReportInvoiceWithPayments(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportAccountReportInvoiceWithPayments": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportAccountReportInvoiceWithPayments": ...
    def create(self, vals: Dict[str, Any]) -> "ReportAccountReportInvoiceWithPayments": ...
    def filtered(self, func: Any) -> "ReportAccountReportInvoiceWithPayments": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportAccountReportInvoiceWithPayments": ...
    def exists(self) -> "ReportAccountReportInvoiceWithPayments": ...
    def sudo(self) -> "ReportAccountReportInvoiceWithPayments": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportAccountReportInvoiceWithPayments": ...

# --- report.account.report_journal ---

class ReportAccountReportJournal(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportAccountReportJournal": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportAccountReportJournal": ...
    def create(self, vals: Dict[str, Any]) -> "ReportAccountReportJournal": ...
    def filtered(self, func: Any) -> "ReportAccountReportJournal": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportAccountReportJournal": ...
    def exists(self) -> "ReportAccountReportJournal": ...
    def sudo(self) -> "ReportAccountReportJournal": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportAccountReportJournal": ...

# --- report.base.report_irmodulereference ---

class ReportBaseReportIrmodulereference(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportBaseReportIrmodulereference": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportBaseReportIrmodulereference": ...
    def create(self, vals: Dict[str, Any]) -> "ReportBaseReportIrmodulereference": ...
    def filtered(self, func: Any) -> "ReportBaseReportIrmodulereference": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportBaseReportIrmodulereference": ...
    def exists(self) -> "ReportBaseReportIrmodulereference": ...
    def sudo(self) -> "ReportBaseReportIrmodulereference": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportBaseReportIrmodulereference": ...

# --- report.case.export_email ---

class ReportCaseExportEmail(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportCaseExportEmail": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportCaseExportEmail": ...
    def create(self, vals: Dict[str, Any]) -> "ReportCaseExportEmail": ...
    def filtered(self, func: Any) -> "ReportCaseExportEmail": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportCaseExportEmail": ...
    def exists(self) -> "ReportCaseExportEmail": ...
    def sudo(self) -> "ReportCaseExportEmail": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportCaseExportEmail": ...

# --- report.export_email ---

class ReportExportEmail(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportExportEmail": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportExportEmail": ...
    def create(self, vals: Dict[str, Any]) -> "ReportExportEmail": ...
    def filtered(self, func: Any) -> "ReportExportEmail": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportExportEmail": ...
    def exists(self) -> "ReportExportEmail": ...
    def sudo(self) -> "ReportExportEmail": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportExportEmail": ...

# --- report.interaction.export_email ---

class ReportInteractionExportEmail(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportInteractionExportEmail": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportInteractionExportEmail": ...
    def create(self, vals: Dict[str, Any]) -> "ReportInteractionExportEmail": ...
    def filtered(self, func: Any) -> "ReportInteractionExportEmail": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportInteractionExportEmail": ...
    def exists(self) -> "ReportInteractionExportEmail": ...
    def sudo(self) -> "ReportInteractionExportEmail": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportInteractionExportEmail": ...

# --- report.layout ---

class ReportLayout(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    image: str
    name: str
    pdf: str
    sequence: int
    show_bit2publish_button: bool
    view_id: "IrUiView"
    def browse(self, ids: Union[int, List[int]]) -> "ReportLayout": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportLayout": ...
    def create(self, vals: Dict[str, Any]) -> "ReportLayout": ...
    def filtered(self, func: Any) -> "ReportLayout": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportLayout": ...
    def exists(self) -> "ReportLayout": ...
    def sudo(self) -> "ReportLayout": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportLayout": ...

# --- report.paperformat ---

class ReportPaperformat(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    default: bool
    disable_shrinking: bool
    dpi: int
    format: str
    has_bit2publish_template: bool
    header_line: bool
    header_spacing: int
    margin_bottom: float
    margin_left: float
    margin_right: float
    margin_top: float
    name: str
    orientation: str
    page_height: int
    page_width: int
    print_page_height: float
    print_page_width: float
    report_ids: "IrActionsReport"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportPaperformat": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportPaperformat": ...
    def create(self, vals: Dict[str, Any]) -> "ReportPaperformat": ...
    def filtered(self, func: Any) -> "ReportPaperformat": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportPaperformat": ...
    def exists(self) -> "ReportPaperformat": ...
    def sudo(self) -> "ReportPaperformat": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportPaperformat": ...

# --- report.product.report_pricelist ---

class ReportProductReportPricelist(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportProductReportPricelist": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportProductReportPricelist": ...
    def create(self, vals: Dict[str, Any]) -> "ReportProductReportPricelist": ...
    def filtered(self, func: Any) -> "ReportProductReportPricelist": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportProductReportPricelist": ...
    def exists(self) -> "ReportProductReportPricelist": ...
    def sudo(self) -> "ReportProductReportPricelist": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportProductReportPricelist": ...

# --- report.product.report_producttemplatelabel ---

class ReportProductReportProducttemplatelabel(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportProductReportProducttemplatelabel": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportProductReportProducttemplatelabel": ...
    def create(self, vals: Dict[str, Any]) -> "ReportProductReportProducttemplatelabel": ...
    def filtered(self, func: Any) -> "ReportProductReportProducttemplatelabel": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportProductReportProducttemplatelabel": ...
    def exists(self) -> "ReportProductReportProducttemplatelabel": ...
    def sudo(self) -> "ReportProductReportProducttemplatelabel": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportProductReportProducttemplatelabel": ...

# --- report.product.report_producttemplatelabel_dymo ---

class ReportProductReportProducttemplatelabelDymo(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportProductReportProducttemplatelabelDymo": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportProductReportProducttemplatelabelDymo": ...
    def create(self, vals: Dict[str, Any]) -> "ReportProductReportProducttemplatelabelDymo": ...
    def filtered(self, func: Any) -> "ReportProductReportProducttemplatelabelDymo": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportProductReportProducttemplatelabelDymo": ...
    def exists(self) -> "ReportProductReportProducttemplatelabelDymo": ...
    def sudo(self) -> "ReportProductReportProducttemplatelabelDymo": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportProductReportProducttemplatelabelDymo": ...

# --- report.rep_agents ---

class ReportRepAgents(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportRepAgents": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportRepAgents": ...
    def create(self, vals: Dict[str, Any]) -> "ReportRepAgents": ...
    def filtered(self, func: Any) -> "ReportRepAgents": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportRepAgents": ...
    def exists(self) -> "ReportRepAgents": ...
    def sudo(self) -> "ReportRepAgents": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportRepAgents": ...

# --- report.rep_jolly_error_lines ---

class ReportRepJollyErrorLines(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportRepJollyErrorLines": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportRepJollyErrorLines": ...
    def create(self, vals: Dict[str, Any]) -> "ReportRepJollyErrorLines": ...
    def filtered(self, func: Any) -> "ReportRepJollyErrorLines": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportRepJollyErrorLines": ...
    def exists(self) -> "ReportRepJollyErrorLines": ...
    def sudo(self) -> "ReportRepJollyErrorLines": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportRepJollyErrorLines": ...

# --- report.report_csv.abstract ---

class ReportReportCsvAbstract(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportReportCsvAbstract": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportReportCsvAbstract": ...
    def create(self, vals: Dict[str, Any]) -> "ReportReportCsvAbstract": ...
    def filtered(self, func: Any) -> "ReportReportCsvAbstract": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportReportCsvAbstract": ...
    def exists(self) -> "ReportReportCsvAbstract": ...
    def sudo(self) -> "ReportReportCsvAbstract": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportReportCsvAbstract": ...

# --- report.report_csv.partner_csv ---

class ReportReportCsvPartnerCsv(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportReportCsvPartnerCsv": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportReportCsvPartnerCsv": ...
    def create(self, vals: Dict[str, Any]) -> "ReportReportCsvPartnerCsv": ...
    def filtered(self, func: Any) -> "ReportReportCsvPartnerCsv": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportReportCsvPartnerCsv": ...
    def exists(self) -> "ReportReportCsvPartnerCsv": ...
    def sudo(self) -> "ReportReportCsvPartnerCsv": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportReportCsvPartnerCsv": ...

# --- report.report_xlsx.abstract ---

class ReportReportXlsxAbstract(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportReportXlsxAbstract": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportReportXlsxAbstract": ...
    def create(self, vals: Dict[str, Any]) -> "ReportReportXlsxAbstract": ...
    def filtered(self, func: Any) -> "ReportReportXlsxAbstract": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportReportXlsxAbstract": ...
    def exists(self) -> "ReportReportXlsxAbstract": ...
    def sudo(self) -> "ReportReportXlsxAbstract": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportReportXlsxAbstract": ...

# --- report.report_xlsx.partner_xlsx ---

class ReportReportXlsxPartnerXlsx(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportReportXlsxPartnerXlsx": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportReportXlsxPartnerXlsx": ...
    def create(self, vals: Dict[str, Any]) -> "ReportReportXlsxPartnerXlsx": ...
    def filtered(self, func: Any) -> "ReportReportXlsxPartnerXlsx": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportReportXlsxPartnerXlsx": ...
    def exists(self) -> "ReportReportXlsxPartnerXlsx": ...
    def sudo(self) -> "ReportReportXlsxPartnerXlsx": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportReportXlsxPartnerXlsx": ...

# --- report.report_xml.abstract ---

class ReportReportXmlAbstract(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportReportXmlAbstract": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportReportXmlAbstract": ...
    def create(self, vals: Dict[str, Any]) -> "ReportReportXmlAbstract": ...
    def filtered(self, func: Any) -> "ReportReportXmlAbstract": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportReportXmlAbstract": ...
    def exists(self) -> "ReportReportXmlAbstract": ...
    def sudo(self) -> "ReportReportXmlAbstract": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportReportXmlAbstract": ...

# --- report.sorgenia_dati_catastali.ade_report_template_txt ---

class ReportSorgeniaDatiCatastaliAdeReportTemplateTxt(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaDatiCatastaliAdeReportTemplateTxt": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaDatiCatastaliAdeReportTemplateTxt": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaDatiCatastaliAdeReportTemplateTxt": ...
    def filtered(self, func: Any) -> "ReportSorgeniaDatiCatastaliAdeReportTemplateTxt": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaDatiCatastaliAdeReportTemplateTxt": ...
    def exists(self) -> "ReportSorgeniaDatiCatastaliAdeReportTemplateTxt": ...
    def sudo(self) -> "ReportSorgeniaDatiCatastaliAdeReportTemplateTxt": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaDatiCatastaliAdeReportTemplateTxt": ...

# --- report.sorgenia_refunder.rep_error_line ---

class ReportSorgeniaRefunderRepErrorLine(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaRefunderRepErrorLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaRefunderRepErrorLine": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaRefunderRepErrorLine": ...
    def filtered(self, func: Any) -> "ReportSorgeniaRefunderRepErrorLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaRefunderRepErrorLine": ...
    def exists(self) -> "ReportSorgeniaRefunderRepErrorLine": ...
    def sudo(self) -> "ReportSorgeniaRefunderRepErrorLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaRefunderRepErrorLine": ...

# --- report.sorgenia_refunder.rep_refunds_by_sorgenia ---

class ReportSorgeniaRefunderRepRefundsBySorgenia(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaRefunderRepRefundsBySorgenia": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaRefunderRepRefundsBySorgenia": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaRefunderRepRefundsBySorgenia": ...
    def filtered(self, func: Any) -> "ReportSorgeniaRefunderRepRefundsBySorgenia": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaRefunderRepRefundsBySorgenia": ...
    def exists(self) -> "ReportSorgeniaRefunderRepRefundsBySorgenia": ...
    def sudo(self) -> "ReportSorgeniaRefunderRepRefundsBySorgenia": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaRefunderRepRefundsBySorgenia": ...

# --- report.sorgenia_report.rep_gdpr ---

class ReportSorgeniaReportRepGdpr(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaReportRepGdpr": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaReportRepGdpr": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaReportRepGdpr": ...
    def filtered(self, func: Any) -> "ReportSorgeniaReportRepGdpr": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaReportRepGdpr": ...
    def exists(self) -> "ReportSorgeniaReportRepGdpr": ...
    def sudo(self) -> "ReportSorgeniaReportRepGdpr": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaReportRepGdpr": ...

# --- report.sorgenia_report.rep_ps_003 ---

class ReportSorgeniaReportRepPs003(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaReportRepPs003": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaReportRepPs003": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaReportRepPs003": ...
    def filtered(self, func: Any) -> "ReportSorgeniaReportRepPs003": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaReportRepPs003": ...
    def exists(self) -> "ReportSorgeniaReportRepPs003": ...
    def sudo(self) -> "ReportSorgeniaReportRepPs003": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaReportRepPs003": ...

# --- report.sorgenia_report.rep_ps_058 ---

class ReportSorgeniaReportRepPs058(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaReportRepPs058": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaReportRepPs058": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaReportRepPs058": ...
    def filtered(self, func: Any) -> "ReportSorgeniaReportRepPs058": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaReportRepPs058": ...
    def exists(self) -> "ReportSorgeniaReportRepPs058": ...
    def sudo(self) -> "ReportSorgeniaReportRepPs058": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaReportRepPs058": ...

# --- report.sorgenia_report.rep_ps_058_interaction ---

class ReportSorgeniaReportRepPs058Interaction(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaReportRepPs058Interaction": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaReportRepPs058Interaction": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaReportRepPs058Interaction": ...
    def filtered(self, func: Any) -> "ReportSorgeniaReportRepPs058Interaction": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaReportRepPs058Interaction": ...
    def exists(self) -> "ReportSorgeniaReportRepPs058Interaction": ...
    def sudo(self) -> "ReportSorgeniaReportRepPs058Interaction": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaReportRepPs058Interaction": ...

# --- report.sorgenia_report.rep_ps_059 ---

class ReportSorgeniaReportRepPs059(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaReportRepPs059": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaReportRepPs059": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaReportRepPs059": ...
    def filtered(self, func: Any) -> "ReportSorgeniaReportRepPs059": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaReportRepPs059": ...
    def exists(self) -> "ReportSorgeniaReportRepPs059": ...
    def sudo(self) -> "ReportSorgeniaReportRepPs059": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaReportRepPs059": ...

# --- report.sorgenia_report.rep_ps_085 ---

class ReportSorgeniaReportRepPs085(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaReportRepPs085": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaReportRepPs085": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaReportRepPs085": ...
    def filtered(self, func: Any) -> "ReportSorgeniaReportRepPs085": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaReportRepPs085": ...
    def exists(self) -> "ReportSorgeniaReportRepPs085": ...
    def sudo(self) -> "ReportSorgeniaReportRepPs085": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaReportRepPs085": ...

# --- report.sorgenia_report.rep_refund ---

class ReportSorgeniaReportRepRefund(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaReportRepRefund": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaReportRepRefund": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaReportRepRefund": ...
    def filtered(self, func: Any) -> "ReportSorgeniaReportRepRefund": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaReportRepRefund": ...
    def exists(self) -> "ReportSorgeniaReportRepRefund": ...
    def sudo(self) -> "ReportSorgeniaReportRepRefund": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaReportRepRefund": ...

# --- report.sorgenia_report.rep_refund_error_revision ---

class ReportSorgeniaReportRepRefundErrorRevision(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaReportRepRefundErrorRevision": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaReportRepRefundErrorRevision": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaReportRepRefundErrorRevision": ...
    def filtered(self, func: Any) -> "ReportSorgeniaReportRepRefundErrorRevision": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaReportRepRefundErrorRevision": ...
    def exists(self) -> "ReportSorgeniaReportRepRefundErrorRevision": ...
    def sudo(self) -> "ReportSorgeniaReportRepRefundErrorRevision": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaReportRepRefundErrorRevision": ...

# --- report.sorgenia_report.rep_tiqv ---

class ReportSorgeniaReportRepTiqv(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaReportRepTiqv": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaReportRepTiqv": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaReportRepTiqv": ...
    def filtered(self, func: Any) -> "ReportSorgeniaReportRepTiqv": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaReportRepTiqv": ...
    def exists(self) -> "ReportSorgeniaReportRepTiqv": ...
    def sudo(self) -> "ReportSorgeniaReportRepTiqv": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaReportRepTiqv": ...

# --- report.sorgenia_report.rep_upsa ---

class ReportSorgeniaReportRepUpsa(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ReportSorgeniaReportRepUpsa": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ReportSorgeniaReportRepUpsa": ...
    def create(self, vals: Dict[str, Any]) -> "ReportSorgeniaReportRepUpsa": ...
    def filtered(self, func: Any) -> "ReportSorgeniaReportRepUpsa": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ReportSorgeniaReportRepUpsa": ...
    def exists(self) -> "ReportSorgeniaReportRepUpsa": ...
    def sudo(self) -> "ReportSorgeniaReportRepUpsa": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ReportSorgeniaReportRepUpsa": ...

# --- res.bank ---

class ResBank(Recordset):
    active: bool
    bic: str
    bit2publish_template_ids: "Bit2publishTemplate"
    city: str
    country: "ResCountry"
    email: str
    has_bit2publish_template: bool
    name: str
    phone: str
    show_bit2publish_button: bool
    state: "ResCountryState"
    street: str
    street2: str
    zip: str
    def browse(self, ids: Union[int, List[int]]) -> "ResBank": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResBank": ...
    def create(self, vals: Dict[str, Any]) -> "ResBank": ...
    def filtered(self, func: Any) -> "ResBank": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResBank": ...
    def exists(self) -> "ResBank": ...
    def sudo(self) -> "ResBank": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResBank": ...

# --- res.city ---

class ResCity(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    cadastral_code: str
    country_id: "ResCountry"
    has_bit2publish_template: bool
    istat_code: str
    name: str
    show_bit2publish_button: bool
    state_id: "ResCountryState"
    zipcode: str
    zip_ids: "ResCityZip"
    def browse(self, ids: Union[int, List[int]]) -> "ResCity": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResCity": ...
    def create(self, vals: Dict[str, Any]) -> "ResCity": ...
    def filtered(self, func: Any) -> "ResCity": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResCity": ...
    def exists(self) -> "ResCity": ...
    def sudo(self) -> "ResCity": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResCity": ...

# --- res.city.istat ---

class ResCityIstat(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    city_id: "ResCity"
    country_id: "ResCountry"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    state_id: "ResCountryState"
    def browse(self, ids: Union[int, List[int]]) -> "ResCityIstat": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResCityIstat": ...
    def create(self, vals: Dict[str, Any]) -> "ResCityIstat": ...
    def filtered(self, func: Any) -> "ResCityIstat": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResCityIstat": ...
    def exists(self) -> "ResCityIstat": ...
    def sudo(self) -> "ResCityIstat": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResCityIstat": ...

# --- res.city.zip ---

class ResCityZip(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    city_id: "ResCity"
    country_id: "ResCountry"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    state_id: "ResCountryState"
    def browse(self, ids: Union[int, List[int]]) -> "ResCityZip": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResCityZip": ...
    def create(self, vals: Dict[str, Any]) -> "ResCityZip": ...
    def filtered(self, func: Any) -> "ResCityZip": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResCityZip": ...
    def exists(self) -> "ResCityZip": ...
    def sudo(self) -> "ResCityZip": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResCityZip": ...

# --- res.company ---

class ResCompany(Recordset):
    account_cash_basis_base_account_id: "AccountAccount"
    account_check_printing_date_label: bool
    account_check_printing_layout: str
    account_check_printing_margin_left: float
    account_check_printing_margin_right: float
    account_check_printing_margin_top: float
    account_check_printing_multi_stub: bool
    account_dashboard_onboarding_state: str
    account_default_pos_receivable_account_id: "AccountAccount"
    account_enabled_tax_country_ids: "ResCountry"
    account_fiscal_country_id: "ResCountry"
    account_invoice_onboarding_state: str
    account_journal_payment_credit_account_id: "AccountAccount"
    account_journal_payment_debit_account_id: "AccountAccount"
    account_journal_suspense_account_id: "AccountAccount"
    account_onboarding_create_invoice_state: str
    account_onboarding_invoice_layout_state: str
    account_onboarding_sale_tax_state: str
    account_opening_date: Optional[_dt.date]
    account_opening_journal_id: "AccountJournal"
    account_opening_move_id: "AccountMove"
    account_purchase_tax_id: "AccountTax"
    account_sale_tax_id: "AccountTax"
    account_setup_bank_data_state: str
    account_setup_bill_state: str
    account_setup_coa_state: str
    account_setup_fy_data_state: str
    account_setup_taxes_state: str
    agcom_contact_id: "ResPartner"
    anglo_saxon_accounting: bool
    anonymous_client_id: "ResPartner"
    anonymous_contact_id: "ResPartner"
    au_contact_id: "ResPartner"
    auto_compute_members_from_roles: bool
    automatic_entry_default_journal_id: "AccountJournal"
    background_image: bytes
    bank_account_code_prefix: str
    bank_ids: "ResPartnerBank"
    bank_journal_ids: "AccountJournal"
    bank_slip_payment_method_id: "PaymentMethod"
    base_onboarding_company_state: str
    bit2publish_api_token: str
    bit2publish_api_url: str
    bit2publish_template_ids: "Bit2publishTemplate"
    bottom_image_mail: bytes
    bottom_image_mail_id: int
    cash_account_code_prefix: str
    catchall_email: str
    catchall_formatted: str
    chart_template_id: "AccountChartTemplate"
    child_ids: "ResCompany"
    city: str
    city_id: "ResCity"
    company_details: str
    company_registry: str
    country_code: str
    country_enforce_cities: bool
    country_id: "ResCountry"
    crm_contact_id: "ResPartner"
    currency_exchange_journal_id: "AccountJournal"
    currency_id: "ResCurrency"
    currency_interval_unit: str
    currency_next_execution_date: Optional[_dt.date]
    currency_provider: str
    default_cash_difference_expense_account_id: "AccountAccount"
    default_cash_difference_income_account_id: "AccountAccount"
    documents_product_settings: bool
    documents_spreadsheet_folder_id: "DocumentsFolder"
    email: str
    email_formatted: str
    expects_chart_of_accounts: bool
    expense_accrual_account_id: "AccountAccount"
    expense_currency_exchange_account_id: "AccountAccount"
    external_report_layout_id: "IrUiView"
    extract_show_ocr_option_selection: str
    extract_single_line_per_tax: bool
    favicon: bytes
    fiber_re_examination_days: int
    fiscal_position_ids: "AccountFiscalPosition"
    fiscalyear_last_day: int
    fiscalyear_last_month: str
    fiscalyear_lock_date: Optional[_dt.date]
    font: str
    generate_interaction_from_mail_in: bool
    generate_interaction_from_mail_out: bool
    has_bit2publish_template: bool
    iap_enrich_auto_done: bool
    income_currency_exchange_account_id: "AccountAccount"
    incoterm_id: "AccountIncoterms"
    interaction_from_mail_in_channel_id: "InteractionChannel"
    interaction_from_mail_out_channel_id: "InteractionChannel"
    invoice_is_email: bool
    invoice_is_print: bool
    invoice_is_snailmail: bool
    invoice_terms: str
    invoice_terms_html: str
    is_mail_persistence_forced: bool
    judicial_authority_contact_id: "ResPartner"
    layout_background: str
    layout_background_image: bytes
    logo: bytes
    logo_web: bytes
    m2c_contact_id: "ResPartner"
    mdm_contact_id: "ResPartner"
    mobile: str
    multi_vat_foreign_country_ids: "ResCountry"
    name: str
    olo2olo_contact_id: "ResPartner"
    olo_referent_fiber_id: "ResPartner"
    olo_referent_support_fiber_id: "ResPartner"
    paperformat_id: "ReportPaperformat"
    parent_id: "ResCompany"
    partner_gid: int
    partner_id: "ResPartner"
    payment_acquirer_onboarding_state: str
    payment_onboarding_payment_method: str
    period_lock_date: Optional[_dt.date]
    phone: str
    pratica_gestita_activation: str
    primary_color: str
    product_folder: "DocumentsFolder"
    product_tags: "DocumentsTag"
    property_stock_account_input_categ_id: "AccountAccount"
    property_stock_account_output_categ_id: "AccountAccount"
    property_stock_valuation_account_id: "AccountAccount"
    qr_code: bool
    refunds_doxee_receiver_email: str
    refunds_report_receiver_email: str
    report_footer: str
    report_header: str
    resource_calendar_id: "ResourceCalendar"
    resource_calendar_ids: "ResourceCalendar"
    res_partner_fiscal_code_blank_goes_null: bool
    res_partner_strip_phone_number_spaces: bool
    res_partner_upper_fiscal_code: bool
    res_partner_vat_blank_goes_null: bool
    revenue_accrual_account_id: "AccountAccount"
    secondary_color: str
    selected_calendar_id: "ResourceCalendar"
    sequence: int
    service_name: str
    show_bit2publish_button: bool
    sii_contact_id: "ResPartner"
    snailmail_color: bool
    snailmail_cover: bool
    snailmail_duplex: bool
    social_facebook: str
    social_github: str
    social_instagram: str
    social_linkedin: str
    social_twitter: str
    social_youtube: str
    state_id: "ResCountryState"
    street: str
    street2: str
    system_helpdesk_team: "HelpdeskTeam"
    tax_calculation_rounding_method: str
    tax_cash_basis_journal_id: "AccountJournal"
    tax_exigibility: bool
    tax_lock_date: Optional[_dt.date]
    terms_type: str
    tiqv_workflow_id: "SympleWorkflow"
    transfer_account_code_prefix: str
    transfer_account_id: "AccountAccount"
    transfer_payment_method_id: "PaymentMethod"
    unexecuted_contact_id: "ResPartner"
    user_ids: "ResUsers"
    vat: str
    vat_check_vies: bool
    website: str
    zip: str
    zip_id: "ResCityZip"
    def browse(self, ids: Union[int, List[int]]) -> "ResCompany": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResCompany": ...
    def create(self, vals: Dict[str, Any]) -> "ResCompany": ...
    def filtered(self, func: Any) -> "ResCompany": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResCompany": ...
    def exists(self) -> "ResCompany": ...
    def sudo(self) -> "ResCompany": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResCompany": ...

# --- res.config ---

class ResConfig(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResConfig": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResConfig": ...
    def create(self, vals: Dict[str, Any]) -> "ResConfig": ...
    def filtered(self, func: Any) -> "ResConfig": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResConfig": ...
    def exists(self) -> "ResConfig": ...
    def sudo(self) -> "ResConfig": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResConfig": ...

# --- res.config.installer ---

class ResConfigInstaller(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResConfigInstaller": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResConfigInstaller": ...
    def create(self, vals: Dict[str, Any]) -> "ResConfigInstaller": ...
    def filtered(self, func: Any) -> "ResConfigInstaller": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResConfigInstaller": ...
    def exists(self) -> "ResConfigInstaller": ...
    def sudo(self) -> "ResConfigInstaller": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResConfigInstaller": ...

# --- res.config.settings ---

class ResConfigSettings(Recordset):
    accept_only_not_prepaid_card: bool
    account_cash_basis_base_account_id: "AccountAccount"
    account_check_printing_date_label: bool
    account_check_printing_layout: str
    account_check_printing_margin_left: float
    account_check_printing_margin_right: float
    account_check_printing_margin_top: float
    account_check_printing_multi_stub: bool
    account_fiscal_country_id: "ResCountry"
    account_journal_payment_credit_account_id: "AccountAccount"
    account_journal_payment_debit_account_id: "AccountAccount"
    account_journal_suspense_account_id: "AccountAccount"
    active_user_count: int
    agcom_contact_id: "ResPartner"
    alias_domain: str
    allow_only_sepa_iban: bool
    allow_saml_uid_and_internal_password: bool
    allow_sla_ids_block_on_chils_tickets: bool
    anonymous_client_id: "ResPartner"
    anonymous_contact_id: "ResPartner"
    au_contact_id: "ResPartner"
    auth_signup_reset_password: bool
    auth_signup_template_user_id: "ResUsers"
    auth_signup_uninvited: str
    auto_compute_members_from_roles: bool
    b2w_client_id: str
    b2w_client_secret: str
    b2w_realm: str
    b2w_server_login: str
    b2w_service_account_password: str
    b2w_service_account_username: str
    bank_slip_payment_method_id: "PaymentMethod"
    bit2publish_api_token: str
    bit2publish_api_url: str
    bit2publish_template_ids: "Bit2publishTemplate"
    chart_template_id: "AccountChartTemplate"
    company_count: int
    company_id: "ResCompany"
    company_informations: str
    company_name: str
    country_code: str
    crm_contact_id: "ResPartner"
    currency_exchange_journal_id: "AccountJournal"
    currency_id: "ResCurrency"
    currency_interval_unit: str
    currency_next_execution_date: Optional[_dt.date]
    currency_provider: str
    digest_emails: bool
    digest_id: "DigestDigest"
    disable_redirect_firebase_dynamic_link: bool
    documents_product_settings: bool
    documents_spreadsheet_folder_id: "DocumentsFolder"
    enable_ocn: bool
    expense_currency_exchange_account_id: "AccountAccount"
    external_email_server_default: bool
    external_report_layout_id: "IrUiView"
    extract_show_ocr_option_selection: str
    extract_single_line_per_tax: bool
    fail_counter: int
    fiber_re_examination_days: int
    generate_interaction_from_mail_in: bool
    generate_interaction_from_mail_out: bool
    google_gmail_client_identifier: str
    google_gmail_client_secret: str
    group_analytic_accounting: bool
    group_analytic_tags: bool
    group_cash_rounding: bool
    group_discount_per_so_line: bool
    group_mass_mailing_campaign: bool
    group_multi_currency: bool
    group_product_pricelist: bool
    group_product_variant: bool
    group_sale_pricelist: bool
    group_show_line_subtotals_tax_excluded: bool
    group_show_line_subtotals_tax_included: bool
    group_show_purchase_receipts: bool
    group_show_sale_receipts: bool
    group_stock_packaging: bool
    group_uom: bool
    group_warning_account: bool
    has_accounting_entries: bool
    has_bit2publish_template: bool
    has_chart_of_accounts: bool
    imperex_allowed_models: str
    imperex_default_format: str
    imperex_enabled: bool
    imperex_max_depth: int
    imperex_system_manifest_id: "ImperexManifestProfile"
    income_currency_exchange_account_id: "AccountAccount"
    incoterm_id: "AccountIncoterms"
    interaction_from_mail_in_channel_id: "InteractionChannel"
    interaction_from_mail_out_channel_id: "InteractionChannel"
    invoice_is_email: bool
    invoice_is_print: bool
    invoice_is_snailmail: bool
    invoice_terms: str
    invoice_terms_html: str
    is_mail_persistence_forced: bool
    judicial_authority_contact_id: "ResPartner"
    language_count: int
    m2c_contact_id: "ResPartner"
    map_box_token: str
    mass_mailing_mail_server_id: "IrMailServer"
    mass_mailing_outgoing_mail_server: bool
    mdm_contact_id: "ResPartner"
    microsoft_outlook_client_identifier: str
    microsoft_outlook_client_secret: str
    module_account_accountant: bool
    module_account_bank_statement_import_camt: bool
    module_account_bank_statement_import_csv: bool
    module_account_bank_statement_import_ofx: bool
    module_account_bank_statement_import_qif: bool
    module_account_batch_payment: bool
    module_account_budget: bool
    module_account_check_printing: bool
    module_account_inter_company_rules: bool
    module_account_intrastat: bool
    module_account_invoice_extract: bool
    module_account_payment: bool
    module_account_reports: bool
    module_account_sepa: bool
    module_account_sepa_direct_debit: bool
    module_account_taxcloud: bool
    module_auth_ldap: bool
    module_auth_oauth: bool
    module_base_gengo: bool
    module_base_geolocalize: bool
    module_base_import: bool
    module_currency_rate_live: bool
    module_google_calendar: bool
    module_google_drive: bool
    module_google_recaptcha: bool
    module_google_spreadsheet: bool
    module_l10n_eu_oss: bool
    module_l10n_fr_fec_import: bool
    module_mail_plugin: bool
    module_microsoft_calendar: bool
    module_pad: bool
    module_partner_autocomplete: bool
    module_product_images: bool
    module_product_margin: bool
    module_sale_product_configurator: bool
    module_sale_product_matrix: bool
    module_snailmail_account: bool
    module_symphonie_interaction: bool
    module_symphonie_interaction_case: bool
    module_symphonie_interaction_case_mail: bool
    module_symphonie_interaction_mail: bool
    module_symphonie_mail: bool
    module_symphonie_mail_fetchmail: bool
    module_symphonie_mail_import_mail_mail: bool
    module_symple_ai_tag: bool
    module_voip: bool
    module_web_unsplash: bool
    olo2olo_contact_id: "ResPartner"
    olo_referent_fiber_id: "ResPartner"
    olo_referent_support_fiber_id: "ResPartner"
    partner_autocomplete_insufficient_credit: bool
    partner_names_order: str
    partner_names_order_changed: bool
    physical_bonus_cutoff_date: str
    portal_allow_api_keys: bool
    pratica_gestita_activation: str
    preview_ready: bool
    product_folder: "DocumentsFolder"
    product_pricelist_setting: str
    products_to_exclude: str
    product_tags: "DocumentsTag"
    product_volume_volume_in_cubic_feet: str
    product_weight_in_lbs: str
    profiling_enabled_until: Optional[_dt.datetime]
    purchase_tax_id: "AccountTax"
    qr_code: bool
    refunds_doxee_receiver_email: str
    refunds_report_receiver_email: str
    report_footer: str
    res_partner_fiscal_code_blank_goes_null: bool
    res_partner_strip_phone_number_spaces: bool
    res_partner_upper_fiscal_code: bool
    res_partner_vat_blank_goes_null: bool
    restrict_template_rendering: bool
    rip_enabled: bool
    rip_force_empty_string_to: str
    rip_get_compact_response: bool
    rip_get_compact_response_one_rec: bool
    rip_get_compact_response_rec_not_found: bool
    rip_get_not_found: str
    rip_notes: str
    rip_post_compact_response: bool
    rip_post_compact_response_one_rec: bool
    rip_post_compact_response_rec_not_found: bool
    rip_post_not_found: str
    rip_request_log: bool
    rip_request_log_max_length: int
    rip_response_layout: str
    rip_token_handler: "RipTokenHandler"
    sale_tax_id: "AccountTax"
    selected_calendar_id: "ResourceCalendar"
    service_name: str
    show_bit2publish_button: bool
    show_blacklist_buttons: bool
    show_effect: bool
    show_line_subtotals_tax_selection: str
    sii_contact_id: "ResPartner"
    snailmail_color: bool
    snailmail_cover: bool
    snailmail_duplex: bool
    social_bonus_notification_days: int
    social_bonus_sla_expiration_days: int
    sorgenia_cti_new_tab_on_call: bool
    sorgenia_cti_show_alert_on_call: bool
    sorgenia_cti_show_chat_on_call: bool
    sorgenia_mdm_fields_whitelist: str
    sorgenia_mdm_sync_code: str
    sorgenia_mdm_sync_enabled: bool
    sorgenia_mdm_sync_max_retries: int
    sorgenia_mdm_sync_save_on_error: bool
    sorgenia_mdm_sync_timeout: int
    sorgenia_mdm_sync_url: str
    sorgenia_mdm_sync_url_create: str
    sorgenia_postalizer_chars_to_purge: str
    sorgenia_postalizer_enabled: bool
    sorgenia_postalizer_password: str
    sorgenia_postalizer_url: str
    sorgenia_postalizer_username: str
    symple_pb_b2w_backend_url: str
    symple_pb_b2w_base_element: str
    symple_pb_b2w_body_slideout_menu: str
    symple_pb_b2w_cdn_url: str
    symple_pb_b2w_css_slideout_menu: str
    symple_pb_b2w_js_process_builder: str
    symple_pb_b2w_js_slideout_menu: str
    symple_pb_b2w_js_system: str
    symple_pb_b2w_js_webcomponent: str
    symple_rcu_market_types: str
    system_helpdesk_team: "HelpdeskTeam"
    tax_calculation_rounding_method: str
    tax_cash_basis_journal_id: "AccountJournal"
    tax_exigibility: bool
    terms_type: str
    tiqv_workflow_id: "SympleWorkflow"
    transfer_account_id: "AccountAccount"
    transfer_payment_method_id: "PaymentMethod"
    twilio_account_sid: str
    twilio_account_token: str
    unexecuted_contact_id: "ResPartner"
    unsplash_access_key: str
    use_internal_SLA: bool
    use_invoice_terms: bool
    use_official_SLA: bool
    user_default_rights: bool
    use_twilio_rtc_servers: bool
    vat_check_vies: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResConfigSettings": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResConfigSettings": ...
    def create(self, vals: Dict[str, Any]) -> "ResConfigSettings": ...
    def filtered(self, func: Any) -> "ResConfigSettings": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResConfigSettings": ...
    def exists(self) -> "ResConfigSettings": ...
    def sudo(self) -> "ResConfigSettings": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResConfigSettings": ...

# --- res.country ---

class ResCountry(Recordset):
    address_format: str
    address_view_id: "IrUiView"
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    country_group_ids: "ResCountryGroup"
    currency_id: "ResCurrency"
    enforce_cities: bool
    geonames_state_code_column: int
    geonames_state_name_column: int
    has_bit2publish_template: bool
    image_url: str
    is_visibile_via_api: bool
    name: str
    name_position: str
    phone_code: int
    show_bit2publish_button: bool
    state_ids: "ResCountryState"
    state_level: int
    state_required: bool
    vat_label: str
    zip_required: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResCountry": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResCountry": ...
    def create(self, vals: Dict[str, Any]) -> "ResCountry": ...
    def filtered(self, func: Any) -> "ResCountry": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResCountry": ...
    def exists(self) -> "ResCountry": ...
    def sudo(self) -> "ResCountry": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResCountry": ...

# --- res.country.group ---

class ResCountryGroup(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    country_ids: "ResCountry"
    has_bit2publish_template: bool
    name: str
    pricelist_ids: "ProductPricelist"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResCountryGroup": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResCountryGroup": ...
    def create(self, vals: Dict[str, Any]) -> "ResCountryGroup": ...
    def filtered(self, func: Any) -> "ResCountryGroup": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResCountryGroup": ...
    def exists(self) -> "ResCountryGroup": ...
    def sudo(self) -> "ResCountryGroup": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResCountryGroup": ...

# --- res.country.state ---

class ResCountryState(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    country_id: "ResCountry"
    has_bit2publish_template: bool
    name: str
    nielsen_region: str
    region: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResCountryState": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResCountryState": ...
    def create(self, vals: Dict[str, Any]) -> "ResCountryState": ...
    def filtered(self, func: Any) -> "ResCountryState": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResCountryState": ...
    def exists(self) -> "ResCountryState": ...
    def sudo(self) -> "ResCountryState": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResCountryState": ...

# --- res.currency ---

class ResCurrency(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    currency_subunit_label: str
    currency_unit_label: str
    date: Optional[_dt.date]
    decimal_places: int
    display_rounding_warning: bool
    full_name: str
    has_bit2publish_template: bool
    inverse_rate: float
    is_current_company_currency: bool
    name: str
    position: str
    rate: float
    rate_ids: "ResCurrencyRate"
    rate_string: str
    rounding: float
    show_bit2publish_button: bool
    symbol: str
    def browse(self, ids: Union[int, List[int]]) -> "ResCurrency": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResCurrency": ...
    def create(self, vals: Dict[str, Any]) -> "ResCurrency": ...
    def filtered(self, func: Any) -> "ResCurrency": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResCurrency": ...
    def exists(self) -> "ResCurrency": ...
    def sudo(self) -> "ResCurrency": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResCurrency": ...

# --- res.currency.rate ---

class ResCurrencyRate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    company_rate: float
    currency_id: "ResCurrency"
    has_bit2publish_template: bool
    inverse_company_rate: float
    name: Optional[_dt.date]
    rate: float
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResCurrencyRate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResCurrencyRate": ...
    def create(self, vals: Dict[str, Any]) -> "ResCurrencyRate": ...
    def filtered(self, func: Any) -> "ResCurrencyRate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResCurrencyRate": ...
    def exists(self) -> "ResCurrencyRate": ...
    def sudo(self) -> "ResCurrencyRate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResCurrencyRate": ...

# --- res.groups ---

class ResGroups(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    category_id: "IrModuleCategory"
    color: int
    comment: str
    full_name: str
    has_bit2publish_template: bool
    implied_ids: "ResGroups"
    menu_access: "IrUiMenu"
    model_access: "IrModelAccess"
    name: str
    rule_groups: "IrRule"
    share: bool
    show_bit2publish_button: bool
    trans_implied_ids: "ResGroups"
    users: "ResUsers"
    view_access: "IrUiView"
    def browse(self, ids: Union[int, List[int]]) -> "ResGroups": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResGroups": ...
    def create(self, vals: Dict[str, Any]) -> "ResGroups": ...
    def filtered(self, func: Any) -> "ResGroups": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResGroups": ...
    def exists(self) -> "ResGroups": ...
    def sudo(self) -> "ResGroups": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResGroups": ...

# --- res.lang ---

class ResLang(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    date_format: str
    decimal_point: str
    direction: str
    flag_image: bytes
    flag_image_url: str
    grouping: str
    has_bit2publish_template: bool
    iso_code: str
    name: str
    show_bit2publish_button: bool
    thousands_sep: str
    time_format: str
    url_code: str
    week_start: str
    def browse(self, ids: Union[int, List[int]]) -> "ResLang": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResLang": ...
    def create(self, vals: Dict[str, Any]) -> "ResLang": ...
    def filtered(self, func: Any) -> "ResLang": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResLang": ...
    def exists(self) -> "ResLang": ...
    def sudo(self) -> "ResLang": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResLang": ...

# --- res.partner ---

class ResPartner(Recordset):
    account_number: str
    acquisition_channel: str
    activation_date: Optional[_dt.date]
    activation_type: str
    active: bool
    active_lang_count: int
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    actual_payment_method_ids: "PaymentMethod"
    additional_info: str
    addresses_ids: "ResPartner"
    address_identification: str
    address_name: str
    address_payment_ids: "ResPartnerPayment"
    address_payment_method_ids: "BillingProfile"
    address_type: str
    admin_address: str
    administrative_index: str
    administrator_code: str
    agency_agreement: str
    agency_all_client_data_ids: "ClientAgencyData"
    agency_birth_location: str
    agency_bo_email_1: str
    agency_bo_email_2: str
    agency_bo_email_3: str
    agency_channel: str
    agency_city: str
    agency_client_data_ids: "ClientAgencyData"
    agency_cluster: str
    agency_code: str
    agency_contract_code: str
    agency_description: str
    agency_email: str
    agency_end_date: Optional[_dt.date]
    agency_id: "ResPartner"
    agency_nation: str
    agency_phone: str
    agency_province: str
    agency_start_date: Optional[_dt.date]
    agency_status: str
    agency_street: str
    agency_type: str
    agency_write_date: Optional[_dt.date]
    agency_zip: str
    agent_code: str
    agent_id: "ResUsers"
    agent_ids: "ResPartner"
    agent_role: str
    agent_sale_channel_id: "ChannelAssociation"
    agents_count: int
    agent_status: str
    all_letters_count: int
    allowed_nut_ids: "ResPartnerNuts"
    annual_revenue: str
    antichurn_index: str
    apartment_number: str
    app_identifier: str
    arera_id: str
    arrearage_index: str
    asl_attachment_id: bytes
    ateco_category_ids: "AtecoCategory"
    avatar_1024: bytes
    avatar_128: bytes
    avatar_1920: bytes
    avatar_256: bytes
    avatar_512: bytes
    bank_account_count: int
    bank_ids: "ResPartnerBank"
    barcode: str
    bbp_visibility: str
    birth_country_id: "ResCountry"
    birth_date: Optional[_dt.date]
    birth_location_id: "ResCity"
    birth_location_name: str
    birth_province_id: "ResCountryState"
    birth_province_name: str
    bit2publish_template_ids: "Bit2publishTemplate"
    blacklist_history_ids: "BlacklistHistory"
    business_email: str
    business_phone: str
    business_type: str
    business_type_mecoms: str
    business_unit: str
    bus_res_code: str
    calendar_last_notif_ack: Optional[_dt.datetime]
    callidus_code: str
    can_agency_be_reactivated: bool
    category: str
    category_id: "ResPartnerCategory"
    cciaa: str
    channel_ids: "ChannelAssociation"
    child_agency_ids: "ResPartner"
    child_ids: "ResPartner"
    churn_index: str
    cig_code: str
    cig_end_date: Optional[_dt.date]
    cig_start_date: Optional[_dt.date]
    city: str
    city_id: "ResCity"
    claim_index: str
    client_billing_profile_ids: "BillingProfile"
    client_case_ids: "HelpdeskTicket"
    client_category: str
    client_code: str
    client_contract_all_ids: "SorgeniaContracts"
    client_contract_ids: "SorgeniaContracts"
    client_interaction_count: int
    client_interaction_ids: "SympleInteraction"
    client_payment_ids: "ResPartnerPayment"
    client_payment_method_ids: "PaymentMethod"
    code_purl: str
    color: int
    comment: str
    commercial_company_name: str
    commercial_partner_id: "ResPartner"
    commissioning_close_date: Optional[_dt.date]
    company_group: str
    company_id: "ResCompany"
    company_name: str
    company_type: str
    complaint_index: str
    complete_contact_address: str
    complete_unsubscribe: bool
    connection_index: str
    contact_address: str
    contact_address_complete: str
    contact_case_ids: "HelpdeskTicket"
    contact_contract_ids: "SorgeniaContracts"
    contact_ids: "ResPartner"
    contact_index: str
    contact_interaction_count: int
    contact_interaction_ids: "SympleInteraction"
    contact_name: str
    contact_number: str
    contact_payment_ids: "ResPartnerPayment"
    contacts_for_quote_management: str
    contract_ids: "AccountAnalyticAccount"
    country: str
    country_code: str
    country_enforce_cities: bool
    country_id: "ResCountry"
    credit: float
    credit_limit: float
    credit_status: "CreditStatus"
    css_wizard: str
    cup: str
    currency_id: "ResCurrency"
    customer_care_category: str
    customer_group: str
    customer_rank: int
    customer_service_numbers_ids: "CustomerServiceNumbers"
    customer_termination_date: Optional[_dt.date]
    date: Optional[_dt.date]
    date_field_modified: Optional[_dt.datetime]
    date_sent_advice_client: Optional[_dt.datetime]
    date_sent_advice_credit_status: Optional[_dt.datetime]
    date_status_greener_changed: Optional[_dt.date]
    debit: float
    debit_limit: float
    denomination: str
    digital_index: str
    dispatch_zone_ids: "DistributorDispatchZone"
    distributor_code_ids: "DistributorCode"
    distributor_number: str
    document_attachment_back_id: bytes
    document_attachment_front_id: bytes
    document_count: int
    document_country: str
    document_date: Optional[_dt.date]
    document_deadline: Optional[_dt.date]
    document_from: str
    document_number: str
    economic_segment: str
    egon_city_id: str
    egon_house_number_id: str
    egon_street_id: str
    e_invoice: bool
    email: str
    email_formatted: str
    email_normalized: str
    employee: bool
    employees_count: str
    end_date_purl: Optional[_dt.datetime]
    end_date_status: Optional[_dt.date]
    end_validity_date: Optional[_dt.date]
    end_validity_is_split_iva: Optional[_dt.date]
    end_validity_iva_type: Optional[_dt.date]
    energy_source_used: str
    etichetta_tutelato: str
    eva_agency: str
    eva_code: str
    exclusivity_mandate: str
    expected_closing_date: Optional[_dt.date]
    expiration_date: Optional[_dt.date]
    export_credit_status_filter_timestamp: Optional[_dt.datetime]
    fax: str
    fiber_client_status: str
    fiber_service_point_ids: "ServicePoint"
    field_modified: str
    first_contract_id: "SorgeniaContracts"
    firstname: str
    fiscal_code: str
    fiscal_code_back_id: bytes
    fiscal_code_front_id: bytes
    fiscal_info: str
    fl_managed_bus: bool
    fl_managed_res: bool
    floor: str
    fl_transporter: bool
    friend_referral_code: str
    function: str
    gas_type: str
    gender: str
    golden_key: str
    greeners_status: str
    greentech_pmi: str
    greetech_retail: str
    has_bit2publish_template: bool
    has_message: bool
    has_self_declared_data: bool
    has_unreconciled_entries: bool
    heating_technology: str
    heating_type: str
    home_dimension: str
    home_tipology: str
    iban_purl: str
    identification_type: str
    id_login: str
    image_1024: bytes
    image_128: bytes
    image_1920: bytes
    image_256: bytes
    image_512: bytes
    image_medium: bytes
    im_status: str
    inbound_sorting_color: str
    incentive_compensation: bool
    index_history_ids: "IndexHistory"
    industry_id: "ResPartnerIndustry"
    info_msg_m2c: str
    insolvency_procedure_type: str
    instance_key_ids: "SymplePbInstanceKey"
    institution_name: str
    insurance_service: str
    intercom: str
    invoice_correction_index: str
    invoice_ids: "AccountMove"
    invoice_recipient_id: "ResPartner"
    invoice_type: str
    invoice_warn: str
    invoice_warn_msg: str
    ipa_code: str
    is_admin_user: bool
    is_agency: bool
    is_agency_valid: bool
    is_agent: bool
    is_automatic_appointment: bool
    is_back_office_close: bool
    is_blacklisted: bool
    is_client: bool
    is_commissioning_close: bool
    is_commodity_ele: bool
    is_commodity_fiber: bool
    is_commodity_gas: bool
    is_company: bool
    is_creating_from_migration: bool
    is_declaration_processed: bool
    is_distribution_date: Optional[_dt.date]
    is_distribution_list: bool
    is_distributor: bool
    is_editor_team: bool
    is_ele_vulnerability: bool
    is_ele_vulnerability_date: Optional[_dt.date]
    is_emobility: bool
    is_emobility_invoice: bool
    is_error_m2c: bool
    is_forceomocodia: bool
    is_front_end_close: bool
    is_gas_vulnerability: bool
    is_gas_vulnerability_date: Optional[_dt.date]
    is_gdpr_consent: bool
    is_gdpr_consent_date: Optional[_dt.date]
    is_greeners_permissions: bool
    is_habitual_exporter: bool
    is_in_blacklist: bool
    is_individual_client: bool
    is_infocamere_monitored: bool
    is_insolvent: bool
    is_multipoint: bool
    is_my_sorgenia_permissions: bool
    is_not_disalimentabile: bool
    is_not_subject_to_checks: bool
    is_operator_identifier: bool
    is_pmi: bool
    is_privacy_consent: bool
    is_prospect: bool
    is_residential_dgo: bool
    is_sace_warranty: bool
    is_selfcare: bool
    is_soft_spam: bool
    is_soft_spam_date: Optional[_dt.date]
    is_split_iva: bool
    is_subject: bool
    is_supplier: bool
    istat_code: str
    is_termination_blocked: bool
    is_top_customer: bool
    is_to_sync_with_m2c: bool
    is_turned_client: bool
    is_user: bool
    is_user_profiling: bool
    is_vip_strategy: bool
    is_withholding_tax: bool
    iva_activation_date: Optional[_dt.date]
    iva_change_date: Optional[_dt.date]
    iva_exemption_reason: str
    iva_rate: str
    iva_type: str
    job_position_id: "JobTitles"
    jolly_index: str
    journal_item_count: int
    keycloak_id: str
    lang: str
    last_agency_id: "ResPartner"
    lastname: str
    last_sync_date: Optional[_dt.datetime]
    last_time_entries_checked: Optional[_dt.datetime]
    latest_agent_status_change_date: Optional[_dt.date]
    legal_fax_number: str
    legal_phone_number: str
    legal_rapresentative_name: str
    legal_rapresentative_surname: str
    letter_of_intent_count: int
    letter_of_intent_ids: "LetterOfIntent"
    liability_waiver_id: bytes
    login_ids: "SorgeniaDigitalLogin"
    logistic_operator_type: str
    mandate_sign_date: Optional[_dt.date]
    mandate_validity_start_date: Optional[_dt.date]
    marginality_segment: str
    marketing_event_count: int
    market_type: str
    mass_market_end_date: Optional[_dt.date]
    mass_market_start_date: Optional[_dt.date]
    master_agency_id: "ResPartner"
    mdm_market: str
    meeting_count: int
    meeting_ids: "CalendarEvent"
    message_attachment_count: int
    message_bounce: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    mobile: str
    mobile_blacklisted: bool
    mobility_vehicle: str
    modified_by_operator: bool
    multi_service_index: str
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    name_purl: str
    name_variation_for_same_cf_iva: str
    nar_index: str
    nielsen_area: str
    note: str
    notice_number: str
    numbers_only_vat: str
    nursery_index: str
    nuts1_id: "ResPartnerNuts"
    nuts2_id: "ResPartnerNuts"
    nuts3_id: "ResPartnerNuts"
    nuts4_id: "ResPartnerNuts"
    occupants: str
    ocn_token: str
    office_code: str
    onboarding_details: str
    operational_fax_number: str
    operational_phone_number: str
    owner_id: "ResUsers"
    pa_pec_email: str
    parent_agency_id: "ResPartner"
    parent_contact_name: str
    parent_id: "ResPartner"
    parent_name: str
    partner_gid: int
    partner_latitude: float
    partner_longitude: float
    partner_share: bool
    party_where_a_ids: "PartyRelation"
    party_where_b_ids: "PartyRelation"
    party_where_present: "PartyRelation"
    payment_deadline: str
    payment_token_count: int
    payment_token_ids: "PaymentToken"
    pdr_code: str
    pdr_codes: str
    pdr_ids: "ResPartnerPdr"
    pec_email: str
    pec_email_infocamere: str
    permission_source: str
    permission_source_id: str
    phone: str
    phone_blacklisted: bool
    phone_mobile_search: str
    phone_sanitized: str
    phone_sanitized_blacklisted: bool
    photovoltaic: str
    plafond_amount: float
    pmi_attachment_id: bytes
    pmi_end_date: Optional[_dt.date]
    pmi_start_date: Optional[_dt.date]
    pod_code_distributor_history_ids: "DistributorPodCodeHistory"
    pod_codes: str
    pod_ids: "ResPartnerPod"
    pod_pdr_client_status: str
    pod_pdr_expired_total: float
    pod_pdr_recommended_limit: float
    postalizer_document_ids: "SorgeniaPostalizerDocument"
    priority: str
    privacy_date: Optional[_dt.date]
    privacy_history_ids: "PrivacyHistory"
    privacy_version: str
    property_account_payable_id: "AccountAccount"
    property_account_position_id: "AccountFiscalPosition"
    property_account_receivable_id: "AccountAccount"
    property_payment_method_id: "AccountPaymentMethod"
    property_payment_term_id: "AccountPaymentTerm"
    property_product_pricelist: "ProductPricelist"
    property_supplier_payment_term_id: "AccountPaymentTerm"
    proposal_token: str
    prospect_close_date: Optional[_dt.date]
    prospect_create_date: Optional[_dt.date]
    prospect_id: str
    prospect_type: str
    ptf_transfer: str
    purl: str
    reading_ids: "MeterReadings"
    ref: str
    ref_company_ids: "ResCompany"
    reference_manager_area_id: "ResPartner"
    reference_manager_greentech_area_id: "ResPartner"
    refering_account_customer: "ResPartner"
    region: str
    registration_date: Optional[_dt.date]
    registration_number: str
    registration_province: str
    responsability_area: str
    rfid_card_ids: "RfidCard"
    rmp: float
    sale_area_role_id: "SaleAreaRole"
    sale_channel_ids: "ChannelAssociation"
    sales_manager_id: "ResPartner"
    same_vat_partner_id: "ResPartner"
    score_index: str
    sdi_code: str
    self: "ResPartner"
    selfcare_contact_ids: "ResPartner"
    service_point_codes: str
    service_point_ids: "ServicePoint"
    severity_index: str
    show_bit2publish_button: bool
    signup_expiration: Optional[_dt.datetime]
    signup_token: str
    signup_type: str
    signup_url: str
    signup_valid: bool
    sla_ids: "HelpdeskSla"
    social_bonus_instance_ids: "SocialBonusInstance"
    stairs: str
    start_date_status: Optional[_dt.date]
    start_validity_is_split_iva: Optional[_dt.date]
    start_validity_iva_type: Optional[_dt.date]
    state_code: str
    state_id: "ResCountryState"
    stato_anagrafica: str
    status: str
    street: str
    street2: str
    street_num: str
    subject_type: str
    supplier_rank: int
    supply_type: str
    symphony_onboarding_requests: str
    tax_exemption_reason: str
    tax_rate: str
    team_ids: "ResPartnerTeam"
    teleselling_end_date: Optional[_dt.date]
    teleselling_start_date: Optional[_dt.date]
    termination_date: Optional[_dt.date]
    ticket_count: int
    title: "ResPartnerTitle"
    titleholder_role: str
    token_end_date: Optional[_dt.date]
    token_start_date: Optional[_dt.date]
    top_customer_flag_date: Optional[_dt.date]
    toponym_id: "ResToponym"
    total_client_status: str
    total_invoiced: float
    training_course_end_date: Optional[_dt.date]
    training_course_end_hour: Optional[_dt.datetime]
    training_course_type: str
    training_status: str
    transporter_id: "ResPartnerTransporter"
    trust: str
    type: str
    tz: str
    tz_offset: str
    uni_office_code: str
    user_id: "ResUsers"
    user_ids: "ResUsers"
    user_profiling_date: Optional[_dt.date]
    user_sequence: str
    validity_date: Optional[_dt.date]
    vat: str
    wallet_management: str
    warranty_ids: "SorgeniaWarranty"
    website: str
    website_message_ids: "MailMessage"
    withholding_tax_code: str
    zip: str
    zip_id: "ResCityZip"
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
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartner": ...

# --- res.partner.abi_cab ---

class ResPartnerAbiCab(Recordset):
    abi: str
    address: str
    agency: str
    bit2publish_template_ids: "Bit2publishTemplate"
    cab: str
    commune: str
    end_date: str
    has_bit2publish_template: bool
    name: str
    region: str
    show_bit2publish_button: bool
    start_date: str
    state: str
    zip: str
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerAbiCab": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerAbiCab": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerAbiCab": ...
    def filtered(self, func: Any) -> "ResPartnerAbiCab": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerAbiCab": ...
    def exists(self) -> "ResPartnerAbiCab": ...
    def sudo(self) -> "ResPartnerAbiCab": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerAbiCab": ...

# --- res.partner.abi_cab_chunk ---

class ResPartnerAbiCabChunk(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    file_data: bytes
    file_id: "ResPartnerAbiCabFile"
    has_bit2publish_template: bool
    name: str
    processed: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerAbiCabChunk": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerAbiCabChunk": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerAbiCabChunk": ...
    def filtered(self, func: Any) -> "ResPartnerAbiCabChunk": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerAbiCabChunk": ...
    def exists(self) -> "ResPartnerAbiCabChunk": ...
    def sudo(self) -> "ResPartnerAbiCabChunk": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerAbiCabChunk": ...

# --- res.partner.abi_cab_file ---

class ResPartnerAbiCabFile(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    chunk_ids: "ResPartnerAbiCabChunk"
    chunk_size: int
    file_data: bytes
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    status: str
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerAbiCabFile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerAbiCabFile": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerAbiCabFile": ...
    def filtered(self, func: Any) -> "ResPartnerAbiCabFile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerAbiCabFile": ...
    def exists(self) -> "ResPartnerAbiCabFile": ...
    def sudo(self) -> "ResPartnerAbiCabFile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerAbiCabFile": ...

# --- res.partner.abi_cab_wizard ---

class ResPartnerAbiCabWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    chunk_size: int
    file_data: bytes
    file_name: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerAbiCabWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerAbiCabWizard": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerAbiCabWizard": ...
    def filtered(self, func: Any) -> "ResPartnerAbiCabWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerAbiCabWizard": ...
    def exists(self) -> "ResPartnerAbiCabWizard": ...
    def sudo(self) -> "ResPartnerAbiCabWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerAbiCabWizard": ...

# --- res.partner.autocomplete.sync ---

class ResPartnerAutocompleteSync(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    synched: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerAutocompleteSync": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerAutocompleteSync": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerAutocompleteSync": ...
    def filtered(self, func: Any) -> "ResPartnerAutocompleteSync": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerAutocompleteSync": ...
    def exists(self) -> "ResPartnerAutocompleteSync": ...
    def sudo(self) -> "ResPartnerAutocompleteSync": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerAutocompleteSync": ...

# --- res.partner.bank ---

class ResPartnerBank(Recordset):
    acc_holder_name: str
    acc_number: str
    acc_type: str
    active: bool
    bank_bic: str
    bank_id: "ResBank"
    bank_name: str
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    currency_id: "ResCurrency"
    has_bit2publish_template: bool
    journal_id: "AccountJournal"
    partner_id: "ResPartner"
    sanitized_acc_number: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerBank": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerBank": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerBank": ...
    def filtered(self, func: Any) -> "ResPartnerBank": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerBank": ...
    def exists(self) -> "ResPartnerBank": ...
    def sudo(self) -> "ResPartnerBank": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerBank": ...

# --- res.partner.category ---

class ResPartnerCategory(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    child_ids: "ResPartnerCategory"
    color: int
    has_bit2publish_template: bool
    name: str
    parent_id: "ResPartnerCategory"
    parent_path: str
    partner_ids: "ResPartner"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerCategory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerCategory": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerCategory": ...
    def filtered(self, func: Any) -> "ResPartnerCategory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerCategory": ...
    def exists(self) -> "ResPartnerCategory": ...
    def sudo(self) -> "ResPartnerCategory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerCategory": ...

# --- res.partner.industry ---

class ResPartnerIndustry(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    full_name: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerIndustry": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerIndustry": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerIndustry": ...
    def filtered(self, func: Any) -> "ResPartnerIndustry": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerIndustry": ...
    def exists(self) -> "ResPartnerIndustry": ...
    def sudo(self) -> "ResPartnerIndustry": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerIndustry": ...

# --- res.partner.infocamere ---

class ResPartnerInfocamere(Recordset):
    action: str
    active: bool
    batch_no: str
    bit2publish_template_ids: "Bit2publishTemplate"
    case_count: int
    child_ids: "ResPartnerInfocamere"
    date: Optional[_dt.datetime]
    delete_logs: str
    emails: str
    event_output_type: str
    file_name: str
    full_url: str
    has_bit2publish_template: bool
    has_downloads: bool
    has_message: bool
    has_subsequent_call: bool
    include_downloaded: str
    infocamere_monitored_field_ids: "InfocamereMapOutput"
    infocamere_monitored_partner_ids: "ResPartner"
    input_file_data: bytes
    log_count: int
    lot_name: str
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    method: str
    min_date: Optional[_dt.date]
    monitor_all_contacts: bool
    name: str
    parent_id: "ResPartnerInfocamere"
    password: str
    periodicity: str
    repeat: bool
    rule_id: "InfocamereRules"
    scope: str
    service_type: str
    show_bit2publish_button: bool
    state: str
    subscope: str
    subsequent_subscope: str
    succeeded: bool
    track_API_history: bool
    url: str
    user_id: "ResUsers"
    username: str
    user_request: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerInfocamere": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerInfocamere": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerInfocamere": ...
    def filtered(self, func: Any) -> "ResPartnerInfocamere": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerInfocamere": ...
    def exists(self) -> "ResPartnerInfocamere": ...
    def sudo(self) -> "ResPartnerInfocamere": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerInfocamere": ...

# --- res.partner.infocamere_logs ---

class ResPartnerInfocamereLogs(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    days: int
    has_bit2publish_template: bool
    name: str
    response: str
    rule_id: "InfocamereRules"
    service_id: "ResPartnerInfocamere"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerInfocamereLogs": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerInfocamereLogs": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerInfocamereLogs": ...
    def filtered(self, func: Any) -> "ResPartnerInfocamereLogs": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerInfocamereLogs": ...
    def exists(self) -> "ResPartnerInfocamereLogs": ...
    def sudo(self) -> "ResPartnerInfocamereLogs": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerInfocamereLogs": ...

# --- res.partner.meter ---

class ResPartnerMeter(Recordset):
    accessibility: str
    activation_date_2g: Optional[_dt.date]
    active: bool
    active_energy_digits: str
    active_number: str
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    address_notes: str
    bit2publish_template_ids: "Bit2publishTemplate"
    client_id: "ResPartner"
    counter_number: str
    deactivation_date: Optional[_dt.date]
    distributor_id: "ResPartner"
    has_bit2publish_template: bool
    has_message: bool
    install_date: Optional[_dt.date]
    is_active: bool
    is_forfait: bool
    is_limited: bool
    is_measurement_group: bool
    max_voltage: str
    mecoms_code: str
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    meter_brand: str
    meter_configurator: str
    meter_constant: float
    meter_number: str
    meter_readings_ids: "MeterReadings"
    meter_responsive_constant: float
    meter_type: str
    meter_voltage_constant: float
    model_name: str
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    notes: str
    parent_pod_id: "ResPartnerPod"
    pdp_code: str
    pdr_code: str
    pdr_id: "ResPartnerPdr"
    pod_address_id: "ResPartner"
    pod_code: str
    pod_create_date: Optional[_dt.datetime]
    pod_create_uid: "ResUsers"
    pod_id: "ResPartnerPod"
    pod_name: str
    pod_notes: str
    pod_write_date: Optional[_dt.datetime]
    pod_write_uid: "ResUsers"
    power_digits: str
    power_meter_install_date: Optional[_dt.date]
    power_meter_number: str
    reactive_energy_digits: str
    reactive_energy_meter_install_date: Optional[_dt.date]
    remi: str
    remotely_managed: str
    show_bit2publish_button: bool
    start_date_2g: Optional[_dt.date]
    supplier_id: "ResPartner"
    supply_voltage: str
    tariff_code: str
    tariff_type: str
    technical_apartment_number: str
    technical_city: str
    technical_city_id: "ResCity"
    technical_country_id: "ResCountry"
    technical_floor: str
    technical_region: str
    technical_stairs: str
    technical_state_code: str
    technical_state_id: "ResCountryState"
    technical_street: str
    technical_street2: str
    technical_street_number: str
    technical_toponym_id: "ResToponym"
    technical_zip: str
    type: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerMeter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerMeter": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerMeter": ...
    def filtered(self, func: Any) -> "ResPartnerMeter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerMeter": ...
    def exists(self) -> "ResPartnerMeter": ...
    def sudo(self) -> "ResPartnerMeter": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerMeter": ...

# --- res.partner.meter.pdr ---

class ResPartnerMeterPdr(Recordset):
    accessibility: str
    active: bool
    address_notes: str
    bit2publish_template_ids: "Bit2publishTemplate"
    c_coefficient: str
    client_id: "ResPartner"
    coeff_cor: float
    deactivation_date: Optional[_dt.date]
    distributor_id: "ResPartner"
    gas_digits: str
    gas_pressure: str
    has_bit2publish_template: bool
    install_date: Optional[_dt.date]
    is_active: bool
    is_forfait: bool
    is_limited: bool
    is_measurement_group: bool
    mecoms_code: str
    meter_brand: str
    meter_configurator: str
    meter_number: str
    meter_readings_ids: "MeterReadingsPdr"
    model_name: str
    name: str
    notes: str
    pdp_code: str
    pdr_address_id: str
    pdr_create_date: Optional[_dt.datetime]
    pdr_create_uid: "ResUsers"
    pdr_id: "ResPartnerPdr"
    pdr_meter_type: str
    pdr_notes: str
    pdr_write_date: Optional[_dt.datetime]
    pdr_write_uid: "ResUsers"
    remi: str
    remotely_managed: str
    show_bit2publish_button: bool
    supplier_id: "ResPartner"
    technical_apartment_number: str
    technical_city: str
    technical_city_id: "ResCity"
    technical_country_id: "ResCountry"
    technical_floor: str
    technical_region: str
    technical_stairs: str
    technical_state_code: str
    technical_state_id: "ResCountryState"
    technical_street: str
    technical_street2: str
    technical_street_number: str
    technical_toponym_id: "ResToponym"
    technical_zip: str
    type: str
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerMeterPdr": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerMeterPdr": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerMeterPdr": ...
    def filtered(self, func: Any) -> "ResPartnerMeterPdr": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerMeterPdr": ...
    def exists(self) -> "ResPartnerMeterPdr": ...
    def sudo(self) -> "ResPartnerMeterPdr": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerMeterPdr": ...

# --- res.partner.nuts ---

class ResPartnerNuts(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    child_ids: "ResPartnerNuts"
    code: str
    country_id: "ResCountry"
    has_bit2publish_template: bool
    level: int
    name: str
    not_updatable: bool
    parent_id: "ResPartnerNuts"
    parent_path: str
    show_bit2publish_button: bool
    state_id: "ResCountryState"
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerNuts": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerNuts": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerNuts": ...
    def filtered(self, func: Any) -> "ResPartnerNuts": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerNuts": ...
    def exists(self) -> "ResPartnerNuts": ...
    def sudo(self) -> "ResPartnerNuts": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerNuts": ...

# --- res.partner.pa ---

class ResPartnerPa(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    cap: str
    cf: str
    cod_amm: str
    cod_ou: str
    cod_uni_ou: str
    comune: str
    data_avvio_sfe: Optional[_dt.date]
    des_ou: str
    dt_verifica_cf: Optional[_dt.date]
    error: str
    file_id: "ResPartnerPaFile"
    has_bit2publish_template: bool
    indirizzo: str
    provincia: str
    regione: str
    show_bit2publish_button: bool
    state: str
    vat: str
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPa": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPa": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPa": ...
    def filtered(self, func: Any) -> "ResPartnerPa": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPa": ...
    def exists(self) -> "ResPartnerPa": ...
    def sudo(self) -> "ResPartnerPa": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPa": ...

# --- res.partner.pa.file ---

class ResPartnerPaFile(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    created_records: int
    data: bytes
    filename: str
    has_bit2publish_template: bool
    is_processed: bool
    is_processing: bool
    last_error: str
    last_processed_line: int
    line_history_ids: "ResPartnerPa"
    line_ids: "ResPartnerPa"
    name: str
    show_bit2publish_button: bool
    state: str
    updated_records: int
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPaFile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPaFile": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPaFile": ...
    def filtered(self, func: Any) -> "ResPartnerPaFile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPaFile": ...
    def exists(self) -> "ResPartnerPaFile": ...
    def sudo(self) -> "ResPartnerPaFile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPaFile": ...

# --- res.partner.pa.importer ---

class ResPartnerPaImporter(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPaImporter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPaImporter": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPaImporter": ...
    def filtered(self, func: Any) -> "ResPartnerPaImporter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPaImporter": ...
    def exists(self) -> "ResPartnerPaImporter": ...
    def sudo(self) -> "ResPartnerPaImporter": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPaImporter": ...

# --- res.partner.payment ---

class ResPartnerPayment(Recordset):
    account_owner_name: str
    account_owner_surname: str
    activation_date: Optional[_dt.date]
    activation_site: str
    active: bool
    address_id: "ResPartner"
    apartment_number: str
    authorization_code: str
    bit2publish_template_ids: "Bit2publishTemplate"
    category_id: "ResPartnerCategory"
    cf_owner: str
    city_id: "ResCity"
    client_id: "ResPartner"
    contact_id: "ResPartner"
    contact_name: str
    contact_type: str
    country_id: "ResCountry"
    date_authorization_code: Optional[_dt.date]
    deactivation_reason: str
    email: str
    end_date: Optional[_dt.date]
    floor: str
    has_bit2publish_template: bool
    iban: str
    ignore_unexecuted: bool
    ignore_unexecuted_date: Optional[_dt.date]
    invoice_frequency: str
    invoice_type: str
    name: str
    parent_client_id: "ResPartner"
    payment_method: str
    pod_ids: "ResPartnerPod"
    pod_status: str
    request_date: Optional[_dt.date]
    show_bit2publish_button: bool
    stairs: str
    state_id: "ResCountryState"
    status: str
    street: str
    street2: str
    street_num: str
    swift: str
    toponym_id: "ResToponym"
    zip: str
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPayment": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPayment": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPayment": ...
    def filtered(self, func: Any) -> "ResPartnerPayment": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPayment": ...
    def exists(self) -> "ResPartnerPayment": ...
    def sudo(self) -> "ResPartnerPayment": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPayment": ...

# --- res.partner.payment.migration.result ---

class ResPartnerPaymentMigrationResult(Recordset):
    asset_ids: str
    billing_profile_id: "BillingProfile"
    bit2publish_template_ids: "Bit2publishTemplate"
    client_id: "ResPartner"
    error_log: str
    has_bit2publish_template: bool
    old_default_payment_method_id: "ResPartnerPayment"
    old_payment_method_id: "ResPartnerPayment"
    payment_method_id: "PaymentMethod"
    pod_ids: "ResPartnerPod"
    result: str
    service_point_ids: "ServicePoint"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPaymentMigrationResult": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPaymentMigrationResult": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPaymentMigrationResult": ...
    def filtered(self, func: Any) -> "ResPartnerPaymentMigrationResult": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPaymentMigrationResult": ...
    def exists(self) -> "ResPartnerPaymentMigrationResult": ...
    def sudo(self) -> "ResPartnerPaymentMigrationResult": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPaymentMigrationResult": ...

# --- res.partner.pdp.mixin ---

class ResPartnerPdpMixin(Recordset):
    acquisition_bid: str
    activation_date: Optional[_dt.date]
    active: bool
    active_service_point_id: "ServicePoint"
    address_id: "ResPartner"
    address_notes: str
    belonging_lot: str
    bit2publish_template_ids: "Bit2publishTemplate"
    category_id: "ResPartnerCategory"
    client_id: "ResPartner"
    client_ids: "ResPartner"
    code: str
    deactivation_date: Optional[_dt.date]
    declared_annual_usage: float
    distributor_annual_usage: str
    distributor_annual_usage_history_ids: "MailTrackingValue"
    distributor_id: "ResPartner"
    distributor_practice_code: str
    distributor_toll_free_number: str
    distributor_website: str
    has_bit2publish_template: bool
    is_get_from_onboarding: bool
    istat_code: str
    iva_effective_date: Optional[_dt.date]
    iva_exemption_reason: str
    iva_rate: str
    last_active_service_point_id: "ServicePoint"
    notes: str
    service_point_ids: "ServicePoint"
    show_bit2publish_button: bool
    state: str
    supplier_id: "ResPartner"
    supply_state: str
    tax_effective_date: Optional[_dt.date]
    tax_exemption_reason: str
    tax_rate: str
    technical_address: str
    technical_apartment_number: str
    technical_city: str
    technical_city_id: "ResCity"
    technical_country_id: "ResCountry"
    technical_egon_city_id: str
    technical_egon_house_number_id: str
    technical_egon_street_id: str
    technical_floor: str
    technical_region: str
    technical_stairs: str
    technical_state_code: str
    technical_state_id: "ResCountryState"
    technical_street: str
    technical_street2: str
    technical_street_number: str
    technical_toponym_id: "ResToponym"
    technical_zip: str
    temp_client_id: "ResPartner"
    user_sequence: str
    weather_region: str
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPdpMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPdpMixin": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPdpMixin": ...
    def filtered(self, func: Any) -> "ResPartnerPdpMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPdpMixin": ...
    def exists(self) -> "ResPartnerPdpMixin": ...
    def sudo(self) -> "ResPartnerPdpMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPdpMixin": ...

# --- res.partner.pdr ---

class ResPartnerPdr(Recordset):
    acquisition_bid: str
    activation_date: Optional[_dt.date]
    active: bool
    active_service_point_id: "ServicePoint"
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    address_id: "ResPartner"
    address_notes: str
    administrative_location: str
    aeeg_distributor_profile: str
    annual_progressive_amount: float
    belonging_lot: str
    bit2publish_template_ids: "Bit2publishTemplate"
    cadastral_code: str
    cadastral_date: Optional[_dt.date]
    cadastral_location: str
    cadastral_map: str
    cadastral_parcel: str
    cadastral_sub: str
    category_id: "ResPartnerCategory"
    client_id: "ResPartner"
    client_ids: "ResPartner"
    cma_sorgenia: int
    code: str
    codice_remi: str
    contractual_gas_extraction_profile: str
    daily_commitment: str
    data_overwritten: bool
    deactivation_date: Optional[_dt.date]
    declarant_type: str
    declared_annual_usage: float
    direct_extraction_type: str
    distance_from_rng: str
    distributor_annual_usage: str
    distributor_annual_usage_history_ids: "MailTrackingValue"
    distributor_id: "ResPartner"
    distributor_practice_code: str
    distributor_toll_free_number: str
    distributor_website: str
    extraction_class: str
    extraction_profile_type: str
    file_id: "ResPartnerPdrMunicipalitiesFile"
    following_parcel: str
    gas_first_supply_date: Optional[_dt.date]
    gas_pressure: float
    has_bit2publish_template: bool
    has_message: bool
    house_number: str
    house_street: str
    is_corrector: bool
    is_direct: bool
    is_get_from_onboarding: bool
    is_not_disconnectable: bool
    is_remote_management: bool
    is_sorgenia_annual_use_validation: float
    istat_code: str
    is_user_transport: bool
    iva_effective_date: Optional[_dt.date]
    iva_exemption_reason: str
    iva_rate: str
    last_active_service_point_id: "ServicePoint"
    max_contractual_extraction: float
    max_withdrawal_hour: float
    measure_pressure: str
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    missing_cadastral_reason: str
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    not_disconnectable_category: str
    notes: str
    parcel_type: str
    pdr_direct_status: str
    pdr_meter_ids: "ResPartnerMeterPdr"
    pdr_type: str
    point_is_direct: str
    profile_withdrawal_code: str
    rcu_transport_capacity: float
    real_estate_unit_type: str
    remi_code_id: "TransportNetworkMapManagement"
    service_point_ids: "ServicePoint"
    show_bit2publish_button: bool
    social_bonus_instance_ids: "SocialBonusInstance"
    sorgenia_annual_use_amount: float
    state: str
    supplier_id: "ResPartner"
    supply_state: str
    tax_effective_date: Optional[_dt.date]
    tax_exemption_reason: str
    tax_rate: str
    technical_address: str
    technical_apartment_number: str
    technical_city: str
    technical_city_id: "ResCity"
    technical_country_id: "ResCountry"
    technical_egon_city_id: str
    technical_egon_house_number_id: str
    technical_egon_street_id: str
    technical_floor: str
    technical_region: str
    technical_stairs: str
    technical_state_code: str
    technical_state_id: "ResCountryState"
    technical_street: str
    technical_street2: str
    technical_street_number: str
    technical_toponym_id: "ResToponym"
    technical_zip: str
    temp_client_id: "ResPartner"
    thermal_flow: float
    transport_capacity: float
    transporter_id: "Unknown"
    trattamento: str
    treatment: str
    urban_section: str
    user_sequence: str
    use_type_validity: bool
    weather_region: str
    website_message_ids: "MailMessage"
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
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPdr": ...

# --- res.partner.pdr.municipalities.file ---

class ResPartnerPdrMunicipalitiesFile(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    is_processed: bool
    is_processing: bool
    last_error: str
    last_processed_line: int
    line_ids: "ResPartnerPdr"
    name: str
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPdrMunicipalitiesFile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPdrMunicipalitiesFile": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPdrMunicipalitiesFile": ...
    def filtered(self, func: Any) -> "ResPartnerPdrMunicipalitiesFile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPdrMunicipalitiesFile": ...
    def exists(self) -> "ResPartnerPdrMunicipalitiesFile": ...
    def sudo(self) -> "ResPartnerPdrMunicipalitiesFile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPdrMunicipalitiesFile": ...

# --- res.partner.pdr.municipalities.importer ---

class ResPartnerPdrMunicipalitiesImporter(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPdrMunicipalitiesImporter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPdrMunicipalitiesImporter": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPdrMunicipalitiesImporter": ...
    def filtered(self, func: Any) -> "ResPartnerPdrMunicipalitiesImporter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPdrMunicipalitiesImporter": ...
    def exists(self) -> "ResPartnerPdrMunicipalitiesImporter": ...
    def sudo(self) -> "ResPartnerPdrMunicipalitiesImporter": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPdrMunicipalitiesImporter": ...

# --- res.partner.pdr.municipality ---

class ResPartnerPdrMunicipality(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    cd_comune: str
    cd_dir_terr: str
    cd_fclim: str
    cd_istat: str
    cd_istat_prov: str
    cd_provincia: str
    cd_regione: str
    d_valido_al: Optional[_dt.date]
    d_valido_dal: Optional[_dt.date]
    error: str
    file_id: "ResPartnerPdrMunicipalitiesFile"
    fl_mezzogiorno: str
    gas_civil_duty: str
    gas_industrial_duty: str
    gas_regional_surcharge_civil_uses: str
    gas_regional_surcharge_industrial_uses: str
    has_bit2publish_template: bool
    regional_additional_replacement: str
    s_comune: str
    s_dir_terr: str
    s_fclim: str
    show_bit2publish_button: bool
    s_mezzogiorno: str
    s_provincia: str
    s_regione: str
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPdrMunicipality": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPdrMunicipality": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPdrMunicipality": ...
    def filtered(self, func: Any) -> "ResPartnerPdrMunicipality": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPdrMunicipality": ...
    def exists(self) -> "ResPartnerPdrMunicipality": ...
    def sudo(self) -> "ResPartnerPdrMunicipality": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPdrMunicipality": ...

# --- res.partner.personal.data ---

class ResPartnerPersonalData(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    field_id: "IrModelFields"
    has_bit2publish_template: bool
    model: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerPersonalData": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerPersonalData": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerPersonalData": ...
    def filtered(self, func: Any) -> "ResPartnerPersonalData": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerPersonalData": ...
    def exists(self) -> "ResPartnerPersonalData": ...
    def sudo(self) -> "ResPartnerPersonalData": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPersonalData": ...

# --- res.partner.pod ---

class ResPartnerPod(Recordset):
    acquisition_bid: str
    activation_date: Optional[_dt.date]
    active: bool
    active_service_point_id: "ServicePoint"
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    address_id: "ResPartner"
    address_notes: str
    administrative_location: str
    annual_history_amount: float
    available_power: str
    available_power_raw: float
    belonging_lot: str
    billing_profile_address: "ResPartner"
    billing_profile_channel: str
    billing_profile_id: "BillingProfile"
    bit2publish_template_ids: "Bit2publishTemplate"
    cadastral_code: str
    cadastral_date: Optional[_dt.date]
    cadastral_location: str
    cadastral_map: str
    cadastral_parcel: str
    cadastral_sub: str
    category_id: "ResPartnerCategory"
    client_id: "ResPartner"
    client_ids: "ResPartner"
    client_status: str
    cma_sorgenia: int
    code: str
    color: int
    connection_type: str
    contract_ids: "SorgeniaContracts"
    contract_state: str
    data_overwritten: bool
    deactivation_date: Optional[_dt.date]
    declarant_type: str
    declared_annual_usage: float
    default_payment_method_id: "ResPartnerPayment"
    dispatch_zone: str
    distributor_annual_usage: str
    distributor_annual_usage_history_ids: "MailTrackingValue"
    distributor_id: "ResPartner"
    distributor_practice_code: str
    distributor_toll_free_number: str
    distributor_website: str
    energy_use_type: str
    engaged_power: str
    engaged_power_raw: float
    expected_end_date: Optional[_dt.date]
    fallback_payment_method_id: "PaymentMethod"
    following_parcel: str
    franc_power: str
    has_bit2publish_template: bool
    has_message: bool
    house_number: str
    house_street: str
    is_get_from_onboarding: bool
    is_not_disconnectable: bool
    is_not_disconnectable_distributor: bool
    is_not_disconnectable_history_ids: "MailTrackingValue"
    istat_code: str
    is_temporary_pod: bool
    iva_effective_date: Optional[_dt.date]
    iva_exemption_reason: str
    iva_rate: str
    last_active_service_point_id: "ServicePoint"
    latest_code: str
    main_payment_method_email: str
    main_payment_method_id: "PaymentMethod"
    main_payment_method_name: str
    main_payment_method_type: str
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    meter_ids: "ResPartnerMeter"
    missing_cadastral_reason: str
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    new_pr_code: str
    not_disconnectable_category: str
    notes: str
    other_free_text: str
    parcel_type: str
    payment_auth_code: str
    payment_iban: str
    payment_method_address: "ResPartner"
    payment_method_channel: str
    payment_method_email: str
    payment_method_id: "ResPartnerPayment"
    payment_method_name: str
    payment_method_type: str
    pesse_code: str
    phase_tension: str
    pod_use: str
    pod_use_edit_date: Optional[_dt.date]
    pr_code: str
    real_estate_unit_type: str
    resolution_type: str
    service_point_ids: "ServicePoint"
    show_bit2publish_button: bool
    social_bonus_instance_ids: "SocialBonusInstance"
    state: str
    supplier_id: "ResPartner"
    supply_state: str
    tariff_code: str
    tax_effective_date: Optional[_dt.date]
    tax_exemption_reason: str
    tax_rate: str
    technical_address: str
    technical_apartment_number: str
    technical_city: str
    technical_city_id: "ResCity"
    technical_country_id: "ResCountry"
    technical_egon_city_id: str
    technical_egon_house_number_id: str
    technical_egon_street_id: str
    technical_floor: str
    technical_region: str
    technical_stairs: str
    technical_state_code: str
    technical_state_id: "ResCountryState"
    technical_street: str
    technical_street2: str
    technical_street_number: str
    technical_toponym_id: "ResToponym"
    technical_zip: str
    temp_client_id: "ResPartner"
    tension_type: str
    urban_section: str
    user_sequence: str
    weather_region: str
    website_message_ids: "MailMessage"
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
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerPod": ...

# --- res.partner.team ---

class ResPartnerTeam(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    group_roles_ids: "SecurityRole"
    has_bit2publish_template: bool
    is_m2c_integration_group: bool
    is_role_active: bool
    name: str
    partner_ids: "ResPartner"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerTeam": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerTeam": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerTeam": ...
    def filtered(self, func: Any) -> "ResPartnerTeam": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerTeam": ...
    def exists(self) -> "ResPartnerTeam": ...
    def sudo(self) -> "ResPartnerTeam": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerTeam": ...

# --- res.partner.title ---

class ResPartnerTitle(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    shortcut: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerTitle": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerTitle": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerTitle": ...
    def filtered(self, func: Any) -> "ResPartnerTitle": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerTitle": ...
    def exists(self) -> "ResPartnerTitle": ...
    def sudo(self) -> "ResPartnerTitle": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerTitle": ...

# --- res.partner.toll.free.number ---

class ResPartnerTollFreeNumber(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    distributor_id: "ResPartner"
    has_bit2publish_template: bool
    number: str
    region_id: "ResPartnerNuts"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerTollFreeNumber": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerTollFreeNumber": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerTollFreeNumber": ...
    def filtered(self, func: Any) -> "ResPartnerTollFreeNumber": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerTollFreeNumber": ...
    def exists(self) -> "ResPartnerTollFreeNumber": ...
    def sudo(self) -> "ResPartnerTollFreeNumber": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerTollFreeNumber": ...

# --- res.partner.transporter ---

class ResPartnerTransporter(Recordset):
    account_number: str
    active: bool
    addresses_ids: "ResPartner"
    arera_id: str
    bit2publish_template_ids: "Bit2publishTemplate"
    city: str
    city_id: "ResCity"
    complete_contact_address: str
    contacts_for_quote_management: str
    customer_service_numbers_ids: "CustomerServiceNumbers"
    email: str
    end_date_status: Optional[_dt.date]
    fiscal_code: str
    fl_managed_bus: bool
    fl_managed_res: bool
    fl_transporter: bool
    gas_type: str
    golden_key: str
    has_bit2publish_template: bool
    info_msg_m2c: str
    is_admin_user: bool
    is_commodity_ele: bool
    is_commodity_fiber: bool
    is_commodity_gas: bool
    is_error_m2c: bool
    is_to_sync_with_m2c: bool
    last_sync_date: Optional[_dt.datetime]
    legal_fax_number: str
    legal_phone_number: str
    logistic_operator_type: str
    modified_by_operator: bool
    municipality: str
    name: str
    numbers_only_vat: str
    operational_fax_number: str
    operational_phone_number: str
    show_bit2publish_button: bool
    start_date_status: Optional[_dt.date]
    subject_type: str
    supply_type: str
    transporter_code: str
    vat: str
    website: str
    def browse(self, ids: Union[int, List[int]]) -> "ResPartnerTransporter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResPartnerTransporter": ...
    def create(self, vals: Dict[str, Any]) -> "ResPartnerTransporter": ...
    def filtered(self, func: Any) -> "ResPartnerTransporter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResPartnerTransporter": ...
    def exists(self) -> "ResPartnerTransporter": ...
    def sudo(self) -> "ResPartnerTransporter": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResPartnerTransporter": ...

# --- res.toponym ---

class ResToponym(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResToponym": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResToponym": ...
    def create(self, vals: Dict[str, Any]) -> "ResToponym": ...
    def filtered(self, func: Any) -> "ResToponym": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResToponym": ...
    def exists(self) -> "ResToponym": ...
    def sudo(self) -> "ResToponym": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResToponym": ...

# --- res.users ---

class ResUsers(Recordset):
    accesses_count: int
    account_number: str
    acquisition_channel: str
    action_id: "IrActionsActions"
    activation_date: Optional[_dt.date]
    activation_type: str
    active: bool
    active_lang_count: int
    active_partner: bool
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    actual_payment_method_ids: "PaymentMethod"
    additional_info: str
    addresses_ids: "ResPartner"
    address_identification: str
    address_name: str
    address_payment_ids: "ResPartnerPayment"
    address_payment_method_ids: "BillingProfile"
    address_type: str
    admin_address: str
    administrative_index: str
    administrator_code: str
    agency_agreement: str
    agency_all_client_data_ids: "ClientAgencyData"
    agency_birth_location: str
    agency_bo_email_1: str
    agency_bo_email_2: str
    agency_bo_email_3: str
    agency_channel: str
    agency_city: str
    agency_client_data_ids: "ClientAgencyData"
    agency_cluster: str
    agency_code: str
    agency_contract_code: str
    agency_description: str
    agency_email: str
    agency_end_date: Optional[_dt.date]
    agency_id: "ResPartner"
    agency_nation: str
    agency_phone: str
    agency_province: str
    agency_start_date: Optional[_dt.date]
    agency_status: str
    agency_street: str
    agency_type: str
    agency_write_date: Optional[_dt.date]
    agency_zip: str
    agent_code: str
    agent_id: "ResUsers"
    agent_ids: "ResPartner"
    agent_role: str
    agent_sale_channel_id: "ChannelAssociation"
    agents_count: int
    agent_status: str
    all_letters_count: int
    allowed_nut_ids: "ResPartnerNuts"
    annual_revenue: str
    antichurn_index: str
    apartment_number: str
    api_key_ids: "ResUsersApikeys"
    app_identifier: str
    arera_id: str
    arrearage_index: str
    asl_attachment_id: bytes
    ateco_category_ids: "AtecoCategory"
    avatar_1024: bytes
    avatar_128: bytes
    avatar_1920: bytes
    avatar_256: bytes
    avatar_512: bytes
    bank_account_count: int
    bank_ids: "ResPartnerBank"
    barcode: str
    bbp_visibility: str
    birth_country_id: "ResCountry"
    birth_date: Optional[_dt.date]
    birth_location_id: "ResCity"
    birth_location_name: str
    birth_province_id: "ResCountryState"
    birth_province_name: str
    bit2publish_template_ids: "Bit2publishTemplate"
    blacklist_history_ids: "BlacklistHistory"
    business_email: str
    business_phone: str
    business_type: str
    business_type_mecoms: str
    business_unit: str
    bus_res_code: str
    calendar_last_notif_ack: Optional[_dt.datetime]
    callidus_code: str
    can_agency_be_reactivated: bool
    category: str
    category_id: "ResPartnerCategory"
    cciaa: str
    channel_ids: "ChannelAssociation"
    child_agency_ids: "ResPartner"
    child_ids: "ResPartner"
    churn_index: str
    cig_code: str
    cig_end_date: Optional[_dt.date]
    cig_start_date: Optional[_dt.date]
    city: str
    city_id: "ResCity"
    claim_index: str
    client_billing_profile_ids: "BillingProfile"
    client_case_ids: "HelpdeskTicket"
    client_category: str
    client_code: str
    client_contract_all_ids: "SorgeniaContracts"
    client_contract_ids: "SorgeniaContracts"
    client_interaction_count: int
    client_interaction_ids: "SympleInteraction"
    client_payment_ids: "ResPartnerPayment"
    client_payment_method_ids: "PaymentMethod"
    code_purl: str
    color: int
    comment: str
    commercial_company_name: str
    commercial_partner_id: "ResPartner"
    commissioning_close_date: Optional[_dt.date]
    companies_count: int
    company_group: str
    company_id: "ResCompany"
    company_ids: "ResCompany"
    company_name: str
    company_type: str
    complaint_index: str
    complete_contact_address: str
    complete_unsubscribe: bool
    connection_index: str
    contact_address: str
    contact_address_complete: str
    contact_case_ids: "HelpdeskTicket"
    contact_contract_ids: "SorgeniaContracts"
    contact_ids: "ResPartner"
    contact_index: str
    contact_interaction_count: int
    contact_interaction_ids: "SympleInteraction"
    contact_name: str
    contact_number: str
    contact_payment_ids: "ResPartnerPayment"
    contacts_for_quote_management: str
    contract_ids: "AccountAnalyticAccount"
    country: str
    country_code: str
    country_enforce_cities: bool
    country_id: "ResCountry"
    credit: float
    credit_limit: float
    credit_status: "CreditStatus"
    css_wizard: str
    cup: str
    currency_id: "ResCurrency"
    customer_care_category: str
    customer_group: str
    customer_rank: int
    customer_service_numbers_ids: "CustomerServiceNumbers"
    customer_termination_date: Optional[_dt.date]
    date: Optional[_dt.date]
    date_field_modified: Optional[_dt.datetime]
    date_sent_advice_client: Optional[_dt.datetime]
    date_sent_advice_credit_status: Optional[_dt.datetime]
    date_status_greener_changed: Optional[_dt.date]
    debit: float
    debit_limit: float
    denomination: str
    digital_index: str
    dispatch_zone_ids: "DistributorDispatchZone"
    distributor_code_ids: "DistributorCode"
    distributor_number: str
    document_attachment_back_id: bytes
    document_attachment_front_id: bytes
    document_count: int
    document_country: str
    document_date: Optional[_dt.date]
    document_deadline: Optional[_dt.date]
    document_from: str
    document_number: str
    economic_segment: str
    egon_city_id: str
    egon_house_number_id: str
    egon_street_id: str
    e_invoice: bool
    email: str
    email_formatted: str
    email_normalized: str
    employee: bool
    employees_count: str
    end_date_purl: Optional[_dt.datetime]
    end_date_status: Optional[_dt.date]
    end_validity_date: Optional[_dt.date]
    end_validity_is_split_iva: Optional[_dt.date]
    end_validity_iva_type: Optional[_dt.date]
    energy_source_used: str
    etichetta_tutelato: str
    eva_agency: str
    eva_code: str
    exclusivity_mandate: str
    expected_closing_date: Optional[_dt.date]
    expiration_date: Optional[_dt.date]
    export_credit_status_filter_timestamp: Optional[_dt.datetime]
    fax: str
    fiber_client_status: str
    fiber_service_point_ids: "ServicePoint"
    field_modified: str
    first_contract_id: "SorgeniaContracts"
    first_name: str
    firstname: str
    fiscal_code: str
    fiscal_code_back_id: bytes
    fiscal_code_front_id: bytes
    fiscal_info: str
    fl_managed_bus: bool
    fl_managed_res: bool
    floor: str
    fl_transporter: bool
    friend_referral_code: str
    function: str
    gas_type: str
    gender: str
    golden_key: str
    greeners_status: str
    greentech_pmi: str
    greetech_retail: str
    groups_count: int
    groups_id: "ResGroups"
    has_bit2publish_template: bool
    has_message: bool
    has_self_declared_data: bool
    has_unreconciled_entries: bool
    heating_technology: str
    heating_type: str
    helpdesk_target_closed: float
    helpdesk_target_rating: float
    helpdesk_target_success: float
    home_dimension: str
    home_tipology: str
    iban_purl: str
    identification_type: str
    id_login: str
    image_1024: bytes
    image_128: bytes
    image_1920: bytes
    image_256: bytes
    image_512: bytes
    image_medium: bytes
    im_status: str
    inbound_sorting_color: str
    incentive_compensation: bool
    index_history_ids: "IndexHistory"
    industry_id: "ResPartnerIndustry"
    info_msg_m2c: str
    insolvency_procedure_type: str
    instance_key: str
    instance_key_ids: "SymplePbInstanceKey"
    institution_name: str
    insurance_service: str
    intercom: str
    invoice_correction_index: str
    invoice_ids: "AccountMove"
    invoice_recipient_id: "ResPartner"
    invoice_type: str
    invoice_warn: str
    invoice_warn_msg: str
    ipa_code: str
    is_admin_user: bool
    is_agency: bool
    is_agency_valid: bool
    is_agent: bool
    is_automatic_appointment: bool
    is_back_office_close: bool
    is_blacklisted: bool
    is_client: bool
    is_commissioning_close: bool
    is_commodity_ele: bool
    is_commodity_fiber: bool
    is_commodity_gas: bool
    is_company: bool
    is_creating_from_migration: bool
    is_declaration_processed: bool
    is_distribution_date: Optional[_dt.date]
    is_distribution_list: bool
    is_distributor: bool
    is_editor_team: bool
    is_ele_vulnerability: bool
    is_ele_vulnerability_date: Optional[_dt.date]
    is_emobility: bool
    is_emobility_invoice: bool
    is_error_m2c: bool
    is_forceomocodia: bool
    is_front_end_close: bool
    is_gas_vulnerability: bool
    is_gas_vulnerability_date: Optional[_dt.date]
    is_gdpr_consent: bool
    is_gdpr_consent_date: Optional[_dt.date]
    is_greeners_permissions: bool
    is_habitual_exporter: bool
    is_in_blacklist: bool
    is_individual_client: bool
    is_infocamere_monitored: bool
    is_insolvent: bool
    is_multipoint: bool
    is_my_sorgenia_permissions: bool
    is_not_disalimentabile: bool
    is_not_subject_to_checks: bool
    is_operator_identifier: bool
    is_pmi: bool
    is_privacy_consent: bool
    is_prospect: bool
    is_residential_dgo: bool
    is_sace_warranty: bool
    is_selfcare: bool
    is_soft_spam: bool
    is_soft_spam_date: Optional[_dt.date]
    is_split_iva: bool
    is_subject: bool
    is_supplier: bool
    istat_code: str
    is_termination_blocked: bool
    is_top_customer: bool
    is_to_sync_with_m2c: bool
    is_turned_client: bool
    is_user: bool
    is_user_profiling: bool
    is_vip_strategy: bool
    is_withholding_tax: bool
    iva_activation_date: Optional[_dt.date]
    iva_change_date: Optional[_dt.date]
    iva_exemption_reason: str
    iva_rate: str
    iva_type: str
    job_position_id: "JobTitles"
    jolly_index: str
    journal_item_count: int
    keycloak_id: str
    lang: str
    last_agency_id: "ResPartner"
    last_name: str
    lastname: str
    last_sync_date: Optional[_dt.datetime]
    last_time_entries_checked: Optional[_dt.datetime]
    latest_agent_status_change_date: Optional[_dt.date]
    legal_fax_number: str
    legal_phone_number: str
    legal_rapresentative_name: str
    legal_rapresentative_surname: str
    letter_of_intent_count: int
    letter_of_intent_ids: "LetterOfIntent"
    liability_waiver_id: bytes
    log_ids: "ResUsersLog"
    login: str
    login_date: Optional[_dt.datetime]
    login_ids: "SorgeniaDigitalLogin"
    logistic_operator_type: str
    mandate_sign_date: Optional[_dt.date]
    mandate_validity_start_date: Optional[_dt.date]
    marginality_segment: str
    marketing_event_count: int
    market_type: str
    mass_market_end_date: Optional[_dt.date]
    mass_market_start_date: Optional[_dt.date]
    master_agency_id: "ResPartner"
    mdm_market: str
    meeting_count: int
    meeting_ids: "CalendarEvent"
    message_attachment_count: int
    message_bounce: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    mobile: str
    mobile_blacklisted: bool
    mobility_vehicle: str
    modified_by_operator: bool
    multi_service_index: str
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    name_purl: str
    name_variation_for_same_cf_iva: str
    nar_index: str
    new_password: str
    nielsen_area: str
    note: str
    notice_number: str
    notification_type: str
    numbers_only_vat: str
    nursery_index: str
    nuts1_id: "ResPartnerNuts"
    nuts2_id: "ResPartnerNuts"
    nuts3_id: "ResPartnerNuts"
    nuts4_id: "ResPartnerNuts"
    occupants: str
    ocn_token: str
    odoobot_failed: bool
    odoobot_state: str
    office_code: str
    onboarding_details: str
    operational_fax_number: str
    operational_phone_number: str
    owner_id: "ResUsers"
    pa_pec_email: str
    parent_agency_id: "ResPartner"
    parent_contact_name: str
    parent_id: "ResPartner"
    parent_name: str
    partner_gid: int
    partner_id: "ResPartner"
    partner_latitude: float
    partner_longitude: float
    partner_share: bool
    party_where_a_ids: "PartyRelation"
    party_where_b_ids: "PartyRelation"
    party_where_present: "PartyRelation"
    password: str
    payment_deadline: str
    payment_token_count: int
    payment_token_ids: "PaymentToken"
    pdr_code: str
    pdr_codes: str
    pdr_ids: "ResPartnerPdr"
    pec_email: str
    pec_email_infocamere: str
    permission_source: str
    permission_source_id: str
    phone: str
    phone_blacklisted: bool
    phone_mobile_search: str
    phone_sanitized: str
    phone_sanitized_blacklisted: bool
    photovoltaic: str
    plafond_amount: float
    pmi_attachment_id: bytes
    pmi_end_date: Optional[_dt.date]
    pmi_start_date: Optional[_dt.date]
    pod_code_distributor_history_ids: "DistributorPodCodeHistory"
    pod_codes: str
    pod_ids: "ResPartnerPod"
    pod_pdr_client_status: str
    pod_pdr_expired_total: float
    pod_pdr_recommended_limit: float
    postalizer_document_ids: "SorgeniaPostalizerDocument"
    priority: str
    privacy_date: Optional[_dt.date]
    privacy_history_ids: "PrivacyHistory"
    privacy_version: str
    property_account_payable_id: "AccountAccount"
    property_account_position_id: "AccountFiscalPosition"
    property_account_receivable_id: "AccountAccount"
    property_payment_method_id: "AccountPaymentMethod"
    property_payment_term_id: "AccountPaymentTerm"
    property_product_pricelist: "ProductPricelist"
    property_supplier_payment_term_id: "AccountPaymentTerm"
    proposal_token: str
    prospect_close_date: Optional[_dt.date]
    prospect_create_date: Optional[_dt.date]
    prospect_id: str
    prospect_type: str
    ptf_transfer: str
    purl: str
    reading_ids: "MeterReadings"
    ref: str
    ref_company_ids: "ResCompany"
    reference_manager_area_id: "ResPartner"
    reference_manager_greentech_area_id: "ResPartner"
    refering_account_customer: "ResPartner"
    region: str
    registration_date: Optional[_dt.date]
    registration_number: str
    registration_province: str
    resource_calendar_id: "ResourceCalendar"
    resource_ids: "ResourceResource"
    responsability_area: str
    res_users_settings_ids: "ResUsersSettings"
    rfid_card_ids: "RfidCard"
    rmp: float
    role: str
    rules_count: int
    sale_area_role_id: "SaleAreaRole"
    sale_channel_ids: "ChannelAssociation"
    sales_manager_id: "ResPartner"
    same_vat_partner_id: "ResPartner"
    saml_ids: "ResUsersSaml"
    score_index: str
    sdi_code: str
    security_role_ids: "SecurityRole"
    self: "ResPartner"
    selfcare_contact_ids: "ResPartner"
    service_point_codes: str
    service_point_ids: "ServicePoint"
    severity_index: str
    share: bool
    show_bit2publish_button: bool
    signature: str
    signup_expiration: Optional[_dt.datetime]
    signup_token: str
    signup_type: str
    signup_url: str
    signup_valid: bool
    sla_ids: "HelpdeskSla"
    social_bonus_instance_ids: "SocialBonusInstance"
    stairs: str
    start_date_status: Optional[_dt.date]
    start_validity_is_split_iva: Optional[_dt.date]
    start_validity_iva_type: Optional[_dt.date]
    state: str
    state_code: str
    state_id: "ResCountryState"
    stato_anagrafica: str
    status: str
    street: str
    street2: str
    street_num: str
    subject_type: str
    supplier_rank: int
    supply_type: str
    symphony_onboarding_requests: str
    tax_exemption_reason: str
    tax_rate: str
    team_ids: "ResPartnerTeam"
    teleselling_end_date: Optional[_dt.date]
    teleselling_start_date: Optional[_dt.date]
    termination_date: Optional[_dt.date]
    ticket_count: int
    title: "ResPartnerTitle"
    titleholder_role: str
    token_end_date: Optional[_dt.date]
    token_start_date: Optional[_dt.date]
    top_customer_flag_date: Optional[_dt.date]
    toponym_id: "ResToponym"
    total_client_status: str
    total_invoiced: float
    totp_enabled: bool
    totp_secret: str
    totp_trusted_device_ids: "AuthTotpDevice"
    training_course_end_date: Optional[_dt.date]
    training_course_end_hour: Optional[_dt.datetime]
    training_course_type: str
    training_status: str
    transporter_id: "ResPartnerTransporter"
    trust: str
    type: str
    tz: str
    tz_offset: str
    uni_office_code: str
    user_code: str
    user_id: "ResUsers"
    user_ids: "ResUsers"
    user_profiling_date: Optional[_dt.date]
    user_sequence: str
    user_type: str
    validity_date: Optional[_dt.date]
    vat: str
    wallet_management: str
    warranty_ids: "SorgeniaWarranty"
    website: str
    website_message_ids: "MailMessage"
    withholding_tax_code: str
    wizard_result: str
    zip: str
    zip_id: "ResCityZip"
    def browse(self, ids: Union[int, List[int]]) -> "ResUsers": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResUsers": ...
    def create(self, vals: Dict[str, Any]) -> "ResUsers": ...
    def filtered(self, func: Any) -> "ResUsers": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResUsers": ...
    def exists(self) -> "ResUsers": ...
    def sudo(self) -> "ResUsers": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResUsers": ...

# --- res.users.apikeys ---

class ResUsersApikeys(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    scope: str
    show_bit2publish_button: bool
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "ResUsersApikeys": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResUsersApikeys": ...
    def create(self, vals: Dict[str, Any]) -> "ResUsersApikeys": ...
    def filtered(self, func: Any) -> "ResUsersApikeys": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResUsersApikeys": ...
    def exists(self) -> "ResUsersApikeys": ...
    def sudo(self) -> "ResUsersApikeys": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResUsersApikeys": ...

# --- res.users.apikeys.description ---

class ResUsersApikeysDescription(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResUsersApikeysDescription": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResUsersApikeysDescription": ...
    def create(self, vals: Dict[str, Any]) -> "ResUsersApikeysDescription": ...
    def filtered(self, func: Any) -> "ResUsersApikeysDescription": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResUsersApikeysDescription": ...
    def exists(self) -> "ResUsersApikeysDescription": ...
    def sudo(self) -> "ResUsersApikeysDescription": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResUsersApikeysDescription": ...

# --- res.users.apikeys.show ---

class ResUsersApikeysShow(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    key: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResUsersApikeysShow": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResUsersApikeysShow": ...
    def create(self, vals: Dict[str, Any]) -> "ResUsersApikeysShow": ...
    def filtered(self, func: Any) -> "ResUsersApikeysShow": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResUsersApikeysShow": ...
    def exists(self) -> "ResUsersApikeysShow": ...
    def sudo(self) -> "ResUsersApikeysShow": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResUsersApikeysShow": ...

# --- res.users.identitycheck ---

class ResUsersIdentitycheck(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    password: str
    request: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResUsersIdentitycheck": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResUsersIdentitycheck": ...
    def create(self, vals: Dict[str, Any]) -> "ResUsersIdentitycheck": ...
    def filtered(self, func: Any) -> "ResUsersIdentitycheck": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResUsersIdentitycheck": ...
    def exists(self) -> "ResUsersIdentitycheck": ...
    def sudo(self) -> "ResUsersIdentitycheck": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResUsersIdentitycheck": ...

# --- res.users.log ---

class ResUsersLog(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ResUsersLog": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResUsersLog": ...
    def create(self, vals: Dict[str, Any]) -> "ResUsersLog": ...
    def filtered(self, func: Any) -> "ResUsersLog": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResUsersLog": ...
    def exists(self) -> "ResUsersLog": ...
    def sudo(self) -> "ResUsersLog": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResUsersLog": ...

# --- res.users.saml ---

class ResUsersSaml(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    saml_access_token: str
    saml_provider_id: "AuthSamlProvider"
    saml_uid: str
    show_bit2publish_button: bool
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "ResUsersSaml": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResUsersSaml": ...
    def create(self, vals: Dict[str, Any]) -> "ResUsersSaml": ...
    def filtered(self, func: Any) -> "ResUsersSaml": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResUsersSaml": ...
    def exists(self) -> "ResUsersSaml": ...
    def sudo(self) -> "ResUsersSaml": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResUsersSaml": ...

# --- res.users.settings ---

class ResUsersSettings(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    is_discuss_sidebar_category_channel_open: bool
    is_discuss_sidebar_category_chat_open: bool
    push_to_talk_key: str
    show_bit2publish_button: bool
    use_push_to_talk: bool
    user_id: "ResUsers"
    voice_active_duration: int
    volume_settings_ids: "ResUsersSettingsVolumes"
    def browse(self, ids: Union[int, List[int]]) -> "ResUsersSettings": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResUsersSettings": ...
    def create(self, vals: Dict[str, Any]) -> "ResUsersSettings": ...
    def filtered(self, func: Any) -> "ResUsersSettings": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResUsersSettings": ...
    def exists(self) -> "ResUsersSettings": ...
    def sudo(self) -> "ResUsersSettings": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResUsersSettings": ...

# --- res.users.settings.volumes ---

class ResUsersSettingsVolumes(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    guest_id: "ResPartner"
    has_bit2publish_template: bool
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    user_setting_id: "ResUsersSettings"
    volume: float
    def browse(self, ids: Union[int, List[int]]) -> "ResUsersSettingsVolumes": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResUsersSettingsVolumes": ...
    def create(self, vals: Dict[str, Any]) -> "ResUsersSettingsVolumes": ...
    def filtered(self, func: Any) -> "ResUsersSettingsVolumes": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResUsersSettingsVolumes": ...
    def exists(self) -> "ResUsersSettingsVolumes": ...
    def sudo(self) -> "ResUsersSettingsVolumes": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResUsersSettingsVolumes": ...

# --- reset.view.arch.wizard ---

class ResetViewArchWizard(Recordset):
    arch_diff: str
    arch_to_compare: str
    bit2publish_template_ids: "Bit2publishTemplate"
    compare_view_id: "IrUiView"
    has_bit2publish_template: bool
    has_diff: bool
    reset_mode: str
    show_bit2publish_button: bool
    view_id: "IrUiView"
    view_name: str
    def browse(self, ids: Union[int, List[int]]) -> "ResetViewArchWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResetViewArchWizard": ...
    def create(self, vals: Dict[str, Any]) -> "ResetViewArchWizard": ...
    def filtered(self, func: Any) -> "ResetViewArchWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResetViewArchWizard": ...
    def exists(self) -> "ResetViewArchWizard": ...
    def sudo(self) -> "ResetViewArchWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResetViewArchWizard": ...

# --- resource.calendar ---

class ResourceCalendar(Recordset):
    active: bool
    attendance_ids: "ResourceCalendarAttendance"
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    global_leave_ids: "ResourceCalendarLeaves"
    has_bit2publish_template: bool
    hours_per_day: float
    leave_ids: "ResourceCalendarLeaves"
    name: str
    show_bit2publish_button: bool
    two_weeks_calendar: bool
    two_weeks_explanation: str
    tz: str
    tz_offset: str
    def browse(self, ids: Union[int, List[int]]) -> "ResourceCalendar": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResourceCalendar": ...
    def create(self, vals: Dict[str, Any]) -> "ResourceCalendar": ...
    def filtered(self, func: Any) -> "ResourceCalendar": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResourceCalendar": ...
    def exists(self) -> "ResourceCalendar": ...
    def sudo(self) -> "ResourceCalendar": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResourceCalendar": ...

# --- resource.calendar.attendance ---

class ResourceCalendarAttendance(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    calendar_id: "ResourceCalendar"
    date_from: Optional[_dt.date]
    date_to: Optional[_dt.date]
    dayofweek: str
    day_period: str
    display_type: str
    has_bit2publish_template: bool
    hour_from: float
    hour_to: float
    name: str
    resource_id: "ResourceResource"
    sequence: int
    show_bit2publish_button: bool
    two_weeks_calendar: bool
    week_type: str
    def browse(self, ids: Union[int, List[int]]) -> "ResourceCalendarAttendance": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResourceCalendarAttendance": ...
    def create(self, vals: Dict[str, Any]) -> "ResourceCalendarAttendance": ...
    def filtered(self, func: Any) -> "ResourceCalendarAttendance": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResourceCalendarAttendance": ...
    def exists(self) -> "ResourceCalendarAttendance": ...
    def sudo(self) -> "ResourceCalendarAttendance": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResourceCalendarAttendance": ...

# --- resource.calendar.leaves ---

class ResourceCalendarLeaves(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    calendar_id: "ResourceCalendar"
    company_id: "ResCompany"
    date_from: Optional[_dt.datetime]
    date_to: Optional[_dt.datetime]
    has_bit2publish_template: bool
    name: str
    resource_id: "ResourceResource"
    show_bit2publish_button: bool
    time_type: str
    def browse(self, ids: Union[int, List[int]]) -> "ResourceCalendarLeaves": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResourceCalendarLeaves": ...
    def create(self, vals: Dict[str, Any]) -> "ResourceCalendarLeaves": ...
    def filtered(self, func: Any) -> "ResourceCalendarLeaves": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResourceCalendarLeaves": ...
    def exists(self) -> "ResourceCalendarLeaves": ...
    def sudo(self) -> "ResourceCalendarLeaves": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResourceCalendarLeaves": ...

# --- resource.mixin ---

class ResourceMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    has_bit2publish_template: bool
    resource_calendar_id: "ResourceCalendar"
    resource_id: "ResourceResource"
    show_bit2publish_button: bool
    tz: str
    def browse(self, ids: Union[int, List[int]]) -> "ResourceMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResourceMixin": ...
    def create(self, vals: Dict[str, Any]) -> "ResourceMixin": ...
    def filtered(self, func: Any) -> "ResourceMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResourceMixin": ...
    def exists(self) -> "ResourceMixin": ...
    def sudo(self) -> "ResourceMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResourceMixin": ...

# --- resource.resource ---

class ResourceResource(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    calendar_id: "ResourceCalendar"
    company_id: "ResCompany"
    has_bit2publish_template: bool
    name: str
    resource_type: str
    show_bit2publish_button: bool
    time_efficiency: float
    tz: str
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "ResourceResource": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResourceResource": ...
    def create(self, vals: Dict[str, Any]) -> "ResourceResource": ...
    def filtered(self, func: Any) -> "ResourceResource": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResourceResource": ...
    def exists(self) -> "ResourceResource": ...
    def sudo(self) -> "ResourceResource": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResourceResource": ...

# --- resource.test ---

class ResourceTest(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_id: "ResCompany"
    has_bit2publish_template: bool
    name: str
    resource_calendar_id: "ResourceCalendar"
    resource_id: "ResourceResource"
    show_bit2publish_button: bool
    tz: str
    def browse(self, ids: Union[int, List[int]]) -> "ResourceTest": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResourceTest": ...
    def create(self, vals: Dict[str, Any]) -> "ResourceTest": ...
    def filtered(self, func: Any) -> "ResourceTest": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResourceTest": ...
    def exists(self) -> "ResourceTest": ...
    def sudo(self) -> "ResourceTest": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResourceTest": ...

# --- result.channel.selector ---

class ResultChannelSelector(Recordset):
    allowed_phase_result_ids: "SympleTripletPhaseResult"
    bit2publish_template_ids: "Bit2publishTemplate"
    channel: str
    has_bit2publish_template: bool
    phase_id: "SympleTripletPhase"
    show_bit2publish_button: bool
    triplet_phase_result_id: "SympleTripletPhaseResult"
    def browse(self, ids: Union[int, List[int]]) -> "ResultChannelSelector": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResultChannelSelector": ...
    def create(self, vals: Dict[str, Any]) -> "ResultChannelSelector": ...
    def filtered(self, func: Any) -> "ResultChannelSelector": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResultChannelSelector": ...
    def exists(self) -> "ResultChannelSelector": ...
    def sudo(self) -> "ResultChannelSelector": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResultChannelSelector": ...

# --- result.code.configurator ---

class ResultCodeConfigurator(Recordset):
    allowed_phase_result_ids: "SympleTripletPhaseResult"
    bit2publish_template_ids: "Bit2publishTemplate"
    code_phase_id: "SympleTripletPhase"
    has_bit2publish_template: bool
    result_value: str
    show_bit2publish_button: bool
    triplet_phase_result_id: "SympleTripletPhaseResult"
    def browse(self, ids: Union[int, List[int]]) -> "ResultCodeConfigurator": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResultCodeConfigurator": ...
    def create(self, vals: Dict[str, Any]) -> "ResultCodeConfigurator": ...
    def filtered(self, func: Any) -> "ResultCodeConfigurator": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResultCodeConfigurator": ...
    def exists(self) -> "ResultCodeConfigurator": ...
    def sudo(self) -> "ResultCodeConfigurator": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResultCodeConfigurator": ...

# --- result.triplet.selector ---

class ResultTripletSelector(Recordset):
    allowed_phase_result_ids: "SympleTripletPhaseResult"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    phase_id: "SympleTripletPhase"
    show_bit2publish_button: bool
    ticket_type_ids: "HelpdeskTicketType"
    triplet_phase_result_id: "SympleTripletPhaseResult"
    workflow_id: "SympleWorkflow"
    def browse(self, ids: Union[int, List[int]]) -> "ResultTripletSelector": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResultTripletSelector": ...
    def create(self, vals: Dict[str, Any]) -> "ResultTripletSelector": ...
    def filtered(self, func: Any) -> "ResultTripletSelector": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResultTripletSelector": ...
    def exists(self) -> "ResultTripletSelector": ...
    def sudo(self) -> "ResultTripletSelector": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResultTripletSelector": ...

# --- result.type ---

class ResultType(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    technical_name: str
    def browse(self, ids: Union[int, List[int]]) -> "ResultType": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ResultType": ...
    def create(self, vals: Dict[str, Any]) -> "ResultType": ...
    def filtered(self, func: Any) -> "ResultType": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ResultType": ...
    def exists(self) -> "ResultType": ...
    def sudo(self) -> "ResultType": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ResultType": ...

# --- rfid.card ---

class RfidCard(Recordset):
    activation_date: Optional[_dt.datetime]
    bit2publish_template_ids: "Bit2publishTemplate"
    block_date: Optional[_dt.datetime]
    card_type: str
    deactivation_date: Optional[_dt.datetime]
    has_bit2publish_template: bool
    name: str
    order_code: str
    order_date: Optional[_dt.datetime]
    partner_id: "ResPartner"
    reconciliation_key: str
    rfid_code: str
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "RfidCard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RfidCard": ...
    def create(self, vals: Dict[str, Any]) -> "RfidCard": ...
    def filtered(self, func: Any) -> "RfidCard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RfidCard": ...
    def exists(self) -> "RfidCard": ...
    def sudo(self) -> "RfidCard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RfidCard": ...

# --- rip.model.access ---

class RipModelAccess(Recordset):
    access_rule_enabled: bool
    access_rule_id: "RipModelAccessRule"
    access_rule_target: str
    bit2publish_template_ids: "Bit2publishTemplate"
    expose_delete: bool
    expose_get: bool
    expose_post: bool
    expose_put: bool
    has_bit2publish_template: bool
    model_id: "IrModel"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "RipModelAccess": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipModelAccess": ...
    def create(self, vals: Dict[str, Any]) -> "RipModelAccess": ...
    def filtered(self, func: Any) -> "RipModelAccess": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipModelAccess": ...
    def exists(self) -> "RipModelAccess": ...
    def sudo(self) -> "RipModelAccess": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipModelAccess": ...

# --- rip.model.access.alias ---

class RipModelAccessAlias(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    model_id: "IrModel"
    model_name: str
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "RipModelAccessAlias": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipModelAccessAlias": ...
    def create(self, vals: Dict[str, Any]) -> "RipModelAccessAlias": ...
    def filtered(self, func: Any) -> "RipModelAccessAlias": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipModelAccessAlias": ...
    def exists(self) -> "RipModelAccessAlias": ...
    def sudo(self) -> "RipModelAccessAlias": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipModelAccessAlias": ...

# --- rip.model.access.rule ---

class RipModelAccessRule(Recordset):
    action: str
    bit2publish_template_ids: "Bit2publishTemplate"
    enabled: bool
    has_bit2publish_template: bool
    model_access_ids: "RipModelAccess"
    model_access_sudo: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    target: str
    user_ids: "ResUsers"
    users_all: bool
    def browse(self, ids: Union[int, List[int]]) -> "RipModelAccessRule": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipModelAccessRule": ...
    def create(self, vals: Dict[str, Any]) -> "RipModelAccessRule": ...
    def filtered(self, func: Any) -> "RipModelAccessRule": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipModelAccessRule": ...
    def exists(self) -> "RipModelAccessRule": ...
    def sudo(self) -> "RipModelAccessRule": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipModelAccessRule": ...

# --- rip.model.function.access ---

class RipModelFunctionAccess(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    description: str
    enabled: bool
    expose_delete: bool
    expose_get: bool
    expose_post: bool
    expose_put: bool
    has_bit2publish_template: bool
    model_id: "IrModel"
    model_name: str
    model_schema_in_id: "RipModelSchemaIn"
    model_schema_out_id: "RipModelSchemaOut"
    name: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "RipModelFunctionAccess": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipModelFunctionAccess": ...
    def create(self, vals: Dict[str, Any]) -> "RipModelFunctionAccess": ...
    def filtered(self, func: Any) -> "RipModelFunctionAccess": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipModelFunctionAccess": ...
    def exists(self) -> "RipModelFunctionAccess": ...
    def sudo(self) -> "RipModelFunctionAccess": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipModelFunctionAccess": ...

# --- rip.model.schema ---

class RipModelSchema(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    default: bool
    description: str
    enabled: bool
    field_ids: "RipModelSchemaField"
    has_bit2publish_template: bool
    model_id: "IrModel"
    model_name: str
    name: str
    override: bool
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "RipModelSchema": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipModelSchema": ...
    def create(self, vals: Dict[str, Any]) -> "RipModelSchema": ...
    def filtered(self, func: Any) -> "RipModelSchema": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipModelSchema": ...
    def exists(self) -> "RipModelSchema": ...
    def sudo(self) -> "RipModelSchema": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipModelSchema": ...

# --- rip.model.schema.field ---

class RipModelSchemaField(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    blank: bool
    has_bit2publish_template: bool
    model_field_id: "IrModelFields"
    model_field_name: str
    model_id: "IrModel"
    model_schema_id: "RipModelSchema"
    name: str
    required: bool
    sequence: int
    show_bit2publish_button: bool
    source: str
    type: str
    def browse(self, ids: Union[int, List[int]]) -> "RipModelSchemaField": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipModelSchemaField": ...
    def create(self, vals: Dict[str, Any]) -> "RipModelSchemaField": ...
    def filtered(self, func: Any) -> "RipModelSchemaField": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipModelSchemaField": ...
    def exists(self) -> "RipModelSchemaField": ...
    def sudo(self) -> "RipModelSchemaField": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipModelSchemaField": ...

# --- rip.model.schema.in ---

class RipModelSchemaIn(Recordset):
    all_records: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    default: bool
    description: str
    enabled: bool
    field_ids: "RipModelSchemaInField"
    has_bit2publish_template: bool
    id_required: bool
    model_id: "IrModel"
    model_name: str
    name: str
    override: bool
    sequence: int
    show_bit2publish_button: bool
    strict: bool
    x_studio_datetime_field_FYH8i: Optional[_dt.datetime]
    def browse(self, ids: Union[int, List[int]]) -> "RipModelSchemaIn": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipModelSchemaIn": ...
    def create(self, vals: Dict[str, Any]) -> "RipModelSchemaIn": ...
    def filtered(self, func: Any) -> "RipModelSchemaIn": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipModelSchemaIn": ...
    def exists(self) -> "RipModelSchemaIn": ...
    def sudo(self) -> "RipModelSchemaIn": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipModelSchemaIn": ...

# --- rip.model.schema.in.field ---

class RipModelSchemaInField(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    blank: bool
    has_bit2publish_template: bool
    model_field_id: "IrModelFields"
    model_field_name: str
    model_id: "IrModel"
    model_schema_id: "RipModelSchemaIn"
    name: str
    required: bool
    sequence: int
    show_bit2publish_button: bool
    source: str
    type: str
    def browse(self, ids: Union[int, List[int]]) -> "RipModelSchemaInField": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipModelSchemaInField": ...
    def create(self, vals: Dict[str, Any]) -> "RipModelSchemaInField": ...
    def filtered(self, func: Any) -> "RipModelSchemaInField": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipModelSchemaInField": ...
    def exists(self) -> "RipModelSchemaInField": ...
    def sudo(self) -> "RipModelSchemaInField": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipModelSchemaInField": ...

# --- rip.model.schema.out ---

class RipModelSchemaOut(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    default: bool
    description: str
    enabled: bool
    field_ids: "RipModelSchemaOutField"
    has_bit2publish_template: bool
    model_id: "IrModel"
    model_name: str
    name: str
    override: bool
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "RipModelSchemaOut": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipModelSchemaOut": ...
    def create(self, vals: Dict[str, Any]) -> "RipModelSchemaOut": ...
    def filtered(self, func: Any) -> "RipModelSchemaOut": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipModelSchemaOut": ...
    def exists(self) -> "RipModelSchemaOut": ...
    def sudo(self) -> "RipModelSchemaOut": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipModelSchemaOut": ...

# --- rip.model.schema.out.field ---

class RipModelSchemaOutField(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    blank: bool
    has_bit2publish_template: bool
    hidden: bool
    model_field_id: "IrModelFields"
    model_field_name: str
    model_id: "IrModel"
    model_schema_id: "RipModelSchemaOut"
    name: str
    related: str
    required: bool
    sequence: int
    show_bit2publish_button: bool
    source: str
    type: str
    def browse(self, ids: Union[int, List[int]]) -> "RipModelSchemaOutField": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipModelSchemaOutField": ...
    def create(self, vals: Dict[str, Any]) -> "RipModelSchemaOutField": ...
    def filtered(self, func: Any) -> "RipModelSchemaOutField": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipModelSchemaOutField": ...
    def exists(self) -> "RipModelSchemaOutField": ...
    def sudo(self) -> "RipModelSchemaOutField": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipModelSchemaOutField": ...

# --- rip.request.log ---

class RipRequestLog(Recordset):
    args: str
    bit2publish_template_ids: "Bit2publishTemplate"
    checksum: str
    content: str
    elapsed_time: float
    endpoint: str
    has_bit2publish_template: bool
    headers: str
    method: str
    response_content: str
    response_headers: str
    short_headers: str
    short_response_content: str
    short_response_headers: str
    show_bit2publish_button: bool
    status: int
    def browse(self, ids: Union[int, List[int]]) -> "RipRequestLog": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipRequestLog": ...
    def create(self, vals: Dict[str, Any]) -> "RipRequestLog": ...
    def filtered(self, func: Any) -> "RipRequestLog": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipRequestLog": ...
    def exists(self) -> "RipRequestLog": ...
    def sudo(self) -> "RipRequestLog": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipRequestLog": ...

# --- rip.token.handler ---

class RipTokenHandler(Recordset):
    access_token_exp: int
    algorithm: str
    bit2publish_template_ids: "Bit2publishTemplate"
    handler: str
    has_bit2publish_template: bool
    name: str
    refresh_token_exp: int
    secret: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "RipTokenHandler": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "RipTokenHandler": ...
    def create(self, vals: Dict[str, Any]) -> "RipTokenHandler": ...
    def filtered(self, func: Any) -> "RipTokenHandler": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "RipTokenHandler": ...
    def exists(self) -> "RipTokenHandler": ...
    def sudo(self) -> "RipTokenHandler": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "RipTokenHandler": ...

# --- sale.area.role ---

class SaleAreaRole(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SaleAreaRole": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SaleAreaRole": ...
    def create(self, vals: Dict[str, Any]) -> "SaleAreaRole": ...
    def filtered(self, func: Any) -> "SaleAreaRole": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SaleAreaRole": ...
    def exists(self) -> "SaleAreaRole": ...
    def sudo(self) -> "SaleAreaRole": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SaleAreaRole": ...

# --- sale.channel ---

class SaleChannel(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    bus_fiber: str
    ccq: str
    channel_association_ids: "ChannelAssociation"
    channel_code: str
    has_bit2publish_template: bool
    instant_call: str
    name: str
    no_standard: str
    payment_type: str
    product_change: str
    replay: str
    res_fiber: str
    residential_contract: bool
    show_bit2publish_button: bool
    standard: str
    verify_card: str
    def browse(self, ids: Union[int, List[int]]) -> "SaleChannel": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SaleChannel": ...
    def create(self, vals: Dict[str, Any]) -> "SaleChannel": ...
    def filtered(self, func: Any) -> "SaleChannel": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SaleChannel": ...
    def exists(self) -> "SaleChannel": ...
    def sudo(self) -> "SaleChannel": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SaleChannel": ...

# --- sale.channel.update ---

class SaleChannelUpdate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    channel: str
    channel_id: "SaleChannel"
    effective_date: Optional[_dt.date]
    error: str
    has_bit2publish_template: bool
    is_processed: bool
    pr_code: str
    processing_date: Optional[_dt.date]
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "SaleChannelUpdate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SaleChannelUpdate": ...
    def create(self, vals: Dict[str, Any]) -> "SaleChannelUpdate": ...
    def filtered(self, func: Any) -> "SaleChannelUpdate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SaleChannelUpdate": ...
    def exists(self) -> "SaleChannelUpdate": ...
    def sudo(self) -> "SaleChannelUpdate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SaleChannelUpdate": ...

# --- sale.channel.update.importer ---

class SaleChannelUpdateImporter(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SaleChannelUpdateImporter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SaleChannelUpdateImporter": ...
    def create(self, vals: Dict[str, Any]) -> "SaleChannelUpdateImporter": ...
    def filtered(self, func: Any) -> "SaleChannelUpdateImporter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SaleChannelUpdateImporter": ...
    def exists(self) -> "SaleChannelUpdateImporter": ...
    def sudo(self) -> "SaleChannelUpdateImporter": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SaleChannelUpdateImporter": ...

# --- save.spreadsheet.template ---

class SaveSpreadsheetTemplate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    template_name: str
    thumbnail: bytes
    def browse(self, ids: Union[int, List[int]]) -> "SaveSpreadsheetTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SaveSpreadsheetTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "SaveSpreadsheetTemplate": ...
    def filtered(self, func: Any) -> "SaveSpreadsheetTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SaveSpreadsheetTemplate": ...
    def exists(self) -> "SaveSpreadsheetTemplate": ...
    def sudo(self) -> "SaveSpreadsheetTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SaveSpreadsheetTemplate": ...

# --- security.role ---

class SecurityRole(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    color: int
    dashboard_permission_ids: "DashboardPermissionTable"
    dashboard_tab_configurator_ids: "DashboardVisibilityTable"
    group_ids: "ResGroups"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    user_ids: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "SecurityRole": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SecurityRole": ...
    def create(self, vals: Dict[str, Any]) -> "SecurityRole": ...
    def filtered(self, func: Any) -> "SecurityRole": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SecurityRole": ...
    def exists(self) -> "SecurityRole": ...
    def sudo(self) -> "SecurityRole": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SecurityRole": ...

# --- self.reading.wizard ---

class SelfReadingWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SelfReadingWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SelfReadingWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SelfReadingWizard": ...
    def filtered(self, func: Any) -> "SelfReadingWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SelfReadingWizard": ...
    def exists(self) -> "SelfReadingWizard": ...
    def sudo(self) -> "SelfReadingWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SelfReadingWizard": ...

# --- sequence.mixin ---

class SequenceMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    sequence_number: int
    sequence_prefix: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SequenceMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SequenceMixin": ...
    def create(self, vals: Dict[str, Any]) -> "SequenceMixin": ...
    def filtered(self, func: Any) -> "SequenceMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SequenceMixin": ...
    def exists(self) -> "SequenceMixin": ...
    def sudo(self) -> "SequenceMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SequenceMixin": ...

# --- service.mixin ---

class ServiceMixin(Recordset):
    activation_date: Optional[_dt.date]
    active: bool
    active_service_point_id: "ServicePoint"
    bit2publish_template_ids: "Bit2publishTemplate"
    client_ids: "ResPartner"
    code: str
    deactivation_date: Optional[_dt.date]
    has_bit2publish_template: bool
    last_active_service_point_id: "ServicePoint"
    service_point_ids: "ServicePoint"
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "ServiceMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ServiceMixin": ...
    def create(self, vals: Dict[str, Any]) -> "ServiceMixin": ...
    def filtered(self, func: Any) -> "ServiceMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ServiceMixin": ...
    def exists(self) -> "ServiceMixin": ...
    def sudo(self) -> "ServiceMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ServiceMixin": ...

# --- service.point ---

class ServicePoint(Recordset):
    acquisition_bid: str
    acquisition_channel: str
    activation_status: str
    active: bool
    additional_region_excise_duty: str
    agency_id: "ResPartner"
    agent_id: "ResPartner"
    area: str
    arera_section: str
    asset_id: str
    auxiliary: str
    auxiliary_at_date: Optional[_dt.date]
    auxiliary_from_date: Optional[_dt.date]
    available_power: float
    bandwidth: str
    belonging_lot: str
    billing_profile_id: "BillingProfile"
    billing_segment: str
    bit2publish_template_ids: "Bit2publishTemplate"
    bonus_type: str
    building_state: str
    ccq_result: str
    ccq_status: str
    channel_id: "SaleChannel"
    client_id: "ResPartner"
    code: str
    commodity: str
    company_code: str
    connection_type: str
    contract_id: "SorgeniaContracts"
    contract_state: bool
    cos: str
    credit_check_point_force_date: Optional[_dt.date]
    credit_check_point_result: str
    credit_check_point_result_date: Optional[_dt.date]
    credit_check_point_state: str
    customer_care_category: str
    date_sent_advice: Optional[_dt.datetime]
    declared_annual_usage: float
    description: str
    device_type: str
    distributor_annual_usage: str
    distributor_id: "ResPartner"
    distributor_name: str
    distributor_new_activation_result: str
    distributor_new_activation_time_slot: str
    distributor_practice_code: str
    download_bandwidth: int
    economic_segment: str
    engaged_power: float
    excise_duty_deposit_date: Optional[_dt.date]
    expected_supply_start_date: Optional[_dt.date]
    export_payment_method_filter_timestamp: Optional[_dt.datetime]
    fiber_migration_cc: str
    fiber_migration_number: str
    fiber_order_end_date: Optional[_dt.date]
    fibra_extra_cost: str
    fo_connection: str
    has_bit2publish_template: bool
    has_message: bool
    id_building: str
    ide2e: str
    id_event: str
    idr_code: str
    id_resource: str
    institution_name: str
    ipa_code: str
    is_bonus_and_misc: bool
    is_corrector: bool
    is_credit_check_point_force: bool
    is_direct: bool
    is_excluded_from_letter_of_intent: bool
    is_force_precheck: bool
    is_habitual_exporter: bool
    is_intensive_consumer: bool
    is_not_disconnectable: bool
    is_not_disconnectable_distributor: bool
    is_not_disconnectable_history_ids: "MailTrackingValue"
    is_owner: bool
    is_point_suspended: bool
    is_resident: bool
    is_safeguard: bool
    istat_code: str
    is_vulnerable: bool
    is_welcome_letter: bool
    iva_effective_date: Optional[_dt.date]
    iva_exemption_reason: str
    iva_rate: str
    iva_rate_ids: "ServicePointIvaRate"
    ko_precheck_reason: str
    mail_check_result: str
    marginality_segment: str
    market: str
    market_type: str
    mercato_di_provenienza: str
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    modem_shipping_address_id: "ResPartner"
    nar_distributor_request_date: Optional[_dt.date]
    natural_disasters_history_ids: "NaturalDisastersHistory"
    new_activation_start_date: Optional[_dt.date]
    nielsen_region: str
    not_disconnectable_category: str
    office_code: str
    old_firstname: str
    old_fiscal_code: str
    old_lastname: str
    old_name: str
    old_vat: str
    olo_profile: str
    order_status: str
    pa_deliberation_number: str
    parental_control_category: str
    parental_control_error_code: str
    parental_control_error_description: str
    parental_control_status: str
    parental_control_write_date: Optional[_dt.datetime]
    party_ids: "PartyRelation"
    pdr_id: "ResPartnerPdr"
    pdr_type: str
    phisical_bonus: str
    placeholder_service_id: "ServiceMixin"
    pod_id: "ResPartnerPod"
    pop_identifier: str
    precheck_result: str
    precheck_status: str
    previous_supplier: str
    pre_welcome_letter_date: Optional[_dt.date]
    pre_welcome_letter_status: str
    proposal_code: str
    reference_year: str
    regional_surcharge_code: str
    regional_surcharge_value: str
    request_type: str
    resolution_type: str
    service: str
    service_address: str
    service_apartment_number: str
    service_city_id: "ResCity"
    service_country_id: "ResCountry"
    service_egon_city_id: str
    service_egon_house_number_id: str
    service_egon_street_id: str
    service_floor: str
    service_model_id: "IrModel"
    service_model_name: str
    service_name: str
    service_region: str
    service_stairs: str
    service_state_code: str
    service_state_id: "ResCountryState"
    service_street: str
    service_street_number: str
    service_toponym_id: "ResToponym"
    service_zip: str
    show_bit2publish_button: bool
    show_pdr: bool
    show_pod: bool
    social_bonus: str
    social_bonus_eco: str
    sp_activated_date: Optional[_dt.date]
    srgsalna_category: str
    state: str
    sub_agency_id: "ResPartner"
    supply_end_date: Optional[_dt.date]
    supply_start_date: Optional[_dt.date]
    supply_termination_reason: str
    switch_result: str
    tariff_code: str
    tariff_code_mecoms: str
    tax_break_class: str
    tax_break_end_date: Optional[_dt.date]
    tax_break_start_date: Optional[_dt.date]
    tax_effective_date: Optional[_dt.date]
    tax_exemption_reason: str
    tax_rate: str
    tax_rate_pdr_ids: "ServicePointTaxRatePdr"
    tax_rate_pod_ids: "ServicePointTaxRatePod"
    tenancy_type: str
    tension: str
    tension_mecoms: str
    termination_request_type: str
    territorial_bonus_end_date: Optional[_dt.date]
    territorial_bonus_start_date: Optional[_dt.date]
    update_data: str
    upload_bandwidth: int
    upsa: str
    upsa_at_date: Optional[_dt.date]
    upsa_from_date: Optional[_dt.date]
    use_category: str
    use_type: str
    use_type_edit_date: Optional[_dt.date]
    vas_rate: str
    voucher: str
    vulnerability_history_ids: "VulnerabilityHistory"
    website_message_ids: "MailMessage"
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
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ServicePoint": ...

# --- service.point.address.mixin ---

class ServicePointAddressMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    istat_code: str
    nielsen_region: str
    service_address: str
    service_apartment_number: str
    service_city_id: "ResCity"
    service_country_id: "ResCountry"
    service_egon_city_id: str
    service_egon_house_number_id: str
    service_egon_street_id: str
    service_floor: str
    service_region: str
    service_stairs: str
    service_state_code: str
    service_state_id: "ResCountryState"
    service_street: str
    service_street_number: str
    service_toponym_id: "ResToponym"
    service_zip: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ServicePointAddressMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ServicePointAddressMixin": ...
    def create(self, vals: Dict[str, Any]) -> "ServicePointAddressMixin": ...
    def filtered(self, func: Any) -> "ServicePointAddressMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ServicePointAddressMixin": ...
    def exists(self) -> "ServicePointAddressMixin": ...
    def sudo(self) -> "ServicePointAddressMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ServicePointAddressMixin": ...

# --- service.point.iva.rate ---

class ServicePointIvaRate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    edited_at: Optional[_dt.datetime]
    edited_at_is_null: bool
    has_bit2publish_template: bool
    iva_change_effective_date: Optional[_dt.date]
    iva_exemption_reason: str
    iva_rate: int
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ServicePointIvaRate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ServicePointIvaRate": ...
    def create(self, vals: Dict[str, Any]) -> "ServicePointIvaRate": ...
    def filtered(self, func: Any) -> "ServicePointIvaRate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ServicePointIvaRate": ...
    def exists(self) -> "ServicePointIvaRate": ...
    def sudo(self) -> "ServicePointIvaRate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ServicePointIvaRate": ...

# --- service.point.migration.result ---

class ServicePointMigrationResult(Recordset):
    activation_date: Optional[_dt.date]
    asset_id: str
    available_power: str
    bit2publish_template_ids: "Bit2publishTemplate"
    client: "ResPartner"
    client_id: str
    code: str
    contract: "SorgeniaContracts"
    contract_id: str
    engaged_power: str
    failing_message: str
    failing_point: str
    has_bit2publish_template: bool
    pod: "ResPartnerPod"
    pod_id: str
    pr_code: str
    result: str
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    state: str
    supply_end_date: Optional[_dt.date]
    supply_start_date: Optional[_dt.date]
    tension: str
    def browse(self, ids: Union[int, List[int]]) -> "ServicePointMigrationResult": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ServicePointMigrationResult": ...
    def create(self, vals: Dict[str, Any]) -> "ServicePointMigrationResult": ...
    def filtered(self, func: Any) -> "ServicePointMigrationResult": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ServicePointMigrationResult": ...
    def exists(self) -> "ServicePointMigrationResult": ...
    def sudo(self) -> "ServicePointMigrationResult": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ServicePointMigrationResult": ...

# --- service.point.tax.rate.pdr ---

class ServicePointTaxRatePdr(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_code: str
    edited_at: Optional[_dt.datetime]
    edited_at_is_null: bool
    effective_start_date: Optional[_dt.date]
    exclusion_percentage: float
    fixed_annual_consumption: float
    has_bit2publish_template: bool
    industrial_use_percentage: float
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    state_tax: str
    def browse(self, ids: Union[int, List[int]]) -> "ServicePointTaxRatePdr": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ServicePointTaxRatePdr": ...
    def create(self, vals: Dict[str, Any]) -> "ServicePointTaxRatePdr": ...
    def filtered(self, func: Any) -> "ServicePointTaxRatePdr": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ServicePointTaxRatePdr": ...
    def exists(self) -> "ServicePointTaxRatePdr": ...
    def sudo(self) -> "ServicePointTaxRatePdr": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ServicePointTaxRatePdr": ...

# --- service.point.tax.rate.pod ---

class ServicePointTaxRatePod(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    company_code: str
    edited_at: Optional[_dt.datetime]
    edited_at_is_null: bool
    excise_change_effective_date: Optional[_dt.date]
    exemption_reason: str
    has_bit2publish_template: bool
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    tax_rate: str
    def browse(self, ids: Union[int, List[int]]) -> "ServicePointTaxRatePod": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ServicePointTaxRatePod": ...
    def create(self, vals: Dict[str, Any]) -> "ServicePointTaxRatePod": ...
    def filtered(self, func: Any) -> "ServicePointTaxRatePod": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ServicePointTaxRatePod": ...
    def exists(self) -> "ServicePointTaxRatePod": ...
    def sudo(self) -> "ServicePointTaxRatePod": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ServicePointTaxRatePod": ...

# --- set.phase ---

class SetPhase(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    has_message: bool
    info_message: str
    is_phase_result_wizard: bool
    is_phase_wizard: bool
    show_bit2publish_button: bool
    ticket_id: "HelpdeskTicket"
    triplet_active_phase_id: "SympleTripletPhase"
    triplet_allowed_phase_ids: "SympleTripletPhase"
    triplet_allowed_phase_result_ids: "SympleTripletPhaseResult"
    triplet_phase_id: "SympleTripletPhase"
    triplet_phase_result_domain: "SympleTripletPhaseResult"
    triplet_phase_result_id: "SympleTripletPhaseResult"
    unsuccess_reason_id: "SympleTripletUnsuccessReason"
    unsuccess_reason_ids: "SympleTripletUnsuccessReason"
    workflow_id: "SympleWorkflow"
    def browse(self, ids: Union[int, List[int]]) -> "SetPhase": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SetPhase": ...
    def create(self, vals: Dict[str, Any]) -> "SetPhase": ...
    def filtered(self, func: Any) -> "SetPhase": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SetPhase": ...
    def exists(self) -> "SetPhase": ...
    def sudo(self) -> "SetPhase": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SetPhase": ...

# --- sii.report ---

class SiiReport(Recordset):
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    lines: int
    lines_awaiting_response: int
    lines_with_ko_response: int
    lines_with_ok_response: int
    rai_fee_line_ids: "RaiFeeLine"
    response_attachment_id: "IrAttachment"
    sent_to_sii: bool
    sent_to_sii_error: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SiiReport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SiiReport": ...
    def create(self, vals: Dict[str, Any]) -> "SiiReport": ...
    def filtered(self, func: Any) -> "SiiReport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SiiReport": ...
    def exists(self) -> "SiiReport": ...
    def sudo(self) -> "SiiReport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SiiReport": ...

# --- sms.api ---

class SmsApi(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SmsApi": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SmsApi": ...
    def create(self, vals: Dict[str, Any]) -> "SmsApi": ...
    def filtered(self, func: Any) -> "SmsApi": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SmsApi": ...
    def exists(self) -> "SmsApi": ...
    def sudo(self) -> "SmsApi": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SmsApi": ...

# --- sms.cancel ---

class SmsCancel(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    help_message: str
    model: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SmsCancel": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SmsCancel": ...
    def create(self, vals: Dict[str, Any]) -> "SmsCancel": ...
    def filtered(self, func: Any) -> "SmsCancel": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SmsCancel": ...
    def exists(self) -> "SmsCancel": ...
    def sudo(self) -> "SmsCancel": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SmsCancel": ...

# --- sms.composer ---

class SmsComposer(Recordset):
    active_domain: str
    active_domain_count: int
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    comment_single_recipient: bool
    composition_mode: str
    has_bit2publish_template: bool
    mailing_id: "MailingMailing"
    marketing_activity_id: "MarketingActivity"
    mass_force_send: bool
    mass_keep_log: bool
    mass_sms_allow_unsubscribe: bool
    mass_use_blacklist: bool
    number_field_name: str
    numbers: str
    recipient_invalid_count: int
    recipient_single_description: str
    recipient_single_number: str
    recipient_single_number_itf: str
    recipient_single_valid: bool
    recipient_valid_count: int
    res_id: int
    res_ids: str
    res_ids_count: int
    res_model: str
    sanitized_numbers: str
    show_bit2publish_button: bool
    template_id: "SmsTemplate"
    use_active_domain: bool
    utm_campaign_id: "UtmCampaign"
    def browse(self, ids: Union[int, List[int]]) -> "SmsComposer": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SmsComposer": ...
    def create(self, vals: Dict[str, Any]) -> "SmsComposer": ...
    def filtered(self, func: Any) -> "SmsComposer": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SmsComposer": ...
    def exists(self) -> "SmsComposer": ...
    def sudo(self) -> "SmsComposer": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SmsComposer": ...

# --- sms.resend ---

class SmsResend(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    has_cancel: bool
    has_insufficient_credit: bool
    has_unregistered_account: bool
    mail_message_id: "MailMessage"
    recipient_ids: "SmsResendRecipient"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SmsResend": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SmsResend": ...
    def create(self, vals: Dict[str, Any]) -> "SmsResend": ...
    def filtered(self, func: Any) -> "SmsResend": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SmsResend": ...
    def exists(self) -> "SmsResend": ...
    def sudo(self) -> "SmsResend": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SmsResend": ...

# --- sms.resend.recipient ---

class SmsResendRecipient(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    failure_type: str
    has_bit2publish_template: bool
    notification_id: "MailNotification"
    partner_id: "ResPartner"
    partner_name: str
    resend: bool
    show_bit2publish_button: bool
    sms_number: str
    sms_resend_id: "SmsResend"
    def browse(self, ids: Union[int, List[int]]) -> "SmsResendRecipient": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SmsResendRecipient": ...
    def create(self, vals: Dict[str, Any]) -> "SmsResendRecipient": ...
    def filtered(self, func: Any) -> "SmsResendRecipient": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SmsResendRecipient": ...
    def exists(self) -> "SmsResendRecipient": ...
    def sudo(self) -> "SmsResendRecipient": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SmsResendRecipient": ...

# --- sms.sms ---

class SmsSms(Recordset):
    active_phase_id: "SympleTripletPhase"
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    case_trigger: str
    customer_code: str
    error_message: str
    failure_type: str
    has_bit2publish_template: bool
    id_transaction: str
    is_readonly: bool
    mailing_id: "MailingMailing"
    mailing_trace_ids: "MailingTrace"
    mail_message_id: "MailMessage"
    number: str
    partner_id: "ResPartner"
    process_name: str
    sent_datetime: Optional[_dt.datetime]
    sent_to_doxee: bool
    show_bit2publish_button: bool
    state: str
    ticket_close_date: Optional[_dt.datetime]
    ticket_create_date: Optional[_dt.datetime]
    ticket_id: "HelpdeskTicket"
    ticket_type_id: "HelpdeskTicketType"
    ticket_write_date: Optional[_dt.datetime]
    triplet_subtype_id: "SympleTripletSubtype"
    triplet_type_id: "SympleTripletType"
    def browse(self, ids: Union[int, List[int]]) -> "SmsSms": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SmsSms": ...
    def create(self, vals: Dict[str, Any]) -> "SmsSms": ...
    def filtered(self, func: Any) -> "SmsSms": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SmsSms": ...
    def exists(self) -> "SmsSms": ...
    def sudo(self) -> "SmsSms": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SmsSms": ...

# --- sms.template ---

class SmsTemplate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    copyvalue: str
    has_bit2publish_template: bool
    is_created_from_marketing_automation: bool
    is_set_sms_to: bool
    lang: str
    model: str
    model_id: "IrModel"
    model_object_field: "IrModelFields"
    name: str
    null_value: str
    render_model: str
    show_bit2publish_button: bool
    sidebar_action_id: "IrActionsActWindow"
    sms_to: str
    sub_model_object_field: "IrModelFields"
    sub_object: "IrModel"
    def browse(self, ids: Union[int, List[int]]) -> "SmsTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SmsTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "SmsTemplate": ...
    def filtered(self, func: Any) -> "SmsTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SmsTemplate": ...
    def exists(self) -> "SmsTemplate": ...
    def sudo(self) -> "SmsTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SmsTemplate": ...

# --- sms.template.preview ---

class SmsTemplatePreview(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    has_bit2publish_template: bool
    lang: str
    model_id: "IrModel"
    no_record: bool
    resource_ref: Any
    show_bit2publish_button: bool
    sms_template_id: "SmsTemplate"
    def browse(self, ids: Union[int, List[int]]) -> "SmsTemplatePreview": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SmsTemplatePreview": ...
    def create(self, vals: Dict[str, Any]) -> "SmsTemplatePreview": ...
    def filtered(self, func: Any) -> "SmsTemplatePreview": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SmsTemplatePreview": ...
    def exists(self) -> "SmsTemplatePreview": ...
    def sudo(self) -> "SmsTemplatePreview": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SmsTemplatePreview": ...

# --- sms.ticket.composer ---

class SmsTicketComposer(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    has_bit2publish_template: bool
    number: str
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    ticket_id: "HelpdeskTicket"
    def browse(self, ids: Union[int, List[int]]) -> "SmsTicketComposer": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SmsTicketComposer": ...
    def create(self, vals: Dict[str, Any]) -> "SmsTicketComposer": ...
    def filtered(self, func: Any) -> "SmsTicketComposer": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SmsTicketComposer": ...
    def exists(self) -> "SmsTicketComposer": ...
    def sudo(self) -> "SmsTicketComposer": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SmsTicketComposer": ...

# --- snailmail.confirm ---

class SnailmailConfirm(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    model_name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SnailmailConfirm": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SnailmailConfirm": ...
    def create(self, vals: Dict[str, Any]) -> "SnailmailConfirm": ...
    def filtered(self, func: Any) -> "SnailmailConfirm": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SnailmailConfirm": ...
    def exists(self) -> "SnailmailConfirm": ...
    def sudo(self) -> "SnailmailConfirm": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SnailmailConfirm": ...

# --- snailmail.confirm.invoice ---

class SnailmailConfirmInvoice(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    invoice_send_id: "AccountInvoiceSend"
    model_name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SnailmailConfirmInvoice": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SnailmailConfirmInvoice": ...
    def create(self, vals: Dict[str, Any]) -> "SnailmailConfirmInvoice": ...
    def filtered(self, func: Any) -> "SnailmailConfirmInvoice": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SnailmailConfirmInvoice": ...
    def exists(self) -> "SnailmailConfirmInvoice": ...
    def sudo(self) -> "SnailmailConfirmInvoice": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SnailmailConfirmInvoice": ...

# --- snailmail.letter ---

class SnailmailLetter(Recordset):
    attachment_datas: bytes
    attachment_fname: str
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    city: str
    color: bool
    company_id: "ResCompany"
    country_id: "ResCountry"
    cover: bool
    duplex: bool
    error_code: str
    has_bit2publish_template: bool
    info_msg: str
    message_id: "MailMessage"
    model: str
    notification_ids: "MailNotification"
    partner_id: "ResPartner"
    reference: str
    report_template: "IrActionsReport"
    res_id: int
    show_bit2publish_button: bool
    state: str
    state_id: "ResCountryState"
    street: str
    street2: str
    user_id: "ResUsers"
    zip: str
    def browse(self, ids: Union[int, List[int]]) -> "SnailmailLetter": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SnailmailLetter": ...
    def create(self, vals: Dict[str, Any]) -> "SnailmailLetter": ...
    def filtered(self, func: Any) -> "SnailmailLetter": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SnailmailLetter": ...
    def exists(self) -> "SnailmailLetter": ...
    def sudo(self) -> "SnailmailLetter": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SnailmailLetter": ...

# --- snailmail.letter.cancel ---

class SnailmailLetterCancel(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    help_message: str
    model: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SnailmailLetterCancel": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SnailmailLetterCancel": ...
    def create(self, vals: Dict[str, Any]) -> "SnailmailLetterCancel": ...
    def filtered(self, func: Any) -> "SnailmailLetterCancel": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SnailmailLetterCancel": ...
    def exists(self) -> "SnailmailLetterCancel": ...
    def sudo(self) -> "SnailmailLetterCancel": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SnailmailLetterCancel": ...

# --- snailmail.letter.format.error ---

class SnailmailLetterFormatError(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    message_id: "MailMessage"
    show_bit2publish_button: bool
    snailmail_cover: bool
    def browse(self, ids: Union[int, List[int]]) -> "SnailmailLetterFormatError": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SnailmailLetterFormatError": ...
    def create(self, vals: Dict[str, Any]) -> "SnailmailLetterFormatError": ...
    def filtered(self, func: Any) -> "SnailmailLetterFormatError": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SnailmailLetterFormatError": ...
    def exists(self) -> "SnailmailLetterFormatError": ...
    def sudo(self) -> "SnailmailLetterFormatError": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SnailmailLetterFormatError": ...

# --- snailmail.letter.missing.required.fields ---

class SnailmailLetterMissingRequiredFields(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    city: str
    country_id: "ResCountry"
    has_bit2publish_template: bool
    letter_id: "SnailmailLetter"
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    state_id: "ResCountryState"
    street: str
    street2: str
    zip: str
    def browse(self, ids: Union[int, List[int]]) -> "SnailmailLetterMissingRequiredFields": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SnailmailLetterMissingRequiredFields": ...
    def create(self, vals: Dict[str, Any]) -> "SnailmailLetterMissingRequiredFields": ...
    def filtered(self, func: Any) -> "SnailmailLetterMissingRequiredFields": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SnailmailLetterMissingRequiredFields": ...
    def exists(self) -> "SnailmailLetterMissingRequiredFields": ...
    def sudo(self) -> "SnailmailLetterMissingRequiredFields": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SnailmailLetterMissingRequiredFields": ...

# --- social.bonus ---

class SocialBonus(Recordset):
    attachment_ids: "IrAttachment"
    attachment_infobox: str
    attachment_warning: str
    bit2publish_template_ids: "Bit2publishTemplate"
    bonus_type: str
    commodity: str
    error: str
    file_line_ids: "SocialBonusFileLine"
    has_bit2publish_template: bool
    last_processed_line: int
    line_ids: "SocialBonusLine"
    month: str
    name: str
    origin: str
    service_type: str
    show_bit2publish_button: bool
    state: str
    year: str
    zip_attachment_ids: "IrAttachment"
    def browse(self, ids: Union[int, List[int]]) -> "SocialBonus": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SocialBonus": ...
    def create(self, vals: Dict[str, Any]) -> "SocialBonus": ...
    def filtered(self, func: Any) -> "SocialBonus": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SocialBonus": ...
    def exists(self) -> "SocialBonus": ...
    def sudo(self) -> "SocialBonus": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SocialBonus": ...

# --- social.bonus.file.line ---

class SocialBonusFileLine(Recordset):
    anno_validita: str
    attachment_create_date: Optional[_dt.datetime]
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    case_ids: "HelpdeskTicket"
    cf: str
    client_fiscal_code: str
    client_id: "ResPartner"
    cod_bonus: str
    cod_causale: str
    cod_causale_segnalazione: str
    cod_pdr: str
    cod_pod: str
    commodity: str
    data_cessazione: Optional[_dt.date]
    data_fine: Optional[_dt.date]
    data_inizio: Optional[_dt.date]
    has_bit2publish_template: bool
    month: str
    motivazione: str
    pdr_id: "ResPartnerPdr"
    pod_id: "ResPartnerPod"
    regime_compensazione: str
    service_type: str
    show_bit2publish_button: bool
    social_bonus_id: "SocialBonus"
    state: str
    tipo_comunicazione: str
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "SocialBonusFileLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SocialBonusFileLine": ...
    def create(self, vals: Dict[str, Any]) -> "SocialBonusFileLine": ...
    def filtered(self, func: Any) -> "SocialBonusFileLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SocialBonusFileLine": ...
    def exists(self) -> "SocialBonusFileLine": ...
    def sudo(self) -> "SocialBonusFileLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SocialBonusFileLine": ...

# --- social.bonus.instance ---

class SocialBonusInstance(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    cancelled_by_line_id: "SocialBonusLine"
    client_id: "ResPartner"
    cod_bonus: str
    created_by_line_id: "SocialBonusLine"
    end_date: Optional[_dt.date]
    ended_by_line_id: "SocialBonusLine"
    has_bit2publish_template: bool
    pdp_code: str
    pdr_id: "ResPartnerPdr"
    pod_id: "ResPartnerPod"
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    start_date: Optional[_dt.date]
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "SocialBonusInstance": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SocialBonusInstance": ...
    def create(self, vals: Dict[str, Any]) -> "SocialBonusInstance": ...
    def filtered(self, func: Any) -> "SocialBonusInstance": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SocialBonusInstance": ...
    def exists(self) -> "SocialBonusInstance": ...
    def sudo(self) -> "SocialBonusInstance": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SocialBonusInstance": ...

# --- social.bonus.line ---

class SocialBonusLine(Recordset):
    anno_validita: str
    attachment_create_date: Optional[_dt.datetime]
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    case_ids: "HelpdeskTicket"
    cf: str
    client_fiscal_code: str
    client_id: "ResPartner"
    cod_bonus: str
    cod_causale: str
    cod_causale_segnalazione: str
    cod_pdr: str
    cod_pod: str
    commodity: str
    data_cessazione: Optional[_dt.date]
    data_fine: Optional[_dt.date]
    data_inizio: Optional[_dt.date]
    error: str
    has_bit2publish_template: bool
    month: str
    motivazione: str
    name: str
    notification_ids: "SocialBonusNotification"
    pdr_id: "ResPartnerPdr"
    pod_id: "ResPartnerPod"
    regime_compensazione: str
    service_point_id: "ServicePoint"
    service_type: str
    show_bit2publish_button: bool
    social_bonus_file_line_id: "SocialBonusFileLine"
    social_bonus_id: "SocialBonus"
    state: str
    tipo_comunicazione: str
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "SocialBonusLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SocialBonusLine": ...
    def create(self, vals: Dict[str, Any]) -> "SocialBonusLine": ...
    def filtered(self, func: Any) -> "SocialBonusLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SocialBonusLine": ...
    def exists(self) -> "SocialBonusLine": ...
    def sudo(self) -> "SocialBonusLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SocialBonusLine": ...

# --- social.bonus.notification ---

class SocialBonusNotification(Recordset):
    anno_validita: str
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    case_id: "HelpdeskTicket"
    cf: str
    client_fiscal_code: str
    client_id: "ResPartner"
    cod_bonus: str
    cod_causale_segnalazione: str
    cod_pdr: str
    cod_pod: str
    commodity: str
    data_cessazione: Optional[_dt.date]
    data_fine: Optional[_dt.date]
    data_inizio: Optional[_dt.date]
    error: str
    has_bit2publish_template: bool
    month: str
    motivazione: str
    name: str
    notification_date: Optional[_dt.date]
    notification_sii_report_id: "SocialBonusSiiReport"
    notification_sii_report_month: str
    notification_sii_report_year: str
    origin: str
    pdr_id: "ResPartnerPdr"
    pod_id: "ResPartnerPod"
    regime_compensazione: str
    sbl_error: str
    show_bit2publish_button: bool
    social_bonus_line_id: "SocialBonusLine"
    social_bonus_notification_result_line_ids: "SocialBonusNotificationResultLine"
    state: str
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "SocialBonusNotification": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SocialBonusNotification": ...
    def create(self, vals: Dict[str, Any]) -> "SocialBonusNotification": ...
    def filtered(self, func: Any) -> "SocialBonusNotification": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SocialBonusNotification": ...
    def exists(self) -> "SocialBonusNotification": ...
    def sudo(self) -> "SocialBonusNotification": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SocialBonusNotification": ...

# --- social.bonus.notification.result ---

class SocialBonusNotificationResult(Recordset):
    attachment_ids: "IrAttachment"
    attachment_infobox: str
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity: str
    error: str
    has_bit2publish_template: bool
    last_processed_line: int
    line_ids: "SocialBonusNotificationResultLine"
    month: str
    name: str
    origin: str
    show_bit2publish_button: bool
    state: str
    year: str
    zip_attachment_ids: "IrAttachment"
    def browse(self, ids: Union[int, List[int]]) -> "SocialBonusNotificationResult": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SocialBonusNotificationResult": ...
    def create(self, vals: Dict[str, Any]) -> "SocialBonusNotificationResult": ...
    def filtered(self, func: Any) -> "SocialBonusNotificationResult": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SocialBonusNotificationResult": ...
    def exists(self) -> "SocialBonusNotificationResult": ...
    def sudo(self) -> "SocialBonusNotificationResult": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SocialBonusNotificationResult": ...

# --- social.bonus.notification.result.line ---

class SocialBonusNotificationResultLine(Recordset):
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    case_id: "HelpdeskTicket"
    client_id: "ResPartner"
    cod_bonus: str
    cod_causale: str
    cod_pdr: str
    cod_pod: str
    commodity: str
    create_date_as_date: Optional[_dt.date]
    error: str
    has_bit2publish_template: bool
    month: str
    motivazione: str
    name: str
    notification_id: "SocialBonusNotification"
    notification_result_id: "SocialBonusNotificationResult"
    pdr_id: "ResPartnerPdr"
    pod_id: "ResPartnerPod"
    show_bit2publish_button: bool
    state: str
    verifica_amm: str
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "SocialBonusNotificationResultLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SocialBonusNotificationResultLine": ...
    def create(self, vals: Dict[str, Any]) -> "SocialBonusNotificationResultLine": ...
    def filtered(self, func: Any) -> "SocialBonusNotificationResultLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SocialBonusNotificationResultLine": ...
    def exists(self) -> "SocialBonusNotificationResultLine": ...
    def sudo(self) -> "SocialBonusNotificationResultLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SocialBonusNotificationResultLine": ...

# --- social.bonus.result ---

class SocialBonusResult(Recordset):
    attachment_ids: "IrAttachment"
    attachment_infobox: str
    attachment_warning: str
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity: str
    error: str
    has_bit2publish_template: bool
    last_processed_line: int
    line_ids: "SocialBonusResultLine"
    month: str
    name: str
    origin: str
    show_bit2publish_button: bool
    state: str
    year: str
    zip_attachment_ids: "IrAttachment"
    def browse(self, ids: Union[int, List[int]]) -> "SocialBonusResult": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SocialBonusResult": ...
    def create(self, vals: Dict[str, Any]) -> "SocialBonusResult": ...
    def filtered(self, func: Any) -> "SocialBonusResult": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SocialBonusResult": ...
    def exists(self) -> "SocialBonusResult": ...
    def sudo(self) -> "SocialBonusResult": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SocialBonusResult": ...

# --- social.bonus.result.line ---

class SocialBonusResultLine(Recordset):
    attachment_create_date: Optional[_dt.datetime]
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    cod_bonus: str
    commodity: str
    error: str
    esito: str
    has_bit2publish_template: bool
    linked_bonus_line_ids: "SocialBonusLine"
    month: str
    name: str
    show_bit2publish_button: bool
    social_bonus_result_id: "SocialBonusResult"
    state: str
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "SocialBonusResultLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SocialBonusResultLine": ...
    def create(self, vals: Dict[str, Any]) -> "SocialBonusResultLine": ...
    def filtered(self, func: Any) -> "SocialBonusResultLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SocialBonusResultLine": ...
    def exists(self) -> "SocialBonusResultLine": ...
    def sudo(self) -> "SocialBonusResultLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SocialBonusResultLine": ...

# --- social.bonus.sii.report ---

class SocialBonusSiiReport(Recordset):
    attachment_id: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    line_ids: "SocialBonusNotification"
    lines: int
    name: str
    sent_to_sii: bool
    sent_to_sii_error: str
    show_bit2publish_button: bool
    social_bonus_line_ids: "SocialBonusLine"
    def browse(self, ids: Union[int, List[int]]) -> "SocialBonusSiiReport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SocialBonusSiiReport": ...
    def create(self, vals: Dict[str, Any]) -> "SocialBonusSiiReport": ...
    def filtered(self, func: Any) -> "SocialBonusSiiReport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SocialBonusSiiReport": ...
    def exists(self) -> "SocialBonusSiiReport": ...
    def sudo(self) -> "SocialBonusSiiReport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SocialBonusSiiReport": ...

# --- sorgenia.contracts ---

class SorgeniaContracts(Recordset):
    activation_date: Optional[_dt.date]
    active: bool
    active_client_id: "ResPartner"
    agent_id: "ResPartner"
    bit2publish_template_ids: "Bit2publishTemplate"
    case_id: "HelpdeskTicket"
    cig_code: str
    cig_end_date: Optional[_dt.date]
    cig_start_date: Optional[_dt.date]
    client_case_ids: "HelpdeskTicket"
    client_category: str
    client_id: "ResPartner"
    commodity_type: str
    contact_cf: str
    contact_email: str
    contact_id: "ResPartner"
    contact_name: str
    contact_phone: str
    contract_end_date: Optional[_dt.date]
    contract_type: str
    cup: str
    cup_end_date: Optional[_dt.date]
    cup_start_date: Optional[_dt.date]
    debt_end_date: Optional[_dt.date]
    debt_owner_id: "ResPartner"
    debt_start_date: Optional[_dt.date]
    effective_date: Optional[_dt.date]
    e_invoice: bool
    fe_change_date: Optional[_dt.date]
    has_bit2publish_template: bool
    institution_name: str
    invoice_channel: str
    invoice_type: str
    ipa_code: str
    is_split_iva: bool
    name: str
    offer_code: str
    offered_type: str
    office_code: str
    old_client_id: "ResPartner"
    other: str
    pdf_contract: bytes
    pod_ids: "ResPartnerPod"
    pr_code: str
    recovery_effective_date: Optional[_dt.date]
    request_date: Optional[_dt.date]
    sdi_code: str
    sdi_write_date: Optional[_dt.date]
    service_point_ids: "ServicePoint"
    show_bit2publish_button: bool
    sign_date: Optional[_dt.date]
    sign_location: str
    subtype_id: "SympleTripletSubtype"
    tenancy_contract: str
    type: str
    type_id: "SympleTripletType"
    uni_office_code: str
    user_sequence: str
    voltura_start_date: Optional[_dt.date]
    voltura_type: str
    waiver_date: Optional[_dt.date]
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaContracts": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaContracts": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaContracts": ...
    def filtered(self, func: Any) -> "SorgeniaContracts": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaContracts": ...
    def exists(self) -> "SorgeniaContracts": ...
    def sudo(self) -> "SorgeniaContracts": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaContracts": ...

# --- sorgenia.digital.login ---

class SorgeniaDigitalLogin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    end_date: Optional[_dt.date]
    has_bit2publish_template: bool
    id_login: str
    partner_id: "ResPartner"
    partner_login_id: "SorgeniaDigitalLoginPartner"
    primary_role: str
    role: str
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    start_date: Optional[_dt.date]
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaDigitalLogin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaDigitalLogin": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaDigitalLogin": ...
    def filtered(self, func: Any) -> "SorgeniaDigitalLogin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaDigitalLogin": ...
    def exists(self) -> "SorgeniaDigitalLogin": ...
    def sudo(self) -> "SorgeniaDigitalLogin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaDigitalLogin": ...

# --- sorgenia.digital.login.partner ---

class SorgeniaDigitalLoginPartner(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    id_login: str
    login_ids: "SorgeniaDigitalLogin"
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    username: str
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaDigitalLoginPartner": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaDigitalLoginPartner": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaDigitalLoginPartner": ...
    def filtered(self, func: Any) -> "SorgeniaDigitalLoginPartner": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaDigitalLoginPartner": ...
    def exists(self) -> "SorgeniaDigitalLoginPartner": ...
    def sudo(self) -> "SorgeniaDigitalLoginPartner": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaDigitalLoginPartner": ...

# --- sorgenia.invoice.external.service.ftp.pdf.queue ---

class SorgeniaInvoiceExternalServiceFtpPdfQueue(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    document_id: "DocumentsDocument"
    filename: str
    has_bit2publish_template: bool
    pod: str
    server_id: "SorgeniaInvoiceExternalServiceFtpServer"
    show_bit2publish_button: bool
    state: str
    url: str
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaInvoiceExternalServiceFtpPdfQueue": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaInvoiceExternalServiceFtpPdfQueue": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaInvoiceExternalServiceFtpPdfQueue": ...
    def filtered(self, func: Any) -> "SorgeniaInvoiceExternalServiceFtpPdfQueue": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaInvoiceExternalServiceFtpPdfQueue": ...
    def exists(self) -> "SorgeniaInvoiceExternalServiceFtpPdfQueue": ...
    def sudo(self) -> "SorgeniaInvoiceExternalServiceFtpPdfQueue": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaInvoiceExternalServiceFtpPdfQueue": ...

# --- sorgenia.invoice.external.service.ftp.server ---

class SorgeniaInvoiceExternalServiceFtpServer(Recordset):
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    auto_import: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    csv_customer_code_column: int
    csv_document_code_column: int
    csv_ignore_header: bool
    csv_invoice_number_column: int
    csv_local_folder: str
    csv_reason_column: int
    csv_sent_date_document_column: int
    csv_sent_date_document_format: str
    csv_separator: str
    csv_type_column: int
    csv_url_column: int
    digital_ticket_type_id: "HelpdeskTicketType"
    energy_corner_ticket_type_id: "HelpdeskTicketType"
    existing_ticket_days: int
    flow: str
    folder: str
    folder_error: str
    folder_processed: str
    has_bit2publish_template: bool
    has_message: bool
    id_tenant: str
    interaction_contact_id: "ResPartner"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    org_token: str
    paper_ticket_type_id: "HelpdeskTicketType"
    password: str
    pod_regex: str
    port: int
    show_bit2publish_button: bool
    symphony_url: str
    template_error_id: "MailTemplate"
    template_send_invoice_id: "MailTemplate"
    ticket_type_id: "HelpdeskTicketType"
    token: str
    unexecuted_associated_triplet_type_ids: "HelpdeskTicketType"
    unexecuted_filename_regex: str
    unexecuted_triplet_case_exists_id: "SympleTripletPhaseResult"
    unexecuted_triplet_client_inactive_id: "SympleTripletPhaseResult"
    unexecuted_triplet_first_ok_id: "SympleTripletPhaseResult"
    unexecuted_triplet_ignore_unexecuted_id: "SympleTripletPhaseResult"
    unexecuted_triplet_result_inconsistent_id: "SympleTripletPhaseResult"
    unexecuted_triplet_second_ok_id: "SympleTripletPhaseResult"
    unexecuted_triplet_type_ids: "HelpdeskTicketType"
    url: str
    username: str
    website_message_ids: "MailMessage"
    zip_local_folder: str
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaInvoiceExternalServiceFtpServer": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaInvoiceExternalServiceFtpServer": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaInvoiceExternalServiceFtpServer": ...
    def filtered(self, func: Any) -> "SorgeniaInvoiceExternalServiceFtpServer": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaInvoiceExternalServiceFtpServer": ...
    def exists(self) -> "SorgeniaInvoiceExternalServiceFtpServer": ...
    def sudo(self) -> "SorgeniaInvoiceExternalServiceFtpServer": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaInvoiceExternalServiceFtpServer": ...

# --- sorgenia.loyalty.external.service.ftp.server ---

class SorgeniaLoyaltyExternalServiceFtpServer(Recordset):
    active: bool
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    cron_ids: "IrCron"
    csv_local_folder: str
    folder: str
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    password: str
    port: int
    show_bit2publish_button: bool
    url: str
    username: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaLoyaltyExternalServiceFtpServer": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaLoyaltyExternalServiceFtpServer": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaLoyaltyExternalServiceFtpServer": ...
    def filtered(self, func: Any) -> "SorgeniaLoyaltyExternalServiceFtpServer": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaLoyaltyExternalServiceFtpServer": ...
    def exists(self) -> "SorgeniaLoyaltyExternalServiceFtpServer": ...
    def sudo(self) -> "SorgeniaLoyaltyExternalServiceFtpServer": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaLoyaltyExternalServiceFtpServer": ...

# --- sorgenia.mdm.gdpr ---

class SorgeniaMdmGdpr(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    email: bool
    has_bit2publish_template: bool
    mobile: bool
    name: bool
    phone: bool
    show_bit2publish_button: bool
    surname: bool
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaMdmGdpr": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaMdmGdpr": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaMdmGdpr": ...
    def filtered(self, func: Any) -> "SorgeniaMdmGdpr": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaMdmGdpr": ...
    def exists(self) -> "SorgeniaMdmGdpr": ...
    def sudo(self) -> "SorgeniaMdmGdpr": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaMdmGdpr": ...

# --- sorgenia.postalizer.document ---

class SorgeniaPostalizerDocument(Recordset):
    active_phase_id: "SympleTripletPhase"
    address_id: "ResPartner"
    attachment_id: bytes
    bit2publish_template_ids: "Bit2publishTemplate"
    body_html: str
    business_name: str
    case_trigger: str
    city_id: "ResCity"
    cni_result_code: str
    cni_result_date: str
    cni_state: str
    country_id: "ResCountry"
    customer_code: str
    has_bit2publish_template: bool
    layout: str
    merged_attachment_id: bytes
    partner_id: "ResPartner"
    process_name: str
    sent_date: Optional[_dt.datetime]
    show_bit2publish_button: bool
    state: str
    state_code: str
    state_id: "ResCountryState"
    state_message: str
    street: str
    street_num: str
    template_id: "PostalizerTemplate"
    ticket_close_date: Optional[_dt.datetime]
    ticket_create_date: Optional[_dt.datetime]
    ticket_id: "HelpdeskTicket"
    ticket_market: str
    ticket_type_id: "HelpdeskTicketType"
    ticket_write_date: Optional[_dt.datetime]
    toponym_id: "ResToponym"
    triplet_subtype_id: "SympleTripletSubtype"
    triplet_type_id: "SympleTripletType"
    type: str
    uuid: str
    zip: str
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaPostalizerDocument": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaPostalizerDocument": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaPostalizerDocument": ...
    def filtered(self, func: Any) -> "SorgeniaPostalizerDocument": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaPostalizerDocument": ...
    def exists(self) -> "SorgeniaPostalizerDocument": ...
    def sudo(self) -> "SorgeniaPostalizerDocument": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaPostalizerDocument": ...

# --- sorgenia.question.input ---

class SorgeniaQuestionInput(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    comment: str
    has_bit2publish_template: bool
    question_id: str
    question_text: str
    question_type: str
    scale: str
    show_bit2publish_button: bool
    sorgenia_survey_id: "SorgeniaSurveyInput"
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaQuestionInput": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaQuestionInput": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaQuestionInput": ...
    def filtered(self, func: Any) -> "SorgeniaQuestionInput": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaQuestionInput": ...
    def exists(self) -> "SorgeniaQuestionInput": ...
    def sudo(self) -> "SorgeniaQuestionInput": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaQuestionInput": ...

# --- sorgenia.response.input ---

class SorgeniaResponseInput(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    ranking: str
    response_id: str
    response_text: str
    show_bit2publish_button: bool
    sorgenia_question_id: "SorgeniaQuestionInput"
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaResponseInput": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaResponseInput": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaResponseInput": ...
    def filtered(self, func: Any) -> "SorgeniaResponseInput": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaResponseInput": ...
    def exists(self) -> "SorgeniaResponseInput": ...
    def sudo(self) -> "SorgeniaResponseInput": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaResponseInput": ...

# --- sorgenia.sms.ftp.server ---

class SorgeniaSmsFtpServer(Recordset):
    active: bool
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    folder: str
    has_bit2publish_template: bool
    has_message: bool
    local_folder: str
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    password: str
    port: int
    show_bit2publish_button: bool
    url: str
    username: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaSmsFtpServer": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaSmsFtpServer": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaSmsFtpServer": ...
    def filtered(self, func: Any) -> "SorgeniaSmsFtpServer": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaSmsFtpServer": ...
    def exists(self) -> "SorgeniaSmsFtpServer": ...
    def sudo(self) -> "SorgeniaSmsFtpServer": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaSmsFtpServer": ...

# --- sorgenia.survey.input ---

class SorgeniaSurveyInput(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    channel: str
    client_type: str
    has_bit2publish_template: bool
    interaction_id: "SympleInteraction"
    note: str
    show_bit2publish_button: bool
    survey_filling_date: Optional[_dt.date]
    survey_id: str
    survey_release_date: Optional[_dt.date]
    survey_type: str
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaSurveyInput": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaSurveyInput": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaSurveyInput": ...
    def filtered(self, func: Any) -> "SorgeniaSurveyInput": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaSurveyInput": ...
    def exists(self) -> "SorgeniaSurveyInput": ...
    def sudo(self) -> "SorgeniaSurveyInput": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaSurveyInput": ...

# --- sorgenia.tisg ---

class SorgeniaTisg(Recordset):
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    distributor_vat: str
    dms_document_ref: str
    document_type: str
    error_note: str
    has_bit2publish_template: bool
    has_message: bool
    last_processed_line: int
    line_ids: "SorgeniaTisgLine"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    month: str
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    origin: str
    progressive_number: str
    sent_to_dms: bool
    sent_to_dms_error: str
    show_bit2publish_button: bool
    state: str
    user_vat: str
    website_message_ids: "MailMessage"
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaTisg": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaTisg": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaTisg": ...
    def filtered(self, func: Any) -> "SorgeniaTisg": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaTisg": ...
    def exists(self) -> "SorgeniaTisg": ...
    def sudo(self) -> "SorgeniaTisg": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaTisg": ...

# --- sorgenia.tisg.line ---

class SorgeniaTisgLine(Recordset):
    af_cf: str
    af_cf_straniero: str
    af_cognome: str
    af_nome: str
    af_piva: str
    af_ragione_sociale_denominazio: str
    bit2publish_template_ids: "Bit2publishTemplate"
    bonus: str
    bs_data_fine: Optional[_dt.date]
    bs_data_inizio: Optional[_dt.date]
    bs_data_rinnovo: Optional[_dt.date]
    bs_tipo_bonus: str
    cap_trasp_pdr: str
    cf: str
    cf_straniero: str
    classe_gruppo_mis: str
    codice_comune: str
    cod_pdr: str
    cod_prof_prel_std: str
    cod_remi: str
    cognome: str
    default_tras: str
    error_note: str
    es_altro: str
    es_cap: str
    es_civ: str
    es_istat: str
    es_localita: str
    es_nazione: str
    es_prov: str
    es_toponimo: str
    es_via: str
    fo_data_inizio: Optional[_dt.date]
    has_bit2publish_template: bool
    id_reg_clim: str
    matr_mis: str
    max_prelievo_ora: str
    nome: str
    piva: str
    piva_udb: str
    prelievo_annuo_prev: str
    press_misura: str
    ragione_sociale_denominazione: str
    show_bit2publish_button: bool
    state: str
    stato_pdr: str
    tipo_fornitura: str
    tipo_pdr: str
    tisg_id: "SorgeniaTisg"
    tisg_month: str
    tisg_type: str
    tisg_year: str
    trattamento: str
    ub_altro: str
    ub_cap: str
    ub_civ: str
    ub_istat: str
    ub_localita: str
    ub_nazione: str
    ub_prov: str
    ub_toponimo: str
    ub_via: str
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaTisgLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaTisgLine": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaTisgLine": ...
    def filtered(self, func: Any) -> "SorgeniaTisgLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaTisgLine": ...
    def exists(self) -> "SorgeniaTisgLine": ...
    def sudo(self) -> "SorgeniaTisgLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaTisgLine": ...

# --- sorgenia.upsa ---

class SorgeniaUpsa(Recordset):
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    count_error: int
    error_note: str
    has_bit2publish_template: bool
    has_message: bool
    last_processed_line: int
    line_ids: "SorgeniaUpsaLine"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    show_bit2publish_button: bool
    state: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaUpsa": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaUpsa": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaUpsa": ...
    def filtered(self, func: Any) -> "SorgeniaUpsa": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaUpsa": ...
    def exists(self) -> "SorgeniaUpsa": ...
    def sudo(self) -> "SorgeniaUpsa": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaUpsa": ...

# --- sorgenia.upsa.line ---

class SorgeniaUpsaLine(Recordset):
    active_service_point_id: "ServicePoint"
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    cod_pod: str
    cod_upsa: str
    error_note: str
    has_bit2publish_template: bool
    has_message: bool
    import_upsa_al: str
    import_upsa_dal: str
    internal_state: str
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    pod_id: "ResPartnerPod"
    show_bit2publish_button: bool
    state: str
    upsa_al: Optional[_dt.date]
    upsa_dal: Optional[_dt.date]
    upsa_id: "SorgeniaUpsa"
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaUpsaLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaUpsaLine": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaUpsaLine": ...
    def filtered(self, func: Any) -> "SorgeniaUpsaLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaUpsaLine": ...
    def exists(self) -> "SorgeniaUpsaLine": ...
    def sudo(self) -> "SorgeniaUpsaLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaUpsaLine": ...

# --- sorgenia.warranty ---

class SorgeniaWarranty(Recordset):
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity: str
    customer_code: str
    customer_name: str
    end_date: Optional[_dt.date]
    funding_entity: str
    has_bit2publish_template: bool
    is_active_warranty: bool
    is_auto_renewal: bool
    partner_id: "ResPartner"
    show_bit2publish_button: bool
    start_date: Optional[_dt.date]
    surety_type: str
    warranty_type: str
    def browse(self, ids: Union[int, List[int]]) -> "SorgeniaWarranty": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SorgeniaWarranty": ...
    def create(self, vals: Dict[str, Any]) -> "SorgeniaWarranty": ...
    def filtered(self, func: Any) -> "SorgeniaWarranty": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SorgeniaWarranty": ...
    def exists(self) -> "SorgeniaWarranty": ...
    def sudo(self) -> "SorgeniaWarranty": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SorgeniaWarranty": ...

# --- spreadsheet.contributor ---

class SpreadsheetContributor(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    document_id: "DocumentsDocument"
    has_bit2publish_template: bool
    last_update_date: Optional[_dt.datetime]
    show_bit2publish_button: bool
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "SpreadsheetContributor": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SpreadsheetContributor": ...
    def create(self, vals: Dict[str, Any]) -> "SpreadsheetContributor": ...
    def filtered(self, func: Any) -> "SpreadsheetContributor": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SpreadsheetContributor": ...
    def exists(self) -> "SpreadsheetContributor": ...
    def sudo(self) -> "SpreadsheetContributor": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SpreadsheetContributor": ...

# --- spreadsheet.revision ---

class SpreadsheetRevision(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    commands: str
    document_id: "DocumentsDocument"
    has_bit2publish_template: bool
    parent_revision_id: str
    revision_id: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SpreadsheetRevision": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SpreadsheetRevision": ...
    def create(self, vals: Dict[str, Any]) -> "SpreadsheetRevision": ...
    def filtered(self, func: Any) -> "SpreadsheetRevision": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SpreadsheetRevision": ...
    def exists(self) -> "SpreadsheetRevision": ...
    def sudo(self) -> "SpreadsheetRevision": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SpreadsheetRevision": ...

# --- spreadsheet.template ---

class SpreadsheetTemplate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    has_bit2publish_template: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    thumbnail: bytes
    def browse(self, ids: Union[int, List[int]]) -> "SpreadsheetTemplate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SpreadsheetTemplate": ...
    def create(self, vals: Dict[str, Any]) -> "SpreadsheetTemplate": ...
    def filtered(self, func: Any) -> "SpreadsheetTemplate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SpreadsheetTemplate": ...
    def exists(self) -> "SpreadsheetTemplate": ...
    def sudo(self) -> "SpreadsheetTemplate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SpreadsheetTemplate": ...

# --- studio.approval.entry ---

class StudioApprovalEntry(Recordset):
    action_id: "IrActionsActions"
    approved: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    group_id: "ResGroups"
    has_bit2publish_template: bool
    method: str
    model: str
    name: str
    reference: str
    res_id: Any
    rule_id: "StudioApprovalRule"
    show_bit2publish_button: bool
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "StudioApprovalEntry": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "StudioApprovalEntry": ...
    def create(self, vals: Dict[str, Any]) -> "StudioApprovalEntry": ...
    def filtered(self, func: Any) -> "StudioApprovalEntry": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "StudioApprovalEntry": ...
    def exists(self) -> "StudioApprovalEntry": ...
    def sudo(self) -> "StudioApprovalEntry": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "StudioApprovalEntry": ...

# --- studio.approval.rule ---

class StudioApprovalRule(Recordset):
    action_id: "IrActionsActions"
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    can_validate: bool
    conditional: bool
    domain: str
    entries_count: int
    entry_ids: "StudioApprovalEntry"
    exclusive_user: bool
    group_id: "ResGroups"
    has_bit2publish_template: bool
    message: str
    method: str
    model_id: "IrModel"
    model_name: str
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "StudioApprovalRule": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "StudioApprovalRule": ...
    def create(self, vals: Dict[str, Any]) -> "StudioApprovalRule": ...
    def filtered(self, func: Any) -> "StudioApprovalRule": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "StudioApprovalRule": ...
    def exists(self) -> "StudioApprovalRule": ...
    def sudo(self) -> "StudioApprovalRule": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "StudioApprovalRule": ...

# --- studio.mixin ---

class StudioMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "StudioMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "StudioMixin": ...
    def create(self, vals: Dict[str, Any]) -> "StudioMixin": ...
    def filtered(self, func: Any) -> "StudioMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "StudioMixin": ...
    def exists(self) -> "StudioMixin": ...
    def sudo(self) -> "StudioMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "StudioMixin": ...

# --- supervip.line ---

class SupervipLine(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    client_id: "ResPartner"
    error_message: str
    has_bit2publish_template: bool
    line_status: str
    show_bit2publish_button: bool
    user_sequence: str
    def browse(self, ids: Union[int, List[int]]) -> "SupervipLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SupervipLine": ...
    def create(self, vals: Dict[str, Any]) -> "SupervipLine": ...
    def filtered(self, func: Any) -> "SupervipLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SupervipLine": ...
    def exists(self) -> "SupervipLine": ...
    def sudo(self) -> "SupervipLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SupervipLine": ...

# --- supply.date.config ---

class SupplyDateConfig(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity: str
    contract_type: str
    energy_tension: str
    has_bit2publish_template: bool
    market: str
    max_gas_usage: str
    min_gas_usage: str
    month_window_from: int
    month_window_to: int
    name: str
    show_bit2publish_button: bool
    supply_start_number_months: int
    tp_conf: str
    def browse(self, ids: Union[int, List[int]]) -> "SupplyDateConfig": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SupplyDateConfig": ...
    def create(self, vals: Dict[str, Any]) -> "SupplyDateConfig": ...
    def filtered(self, func: Any) -> "SupplyDateConfig": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SupplyDateConfig": ...
    def exists(self) -> "SupplyDateConfig": ...
    def sudo(self) -> "SupplyDateConfig": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SupplyDateConfig": ...

# --- symphony.case.id ---

class SymphonyCaseId(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    case_id: "HelpdeskTicket"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    symphony_process_id: str
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyCaseId": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyCaseId": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyCaseId": ...
    def filtered(self, func: Any) -> "SymphonyCaseId": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyCaseId": ...
    def exists(self) -> "SymphonyCaseId": ...
    def sudo(self) -> "SymphonyCaseId": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyCaseId": ...

# --- symphony.config.ccq ---

class SymphonyConfigCcq(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyConfigCcq": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyConfigCcq": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyConfigCcq": ...
    def filtered(self, func: Any) -> "SymphonyConfigCcq": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyConfigCcq": ...
    def exists(self) -> "SymphonyConfigCcq": ...
    def sudo(self) -> "SymphonyConfigCcq": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyConfigCcq": ...

# --- symphony.config.cuscinetto ---

class SymphonyConfigCuscinetto(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyConfigCuscinetto": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyConfigCuscinetto": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyConfigCuscinetto": ...
    def filtered(self, func: Any) -> "SymphonyConfigCuscinetto": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyConfigCuscinetto": ...
    def exists(self) -> "SymphonyConfigCuscinetto": ...
    def sudo(self) -> "SymphonyConfigCuscinetto": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyConfigCuscinetto": ...

# --- symphony.config.metodo_pagamento ---

class SymphonyConfigMetodoPagamento(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyConfigMetodoPagamento": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyConfigMetodoPagamento": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyConfigMetodoPagamento": ...
    def filtered(self, func: Any) -> "SymphonyConfigMetodoPagamento": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyConfigMetodoPagamento": ...
    def exists(self) -> "SymphonyConfigMetodoPagamento": ...
    def sudo(self) -> "SymphonyConfigMetodoPagamento": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyConfigMetodoPagamento": ...

# --- symphony.config.rivalutazione ---

class SymphonyConfigRivalutazione(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyConfigRivalutazione": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyConfigRivalutazione": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyConfigRivalutazione": ...
    def filtered(self, func: Any) -> "SymphonyConfigRivalutazione": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyConfigRivalutazione": ...
    def exists(self) -> "SymphonyConfigRivalutazione": ...
    def sudo(self) -> "SymphonyConfigRivalutazione": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyConfigRivalutazione": ...

# --- symphony.config.verifica_carta ---

class SymphonyConfigVerificaCarta(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyConfigVerificaCarta": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyConfigVerificaCarta": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyConfigVerificaCarta": ...
    def filtered(self, func: Any) -> "SymphonyConfigVerificaCarta": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyConfigVerificaCarta": ...
    def exists(self) -> "SymphonyConfigVerificaCarta": ...
    def sudo(self) -> "SymphonyConfigVerificaCarta": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyConfigVerificaCarta": ...

# --- symphony.customer_pricelist ---

class SymphonyCustomerPricelist(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyCustomerPricelist": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyCustomerPricelist": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyCustomerPricelist": ...
    def filtered(self, func: Any) -> "SymphonyCustomerPricelist": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyCustomerPricelist": ...
    def exists(self) -> "SymphonyCustomerPricelist": ...
    def sudo(self) -> "SymphonyCustomerPricelist": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyCustomerPricelist": ...

# --- symphony.fastweb.communication ---

class SymphonyFastwebCommunication(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyFastwebCommunication": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyFastwebCommunication": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyFastwebCommunication": ...
    def filtered(self, func: Any) -> "SymphonyFastwebCommunication": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyFastwebCommunication": ...
    def exists(self) -> "SymphonyFastwebCommunication": ...
    def sudo(self) -> "SymphonyFastwebCommunication": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyFastwebCommunication": ...

# --- symphony.market.communication ---

class SymphonyMarketCommunication(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyMarketCommunication": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyMarketCommunication": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyMarketCommunication": ...
    def filtered(self, func: Any) -> "SymphonyMarketCommunication": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyMarketCommunication": ...
    def exists(self) -> "SymphonyMarketCommunication": ...
    def sudo(self) -> "SymphonyMarketCommunication": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyMarketCommunication": ...

# --- symphony.openfiber.communication ---

class SymphonyOpenfiberCommunication(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyOpenfiberCommunication": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyOpenfiberCommunication": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyOpenfiberCommunication": ...
    def filtered(self, func: Any) -> "SymphonyOpenfiberCommunication": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyOpenfiberCommunication": ...
    def exists(self) -> "SymphonyOpenfiberCommunication": ...
    def sudo(self) -> "SymphonyOpenfiberCommunication": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyOpenfiberCommunication": ...

# --- symphony.order.management ---

class SymphonyOrderManagement(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyOrderManagement": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyOrderManagement": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyOrderManagement": ...
    def filtered(self, func: Any) -> "SymphonyOrderManagement": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyOrderManagement": ...
    def exists(self) -> "SymphonyOrderManagement": ...
    def sudo(self) -> "SymphonyOrderManagement": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyOrderManagement": ...

# --- symphony.point.order.management ---

class SymphonyPointOrderManagement(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyPointOrderManagement": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyPointOrderManagement": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyPointOrderManagement": ...
    def filtered(self, func: Any) -> "SymphonyPointOrderManagement": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyPointOrderManagement": ...
    def exists(self) -> "SymphonyPointOrderManagement": ...
    def sudo(self) -> "SymphonyPointOrderManagement": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyPointOrderManagement": ...

# --- symphony.task.order.management ---

class SymphonyTaskOrderManagement(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyTaskOrderManagement": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyTaskOrderManagement": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyTaskOrderManagement": ...
    def filtered(self, func: Any) -> "SymphonyTaskOrderManagement": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyTaskOrderManagement": ...
    def exists(self) -> "SymphonyTaskOrderManagement": ...
    def sudo(self) -> "SymphonyTaskOrderManagement": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyTaskOrderManagement": ...

# --- symphony.wallet.dashboard ---

class SymphonyWalletDashboard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyWalletDashboard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyWalletDashboard": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyWalletDashboard": ...
    def filtered(self, func: Any) -> "SymphonyWalletDashboard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyWalletDashboard": ...
    def exists(self) -> "SymphonyWalletDashboard": ...
    def sudo(self) -> "SymphonyWalletDashboard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyWalletDashboard": ...

# --- symphony.webcomponent.dashboard.blacklist ---

class SymphonyWebcomponentDashboardBlacklist(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyWebcomponentDashboardBlacklist": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyWebcomponentDashboardBlacklist": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyWebcomponentDashboardBlacklist": ...
    def filtered(self, func: Any) -> "SymphonyWebcomponentDashboardBlacklist": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyWebcomponentDashboardBlacklist": ...
    def exists(self) -> "SymphonyWebcomponentDashboardBlacklist": ...
    def sudo(self) -> "SymphonyWebcomponentDashboardBlacklist": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyWebcomponentDashboardBlacklist": ...

# --- symphony.webcomponent.dashboard.credit.check ---

class SymphonyWebcomponentDashboardCreditCheck(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyWebcomponentDashboardCreditCheck": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyWebcomponentDashboardCreditCheck": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyWebcomponentDashboardCreditCheck": ...
    def filtered(self, func: Any) -> "SymphonyWebcomponentDashboardCreditCheck": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyWebcomponentDashboardCreditCheck": ...
    def exists(self) -> "SymphonyWebcomponentDashboardCreditCheck": ...
    def sudo(self) -> "SymphonyWebcomponentDashboardCreditCheck": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyWebcomponentDashboardCreditCheck": ...

# --- symphony.webcomponent.dashboard.fiber.coverage ---

class SymphonyWebcomponentDashboardFiberCoverage(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyWebcomponentDashboardFiberCoverage": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyWebcomponentDashboardFiberCoverage": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyWebcomponentDashboardFiberCoverage": ...
    def filtered(self, func: Any) -> "SymphonyWebcomponentDashboardFiberCoverage": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyWebcomponentDashboardFiberCoverage": ...
    def exists(self) -> "SymphonyWebcomponentDashboardFiberCoverage": ...
    def sudo(self) -> "SymphonyWebcomponentDashboardFiberCoverage": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyWebcomponentDashboardFiberCoverage": ...

# --- symphony.webcomponent.dashboard.fiber.upselling ---

class SymphonyWebcomponentDashboardFiberUpselling(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyWebcomponentDashboardFiberUpselling": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyWebcomponentDashboardFiberUpselling": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyWebcomponentDashboardFiberUpselling": ...
    def filtered(self, func: Any) -> "SymphonyWebcomponentDashboardFiberUpselling": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyWebcomponentDashboardFiberUpselling": ...
    def exists(self) -> "SymphonyWebcomponentDashboardFiberUpselling": ...
    def sudo(self) -> "SymphonyWebcomponentDashboardFiberUpselling": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyWebcomponentDashboardFiberUpselling": ...

# --- symphony.webcomponent.dashboard.integration.flow ---

class SymphonyWebcomponentDashboardIntegrationFlow(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymphonyWebcomponentDashboardIntegrationFlow": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymphonyWebcomponentDashboardIntegrationFlow": ...
    def create(self, vals: Dict[str, Any]) -> "SymphonyWebcomponentDashboardIntegrationFlow": ...
    def filtered(self, func: Any) -> "SymphonyWebcomponentDashboardIntegrationFlow": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymphonyWebcomponentDashboardIntegrationFlow": ...
    def exists(self) -> "SymphonyWebcomponentDashboardIntegrationFlow": ...
    def sudo(self) -> "SymphonyWebcomponentDashboardIntegrationFlow": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymphonyWebcomponentDashboardIntegrationFlow": ...

# --- symple.ai.automation ---

class SympleAiAutomation(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    filters: str
    has_bit2publish_template: bool
    model_id: "IrModel"
    name: str
    on_create: bool
    on_delete: bool
    on_write: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleAiAutomation": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleAiAutomation": ...
    def create(self, vals: Dict[str, Any]) -> "SympleAiAutomation": ...
    def filtered(self, func: Any) -> "SympleAiAutomation": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleAiAutomation": ...
    def exists(self) -> "SympleAiAutomation": ...
    def sudo(self) -> "SympleAiAutomation": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleAiAutomation": ...

# --- symple.ai.tag ---

class SympleAiTag(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleAiTag": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleAiTag": ...
    def create(self, vals: Dict[str, Any]) -> "SympleAiTag": ...
    def filtered(self, func: Any) -> "SympleAiTag": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleAiTag": ...
    def exists(self) -> "SympleAiTag": ...
    def sudo(self) -> "SympleAiTag": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleAiTag": ...

# --- symple.ai.tag.confidence ---

class SympleAiTagConfidence(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    confidence: float
    confidence_percentage: int
    has_bit2publish_template: bool
    name: str
    res_id: int
    res_model: str
    show_bit2publish_button: bool
    tag_id: "SympleAiTag"
    def browse(self, ids: Union[int, List[int]]) -> "SympleAiTagConfidence": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleAiTagConfidence": ...
    def create(self, vals: Dict[str, Any]) -> "SympleAiTagConfidence": ...
    def filtered(self, func: Any) -> "SympleAiTagConfidence": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleAiTagConfidence": ...
    def exists(self) -> "SympleAiTagConfidence": ...
    def sudo(self) -> "SympleAiTagConfidence": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleAiTagConfidence": ...

# --- symple.ai.tag.confidence.history ---

class SympleAiTagConfidenceHistory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    new_confidence: float
    old_confidence: float
    record_id: "SympleAiTagConfidence"
    res_id: int
    res_model: str
    show_bit2publish_button: bool
    tag_id: "SympleAiTag"
    def browse(self, ids: Union[int, List[int]]) -> "SympleAiTagConfidenceHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleAiTagConfidenceHistory": ...
    def create(self, vals: Dict[str, Any]) -> "SympleAiTagConfidenceHistory": ...
    def filtered(self, func: Any) -> "SympleAiTagConfidenceHistory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleAiTagConfidenceHistory": ...
    def exists(self) -> "SympleAiTagConfidenceHistory": ...
    def sudo(self) -> "SympleAiTagConfidenceHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleAiTagConfidenceHistory": ...

# --- symple.ai.tag.mixin ---

class SympleAiTagMixin(Recordset):
    ai_tag_ids: "SympleAiTagConfidence"
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    main_ai_tag_id: "SympleAiTag"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleAiTagMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleAiTagMixin": ...
    def create(self, vals: Dict[str, Any]) -> "SympleAiTagMixin": ...
    def filtered(self, func: Any) -> "SympleAiTagMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleAiTagMixin": ...
    def exists(self) -> "SympleAiTagMixin": ...
    def sudo(self) -> "SympleAiTagMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleAiTagMixin": ...

# --- symple.cluster ---

class SympleCluster(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleCluster": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleCluster": ...
    def create(self, vals: Dict[str, Any]) -> "SympleCluster": ...
    def filtered(self, func: Any) -> "SympleCluster": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleCluster": ...
    def exists(self) -> "SympleCluster": ...
    def sudo(self) -> "SympleCluster": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleCluster": ...

# --- symple.dms.folder ---

class SympleDmsFolder(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    domain_code: str
    folder_code: str
    has_bit2publish_template: bool
    has_message: bool
    image: bytes
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    metadata_code: str
    model_id: "IrModel"
    name: str
    remote_delete: bool
    server_id: "SympleDmsServer"
    show_bit2publish_button: bool
    tags_code: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "SympleDmsFolder": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleDmsFolder": ...
    def create(self, vals: Dict[str, Any]) -> "SympleDmsFolder": ...
    def filtered(self, func: Any) -> "SympleDmsFolder": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleDmsFolder": ...
    def exists(self) -> "SympleDmsFolder": ...
    def sudo(self) -> "SympleDmsFolder": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleDmsFolder": ...

# --- symple.dms.server ---

class SympleDmsServer(Recordset):
    active: bool
    auth_type: str
    auth_url: str
    bit2publish_template_ids: "Bit2publishTemplate"
    client_id: str
    client_secret: str
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    metadata: str
    name: str
    password: str
    realm: str
    show_bit2publish_button: bool
    url: str
    username: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "SympleDmsServer": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleDmsServer": ...
    def create(self, vals: Dict[str, Any]) -> "SympleDmsServer": ...
    def filtered(self, func: Any) -> "SympleDmsServer": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleDmsServer": ...
    def exists(self) -> "SympleDmsServer": ...
    def sudo(self) -> "SympleDmsServer": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleDmsServer": ...

# --- symple.dms.token ---

class SympleDmsToken(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    server_id: "SympleDmsServer"
    show_bit2publish_button: bool
    token: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleDmsToken": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleDmsToken": ...
    def create(self, vals: Dict[str, Any]) -> "SympleDmsToken": ...
    def filtered(self, func: Any) -> "SympleDmsToken": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleDmsToken": ...
    def exists(self) -> "SympleDmsToken": ...
    def sudo(self) -> "SympleDmsToken": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleDmsToken": ...

# --- symple.importer.import.case ---

class SympleImporterImportCase(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    put_in_process_queue: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleImporterImportCase": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleImporterImportCase": ...
    def create(self, vals: Dict[str, Any]) -> "SympleImporterImportCase": ...
    def filtered(self, func: Any) -> "SympleImporterImportCase": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleImporterImportCase": ...
    def exists(self) -> "SympleImporterImportCase": ...
    def sudo(self) -> "SympleImporterImportCase": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleImporterImportCase": ...

# --- symple.importer.line ---

class SympleImporterLine(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    case_code: str
    case_id: "HelpdeskTicket"
    current_phase: "SympleTripletPhase"
    error: str
    has_bit2publish_template: bool
    next_phase_result: str
    processing_date: Optional[_dt.datetime]
    process_is_running: bool
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleImporterLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleImporterLine": ...
    def create(self, vals: Dict[str, Any]) -> "SympleImporterLine": ...
    def filtered(self, func: Any) -> "SympleImporterLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleImporterLine": ...
    def exists(self) -> "SympleImporterLine": ...
    def sudo(self) -> "SympleImporterLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleImporterLine": ...

# --- symple.inbound.message.registry ---

class SympleInboundMessageRegistry(Recordset):
    active: bool
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    body_html: str
    email_from: str
    has_bit2publish_template: bool
    message_type: str
    name: str
    res_id: int
    res_model: str
    show_bit2publish_button: bool
    subject: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleInboundMessageRegistry": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleInboundMessageRegistry": ...
    def create(self, vals: Dict[str, Any]) -> "SympleInboundMessageRegistry": ...
    def filtered(self, func: Any) -> "SympleInboundMessageRegistry": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleInboundMessageRegistry": ...
    def exists(self) -> "SympleInboundMessageRegistry": ...
    def sudo(self) -> "SympleInboundMessageRegistry": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleInboundMessageRegistry": ...

# --- symple.interaction ---

class SympleInteraction(Recordset):
    active: bool
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    ai_tag_ids: "SympleAiTagConfidence"
    allowed_contact_parent_ids: "ResPartner"
    bit2publish_template_ids: "Bit2publishTemplate"
    cadastral_data_ids: "CadastreData"
    cadastral_data_info: str
    cadastre_data_count: int
    campaign_id: "UtmCampaign"
    cancel_reason_id: "SympleInteractionCancelReason"
    channel: str
    channel_id: "InteractionChannel"
    channel_to_set: "InteractionChannel"
    child_ticket_ids: "HelpdeskTicket"
    close_date: Optional[_dt.date]
    close_login: str
    complaint_start_date: Optional[_dt.datetime]
    connection_id: str
    contact_role_id: "JobTitles"
    created_from_res_partner: bool
    create_login: str
    customer_email: str
    customer_id: "ResPartner"
    customer_insurance_service: str
    customer_interaction_count: int
    customer_interaction_ids: "SympleInteraction"
    customer_keys: str
    customer_mobile: str
    customer_phone: str
    customer_univocal_code: str
    date_end: Optional[_dt.datetime]
    date_start: Optional[_dt.datetime]
    edu_id: str
    email: str
    email_cc: str
    email_id: "SympleMail"
    email_normalized: str
    error_message: str
    external_message_id: str
    external_payload: str
    external_status: str
    filtered_customer_domain: str
    has_bit2publish_template: bool
    has_message: bool
    id_vocal_order: str
    incoming_mail_server_id: "FetchmailServer"
    incoming_mail_server_user: str
    instance_key_ids: "SymplePbInstanceKey"
    interaction_result: str
    interaction_subtype_1: str
    interaction_subtype_2: str
    interaction_subtype_code_1: str
    interaction_subtype_code_2: str
    interaction_type: str
    interaction_type_code: str
    is_blacklisted: bool
    is_canceled: bool
    is_close: bool
    is_not_modifiable: bool
    is_readonly_contact: bool
    is_sender_doxee: bool
    is_transferred: bool
    mail_genre: str
    main_ai_tag_id: "SympleAiTag"
    mandatory_snailmail_pdf: bytes
    market: str
    medium_id: "UtmMedium"
    message_attachment_count: int
    message_bounce: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    migrated: bool
    multiple_contacts: bool
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    note: str
    options: str
    origin: str
    original_sender_email: str
    other_ticket_ids: "HelpdeskTicket"
    parent_interaction: str
    partner_email: str
    partner_id: "ResPartner"
    partner_mobile: str
    partner_phone: str
    partner_to_set: "ResPartner"
    phone: str
    protocol_code: str
    protocol_identifier: str
    registered_mail_number: str
    search_all_customers: bool
    send_date: Optional[_dt.date]
    show_bit2publish_button: bool
    show_original_sender_email: bool
    source_id: "UtmSource"
    state: str
    ticket_count: int
    ticket_ids: "HelpdeskTicket"
    transferred_from_id: "SympleInteraction"
    transferred_to_id: "SympleInteraction"
    type: str
    user_id: "ResUsers"
    user_notes: str
    user_type: str
    website_message_ids: "MailMessage"
    work_group: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleInteraction": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleInteraction": ...
    def create(self, vals: Dict[str, Any]) -> "SympleInteraction": ...
    def filtered(self, func: Any) -> "SympleInteraction": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleInteraction": ...
    def exists(self) -> "SympleInteraction": ...
    def sudo(self) -> "SympleInteraction": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleInteraction": ...

# --- symple.interaction.cancel.reason ---

class SympleInteractionCancelReason(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleInteractionCancelReason": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleInteractionCancelReason": ...
    def create(self, vals: Dict[str, Any]) -> "SympleInteractionCancelReason": ...
    def filtered(self, func: Any) -> "SympleInteractionCancelReason": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleInteractionCancelReason": ...
    def exists(self) -> "SympleInteractionCancelReason": ...
    def sudo(self) -> "SympleInteractionCancelReason": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleInteractionCancelReason": ...

# --- symple.mail ---

class SympleMail(Recordset):
    active_phase_id: "SympleTripletPhase"
    ai_tag_ids: "SympleAiTagConfidence"
    attachment_ids: "IrAttachment"
    bcc_addresses: str
    bit2publish_template_ids: "Bit2publishTemplate"
    body: str
    case_trigger: str
    cc_addresses: str
    content_type: str
    date: Optional[_dt.datetime]
    dkim: str
    email_priority: str
    envelope_to_address: str
    error: str
    from_address: str
    has_bit2publish_template: bool
    has_message: bool
    headers: str
    identifier: str
    in_server_id: "FetchmailServer"
    is_pec_server: bool
    mail_type: str
    main_ai_tag_id: "SympleAiTag"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    metadata: str
    mime: str
    name: str
    out_server_id: "IrMailServer"
    process_name: str
    received: str
    recipient_names: str
    reply_to_address: str
    res_id: int
    res_model: str
    return_path: str
    send_immediately: bool
    show_bit2publish_button: bool
    state: str
    subject: str
    ticket_close_date: Optional[_dt.datetime]
    ticket_create_date: Optional[_dt.datetime]
    ticket_id: "HelpdeskTicket"
    ticket_type_id: "HelpdeskTicketType"
    ticket_write_date: Optional[_dt.datetime]
    to_address: str
    triplet_subtype_id: "SympleTripletSubtype"
    triplet_type_id: "SympleTripletType"
    usercodes: str
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "SympleMail": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleMail": ...
    def create(self, vals: Dict[str, Any]) -> "SympleMail": ...
    def filtered(self, func: Any) -> "SympleMail": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleMail": ...
    def exists(self) -> "SympleMail": ...
    def sudo(self) -> "SympleMail": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleMail": ...

# --- symple.mail.import.mail.mail ---

class SympleMailImportMailMail(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleMailImportMailMail": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleMailImportMailMail": ...
    def create(self, vals: Dict[str, Any]) -> "SympleMailImportMailMail": ...
    def filtered(self, func: Any) -> "SympleMailImportMailMail": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleMailImportMailMail": ...
    def exists(self) -> "SympleMailImportMailMail": ...
    def sudo(self) -> "SympleMailImportMailMail": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleMailImportMailMail": ...

# --- symple.mail.report ---

class SympleMailReport(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    date: Optional[_dt.datetime]
    has_bit2publish_template: bool
    in_mails: int
    out_mails: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleMailReport": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleMailReport": ...
    def create(self, vals: Dict[str, Any]) -> "SympleMailReport": ...
    def filtered(self, func: Any) -> "SympleMailReport": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleMailReport": ...
    def exists(self) -> "SympleMailReport": ...
    def sudo(self) -> "SympleMailReport": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleMailReport": ...

# --- symple.message.registry ---

class SympleMessageRegistry(Recordset):
    active: bool
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    body_html: str
    email_from: str
    has_bit2publish_template: bool
    message_type: str
    name: str
    res_id: int
    res_model: str
    show_bit2publish_button: bool
    subject: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleMessageRegistry": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleMessageRegistry": ...
    def create(self, vals: Dict[str, Any]) -> "SympleMessageRegistry": ...
    def filtered(self, func: Any) -> "SympleMessageRegistry": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleMessageRegistry": ...
    def exists(self) -> "SympleMessageRegistry": ...
    def sudo(self) -> "SympleMessageRegistry": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleMessageRegistry": ...

# --- symple.message.registry.mixin ---

class SympleMessageRegistryMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleMessageRegistryMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleMessageRegistryMixin": ...
    def create(self, vals: Dict[str, Any]) -> "SympleMessageRegistryMixin": ...
    def filtered(self, func: Any) -> "SympleMessageRegistryMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleMessageRegistryMixin": ...
    def exists(self) -> "SympleMessageRegistryMixin": ...
    def sudo(self) -> "SympleMessageRegistryMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleMessageRegistryMixin": ...

# --- symple.outbound.message.registry ---

class SympleOutboundMessageRegistry(Recordset):
    active: bool
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    body_html: str
    email_from: str
    has_bit2publish_template: bool
    message_type: str
    name: str
    res_id: int
    res_model: str
    show_bit2publish_button: bool
    subject: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleOutboundMessageRegistry": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleOutboundMessageRegistry": ...
    def create(self, vals: Dict[str, Any]) -> "SympleOutboundMessageRegistry": ...
    def filtered(self, func: Any) -> "SympleOutboundMessageRegistry": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleOutboundMessageRegistry": ...
    def exists(self) -> "SympleOutboundMessageRegistry": ...
    def sudo(self) -> "SympleOutboundMessageRegistry": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleOutboundMessageRegistry": ...

# --- symple.pb.instance.key ---

class SymplePbInstanceKey(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    instance_key: str
    process_name: str
    res_id: Any
    res_model: str
    res_model_id: "IrModel"
    show_bit2publish_button: bool
    wizard_cancel_reason: str
    wizard_result_state_code: str
    wizard_result_status: str
    def browse(self, ids: Union[int, List[int]]) -> "SymplePbInstanceKey": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymplePbInstanceKey": ...
    def create(self, vals: Dict[str, Any]) -> "SymplePbInstanceKey": ...
    def filtered(self, func: Any) -> "SymplePbInstanceKey": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymplePbInstanceKey": ...
    def exists(self) -> "SymplePbInstanceKey": ...
    def sudo(self) -> "SymplePbInstanceKey": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymplePbInstanceKey": ...

# --- symple.pb.instance.key.mixin ---

class SymplePbInstanceKeyMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    instance_key_ids: "SymplePbInstanceKey"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymplePbInstanceKeyMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymplePbInstanceKeyMixin": ...
    def create(self, vals: Dict[str, Any]) -> "SymplePbInstanceKeyMixin": ...
    def filtered(self, func: Any) -> "SymplePbInstanceKeyMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymplePbInstanceKeyMixin": ...
    def exists(self) -> "SymplePbInstanceKeyMixin": ...
    def sudo(self) -> "SymplePbInstanceKeyMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymplePbInstanceKeyMixin": ...

# --- symple.pb.launcher ---

class SymplePbLauncher(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    has_bit2publish_template: bool
    model_ids: "IrModel"
    name: str
    process_ids: "SymplePbProcess"
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymplePbLauncher": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymplePbLauncher": ...
    def create(self, vals: Dict[str, Any]) -> "SymplePbLauncher": ...
    def filtered(self, func: Any) -> "SymplePbLauncher": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymplePbLauncher": ...
    def exists(self) -> "SymplePbLauncher": ...
    def sudo(self) -> "SymplePbLauncher": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymplePbLauncher": ...

# --- symple.pb.process ---

class SymplePbProcess(Recordset):
    autorun_code: str
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    element_ids: "SymplePbProcessElement"
    group_ids: "ResGroups"
    has_bit2publish_template: bool
    is_shown_code: str
    is_valid_code: str
    name: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymplePbProcess": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymplePbProcess": ...
    def create(self, vals: Dict[str, Any]) -> "SymplePbProcess": ...
    def filtered(self, func: Any) -> "SymplePbProcess": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymplePbProcess": ...
    def exists(self) -> "SymplePbProcess": ...
    def sudo(self) -> "SymplePbProcess": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymplePbProcess": ...

# --- symple.pb.process.data ---

class SymplePbProcessData(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    payload: str
    pb_id: str
    process_name: str
    res_id: int
    res_model: str
    show_bit2publish_button: bool
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
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymplePbProcessData": ...
    def exists(self) -> "SymplePbProcessData": ...
    def sudo(self) -> "SymplePbProcessData": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymplePbProcessData": ...

# --- symple.pb.process.element ---

class SymplePbProcessElement(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    process_id: "SymplePbProcess"
    show_bit2publish_button: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "SymplePbProcessElement": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymplePbProcessElement": ...
    def create(self, vals: Dict[str, Any]) -> "SymplePbProcessElement": ...
    def filtered(self, func: Any) -> "SymplePbProcessElement": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymplePbProcessElement": ...
    def exists(self) -> "SymplePbProcessElement": ...
    def sudo(self) -> "SymplePbProcessElement": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymplePbProcessElement": ...

# --- symple.pb.summary.launcher ---

class SymplePbSummaryLauncher(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    has_bit2publish_template: bool
    model_ids: "IrModel"
    name: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymplePbSummaryLauncher": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymplePbSummaryLauncher": ...
    def create(self, vals: Dict[str, Any]) -> "SymplePbSummaryLauncher": ...
    def filtered(self, func: Any) -> "SymplePbSummaryLauncher": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymplePbSummaryLauncher": ...
    def exists(self) -> "SymplePbSummaryLauncher": ...
    def sudo(self) -> "SymplePbSummaryLauncher": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymplePbSummaryLauncher": ...

# --- symple.pb.webcomponent ---

class SymplePbWebcomponent(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    event_ids: "SymplePbWebcomponentEvent"
    has_bit2publish_template: bool
    is_shown_code: str
    model_ids: "IrModel"
    name: str
    placeholder: str
    sequence: int
    show_bit2publish_button: bool
    show_in_launcher_tab: bool
    value: str
    def browse(self, ids: Union[int, List[int]]) -> "SymplePbWebcomponent": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymplePbWebcomponent": ...
    def create(self, vals: Dict[str, Any]) -> "SymplePbWebcomponent": ...
    def filtered(self, func: Any) -> "SymplePbWebcomponent": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymplePbWebcomponent": ...
    def exists(self) -> "SymplePbWebcomponent": ...
    def sudo(self) -> "SymplePbWebcomponent": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymplePbWebcomponent": ...

# --- symple.pb.webcomponent.event ---

class SymplePbWebcomponentEvent(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    has_bit2publish_template: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    value: str
    webcomponent_id: "SymplePbWebcomponent"
    def browse(self, ids: Union[int, List[int]]) -> "SymplePbWebcomponentEvent": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymplePbWebcomponentEvent": ...
    def create(self, vals: Dict[str, Any]) -> "SymplePbWebcomponentEvent": ...
    def filtered(self, func: Any) -> "SymplePbWebcomponentEvent": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymplePbWebcomponentEvent": ...
    def exists(self) -> "SymplePbWebcomponentEvent": ...
    def sudo(self) -> "SymplePbWebcomponentEvent": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymplePbWebcomponentEvent": ...

# --- symple.pdf.utils ---

class SymplePdfUtils(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SymplePdfUtils": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SymplePdfUtils": ...
    def create(self, vals: Dict[str, Any]) -> "SymplePdfUtils": ...
    def filtered(self, func: Any) -> "SymplePdfUtils": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SymplePdfUtils": ...
    def exists(self) -> "SymplePdfUtils": ...
    def sudo(self) -> "SymplePdfUtils": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SymplePdfUtils": ...

# --- symple.rcu ---

class SympleRcu(Recordset):
    addresses_attachment_ids: "IrAttachment"
    attachment_ids: "IrAttachment"
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity: str
    errors_count: int
    has_bit2publish_template: bool
    has_error: bool
    last_error: str
    last_processed_line: int
    line_ids: "SympleRcuLine"
    line_processed_ids: "SympleRcuLine"
    line_to_process_ids: "SympleRcuLine"
    month: str
    name: str
    processing_what: str
    show_bit2publish_button: bool
    state: str
    supply_attachment_ids: "IrAttachment"
    year: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcu": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcu": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcu": ...
    def filtered(self, func: Any) -> "SympleRcu": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcu": ...
    def exists(self) -> "SympleRcu": ...
    def sudo(self) -> "SympleRcu": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcu": ...

# --- symple.rcu.cancel.case.wizard ---

class SympleRcuCancelCaseWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    case_id: "HelpdeskTicket"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    triplet_allowed_phase_result_ids: "SympleTripletPhaseResult"
    triplet_phase_result_id: "SympleTripletPhaseResult"
    unsuccess_reason_id: "SympleTripletUnsuccessReason"
    unsuccess_reason_ids: "SympleTripletUnsuccessReason"
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuCancelCaseWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuCancelCaseWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuCancelCaseWizard": ...
    def filtered(self, func: Any) -> "SympleRcuCancelCaseWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuCancelCaseWizard": ...
    def exists(self) -> "SympleRcuCancelCaseWizard": ...
    def sudo(self) -> "SympleRcuCancelCaseWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuCancelCaseWizard": ...

# --- symple.rcu.check.work.wizard ---

class SympleRcuCheckWorkWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuCheckWorkWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuCheckWorkWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuCheckWorkWizard": ...
    def filtered(self, func: Any) -> "SympleRcuCheckWorkWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuCheckWorkWizard": ...
    def exists(self) -> "SympleRcuCheckWorkWizard": ...
    def sudo(self) -> "SympleRcuCheckWorkWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuCheckWorkWizard": ...

# --- symple.rcu.commodity.operation ---

class SympleRcuCommodityOperation(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    description: str
    has_bit2publish_template: bool
    name: str
    operation_ids: "SympleRcuOperation"
    show_bit2publish_button: bool
    ucode: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuCommodityOperation": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuCommodityOperation": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuCommodityOperation": ...
    def filtered(self, func: Any) -> "SympleRcuCommodityOperation": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuCommodityOperation": ...
    def exists(self) -> "SympleRcuCommodityOperation": ...
    def sudo(self) -> "SympleRcuCommodityOperation": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuCommodityOperation": ...

# --- symple.rcu.create.case.wizard ---

class SympleRcuCreateCaseWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    date: Optional[_dt.date]
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuCreateCaseWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuCreateCaseWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuCreateCaseWizard": ...
    def filtered(self, func: Any) -> "SympleRcuCreateCaseWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuCreateCaseWizard": ...
    def exists(self) -> "SympleRcuCreateCaseWizard": ...
    def sudo(self) -> "SympleRcuCreateCaseWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuCreateCaseWizard": ...

# --- symple.rcu.force_resolved.wizard ---

class SympleRcuForceResolvedWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuForceResolvedWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuForceResolvedWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuForceResolvedWizard": ...
    def filtered(self, func: Any) -> "SympleRcuForceResolvedWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuForceResolvedWizard": ...
    def exists(self) -> "SympleRcuForceResolvedWizard": ...
    def sudo(self) -> "SympleRcuForceResolvedWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuForceResolvedWizard": ...

# --- symple.rcu.line ---

class SympleRcuLine(Recordset):
    accesso_ui: str
    acc_mis: str
    activation_error: str
    activation_state: str
    activation_type: str
    addiz_regionale: str
    af_cf: str
    af_cf_straniero: str
    af_cognome: str
    af_nome: str
    af_piva: str
    af_ragione_sociale_denominazione: str
    aliquota_accise: str
    aliquota_iva: str
    altre_informazioni: str
    anno_fabb_conv: str
    anno_fabb_mis: str
    anno_termico: str
    area_rif: str
    autocertificazione: str
    be_anno_validita: str
    be_data_cessazione: str
    be_data_fine: str
    be_data_inizio: str
    bf_data_fine: str
    bf_data_inizio: str
    bf_data_rinnovo: str
    bit2publish_template_ids: "Bit2publishTemplate"
    bonus: str
    bs_anno_validita: str
    bs_data_cessazione_bonus: str
    bs_data_fine: str
    bs_data_inizio: str
    bs_regime_compensazione: str
    cap: str
    capacita_trasporto: str
    cap_es: str
    cap_forn: str
    cap_sl: str
    case_error_message: str
    case_error_message_short: str
    case_stage_id: "HelpdeskStage"
    case_stage_last_update: Optional[_dt.datetime]
    case_type_id: "HelpdeskTicketType"
    cat_uso: str
    cf: str
    cf_straniero: str
    civ: str
    civ_es: str
    civ_forn: str
    civ_sl: str
    classe_agevolazione: str
    classe_gruppo_mis: str
    classe_prelievo: str
    client_fiscal_code: str
    client_id: "ResPartner"
    client_vat: str
    cod: str
    codice_contratto: str
    codice_ufficio: str
    cod_offerta: str
    cod_pdr: str
    cod_pod: str
    cod_prof_prel_std: str
    cod_remi: str
    coeff_corr: str
    cognome: str
    commodity: str
    consumo: str
    data_abb_udb: str
    data_decorrenza_ret: Optional[_dt.date]
    data_fine_for: str
    data_fine_fornitura: Optional[_dt.date]
    data_fine_mand: str
    data_fine_sosp: str
    data_inizio_dispacciamento: Optional[_dt.date]
    data_inizio_for: str
    data_inizio_fornitura: Optional[_dt.date]
    data_inizio_mand: str
    data_inizio_sosp: Optional[_dt.date]
    data_inst_conv: str
    data_inst_mis: str
    data_messa_regime: Optional[_dt.date]
    data_val_res: str
    deactivation_error: str
    deactivation_state: str
    deactivation_type: str
    default_tras: str
    disalimentabilita: str
    dp: str
    email: str
    email_cliente: str
    email_referente: str
    en_data_fine: str
    en_data_inizio: str
    erog_servizio_energ: str
    errors: str
    es_altro: str
    es_cap: str
    es_civ: str
    es_istat: str
    es_localita: str
    es_nazione: str
    es_prov: str
    es_toponimo: str
    es_via: str
    fine_tipo_pod: str
    for_altro: str
    for_cap: str
    for_civ: str
    for_istat: str
    for_localita: str
    for_nazione: str
    for_prov: str
    for_toponimo: str
    for_via: str
    gest_forfait: str
    gruppo_mis_int: str
    has_bit2publish_template: bool
    id_reg_clim: str
    imposte: str
    inst_misurator_att: str
    inst_misurator_pot: str
    inst_misurator_rea: str
    is_activated: bool
    is_deactivated: bool
    is_mismatched: bool
    is_reconciled: bool
    istat: str
    istat_es: str
    istat_forn: str
    istat_sl: str
    iva: str
    k_trasfor_att: str
    k_trasfor_pot: str
    k_trasfor_rea: str
    localita: str
    localita_es: str
    localita_forn: str
    localita_sl: str
    mat_misuratore_att: str
    mat_misuratore_pot: str
    mat_misuratore_rea: str
    matr_conv: str
    matr_mis: str
    max_prelievo_ora: str
    mismatch_annual_usage_state: str
    mismatch_available_power_state: str
    mismatch_checked: bool
    mismatch_contracted_power_state: str
    mismatch_dau_state: str
    mismatch_disconnectable_state: str
    mismatch_extraction_class_state: str
    mismatch_extraction_profile_state: str
    mismatch_fc_vat_action: str
    mismatch_fc_vat_state: str
    mismatch_insurance_service_state: str
    mismatch_market_state: str
    mismatch_max_extraction_state: str
    mismatch_measure_pressure_state: str
    mismatch_pdr_type_state: str
    mismatch_processing_state: str
    mismatch_remi_code_state: str
    mismatch_remote_management_state: str
    mismatch_tariff_code_state: str
    mismatch_transport_capacity_state: str
    month: str
    motivazione: str
    nazione: str
    nazione_es: str
    nazione_forn: str
    nazione_sl: str
    n_cifre_conv: str
    n_cifre_mis: str
    nome: str
    num_cifre_att: str
    num_cifre_ea: str
    num_cifre_er: str
    num_cifre_pot: str
    num_cifre_rea: str
    pagamento_iva: str
    pdr_annual_extraction_forecast: str
    pdr_extraction_class: str
    pdr_id: "ResPartnerPdr"
    pdr_max_withdrawal_hour: float
    pdr_measure_pressure: str
    pdr_pdr_type: str
    pdr_rcu_transport_capacity: float
    pdr_remi_code: str
    pdr_standard_extraction_profile_code: str
    pdr_treatment: str
    piva: str
    piva_cc: str
    piva_dd: str
    piva_distr: str
    piva_udb: str
    piva_udd: str
    pma: str
    pod_available_power: str
    pod_contracted_power_import: str
    pod_dau: str
    pod_id: "ResPartnerPod"
    pod_market: str
    pod_market_type: str
    pod_pdr_disconnectable: str
    pod_pdr_remote_management: bool
    pod_tariff_code: str
    potcontrimp: str
    potdisp: str
    pot_max_ric: str
    pot_tot_inst: str
    pre_conv: str
    prel_annuo_prev: str
    prelievo_convenzionale_max: str
    presenza_ds: str
    presenza_mis: str
    press_misura: str
    prov: str
    prov_es: str
    prov_forn: str
    prov_sl: str
    ragione_sociale_cc: str
    ragione_sociale_dd: str
    ragione_sociale_denominazione: str
    ragione_sociale_distr: str
    ragione_sociale_udd: str
    rcu_id: "SympleRcu"
    ref_cognome: str
    ref_email: str
    referente: str
    ref_nome: str
    ref_telefono: str
    reg_clim: str
    regime_compensazione: str
    residenza: str
    se_altro: str
    se_cap: str
    se_cf: str
    se_civ: str
    se_email: str
    se_istat: str
    se_localita: str
    se_nazione: str
    se_piva: str
    se_prov: str
    se_ragione_sociale_denominazione: str
    servizio_tutela: str
    se_telefono: str
    se_toponimo: str
    sett_merceologico: str
    se_via: str
    show_bit2publish_button: bool
    sospeso: str
    stato_pdr: str
    stato_pod: str
    symphony_process_id: str
    tariffa_distribuzione: str
    telefono: str
    telefono_cliente: str
    telegestione: str
    tensione: str
    ticket_id: "HelpdeskTicket"
    tipo_fornitura: str
    tipo_mercato: str
    tipo_mis: str
    tipo_misuratore: str
    tipo_pdr: str
    tipo_pod: str
    tipo_sosp: str
    toponimo: str
    toponimo_es: str
    toponimo_forn: str
    toponimo_sl: str
    trattamento: str
    trattamento_succ: str
    ub_altro: str
    ub_cap: str
    ub_civ: str
    ub_istat: str
    ub_localita: str
    ub_nazione: str
    ub_prov: str
    ub_toponimo: str
    ub_via: str
    via: str
    via_es: str
    via_forn: str
    via_sl: str
    year: str
    zona_climatica: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuLine": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuLine": ...
    def filtered(self, func: Any) -> "SympleRcuLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuLine": ...
    def exists(self) -> "SympleRcuLine": ...
    def sudo(self) -> "SympleRcuLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuLine": ...

# --- symple.rcu.massive.procedure.result.fc.vat.wizard ---

class SympleRcuMassiveProcedureResultFcVatWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    total_acg1: int
    total_ae1: int
    total_error: int
    total_vt1: int
    total_vtg1: int
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuMassiveProcedureResultFcVatWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuMassiveProcedureResultFcVatWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuMassiveProcedureResultFcVatWizard": ...
    def filtered(self, func: Any) -> "SympleRcuMassiveProcedureResultFcVatWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuMassiveProcedureResultFcVatWizard": ...
    def exists(self) -> "SympleRcuMassiveProcedureResultFcVatWizard": ...
    def sudo(self) -> "SympleRcuMassiveProcedureResultFcVatWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuMassiveProcedureResultFcVatWizard": ...

# --- symple.rcu.massive.procedure.wizard ---

class SympleRcuMassiveProcedureWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    file: bytes
    has_bit2publish_template: bool
    procedure: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuMassiveProcedureWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuMassiveProcedureWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuMassiveProcedureWizard": ...
    def filtered(self, func: Any) -> "SympleRcuMassiveProcedureWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuMassiveProcedureWizard": ...
    def exists(self) -> "SympleRcuMassiveProcedureWizard": ...
    def sudo(self) -> "SympleRcuMassiveProcedureWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuMassiveProcedureWizard": ...

# --- symple.rcu.operation ---

class SympleRcuOperation(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    commodity_id: "SympleRcuCommodityOperation"
    description: str
    has_bit2publish_template: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    type_ids: "SympleRcuOperationType"
    ucode: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuOperation": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuOperation": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuOperation": ...
    def filtered(self, func: Any) -> "SympleRcuOperation": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuOperation": ...
    def exists(self) -> "SympleRcuOperation": ...
    def sudo(self) -> "SympleRcuOperation": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuOperation": ...

# --- symple.rcu.operation.type ---

class SympleRcuOperationType(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code_ids: "SympleRcuOperationTypeCode"
    description: str
    detail_ids: "HelpdeskTicketType"
    has_bit2publish_template: bool
    name: str
    operation_id: "SympleRcuOperation"
    sequence: int
    show_bit2publish_button: bool
    ucode: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuOperationType": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuOperationType": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuOperationType": ...
    def filtered(self, func: Any) -> "SympleRcuOperationType": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuOperationType": ...
    def exists(self) -> "SympleRcuOperationType": ...
    def sudo(self) -> "SympleRcuOperationType": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuOperationType": ...

# --- symple.rcu.operation.type.code ---

class SympleRcuOperationTypeCode(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    description: str
    detail_ids: "HelpdeskTicketType"
    has_bit2publish_template: bool
    name: str
    operation_type_id: "SympleRcuOperationType"
    sequence: int
    show_bit2publish_button: bool
    ucode: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuOperationTypeCode": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuOperationTypeCode": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuOperationTypeCode": ...
    def filtered(self, func: Any) -> "SympleRcuOperationTypeCode": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuOperationTypeCode": ...
    def exists(self) -> "SympleRcuOperationTypeCode": ...
    def sudo(self) -> "SympleRcuOperationTypeCode": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuOperationTypeCode": ...

# --- symple.rcu.pmax ---

class SympleRcuPmax(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    value: float
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuPmax": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuPmax": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuPmax": ...
    def filtered(self, func: Any) -> "SympleRcuPmax": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuPmax": ...
    def exists(self) -> "SympleRcuPmax": ...
    def sudo(self) -> "SympleRcuPmax": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuPmax": ...

# --- symple.rcu.refresh_deactivation.wizard ---

class SympleRcuRefreshDeactivationWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuRefreshDeactivationWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuRefreshDeactivationWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuRefreshDeactivationWizard": ...
    def filtered(self, func: Any) -> "SympleRcuRefreshDeactivationWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuRefreshDeactivationWizard": ...
    def exists(self) -> "SympleRcuRefreshDeactivationWizard": ...
    def sudo(self) -> "SympleRcuRefreshDeactivationWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuRefreshDeactivationWizard": ...

# --- symple.rcu.resolved.ok.wizard ---

class SympleRcuResolvedOkWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuResolvedOkWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuResolvedOkWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuResolvedOkWizard": ...
    def filtered(self, func: Any) -> "SympleRcuResolvedOkWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuResolvedOkWizard": ...
    def exists(self) -> "SympleRcuResolvedOkWizard": ...
    def sudo(self) -> "SympleRcuResolvedOkWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuResolvedOkWizard": ...

# --- symple.rcu.resolved.work.wizard ---

class SympleRcuResolvedWorkWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuResolvedWorkWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuResolvedWorkWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuResolvedWorkWizard": ...
    def filtered(self, func: Any) -> "SympleRcuResolvedWorkWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuResolvedWorkWizard": ...
    def exists(self) -> "SympleRcuResolvedWorkWizard": ...
    def sudo(self) -> "SympleRcuResolvedWorkWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuResolvedWorkWizard": ...

# --- symple.rcu.sending.resolved.wizard ---

class SympleRcuSendingResolvedWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuSendingResolvedWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuSendingResolvedWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuSendingResolvedWizard": ...
    def filtered(self, func: Any) -> "SympleRcuSendingResolvedWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuSendingResolvedWizard": ...
    def exists(self) -> "SympleRcuSendingResolvedWizard": ...
    def sudo(self) -> "SympleRcuSendingResolvedWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuSendingResolvedWizard": ...

# --- symple.rcu.sending.work.wizard ---

class SympleRcuSendingWorkWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuSendingWorkWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuSendingWorkWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuSendingWorkWizard": ...
    def filtered(self, func: Any) -> "SympleRcuSendingWorkWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuSendingWorkWizard": ...
    def exists(self) -> "SympleRcuSendingWorkWizard": ...
    def sudo(self) -> "SympleRcuSendingWorkWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuSendingWorkWizard": ...

# --- symple.rcu.show_error_message.case.wizard ---

class SympleRcuShowErrorMessageCaseWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    error_message: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuShowErrorMessageCaseWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuShowErrorMessageCaseWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuShowErrorMessageCaseWizard": ...
    def filtered(self, func: Any) -> "SympleRcuShowErrorMessageCaseWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuShowErrorMessageCaseWizard": ...
    def exists(self) -> "SympleRcuShowErrorMessageCaseWizard": ...
    def sudo(self) -> "SympleRcuShowErrorMessageCaseWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuShowErrorMessageCaseWizard": ...

# --- symple.rcu.work.check.wizard ---

class SympleRcuWorkCheckWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuWorkCheckWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuWorkCheckWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuWorkCheckWizard": ...
    def filtered(self, func: Any) -> "SympleRcuWorkCheckWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuWorkCheckWizard": ...
    def exists(self) -> "SympleRcuWorkCheckWizard": ...
    def sudo(self) -> "SympleRcuWorkCheckWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuWorkCheckWizard": ...

# --- symple.rcu.work.sending.wizard ---

class SympleRcuWorkSendingWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRcuWorkSendingWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRcuWorkSendingWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRcuWorkSendingWizard": ...
    def filtered(self, func: Any) -> "SympleRcuWorkSendingWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRcuWorkSendingWizard": ...
    def exists(self) -> "SympleRcuWorkSendingWizard": ...
    def sudo(self) -> "SympleRcuWorkSendingWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRcuWorkSendingWizard": ...

# --- symple.refunder.ax ---

class SympleRefunderAx(Recordset):
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    data: bytes
    error: str
    filename: str
    has_bit2publish_template: bool
    has_message: bool
    line_ids: "SympleRefunderAxLine"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    processing_state: str
    record_count: int
    report_filename: str
    show_bit2publish_button: bool
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderAx": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderAx": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderAx": ...
    def filtered(self, func: Any) -> "SympleRefunderAx": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderAx": ...
    def exists(self) -> "SympleRefunderAx": ...
    def sudo(self) -> "SympleRefunderAx": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderAx": ...

# --- symple.refunder.ax.line ---

class SympleRefunderAxLine(Recordset):
    address: str
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    business_type: str
    client_code: str
    client_id: "ResPartner"
    code: str
    company_name: str
    email: str
    error: str
    fiscal_code: str
    gender: str
    golden_key: str
    has_bit2publish_template: bool
    latest_send_date: Optional[_dt.date]
    mobile: str
    name: str
    refunder_file_id: "SympleRefunderAx"
    send_counter: int
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderAxLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderAxLine": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderAxLine": ...
    def filtered(self, func: Any) -> "SympleRefunderAxLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderAxLine": ...
    def exists(self) -> "SympleRefunderAxLine": ...
    def sudo(self) -> "SympleRefunderAxLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderAxLine": ...

# --- symple.refunder.doxee ---

class SympleRefunderDoxee(Recordset):
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    data: bytes
    error: str
    filename: str
    has_bit2publish_template: bool
    has_message: bool
    line_ids: "SympleRefunderDoxeeLine"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    processing_state: str
    record_count: int
    report_filename: str
    show_bit2publish_button: bool
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderDoxee": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderDoxee": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderDoxee": ...
    def filtered(self, func: Any) -> "SympleRefunderDoxee": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderDoxee": ...
    def exists(self) -> "SympleRefunderDoxee": ...
    def sudo(self) -> "SympleRefunderDoxee": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderDoxee": ...

# --- symple.refunder.doxee.line ---

class SympleRefunderDoxeeLine(Recordset):
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    case_id: "HelpdeskTicket"
    channel: str
    client_code: str
    client_id: "ResPartner"
    code: str
    error: str
    has_bit2publish_template: bool
    iban: str
    iban_holder: str
    is_privacy: bool
    name: str
    purl: str
    purl_validity_date: Optional[_dt.date]
    refunder_file_id: "SympleRefunderDoxee"
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderDoxeeLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderDoxeeLine": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderDoxeeLine": ...
    def filtered(self, func: Any) -> "SympleRefunderDoxeeLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderDoxeeLine": ...
    def exists(self) -> "SympleRefunderDoxeeLine": ...
    def sudo(self) -> "SympleRefunderDoxeeLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderDoxeeLine": ...

# --- symple.refunder.import.wizard ---

class SympleRefunderImportWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    model: str
    op_type: str
    process: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderImportWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderImportWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderImportWizard": ...
    def filtered(self, func: Any) -> "SympleRefunderImportWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderImportWizard": ...
    def exists(self) -> "SympleRefunderImportWizard": ...
    def sudo(self) -> "SympleRefunderImportWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderImportWizard": ...

# --- symple.refunder.line ---

class SympleRefunderLine(Recordset):
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    case: str
    case_id: "HelpdeskTicket"
    date: Optional[_dt.date]
    error: str
    has_bit2publish_template: bool
    reason: str
    result: str
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderLine": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderLine": ...
    def filtered(self, func: Any) -> "SympleRefunderLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderLine": ...
    def exists(self) -> "SympleRefunderLine": ...
    def sudo(self) -> "SympleRefunderLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderLine": ...

# --- symple.refunder.line.mixin ---

class SympleRefunderLineMixin(Recordset):
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    client_code: str
    client_id: "ResPartner"
    code: str
    error: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderLineMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderLineMixin": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderLineMixin": ...
    def filtered(self, func: Any) -> "SympleRefunderLineMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderLineMixin": ...
    def exists(self) -> "SympleRefunderLineMixin": ...
    def sudo(self) -> "SympleRefunderLineMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderLineMixin": ...

# --- symple.refunder.mixin ---

class SympleRefunderMixin(Recordset):
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    data: bytes
    error: str
    filename: str
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    processing_state: str
    record_count: int
    report_filename: str
    show_bit2publish_button: bool
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderMixin": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderMixin": ...
    def filtered(self, func: Any) -> "SympleRefunderMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderMixin": ...
    def exists(self) -> "SympleRefunderMixin": ...
    def sudo(self) -> "SympleRefunderMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderMixin": ...

# --- symple.refunder.process.wizard ---

class SympleRefunderProcessWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderProcessWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderProcessWizard": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderProcessWizard": ...
    def filtered(self, func: Any) -> "SympleRefunderProcessWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderProcessWizard": ...
    def exists(self) -> "SympleRefunderProcessWizard": ...
    def sudo(self) -> "SympleRefunderProcessWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderProcessWizard": ...

# --- symple.refunder.result ---

class SympleRefunderResult(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    has_bit2publish_template: bool
    help: str
    result: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderResult": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderResult": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderResult": ...
    def filtered(self, func: Any) -> "SympleRefunderResult": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderResult": ...
    def exists(self) -> "SympleRefunderResult": ...
    def sudo(self) -> "SympleRefunderResult": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderResult": ...

# --- symple.refunder.update ---

class SympleRefunderUpdate(Recordset):
    activity_calendar_event_id: "CalendarEvent"
    activity_date_deadline: Optional[_dt.date]
    activity_exception_decoration: str
    activity_exception_icon: str
    activity_ids: "MailActivity"
    activity_state: str
    activity_summary: str
    activity_type_icon: str
    activity_type_id: "MailActivityType"
    activity_user_id: "ResUsers"
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    data: bytes
    error: str
    filename: str
    has_bit2publish_template: bool
    has_message: bool
    line_ids: "SympleRefunderUpdateLine"
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    my_activity_date_deadline: Optional[_dt.date]
    name: str
    processing_state: str
    record_count: int
    report_filename: str
    show_bit2publish_button: bool
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderUpdate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderUpdate": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderUpdate": ...
    def filtered(self, func: Any) -> "SympleRefunderUpdate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderUpdate": ...
    def exists(self) -> "SympleRefunderUpdate": ...
    def sudo(self) -> "SympleRefunderUpdate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderUpdate": ...

# --- symple.refunder.update.line ---

class SympleRefunderUpdateLine(Recordset):
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    case: str
    case_id: "HelpdeskTicket"
    client_code: str
    client_id: "ResPartner"
    code: str
    date: Optional[_dt.date]
    error: str
    has_bit2publish_template: bool
    name: str
    reason: str
    refund_check_number: str
    refund_city: str
    refunder_file_id: "SympleRefunderUpdate"
    refund_iban: str
    refund_raccomandata_number: str
    refund_state: str
    refund_street: str
    refund_zip: str
    result: str
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "SympleRefunderUpdateLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleRefunderUpdateLine": ...
    def create(self, vals: Dict[str, Any]) -> "SympleRefunderUpdateLine": ...
    def filtered(self, func: Any) -> "SympleRefunderUpdateLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleRefunderUpdateLine": ...
    def exists(self) -> "SympleRefunderUpdateLine": ...
    def sudo(self) -> "SympleRefunderUpdateLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleRefunderUpdateLine": ...

# --- symple.slideout.menu ---

class SympleSlideoutMenu(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code_for_attributes: str
    code_for_auto_open: str
    description: str
    has_bit2publish_template: bool
    model_ids: "IrModel"
    name: str
    security_role_ids: "SecurityRole"
    sequence: int
    show_bit2publish_button: bool
    user_ids: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "SympleSlideoutMenu": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleSlideoutMenu": ...
    def create(self, vals: Dict[str, Any]) -> "SympleSlideoutMenu": ...
    def filtered(self, func: Any) -> "SympleSlideoutMenu": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleSlideoutMenu": ...
    def exists(self) -> "SympleSlideoutMenu": ...
    def sudo(self) -> "SympleSlideoutMenu": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleSlideoutMenu": ...

# --- symple.triplet.phase ---

class SympleTripletPhase(Recordset):
    active: bool
    allowed_phase_ids: "SympleTripletPhase"
    allowed_phase_result_ids: "SympleTripletPhaseResult"
    allowed_process_ids: "SymplePbProcess"
    automatic_email_template_ids: "MailTemplate"
    automatic_phase_result_id: "SympleTripletPhaseResult"
    automatic_postalizer_template_ids: "AutomaticPostalizerSelector"
    automatic_sms_template_id: "SmsTemplate"
    automatic_template_id: "MailTemplate"
    automatic_template_ids: "AutomaticEmailSelector"
    bit2publish_template_ids: "Bit2publishTemplate"
    channel_result_selector: "ResultChannelSelector"
    check_closed_child_tickets: bool
    child_case: bool
    cluster_id: "SympleCluster"
    code: str
    code_result_configurator: "ResultCodeConfigurator"
    default_template_ids: "MailTemplate"
    dl_reminder: int
    email_priority: str
    email_topic: str
    exceeding_iterations_limit_phase_id: "SympleTripletPhase"
    excluded_from_workflow_code: "SympleWorkflow"
    flow_code: str
    has_bit2publish_template: bool
    helpdesk_group_id: "HelpdeskTeam"
    helpdesk_stage_id: "HelpdeskStage"
    is_a_postalizer_phase: bool
    is_checkpoint_phase: bool
    is_compute_refund: bool
    is_dl: bool
    is_execute_code_at_phase_change: bool
    is_execute_code_when_resumed: bool
    is_externally_integrated: bool
    is_interaction_outbound: bool
    is_mail_managed: str
    is_managed_by_rcu: bool
    is_needs_child_case: bool
    is_pick_refund_template: bool
    is_process_cancellable_relaunchable: bool
    is_process_managed: bool
    is_quote_accepted: bool
    is_quote_sent: bool
    is_run_code_by_cron: bool
    is_sms_managed: str
    is_timeout: bool
    is_tiqv: bool
    is_voidable: bool
    iterations_limit: int
    name: str
    needs_child_result_id: "SympleTripletPhaseResult"
    next_result_on_closed_child_tickets: "SympleTripletPhaseResult"
    node_type: str
    no_refund_phase_result_id: "SympleTripletPhaseResult"
    no_refund_template_id: "MailTemplate"
    phase_code: str
    postalizer_phase_ids: "PhaseResultSelector"
    process_type: str
    quote_reminder: int
    refund_phase_result_id: "SympleTripletPhaseResult"
    refund_template_id: "MailTemplate"
    response_channel_id: "InteractionChannel"
    result_to_set_on_email_answer: "SympleTripletPhaseResult"
    send_email: str
    send_email_and_set_result: str
    send_with_postalizer: str
    service_code: str
    set_result_automatically: str
    show_bit2publish_button: bool
    sms_phase_ko_result_id: "SympleTripletPhaseResult"
    sms_phase_result_ok_id: "SympleTripletPhaseResult"
    supply_state_change_to: str
    ticket_type_id: "HelpdeskTicketType"
    timeout_days: int
    timeout_hours: int
    timeout_months: int
    timeout_phase_result: "SympleTripletPhaseResult"
    timeout_time: int
    timeout_years: int
    triplet_result_selector: "ResultTripletSelector"
    triplet_subtype_id: "SympleTripletSubtype"
    triplet_subtype_ticket_type_ids: "HelpdeskTicketType"
    triplet_type_id: "SympleTripletType"
    triplet_type_subtype_ids: "SympleTripletSubtype"
    wizard_info: str
    workflow_id: "SympleWorkflow"
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
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleTripletPhase": ...
    def exists(self) -> "SympleTripletPhase": ...
    def sudo(self) -> "SympleTripletPhase": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleTripletPhase": ...

# --- symple.triplet.phase.history ---

class SympleTripletPhaseHistory(Recordset):
    active_phase_id: "SympleTripletPhase"
    bit2publish_template_ids: "Bit2publishTemplate"
    date: Optional[_dt.datetime]
    error_message: str
    esito_mig: str
    fase_mig: str
    has_bit2publish_template: bool
    helpdesk_group_id: "HelpdeskTeam"
    info_message: str
    is_close: bool
    last_active: bool
    name: str
    note: str
    phase_id: "SympleTripletPhase"
    phase_result_id: "SympleTripletPhaseResult"
    show_bit2publish_button: bool
    start_phase_id: "SympleTripletPhase"
    ticket_id: "HelpdeskTicket"
    ticket_migrated: bool
    ticket_stage_id: "HelpdeskStage"
    user_id: "ResUsers"
    workflow_id: "SympleWorkflow"
    def browse(self, ids: Union[int, List[int]]) -> "SympleTripletPhaseHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleTripletPhaseHistory": ...
    def create(self, vals: Dict[str, Any]) -> "SympleTripletPhaseHistory": ...
    def filtered(self, func: Any) -> "SympleTripletPhaseHistory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleTripletPhaseHistory": ...
    def exists(self) -> "SympleTripletPhaseHistory": ...
    def sudo(self) -> "SympleTripletPhaseHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleTripletPhaseHistory": ...

# --- symple.triplet.phase.result ---

class SympleTripletPhaseResult(Recordset):
    action_server_id: "IrActionsServer"
    active: bool
    b2w_product_code: str
    bit2publish_template_ids: "Bit2publishTemplate"
    cluster_id: "SympleCluster"
    has_bit2publish_template: bool
    has_message: bool
    helpdesk_group_id: "HelpdeskTeam"
    is_annulment: bool
    is_dl_solicitation_result: bool
    is_hidden: bool
    is_quote_expired: bool
    name: str
    next_phase_id: "SympleTripletPhase"
    result_type_id: "ResultType"
    selectable_unsuccess_reason_ids: "SympleTripletUnsuccessReason"
    show_bit2publish_button: bool
    starting_phase_ids: "SympleTripletPhase"
    state_code: str
    unsuccess_reason_ids: "SympleTripletUnsuccessReason"
    visible_to_triplet_ids: "HelpdeskTicketType"
    wizard_result: str
    workflow_id: "SympleWorkflow"
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
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleTripletPhaseResult": ...
    def exists(self) -> "SympleTripletPhaseResult": ...
    def sudo(self) -> "SympleTripletPhaseResult": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleTripletPhaseResult": ...

# --- symple.triplet.phase.type ---

class SympleTripletPhaseType(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleTripletPhaseType": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleTripletPhaseType": ...
    def create(self, vals: Dict[str, Any]) -> "SympleTripletPhaseType": ...
    def filtered(self, func: Any) -> "SympleTripletPhaseType": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleTripletPhaseType": ...
    def exists(self) -> "SympleTripletPhaseType": ...
    def sudo(self) -> "SympleTripletPhaseType": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleTripletPhaseType": ...

# --- symple.triplet.subtype ---

class SympleTripletSubtype(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    has_bit2publish_template: bool
    is_from_migration: bool
    is_visible_to_operators: bool
    name: str
    show_bit2publish_button: bool
    ticket_type_ids: "HelpdeskTicketType"
    type_id: "SympleTripletType"
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
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleTripletSubtype": ...
    def exists(self) -> "SympleTripletSubtype": ...
    def sudo(self) -> "SympleTripletSubtype": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleTripletSubtype": ...

# --- symple.triplet.type ---

class SympleTripletType(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    domain_of_type: str
    has_bit2publish_template: bool
    is_from_migration: bool
    is_pods_in_pop_up: bool
    is_service_points_in_pop_up: bool
    is_visible_to_anonymous: bool
    is_visible_to_operators: bool
    name: str
    show_bit2publish_button: bool
    subtype_ids: "SympleTripletSubtype"
    type_code: str
    visible_to_channel_ids: "InteractionChannel"
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
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleTripletType": ...

# --- symple.triplet.unsuccess.reason ---

class SympleTripletUnsuccessReason(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    is_cancel: bool
    is_ko: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "SympleTripletUnsuccessReason": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "SympleTripletUnsuccessReason": ...
    def create(self, vals: Dict[str, Any]) -> "SympleTripletUnsuccessReason": ...
    def filtered(self, func: Any) -> "SympleTripletUnsuccessReason": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "SympleTripletUnsuccessReason": ...
    def exists(self) -> "SympleTripletUnsuccessReason": ...
    def sudo(self) -> "SympleTripletUnsuccessReason": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleTripletUnsuccessReason": ...

# --- symple.triplet_type ---

class SympleTripletType(Recordset):
    is_pods_in_pop_up: bool
    name: str
    subtype_ids: "SympleTripletSubtype"
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
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleTripletType": ...

# --- symple.workflow ---

class SympleWorkflow(Recordset):
    active: bool
    alternative_phone: bool
    alternative_phone_domain: str
    bit2publish_template_ids: "Bit2publishTemplate"
    bpmn_diagram: str
    can_update_pod_supply_state: bool
    code: str
    commodity_required: bool
    connect_parent_case_domain: str
    connect_parent_case_is_same_client: bool
    connect_parent_case_is_same_point: bool
    detail_ids: "HelpdeskTicketType"
    excluded_phase_ids: "SympleTripletPhase"
    execute_code_every_phase: bool
    feature_flag_async_engine: bool
    has_bit2publish_template: bool
    is_fiber_activation: bool
    is_fiber_deactivation: bool
    is_tiqv: bool
    name: str
    phase_ids: "SympleTripletPhase"
    process_type: str
    send_sms: bool
    send_sms_case_domain: str
    show_bit2publish_button: bool
    show_connect_parent_case_button: bool
    show_deactivation_tab: bool
    show_invoice_tab: bool
    sla_ids: "HelpdeskSlaPolicy"
    triplet_phase_id: "SympleTripletPhase"
    use_sla: bool
    wf_code: str
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
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "SympleWorkflow": ...

# --- tab.visibility ---

class TabVisibility(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    domain: str
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "TabVisibility": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "TabVisibility": ...
    def create(self, vals: Dict[str, Any]) -> "TabVisibility": ...
    def filtered(self, func: Any) -> "TabVisibility": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "TabVisibility": ...
    def exists(self) -> "TabVisibility": ...
    def sudo(self) -> "TabVisibility": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "TabVisibility": ...

# --- tax.adjustments.wizard ---

class TaxAdjustmentsWizard(Recordset):
    adjustment_type: str
    amount: float
    bit2publish_template_ids: "Bit2publishTemplate"
    company_currency_id: "ResCurrency"
    credit_account_id: "AccountAccount"
    date: Optional[_dt.date]
    debit_account_id: "AccountAccount"
    has_bit2publish_template: bool
    journal_id: "AccountJournal"
    reason: str
    report_id: "AccountTaxReport"
    show_bit2publish_button: bool
    tax_report_line_id: "AccountTaxReportLine"
    def browse(self, ids: Union[int, List[int]]) -> "TaxAdjustmentsWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "TaxAdjustmentsWizard": ...
    def create(self, vals: Dict[str, Any]) -> "TaxAdjustmentsWizard": ...
    def filtered(self, func: Any) -> "TaxAdjustmentsWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "TaxAdjustmentsWizard": ...
    def exists(self) -> "TaxAdjustmentsWizard": ...
    def sudo(self) -> "TaxAdjustmentsWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "TaxAdjustmentsWizard": ...

# --- temporary.client ---

class TemporaryClient(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    fiscal_code: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    user_sequence: str
    vat: str
    def browse(self, ids: Union[int, List[int]]) -> "TemporaryClient": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "TemporaryClient": ...
    def create(self, vals: Dict[str, Any]) -> "TemporaryClient": ...
    def filtered(self, func: Any) -> "TemporaryClient": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "TemporaryClient": ...
    def exists(self) -> "TemporaryClient": ...
    def sudo(self) -> "TemporaryClient": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "TemporaryClient": ...

# --- trader ---

class Trader(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    code: str
    energy_supplier: str
    gas_supplier: str
    has_bit2publish_template: bool
    managed_by_arera: bool
    name: str
    show_bit2publish_button: bool
    status: str
    def browse(self, ids: Union[int, List[int]]) -> "Trader": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "Trader": ...
    def create(self, vals: Dict[str, Any]) -> "Trader": ...
    def filtered(self, func: Any) -> "Trader": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "Trader": ...
    def exists(self) -> "Trader": ...
    def sudo(self) -> "Trader": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "Trader": ...

# --- trader.import.wizard ---

class TraderImportWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    file_data: bytes
    file_name: str
    has_bit2publish_template: bool
    import_type: str
    show_bit2publish_button: bool
    source_type: str
    url: str
    def browse(self, ids: Union[int, List[int]]) -> "TraderImportWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "TraderImportWizard": ...
    def create(self, vals: Dict[str, Any]) -> "TraderImportWizard": ...
    def filtered(self, func: Any) -> "TraderImportWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "TraderImportWizard": ...
    def exists(self) -> "TraderImportWizard": ...
    def sudo(self) -> "TraderImportWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "TraderImportWizard": ...

# --- transport.network.map.management ---

class TransportNetworkMapManagement(Recordset):
    available_capacity: float
    bit2publish_template_ids: "Bit2publishTemplate"
    capacity_availability_date: Optional[_dt.date]
    cpi_pressure: float
    delivery_point: str
    deviation_count: str
    distance_from_rng: str
    has_bit2publish_template: bool
    mechanical_resistance_pressure: float
    minimum_pressure: float
    municipality: str
    name: str
    note: str
    physical_delivery_point: str
    pickup_type: str
    province: str
    reduction_pressure: float
    region: str
    show_bit2publish_button: bool
    status: str
    tisg: str
    total_allocated_capacity: float
    transport_capacity: float
    transporter: str
    validity_end_date: Optional[_dt.date]
    validity_start_date: Optional[_dt.date]
    withdrawal_area: str
    def browse(self, ids: Union[int, List[int]]) -> "TransportNetworkMapManagement": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "TransportNetworkMapManagement": ...
    def create(self, vals: Dict[str, Any]) -> "TransportNetworkMapManagement": ...
    def filtered(self, func: Any) -> "TransportNetworkMapManagement": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "TransportNetworkMapManagement": ...
    def exists(self) -> "TransportNetworkMapManagement": ...
    def sudo(self) -> "TransportNetworkMapManagement": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "TransportNetworkMapManagement": ...

# --- transport.network.map.management.history ---

class TransportNetworkMapManagementHistory(Recordset):
    available_capacity: float
    bit2publish_template_ids: "Bit2publishTemplate"
    capacity_availability_date: Optional[_dt.date]
    cpi_pressure: float
    delivery_point: str
    deviation_count: str
    distance_from_rng: str
    has_bit2publish_template: bool
    mechanical_resistance_pressure: float
    minimum_pressure: float
    municipality: str
    name: str
    note: str
    physical_delivery_point: str
    pickup_type: str
    province: str
    reduction_pressure: float
    region: str
    show_bit2publish_button: bool
    status: str
    tisg: str
    total_allocated_capacity: float
    transport_capacity: float
    transporter: str
    validity_end_date: Optional[_dt.date]
    validity_start_date: Optional[_dt.date]
    withdrawal_area: str
    def browse(self, ids: Union[int, List[int]]) -> "TransportNetworkMapManagementHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "TransportNetworkMapManagementHistory": ...
    def create(self, vals: Dict[str, Any]) -> "TransportNetworkMapManagementHistory": ...
    def filtered(self, func: Any) -> "TransportNetworkMapManagementHistory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "TransportNetworkMapManagementHistory": ...
    def exists(self) -> "TransportNetworkMapManagementHistory": ...
    def sudo(self) -> "TransportNetworkMapManagementHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "TransportNetworkMapManagementHistory": ...

# --- transporter.distributor.mixin ---

class TransporterDistributorMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    complete_contact_address: str
    contacts_for_quote_management: str
    end_date_status: Optional[_dt.date]
    fl_managed_bus: bool
    fl_managed_res: bool
    fl_transporter: bool
    gas_type: str
    has_bit2publish_template: bool
    info_msg_m2c: str
    is_admin_user: bool
    is_error_m2c: bool
    is_to_sync_with_m2c: bool
    last_sync_date: Optional[_dt.datetime]
    logistic_operator_type: str
    modified_by_operator: bool
    show_bit2publish_button: bool
    start_date_status: Optional[_dt.date]
    def browse(self, ids: Union[int, List[int]]) -> "TransporterDistributorMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "TransporterDistributorMixin": ...
    def create(self, vals: Dict[str, Any]) -> "TransporterDistributorMixin": ...
    def filtered(self, func: Any) -> "TransporterDistributorMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "TransporterDistributorMixin": ...
    def exists(self) -> "TransporterDistributorMixin": ...
    def sudo(self) -> "TransporterDistributorMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "TransporterDistributorMixin": ...

# --- unexecuted.file ---

class UnexecutedFile(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    error_description: str
    has_bit2publish_template: bool
    market_type: str
    name: str
    record_count: int
    record_ids: "UnexecutedRecord"
    server_id: "SorgeniaInvoiceExternalServiceFtpServer"
    show_bit2publish_button: bool
    state: str
    unexecuted_type: str
    def browse(self, ids: Union[int, List[int]]) -> "UnexecutedFile": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "UnexecutedFile": ...
    def create(self, vals: Dict[str, Any]) -> "UnexecutedFile": ...
    def filtered(self, func: Any) -> "UnexecutedFile": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "UnexecutedFile": ...
    def exists(self) -> "UnexecutedFile": ...
    def sudo(self) -> "UnexecutedFile": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "UnexecutedFile": ...

# --- unexecuted.record ---

class UnexecutedRecord(Recordset):
    amount: float
    billing_profile_id: "BillingProfile"
    bit2publish_template_ids: "Bit2publishTemplate"
    case_id: "HelpdeskTicket"
    case_state: "HelpdeskStage"
    client_id: "ResPartner"
    created_date: Optional[_dt.datetime]
    delivery_status: str
    detail_description: str
    document_code: str
    end_date: Optional[_dt.date]
    error_description: str
    external_document_code: str
    file_id: "UnexecutedFile"
    filename: str
    has_bit2publish_template: bool
    issue_date: Optional[_dt.date]
    last_delivery_update: Optional[_dt.datetime]
    market_type: str
    pod_id: "ResPartnerPod"
    pr_code: str
    processing_phase: str
    recipient_code: str
    recipient_name: str
    recipient_tax_code: str
    service_point_id: "ServicePoint"
    service_point_state: str
    show_bit2publish_button: bool
    start_date: Optional[_dt.date]
    state: str
    supplier_name: str
    unexecuted_invoice: str
    unexecuted_type: str
    updated_date: Optional[_dt.datetime]
    def browse(self, ids: Union[int, List[int]]) -> "UnexecutedRecord": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "UnexecutedRecord": ...
    def create(self, vals: Dict[str, Any]) -> "UnexecutedRecord": ...
    def filtered(self, func: Any) -> "UnexecutedRecord": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "UnexecutedRecord": ...
    def exists(self) -> "UnexecutedRecord": ...
    def sudo(self) -> "UnexecutedRecord": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "UnexecutedRecord": ...

# --- uom.category ---

class UomCategory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    reference_uom_id: "UomUom"
    show_bit2publish_button: bool
    uom_ids: "UomUom"
    def browse(self, ids: Union[int, List[int]]) -> "UomCategory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "UomCategory": ...
    def create(self, vals: Dict[str, Any]) -> "UomCategory": ...
    def filtered(self, func: Any) -> "UomCategory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "UomCategory": ...
    def exists(self) -> "UomCategory": ...
    def sudo(self) -> "UomCategory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "UomCategory": ...

# --- uom.uom ---

class UomUom(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    category_id: "UomCategory"
    color: int
    factor: float
    factor_inv: float
    has_bit2publish_template: bool
    name: str
    ratio: float
    rounding: float
    show_bit2publish_button: bool
    uom_type: str
    def browse(self, ids: Union[int, List[int]]) -> "UomUom": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "UomUom": ...
    def create(self, vals: Dict[str, Any]) -> "UomUom": ...
    def filtered(self, func: Any) -> "UomUom": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "UomUom": ...
    def exists(self) -> "UomUom": ...
    def sudo(self) -> "UomUom": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "UomUom": ...

# --- update.cadastre.data ---

class UpdateCadastreData(Recordset):
    administrative_location: str
    allowed_result_ids: "SympleTripletPhaseResult"
    bit2publish_template_ids: "Bit2publishTemplate"
    cadastral_code: str
    cadastral_date: Optional[_dt.date]
    cadastral_location: str
    cadastral_map: str
    cadastral_parcel: str
    cadastral_sub: str
    cadastre_data_id: "CadastreData"
    commodity: str
    customer_id: "ResPartner"
    declarant_type: str
    following_parcel: str
    has_bit2publish_template: bool
    house_number: str
    house_street: str
    missing_cadastral_reason: str
    parcel_type: str
    real_estate_unit_type: str
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    state_to_set: str
    subscriber_first_name: str
    subscriber_fiscal_code: str
    subscriber_last_name: str
    ticket_dc01_id: "HelpdeskTicket"
    ticket_gd07_id: "HelpdeskTicket"
    urban_section: str
    def browse(self, ids: Union[int, List[int]]) -> "UpdateCadastreData": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "UpdateCadastreData": ...
    def create(self, vals: Dict[str, Any]) -> "UpdateCadastreData": ...
    def filtered(self, func: Any) -> "UpdateCadastreData": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "UpdateCadastreData": ...
    def exists(self) -> "UpdateCadastreData": ...
    def sudo(self) -> "UpdateCadastreData": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "UpdateCadastreData": ...

# --- utm.campaign ---

class UtmCampaign(Recordset):
    ab_testing_completed: bool
    ab_testing_mailings_count: int
    ab_testing_schedule_datetime: Optional[_dt.datetime]
    ab_testing_sms_winner_selection: str
    ab_testing_total_pc: int
    ab_testing_winner_selection: str
    bit2publish_template_ids: "Bit2publishTemplate"
    bounced_ratio: int
    click_count: int
    color: int
    has_bit2publish_template: bool
    is_auto_campaign: bool
    mailing_mail_count: int
    mailing_mail_ids: "MailingMailing"
    mailing_sms_count: int
    mailing_sms_ids: "MailingMailing"
    name: str
    opened_ratio: int
    received_ratio: int
    replied_ratio: int
    show_bit2publish_button: bool
    stage_id: "UtmStage"
    tag_ids: "UtmTag"
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "UtmCampaign": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "UtmCampaign": ...
    def create(self, vals: Dict[str, Any]) -> "UtmCampaign": ...
    def filtered(self, func: Any) -> "UtmCampaign": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "UtmCampaign": ...
    def exists(self) -> "UtmCampaign": ...
    def sudo(self) -> "UtmCampaign": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "UtmCampaign": ...

# --- utm.medium ---

class UtmMedium(Recordset):
    active: bool
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "UtmMedium": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "UtmMedium": ...
    def create(self, vals: Dict[str, Any]) -> "UtmMedium": ...
    def filtered(self, func: Any) -> "UtmMedium": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "UtmMedium": ...
    def exists(self) -> "UtmMedium": ...
    def sudo(self) -> "UtmMedium": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "UtmMedium": ...

# --- utm.mixin ---

class UtmMixin(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    campaign_id: "UtmCampaign"
    has_bit2publish_template: bool
    medium_id: "UtmMedium"
    show_bit2publish_button: bool
    source_id: "UtmSource"
    def browse(self, ids: Union[int, List[int]]) -> "UtmMixin": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "UtmMixin": ...
    def create(self, vals: Dict[str, Any]) -> "UtmMixin": ...
    def filtered(self, func: Any) -> "UtmMixin": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "UtmMixin": ...
    def exists(self) -> "UtmMixin": ...
    def sudo(self) -> "UtmMixin": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "UtmMixin": ...

# --- utm.source ---

class UtmSource(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "UtmSource": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "UtmSource": ...
    def create(self, vals: Dict[str, Any]) -> "UtmSource": ...
    def filtered(self, func: Any) -> "UtmSource": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "UtmSource": ...
    def exists(self) -> "UtmSource": ...
    def sudo(self) -> "UtmSource": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "UtmSource": ...

# --- utm.stage ---

class UtmStage(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    sequence: int
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "UtmStage": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "UtmStage": ...
    def create(self, vals: Dict[str, Any]) -> "UtmStage": ...
    def filtered(self, func: Any) -> "UtmStage": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "UtmStage": ...
    def exists(self) -> "UtmStage": ...
    def sudo(self) -> "UtmStage": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "UtmStage": ...

# --- utm.tag ---

class UtmTag(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    color: int
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "UtmTag": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "UtmTag": ...
    def create(self, vals: Dict[str, Any]) -> "UtmTag": ...
    def filtered(self, func: Any) -> "UtmTag": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "UtmTag": ...
    def exists(self) -> "UtmTag": ...
    def sudo(self) -> "UtmTag": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "UtmTag": ...

# --- validate.account.move ---

class ValidateAccountMove(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    force_post: bool
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "ValidateAccountMove": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "ValidateAccountMove": ...
    def create(self, vals: Dict[str, Any]) -> "ValidateAccountMove": ...
    def filtered(self, func: Any) -> "ValidateAccountMove": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "ValidateAccountMove": ...
    def exists(self) -> "ValidateAccountMove": ...
    def sudo(self) -> "ValidateAccountMove": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "ValidateAccountMove": ...

# --- vulnerability.history ---

class VulnerabilityHistory(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    vulnerability_date: Optional[_dt.date]
    vulnerability_value: bool
    def browse(self, ids: Union[int, List[int]]) -> "VulnerabilityHistory": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "VulnerabilityHistory": ...
    def create(self, vals: Dict[str, Any]) -> "VulnerabilityHistory": ...
    def filtered(self, func: Any) -> "VulnerabilityHistory": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "VulnerabilityHistory": ...
    def exists(self) -> "VulnerabilityHistory": ...
    def sudo(self) -> "VulnerabilityHistory": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "VulnerabilityHistory": ...

# --- wallet.import.wizard ---

class WalletImportWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data: bytes
    filename: str
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "WalletImportWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "WalletImportWizard": ...
    def create(self, vals: Dict[str, Any]) -> "WalletImportWizard": ...
    def filtered(self, func: Any) -> "WalletImportWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "WalletImportWizard": ...
    def exists(self) -> "WalletImportWizard": ...
    def sudo(self) -> "WalletImportWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "WalletImportWizard": ...

# --- wallet.management.line ---

class WalletManagementLine(Recordset):
    agency: str
    agency_code: str
    agency_id: "ResPartner"
    agent: str
    agent_code: str
    agent_id: "ResPartner"
    bit2publish_template_ids: "Bit2publishTemplate"
    effective_date: Optional[_dt.date]
    effective_date_timedelta: str
    error: str
    has_bit2publish_template: bool
    is_multipoint: bool
    pr_code: str
    service_point_id: "ServicePoint"
    show_bit2publish_button: bool
    state: str
    def browse(self, ids: Union[int, List[int]]) -> "WalletManagementLine": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "WalletManagementLine": ...
    def create(self, vals: Dict[str, Any]) -> "WalletManagementLine": ...
    def filtered(self, func: Any) -> "WalletManagementLine": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "WalletManagementLine": ...
    def exists(self) -> "WalletManagementLine": ...
    def sudo(self) -> "WalletManagementLine": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "WalletManagementLine": ...

# --- watchlist.add.wizard ---

class WatchlistAddWizard(Recordset):
    batch_no: str
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    infocamere_monitored_partner_ids: "ResPartner"
    monitor_all_contacts: bool
    scope: str
    show_bit2publish_button: bool
    subscope: str
    def browse(self, ids: Union[int, List[int]]) -> "WatchlistAddWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "WatchlistAddWizard": ...
    def create(self, vals: Dict[str, Any]) -> "WatchlistAddWizard": ...
    def filtered(self, func: Any) -> "WatchlistAddWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "WatchlistAddWizard": ...
    def exists(self) -> "WatchlistAddWizard": ...
    def sudo(self) -> "WatchlistAddWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "WatchlistAddWizard": ...

# --- watchlist.download.wizard ---

class WatchlistDownloadWizard(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    has_subsequent_call: bool
    scope: str
    show_bit2publish_button: bool
    subscope: str
    subsequent_subscope: str
    def browse(self, ids: Union[int, List[int]]) -> "WatchlistDownloadWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "WatchlistDownloadWizard": ...
    def create(self, vals: Dict[str, Any]) -> "WatchlistDownloadWizard": ...
    def filtered(self, func: Any) -> "WatchlistDownloadWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "WatchlistDownloadWizard": ...
    def exists(self) -> "WatchlistDownloadWizard": ...
    def sudo(self) -> "WatchlistDownloadWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "WatchlistDownloadWizard": ...

# --- watchlist.remove.wizard ---

class WatchlistRemoveWizard(Recordset):
    batch_no: str
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    infocamere_monitored_partner_ids: "ResPartner"
    scope: str
    show_bit2publish_button: bool
    subscope: str
    def browse(self, ids: Union[int, List[int]]) -> "WatchlistRemoveWizard": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "WatchlistRemoveWizard": ...
    def create(self, vals: Dict[str, Any]) -> "WatchlistRemoveWizard": ...
    def filtered(self, func: Any) -> "WatchlistRemoveWizard": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "WatchlistRemoveWizard": ...
    def exists(self) -> "WatchlistRemoveWizard": ...
    def sudo(self) -> "WatchlistRemoveWizard": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "WatchlistRemoveWizard": ...

# --- web_editor.assets ---

class WebEditorAssets(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "WebEditorAssets": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "WebEditorAssets": ...
    def create(self, vals: Dict[str, Any]) -> "WebEditorAssets": ...
    def filtered(self, func: Any) -> "WebEditorAssets": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "WebEditorAssets": ...
    def exists(self) -> "WebEditorAssets": ...
    def sudo(self) -> "WebEditorAssets": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "WebEditorAssets": ...

# --- web_editor.converter.test ---

class WebEditorConverterTest(Recordset):
    binary: bytes
    bit2publish_template_ids: "Bit2publishTemplate"
    char: str
    date: Optional[_dt.date]
    datetime: Optional[_dt.datetime]
    float: float
    has_bit2publish_template: bool
    html: str
    integer: int
    many2one: "WebEditorConverterTestSub"
    numeric: float
    selection_str: str
    show_bit2publish_button: bool
    text: str
    def browse(self, ids: Union[int, List[int]]) -> "WebEditorConverterTest": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "WebEditorConverterTest": ...
    def create(self, vals: Dict[str, Any]) -> "WebEditorConverterTest": ...
    def filtered(self, func: Any) -> "WebEditorConverterTest": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "WebEditorConverterTest": ...
    def exists(self) -> "WebEditorConverterTest": ...
    def sudo(self) -> "WebEditorConverterTest": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "WebEditorConverterTest": ...

# --- web_editor.converter.test.sub ---

class WebEditorConverterTestSub(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "WebEditorConverterTestSub": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "WebEditorConverterTestSub": ...
    def create(self, vals: Dict[str, Any]) -> "WebEditorConverterTestSub": ...
    def filtered(self, func: Any) -> "WebEditorConverterTestSub": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "WebEditorConverterTestSub": ...
    def exists(self) -> "WebEditorConverterTestSub": ...
    def sudo(self) -> "WebEditorConverterTestSub": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "WebEditorConverterTestSub": ...

# --- web_tour.tour ---

class WebTourTour(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    name: str
    show_bit2publish_button: bool
    user_id: "ResUsers"
    def browse(self, ids: Union[int, List[int]]) -> "WebTourTour": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "WebTourTour": ...
    def create(self, vals: Dict[str, Any]) -> "WebTourTour": ...
    def filtered(self, func: Any) -> "WebTourTour": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "WebTourTour": ...
    def exists(self) -> "WebTourTour": ...
    def sudo(self) -> "WebTourTour": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "WebTourTour": ...

# --- wizard.ir.model.menu.create ---

class WizardIrModelMenuCreate(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    menu_id: "IrUiMenu"
    name: str
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "WizardIrModelMenuCreate": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "WizardIrModelMenuCreate": ...
    def create(self, vals: Dict[str, Any]) -> "WizardIrModelMenuCreate": ...
    def filtered(self, func: Any) -> "WizardIrModelMenuCreate": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "WizardIrModelMenuCreate": ...
    def exists(self) -> "WizardIrModelMenuCreate": ...
    def sudo(self) -> "WizardIrModelMenuCreate": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "WizardIrModelMenuCreate": ...

# --- x_ ---

class X(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    x_b2w_taskinstance_id: str
    x_data_chiusura: Optional[_dt.datetime]
    x_data_forzatura: Optional[_dt.datetime]
    x_data_richiesta: Optional[_dt.datetime]
    x_esito: str
    x_forzatura: bool
    x_id_richiesta: str
    x_name: str
    x_operatore: str
    x_operatore_forzatura: str
    x_stato: str
    def browse(self, ids: Union[int, List[int]]) -> "X": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "X": ...
    def create(self, vals: Dict[str, Any]) -> "X": ...
    def filtered(self, func: Any) -> "X": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "X": ...
    def exists(self) -> "X": ...
    def sudo(self) -> "X": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "X": ...

# --- x_ccq ---

class XCcq(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    x_b2w_taskinstance_id: str
    x_data: Optional[_dt.datetime]
    x_data_ricontatto: Optional[_dt.date]
    x_descrizione: str
    x_esito: str
    x_fascia_oraria_ricontatto: str
    x_notes: str
    x_status: str
    x_type: str
    def browse(self, ids: Union[int, List[int]]) -> "XCcq": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "XCcq": ...
    def create(self, vals: Dict[str, Any]) -> "XCcq": ...
    def filtered(self, func: Any) -> "XCcq": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "XCcq": ...
    def exists(self) -> "XCcq": ...
    def sudo(self) -> "XCcq": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "XCcq": ...

# --- x_mkt_com ---

class XMktCom(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    x_name: str
    def browse(self, ids: Union[int, List[int]]) -> "XMktCom": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "XMktCom": ...
    def create(self, vals: Dict[str, Any]) -> "XMktCom": ...
    def filtered(self, func: Any) -> "XMktCom": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "XMktCom": ...
    def exists(self) -> "XMktCom": ...
    def sudo(self) -> "XMktCom": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "XMktCom": ...

# --- x_pod ---

class XPod(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    x_name: str
    def browse(self, ids: Union[int, List[int]]) -> "XPod": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "XPod": ...
    def create(self, vals: Dict[str, Any]) -> "XPod": ...
    def filtered(self, func: Any) -> "XPod": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "XPod": ...
    def exists(self) -> "XPod": ...
    def sudo(self) -> "XPod": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "XPod": ...

# --- x_precheck ---

class XPrecheck(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    x_codice_pratica_utente: str
    x_data_precheck: Optional[_dt.datetime]
    x_esito: str
    x_note: str
    x_pdr: str
    x_pod: str
    x_stato: str
    x_task_id: str
    def browse(self, ids: Union[int, List[int]]) -> "XPrecheck": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "XPrecheck": ...
    def create(self, vals: Dict[str, Any]) -> "XPrecheck": ...
    def filtered(self, func: Any) -> "XPrecheck": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "XPrecheck": ...
    def exists(self) -> "XPrecheck": ...
    def sudo(self) -> "XPrecheck": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "XPrecheck": ...

# --- x_topny ---

class XTopny(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    has_bit2publish_template: bool
    show_bit2publish_button: bool
    x_name: str
    def browse(self, ids: Union[int, List[int]]) -> "XTopny": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "XTopny": ...
    def create(self, vals: Dict[str, Any]) -> "XTopny": ...
    def filtered(self, func: Any) -> "XTopny": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "XTopny": ...
    def exists(self) -> "XTopny": ...
    def sudo(self) -> "XTopny": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "XTopny": ...

# --- xmlgenerator.data_aggregator ---

class XmlgeneratorDataAggregator(Recordset):
    bit2publish_template_ids: "Bit2publishTemplate"
    data_model_ids: "XmlgeneratorDataModel"
    destination_module: str
    has_bit2publish_template: bool
    has_message: bool
    message_attachment_count: int
    message_follower_ids: "MailFollowers"
    message_has_error: bool
    message_has_error_counter: int
    message_has_sms_error: bool
    message_ids: "MailMessage"
    message_is_follower: bool
    message_main_attachment_id: "IrAttachment"
    message_needaction: bool
    message_needaction_counter: int
    message_partner_ids: "ResPartner"
    message_unread: bool
    message_unread_counter: int
    name: str
    show_bit2publish_button: bool
    total_data_models: int
    website_message_ids: "MailMessage"
    def browse(self, ids: Union[int, List[int]]) -> "XmlgeneratorDataAggregator": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "XmlgeneratorDataAggregator": ...
    def create(self, vals: Dict[str, Any]) -> "XmlgeneratorDataAggregator": ...
    def filtered(self, func: Any) -> "XmlgeneratorDataAggregator": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "XmlgeneratorDataAggregator": ...
    def exists(self) -> "XmlgeneratorDataAggregator": ...
    def sudo(self) -> "XmlgeneratorDataAggregator": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "XmlgeneratorDataAggregator": ...

# --- xmlgenerator.data_field ---

class XmlgeneratorDataField(Recordset):
    aggregator_id: "XmlgeneratorDataAggregator"
    bit2publish_template_ids: "Bit2publishTemplate"
    data_model_id: "XmlgeneratorDataModel"
    full_name: str
    has_bit2publish_template: bool
    is_relation_managed: bool
    relation_fields_to_search_ids: "IrModelFields"
    res_field_id: "IrModelFields"
    res_field_name: str
    res_field_relation: str
    res_field_ttype: str
    res_model_id: "IrModel"
    show_bit2publish_button: bool
    def browse(self, ids: Union[int, List[int]]) -> "XmlgeneratorDataField": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "XmlgeneratorDataField": ...
    def create(self, vals: Dict[str, Any]) -> "XmlgeneratorDataField": ...
    def filtered(self, func: Any) -> "XmlgeneratorDataField": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "XmlgeneratorDataField": ...
    def exists(self) -> "XmlgeneratorDataField": ...
    def sudo(self) -> "XmlgeneratorDataField": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "XmlgeneratorDataField": ...

# --- xmlgenerator.data_model ---

class XmlgeneratorDataModel(Recordset):
    aggregator_id: "XmlgeneratorDataAggregator"
    bit2publish_template_ids: "Bit2publishTemplate"
    data_field_ids: "XmlgeneratorDataField"
    destination_module: str
    full_name: str
    has_bit2publish_template: bool
    order: int
    order_by_expression: str
    res_model_domain: str
    res_model_id: "IrModel"
    show_bit2publish_button: bool
    total_data_fields: int
    xml_record_id: str
    xml_record_suffix_name: str
    def browse(self, ids: Union[int, List[int]]) -> "XmlgeneratorDataModel": ...
    def search(
        self,
        domain: List[Any],
        limit: Optional[int] = None,
        order: Optional[str] = None,
        offset: int = 0,
    ) -> "XmlgeneratorDataModel": ...
    def create(self, vals: Dict[str, Any]) -> "XmlgeneratorDataModel": ...
    def filtered(self, func: Any) -> "XmlgeneratorDataModel": ...
    def sorted(self, key: Any = None, reverse: bool = False) -> "XmlgeneratorDataModel": ...
    def exists(self) -> "XmlgeneratorDataModel": ...
    def sudo(self) -> "XmlgeneratorDataModel": ...
    def with_context(self, ctx: Dict[str, Any] = ..., **kwargs: Any) -> "XmlgeneratorDataModel": ...
