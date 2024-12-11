from dataclasses import dataclass
from typing import Optional


@dataclass
class Address:
    street: Optional[str] = None
    number: Optional[str] = None
    postalCode: str = ""
    city: str = ""
