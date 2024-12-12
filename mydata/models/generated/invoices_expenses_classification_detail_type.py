from dataclasses import dataclass, field
from typing import List, Optional

from mydata.models.generated.expenses_classification_type import (
    ExpensesClassification,
)

__NAMESPACE__ = "https://www.aade.gr/myDATA/expensesClassificaton/v1.0"


@dataclass
class InvoicesExpensesClassificationDetail:
    """
    Attributes:
        line_number: Γραμμή Παραστατικού
        expenses_classification_detail_data: Λίστα Χαρακτηρισμών Εσόδων
    """

    class Meta:
        name = "InvoicesExpensesClassificationDetailType"

    line_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "required": True,
        },
    )
    expenses_classification_detail_data: List[ExpensesClassification] = field(
        default_factory=list,
        metadata={
            "name": "expensesClassificationDetailData",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "min_occurs": 1,
        },
    )
