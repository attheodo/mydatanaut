from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class CancelledInvoice:
    """
    Attributes:
        invoice_mark: Μοναδικός Αριθμός Καταχώρησης του ακυρωμένου
            Παραστατικού
        cancellation_mark: Μοναδικός Αριθμός Καταχώρησης της Ακύρωσης
        cancellation_date: Ημερομηνία Ακύρωσης Παραστατικού
    """

    class Meta:
        name = "CancelledInvoiceType"

    invoice_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceMark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    cancellation_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "cancellationMark",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    cancellation_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "cancellationDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
