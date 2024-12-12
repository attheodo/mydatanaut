from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class TaxTotals:
    """
    Attributes:
        tax_type: Είδος Φόρου
        tax_category: Κατηγορία Φόρου
        underlying_value: Υποκείμενη Αξία
        tax_amount: Ποσό Φόρου
        id:
    """

    class Meta:
        name = "TaxTotalsType"

    tax_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "taxType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 5,
        },
    )
    tax_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "taxCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
        },
    )
    underlying_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "underlyingValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    tax_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "taxAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
