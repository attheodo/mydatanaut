from dataclasses import dataclass, field
from typing import Optional


@dataclass
class InvoiceProvider:
    """
    Attributes:
        issuer_vat: ΑΦΜ Εκδότη
        invoice_provider_mark: Μοναδικός Αριθμός Καταχώρησης
            παραστατικού Παρόχου
        invoice_uid: Αναγνωριστικό οντότητας
        authentication_code: Συμβολοσειρά Αυθεντικοποίησης Παραστατικού
            Παρόχου
    """

    class Meta:
        name = "InvoiceProviderType"

    issuer_vat: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerVAT",
            "type": "Element",
            "required": True,
        },
    )
    invoice_provider_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceProviderMark",
            "type": "Element",
            "required": True,
        },
    )
    invoice_uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "invoiceUid",
            "type": "Element",
            "required": True,
        },
    )
    authentication_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "authenticationCode",
            "type": "Element",
            "required": True,
        },
    )
