from dataclasses import dataclass, field
from typing import Optional

from mydata.models.generated.party_type import Party

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class Entity:
    """
    Attributes:
        type_value: Κατηγορία
        entity_data: Στοιχεία Οντότητας
    """

    class Meta:
        name = "EntityType"

    type_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 6,
        },
    )
    entity_data: Optional[Party] = field(
        default=None,
        metadata={
            "name": "entityData",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
