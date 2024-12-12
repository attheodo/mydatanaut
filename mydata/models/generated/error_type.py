from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Error:
    """
    Attributes:
        message: Μήνυμα Σφάλματος
        code: Κωδικός Σφάλαματος
    """

    class Meta:
        name = "ErrorType"

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
