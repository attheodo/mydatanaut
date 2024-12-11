from dataclasses import dataclass, field
from typing import List, Optional

from .address import Address
from .party import Party


@dataclass
class InvoiceHeader:
    series: str = ""
    aa: str = ""
    issueDate: str = ""
    invoiceType: str = ""
    vatPaymentSuspension: Optional[bool] = None
    currency: Optional[str] = None
    exchangeRate: Optional[float] = None
    correlatedInvoices: List[int] = field(default_factory=list)
    selfPricing: Optional[bool] = None
    dispatchDate: Optional[str] = None
    dispatchTime: Optional[str] = None
    vehicleNumber: Optional[str] = None
    movePurpose: Optional[int] = None
    fuelInvoice: Optional[bool] = None
    specialInvoiceCategory: Optional[int] = None
    invoiceVariationType: Optional[int] = None
    otherCorrelatedEntities: List[Party] = field(default_factory=list)
    otherDeliveryNoteHeader: Optional[Address] = None
    isDeliveryNote: Optional[bool] = None
    otherMovePurposeTitle: Optional[str] = None
    thirdPartyCollection: Optional[bool] = None
    multipleConnectedMarks: List[int] = field(default_factory=list)
    tableAA: Optional[str] = None
    totalCancelDeliveryOrders: Optional[bool] = None
