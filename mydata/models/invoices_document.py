from typing import List, Optional

from xsdata.formats.dataclass.models.elements import XmlType

from mydata.models.generated.invoices_doc import InvoicesDoc
from mydata.models.invoice import Invoice
from mydata.utils.xml_serializer import XmlSerializerService


class InvoicesDocument(InvoicesDoc):
    NAMESPACE_MAP = {
        None: "http://www.aade.gr/myDATA/invoice/v1.0",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "icls": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        "ecls": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
    }

    def __init__(self, invoices=List[Invoice], serializer=None):
        self.invoice = invoices
        self.serializer = serializer or XmlSerializerService()

    class Meta:
        name = "InvoicesDoc"
        nillable = False
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"
        type = XmlType.ELEMENT

    def as_xml(self, ns_map: Optional[dict] = None) -> str:
        return self.serializer.serialize(
            self, ns_map=ns_map or self.NAMESPACE_MAP
        )
