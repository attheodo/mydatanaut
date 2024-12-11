from dataclasses import dataclass, field
from typing import List

from .invoice import Invoice


@dataclass
class InvoicesDoc:
    invoice: List[Invoice] = field(default_factory=list)
