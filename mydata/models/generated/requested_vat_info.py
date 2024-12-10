from dataclasses import dataclass

from mydata.models.generated.requested_vat_info_type import RequestedVatInfo

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class RequestedVatInfo(RequestedVatInfo):
    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"
