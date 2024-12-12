from dataclasses import dataclass, field
from typing import List

from mydata.models.generated.provider_info_type import ProviderInfo


@dataclass
class ReceptionProviders:
    """
    Attributes:
        provider_info: Πληροφορίες Παρόχου
    """

    class Meta:
        name = "receptionProvidersType"

    provider_info: List[ProviderInfo] = field(
        default_factory=list,
        metadata={
            "name": "ProviderInfo",
            "type": "Element",
        },
    )
