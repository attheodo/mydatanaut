from dataclasses import dataclass, field
from typing import List

from mydata.models.generated.payment_method_type import PaymentMethod

__NAMESPACE__ = "https://www.aade.gr/myDATA/paymentMethod/v1.0"


@dataclass
class PaymentMethodsDoc:
    """
    Μέθοδοι Πληρωμής.
    """

    class Meta:
        namespace = "https://www.aade.gr/myDATA/paymentMethod/v1.0"

    payment_methods: List[PaymentMethod] = field(
        default_factory=list,
        metadata={
            "name": "paymentMethods",
            "type": "Element",
            "min_occurs": 1,
        },
    )
