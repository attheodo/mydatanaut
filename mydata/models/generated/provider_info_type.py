from dataclasses import dataclass, field
from typing import List


@dataclass
class ProviderInfo:
    """
    Attributes:
        vatnumber: ΑΦΜ
    """

    class Meta:
        name = "ProviderInfoType"

    vatnumber: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VATNumber",
            "type": "Element",
        },
    )
