from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from mydata.models.generated.income_classification_category_type import (
    IncomeClassificationCategory,
)
from mydata.models.generated.income_classification_value_type import (
    IncomeClassificationValue,
)

__NAMESPACE__ = "https://www.aade.gr/myDATA/incomeClassificaton/v1.0"


@dataclass
class IncomeClassification:
    """
    Attributes:
        classification_type: Κωδικός Χαρακτηρισμού
        classification_category: Κατηγορία Χαρακτηρισμού
        amount: Ποσό Χαρακτηρισμού
        id: Μοναδικός Αριθμός Χαρακτηρισμού
    """

    class Meta:
        name = "IncomeClassificationType"

    classification_type: Optional[IncomeClassificationValue] = field(
        default=None,
        metadata={
            "name": "classificationType",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )
    classification_category: Optional[IncomeClassificationCategory] = field(
        default=None,
        metadata={
            "name": "classificationCategory",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "required": True,
        },
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )
