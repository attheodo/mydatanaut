from dataclasses import dataclass, field
from typing import List, Optional

from mydata.models.generated.income_classification_type import (
    IncomeClassification,
)

__NAMESPACE__ = "https://www.aade.gr/myDATA/incomeClassificaton/v1.0"


@dataclass
class InvoicesIncomeClassificationDetail:
    """
    Attributes:
        line_number: Γραμμή Παραστατικού
        income_classification_detail_data: Λίστα Χαρακτηρισμών Εσόδων
    """

    class Meta:
        name = "InvoicesIncomeClassificationDetailType"

    line_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "required": True,
        },
    )
    income_classification_detail_data: List[IncomeClassification] = field(
        default_factory=list,
        metadata={
            "name": "incomeClassificationDetailData",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "min_occurs": 1,
        },
    )
