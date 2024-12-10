from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class ProviderSignature:
    """
    Attributes:
        signing_author: Provider’s Id
        signature: Υπογραφή
    """

    class Meta:
        name = "ProviderSignatureType"

    signing_author: Optional[str] = field(
        default=None,
        metadata={
            "name": "SigningAuthor",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 20,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
