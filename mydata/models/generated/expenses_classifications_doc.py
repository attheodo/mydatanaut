from dataclasses import dataclass, field
from typing import List

from mydata.models.generated.invoice_expenses_classification_type import (
    InvoiceExpensesClassification,
)

__NAMESPACE__ = "https://www.aade.gr/myDATA/expensesClassificaton/v1.0"


@dataclass
class ExpensesClassificationsDoc:
    """
    Χαρατηρισμοί Εξόδων Πρότυπων Παραστατικών ΑΑΔΕ.
    """

    class Meta:
        namespace = "https://www.aade.gr/myDATA/expensesClassificaton/v1.0"

    expenses_invoice_classification: List[InvoiceExpensesClassification] = (
        field(
            default_factory=list,
            metadata={
                "name": "expensesInvoiceClassification",
                "type": "Element",
                "min_occurs": 1,
            },
        )
    )
