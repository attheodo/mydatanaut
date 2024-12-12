from dataclasses import dataclass, field
from typing import List

from mydata.models.generated.continuation_token_type_2 import (
    ContinuationTokenType2,
)
from mydata.models.generated.invoice_provider_type import InvoiceProvider


@dataclass
class RequestedProviderDoc:
    """
    Παραστατικά από Πάροχο.
    """

    continuation_token: List[ContinuationTokenType2] = field(
        default_factory=list,
        metadata={
            "name": "continuationToken",
            "type": "Element",
            "sequence": 1,
        },
    )
    invoice_provider_type: List[InvoiceProvider] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceProviderType",
            "type": "Element",
            "sequence": 1,
        },
    )
