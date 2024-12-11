from dataclasses import dataclass
from typing import Optional


@dataclass
class PaymentMethodDetail:
    type: int = 0
    amount: float = 0.0
    paymentMethodInfo: Optional[str] = None
    tipAmount: Optional[float] = None
    transactionId: Optional[str] = None
    tid: Optional[str] = None
    ProvidersSignature: Optional[str] = None
    ECRToken: Optional[str] = None
