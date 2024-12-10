from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class Address:
    """
    Attributes:
        street:
        number: Αριθμός
        postal_code: ΤΚ
        city:
    """

    class Meta:
        name = "AddressType"

    street: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 150,
        },
    )
