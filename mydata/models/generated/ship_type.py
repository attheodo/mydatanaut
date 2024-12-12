from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class Ship:
    """
    Attributes:
        application_id: Αριθμός Δήλωσης διενέργειας δραστηριότητας
        application_date: Ημερομηνία Δήλωσης
        doy:
        ship_id: Στοιχεία Πλοίου
    """

    class Meta:
        name = "ShipType"

    application_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "applicationId",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    application_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "applicationDate",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
    doy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    ship_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "shipId",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
        },
    )
