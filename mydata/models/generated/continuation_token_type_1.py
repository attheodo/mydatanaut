from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class ContinuationTokenType1:
    class Meta:
        name = "ContinuationTokenType"

    next_partition_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "nextPartitionKey",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    next_row_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "nextRowKey",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
