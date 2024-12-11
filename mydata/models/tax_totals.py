from dataclasses import dataclass
from typing import Optional


@dataclass
class TaxTotals:
    taxType: int = 0
    taxCategory: Optional[int] = None
    underlyingValue: Optional[float] = None
    taxAmount: float = 0.0
    id: Optional[int] = None
