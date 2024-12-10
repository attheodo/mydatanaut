from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class Ecrtoken:
    """
    Attributes:
        signing_author: ECR id: Αριθμός μητρώου του φορολογικού
            μηχανισμού
        session_number: Μοναδικός 6-ψήφιος κωδικός που χαρακτηρίζει την
            κάθε συναλλαγή
    """

    class Meta:
        name = "ECRTokenType"

    signing_author: Optional[str] = field(
        default=None,
        metadata={
            "name": "SigningAuthor",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "max_length": 15,
        },
    )
    session_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SessionNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "length": 6,
        },
    )
