from dataclasses import dataclass, field
from typing import List

from mydata.models.generated.aade_book_invoice_type import AadeBookInvoice

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class InvoicesDoc:
    """
    Παραστατικό ΑΑΔΕ.
    """

    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    invoice: List[AadeBookInvoice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
