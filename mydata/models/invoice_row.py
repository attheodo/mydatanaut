from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class InvoiceRowType:
    lineNumber: int = 1
    recType: Optional[int] = None
    TaricNo: Optional[str] = None
    itemCode: Optional[str] = None
    itemDescr: Optional[str] = None
    fuelCode: Optional[str] = None
    quantity: Optional[float] = None
    measurementUnit: Optional[str] = None
    invoiceDetailType: Optional[int] = None
    netValue: float = 0.0
    vatCategory: int = 0
    vatAmount: float = 0.0
    vatExemptionCategory: Optional[int] = None
    dienergia: Optional[str] = None
    discountOption: Optional[bool] = None
    withheldAmount: Optional[float] = None
    withheldPercentCategory: Optional[int] = None
    stampDutyAmount: Optional[float] = None
    stampDutyPercentCategory: Optional[int] = None
    feesAmount: Optional[float] = None
    feesPercentCategory: Optional[int] = None
    otherTaxesPercentCategory: Optional[int] = None
    otherTaxesAmount: Optional[float] = None
    deductionsAmount: Optional[float] = None
    lineComments: Optional[str] = None
    incomeClassification: List[str] = field(default_factory=list)
    expensesClassification: List[str] = field(default_factory=list)
    quantity15: Optional[float] = None
    otherMeasurementUnitQuantity: Optional[int] = None
    otherMeasurementUnitTitle: Optional[str] = None
    notVAT195: Optional[bool] = None
