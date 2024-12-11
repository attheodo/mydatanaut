from dataclasses import dataclass
from typing import Optional

from .address import Address


@dataclass
class Party:
    vatNumber: str = ""
    country: str = ""
    branch: int = 0
    name: Optional[str] = None
    address: Optional[Address] = None
    documentIdNo: Optional[str] = None
    supplyAccountNo: Optional[str] = None
    countryDocumentId: Optional[str] = None
