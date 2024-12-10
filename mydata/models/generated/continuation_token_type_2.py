from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ContinuationTokenType2:
    class Meta:
        name = "continuationTokenType"

    next_partition_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "nextPartitionKey",
            "type": "Element",
            "required": True,
        },
    )
    next_row_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "nextRowKey",
            "type": "Element",
            "required": True,
        },
    )
