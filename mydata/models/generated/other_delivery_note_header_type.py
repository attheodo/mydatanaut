from dataclasses import dataclass, field
from typing import Optional

from mydata.models.generated.address_type import Address

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class OtherDeliveryNoteHeader:
    """
    Attributes:
        loading_address: Διεύθυνση Φόρτωσης
        delivery_address: Διεύθυνση Παράδοσης
        start_shipping_branch: Εγκατάσταση έναρξης διακίνησης (Εκδότη)
        complete_shipping_branch: Εγκατάσταση ολοκλήρωσης διακίνησης
            (Λήπτη)
    """

    class Meta:
        name = "OtherDeliveryNoteHeaderType"

    loading_address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "loadingAddress",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    delivery_address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "deliveryAddress",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    start_shipping_branch: Optional[int] = field(
        default=None,
        metadata={
            "name": "startShippingBranch",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    complete_shipping_branch: Optional[int] = field(
        default=None,
        metadata={
            "name": "completeShippingBranch",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
