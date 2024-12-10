from dataclasses import dataclass, field
from typing import List

from mydata.models.generated.response_type import Response


@dataclass
class ResponseDoc:
    """
    Comment describing your root element.
    """

    response: List[Response] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
