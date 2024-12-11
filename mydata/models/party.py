from dataclasses import dataclass
from typing import Optional

from .address import Address


@dataclass
class Party:
    """
    Represents a party with relevant identification and address details.

    Attributes:
        vatNumber (str): Required. Any valid VAT number.

        country (str): Required. Two-character country code based on ISO 3166.

        branch (int): Required. Branch number. Must be 0 if it is the
        headquarters or does not exist.

        name (Optional[str]): Optional. Valid for issuer only if the entity
        is not from Greece. Must not be submitted for the counterpart if the
        entity is from Greece.

        address (Optional[Address]): Optional. Valid for issuer only if the
        entity is not from Greece.

        documentIdNo (Optional[str]): Optional. Allowed only for tax-free
        vouchers (specialInvoiceCategory = 4). It can be any official
        identification document (e.g., passport number) of the voucher
        recipient. Maximum length is 100.

        supplyAccountNo (Optional[str]): Optional. Allowed only for fuel
        vouchers (fuelInvoice = true). Refers to the Electricity Supply Number
        of the voucher recipient. Maximum length is 100.

        countryDocumentId (Optional[str]): Optional. Allowed only for tax-free
        vouchers (specialInvoiceCategory = 4) if documentIdNo is provided.
        Refers to the country code of issuance of the official document
        (e.g., passport).
    """

    vatNumber: str = ""
    country: str = ""
    branch: int = 0
    name: Optional[str] = None
    address: Optional[Address] = None
    documentIdNo: Optional[str] = None
    supplyAccountNo: Optional[str] = None
    countryDocumentId: Optional[str] = None


@dataclass
class Issuer(Party):
    pass


@dataclass
class Counterpart(Party):
    pass
