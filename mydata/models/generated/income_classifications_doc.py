from dataclasses import dataclass, field
from typing import List

from mydata.models.generated.invoice_income_classification_type import (
    InvoiceIncomeClassification,
)

__NAMESPACE__ = "https://www.aade.gr/myDATA/incomeClassificaton/v1.0"


@dataclass
class IncomeClassificationsDoc:
    """
    Χαρατηρισμοί Εσόδων Πρότυπων Παραστατικών ΑΑΔΕ.
    """

    class Meta:
        namespace = "https://www.aade.gr/myDATA/incomeClassificaton/v1.0"

    income_invoice_classification: List[InvoiceIncomeClassification] = field(
        default_factory=list,
        metadata={
            "name": "incomeInvoiceClassification",
            "type": "Element",
            "min_occurs": 1,
        },
    )
