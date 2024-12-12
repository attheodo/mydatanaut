from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class TransportDetail:
    """
    Attributes:
        vehicle_number: Αριθμός Μεταφορικού Μέσου
    """

    class Meta:
        name = "TransportDetailType"

    vehicle_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 50,
        },
    )
