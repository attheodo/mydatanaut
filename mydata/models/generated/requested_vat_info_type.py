from dataclasses import dataclass, field
from typing import List, Optional

from mydata.models.generated.continuation_token_type_1 import (
    ContinuationTokenType1,
)
from mydata.models.generated.invoice_vat_detail_type import InvoiceVatDetail

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class RequestedVatInfo:
    class Meta:
        name = "RequestedVatInfoType"

    continuation_token: Optional[ContinuationTokenType1] = field(
        default=None,
        metadata={
            "name": "continuationToken",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    vat_info: List[InvoiceVatDetail] = field(
        default_factory=list,
        metadata={
            "name": "VatInfo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
