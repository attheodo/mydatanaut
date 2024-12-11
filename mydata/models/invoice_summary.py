from dataclasses import dataclass, field
from typing import List


@dataclass
class InvoiceSummary:
    totalNetValue: float = 0.0
    totalVatAmount: float = 0.0
    totalWithheldAmount: float = 0.0
    totalFeesAmount: float = 0.0
    totalStampDutyAmount: float = 0.0
    totalOtherTaxesAmount: float = 0.0
    totalDeductionsAmount: float = 0.0
    totalGrossValue: float = 0.0
    incomeClassification: List[str] = field(default_factory=list)
    expensesClassification: List[str] = field(default_factory=list)
