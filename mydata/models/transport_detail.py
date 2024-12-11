from dataclasses import dataclass, field


@dataclass
class TransportDetail:
    """
    Represents transport details for a transaction.

    Attributes:
        vehicleNumber (str): Required. Transport means number. Maximum
        allowed length is 50.
    """

    vehicleNumber: str = field(default="", metadata={"max_length": 50})

    def __post_init__(self):
        if len(self.vehicleNumber) > 50:
            raise ValueError("vehicleNumber exceeds maximum length of 50 characters.")
