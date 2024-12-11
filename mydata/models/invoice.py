from dataclasses import dataclass, field
from typing import List, Optional

from .invoice_header import InvoiceHeader
from .invoice_row import InvoiceRow
from .invoice_summary import InvoiceSummary
from .party import Party
from .payment_method_detail import PaymentMethodDetail
from .tax_totals import TaxTotals
from .transport_detail import TransportDetail


@dataclass
class Invoice:
    uid: Optional[str] = None
    mark: Optional[int] = None
    cancelledByMark: Optional[int] = None
    authenticationCode: Optional[str] = None
    transmissionFailure: Optional[int] = None
    issuer: Optional[Party] = None
    counterpart: Optional[Party] = None
    invoiceHeader: InvoiceHeader = None
    paymentMethods: List[PaymentMethodDetail] = field(default_factory=list)
    invoiceDetails: List[InvoiceRow] = field(default_factory=list)
    taxesTotals: List[TaxTotals] = field(default_factory=list)
    invoiceSummary: InvoiceSummary = None
    qrCodeUrl: Optional[str] = None
    otherTransportDetails: List[TransportDetail] = field(default_factory=list)
