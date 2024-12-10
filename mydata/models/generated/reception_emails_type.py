from dataclasses import dataclass, field
from typing import List


@dataclass
class ReceptionEmails:
    """
    Attributes:
        email: Email
    """

    class Meta:
        name = "receptionEmailsType"

    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
