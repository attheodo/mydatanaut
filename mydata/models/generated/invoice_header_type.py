from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlTime

from mydata.models.generated.currency_type import Currency
from mydata.models.generated.entity_type import Entity
from mydata.models.generated.invoice_type import InvoiceType
from mydata.models.generated.other_delivery_note_header_type import (
    OtherDeliveryNoteHeader,
)

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class InvoiceHeader:
    """
    Attributes:
        series: Σειρά Παραστατικού
        aa: ΑΑ Παραστατικού
        issue_date: Ημερομηνία Έκδοσης
        invoice_type: Είδος Παραστατικού
        vat_payment_suspension: Αναστολή Καταβολής ΦΠΑ
        currency: Νόμισμα
        exchange_rate: Ισοτιμία
        correlated_invoices: Συσχετιζόμενα Παραστατικά
        self_pricing: Ένδειξη Αυτοτιμολόγησης
        dispatch_date: Ημερομηνία  Έναρξης Αποστολής
        dispatch_time: Ώρα Έναρξης Αποστολής
        vehicle_number: Αριθμός Οχήματος
        move_purpose: Σκοπός Διακίνησης
        fuel_invoice: Παραστατικό Καυσίμων
        special_invoice_category: Ειδική Κατηγορία Παραστατικού
        invoice_variation_type: Τύπος Απόκλισης Παραστατικού
        other_correlated_entities: Λοιπές συσχετιζόμενες οντοτήτες
        other_delivery_note_header: Λοιπά Γενικά Στοιχεία Διακίνησης
        is_delivery_note: Ένδειξη Παραστατικού Διακίνησης
        other_move_purpose_title: Τίτλος της Λοιπής Αιτίας Διακίνησης
        third_party_collection: Ένδειξη Εισπράξης Τρίτων
        multiple_connected_marks: Πολλαπλά Συνδεόμενα MARKs
        table_aa: AA ΤΡΑΠΕΖΙOY (για Δελτία Παραγγελίας Εστίασης)
        total_cancel_delivery_orders: Ένδειξη συνολικής αναίρεσης
            Δελτίων Παραγελίας
    """

    class Meta:
        name = "InvoiceHeaderType"

    series: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 50,
        },
    )
    aa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 50,
        },
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "issueDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    invoice_type: Optional[InvoiceType] = field(
        default=None,
        metadata={
            "name": "invoiceType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    vat_payment_suspension: Optional[bool] = field(
        default=None,
        metadata={
            "name": "vatPaymentSuspension",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    exchange_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "exchangeRate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("50000"),
            "fraction_digits": 5,
        },
    )
    correlated_invoices: List[int] = field(
        default_factory=list,
        metadata={
            "name": "correlatedInvoices",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    self_pricing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "selfPricing",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    dispatch_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "dispatchDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    dispatch_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "dispatchTime",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vehicle_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    move_purpose: Optional[int] = field(
        default=None,
        metadata={
            "name": "movePurpose",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 19,
        },
    )
    fuel_invoice: Optional[bool] = field(
        default=None,
        metadata={
            "name": "fuelInvoice",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    special_invoice_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "specialInvoiceCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 12,
        },
    )
    invoice_variation_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceVariationType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 4,
        },
    )
    other_correlated_entities: List[Entity] = field(
        default_factory=list,
        metadata={
            "name": "otherCorrelatedEntities",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_delivery_note_header: Optional[OtherDeliveryNoteHeader] = field(
        default=None,
        metadata={
            "name": "otherDeliveryNoteHeader",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    is_delivery_note: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isDeliveryNote",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_move_purpose_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "otherMovePurposeTitle",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    third_party_collection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "thirdPartyCollection",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    multiple_connected_marks: List[int] = field(
        default_factory=list,
        metadata={
            "name": "multipleConnectedMarks",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    table_aa: Optional[str] = field(
        default=None,
        metadata={
            "name": "tableAA",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 50,
        },
    )
    total_cancel_delivery_orders: Optional[bool] = field(
        default=None,
        metadata={
            "name": "totalCancelDeliveryOrders",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
