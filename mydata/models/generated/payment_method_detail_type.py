from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from mydata.models.generated.ecrtoken_type import Ecrtoken
from mydata.models.generated.provider_signature_type import ProviderSignature

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class PaymentMethodDetail:
    """
    Attributes:
        type_value: Τύπος Πληρωμής
        amount: Αναλογούν Ποσό
        payment_method_info: Λοιπές Πληροφορίες
        tip_amount: Φιλοδώρημα
        transaction_id: Μοναδική Ταυτότητα Πληρωμής
        tid: tid POS
        providers_signature: Υπογραφή Πληρωμής Παρόχου
        ecrtoken: Υπογραφή Πληρωμής ΦΗΜ με σύστημα λογισμικού (ERP)
    """

    class Meta:
        name = "PaymentMethodDetailType"

    type_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 8,
        },
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    payment_method_info: Optional[str] = field(
        default=None,
        metadata={
            "name": "paymentMethodInfo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    tip_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "tipAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    transaction_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "transactionId",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    tid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 200,
        },
    )
    providers_signature: Optional[ProviderSignature] = field(
        default=None,
        metadata={
            "name": "ProvidersSignature",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    ecrtoken: Optional[Ecrtoken] = field(
        default=None,
        metadata={
            "name": "ECRToken",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
