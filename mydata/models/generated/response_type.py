from dataclasses import dataclass, field
from typing import List, Optional

from mydata.models.generated.error_type import Error
from mydata.models.generated.reception_emails_type import ReceptionEmails
from mydata.models.generated.reception_providers_type import ReceptionProviders


@dataclass
class Response:
    """
    Attributes:
        index: ΑΑ γραμμής οντότητας
        invoice_uid: Αναγνωριστικό οντότητας
        invoice_mark: Μοναδικός Αριθμός Καταχώρησης παραστατικού
        qr_url: QR Code Url
        classification_mark: Μοναδικός Αριθμός Παραλαβής Χαρακτηρισμού
        cancellation_mark: Μοναδικός Αριθμός Ακύρωσης
        payment_method_mark: Μοναδικός Αριθμός Παραλαβής Τρόπου Πληρωμής
        authentication_code: Συμβολοσειρά Αυθεντικοποίησης Παρόχου
        reception_providers: Πάροχοι Λήπτη
        reception_emails: Email Παραλαβής
        errors: Λίστα Σφαλμάτων
        status_code: Κωδικός αποτελέσματος
    """

    class Meta:
        name = "ResponseType"

    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    invoice_uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "invoiceUid",
            "type": "Element",
        },
    )
    invoice_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceMark",
            "type": "Element",
        },
    )
    qr_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "qrUrl",
            "type": "Element",
        },
    )
    classification_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "classificationMark",
            "type": "Element",
        },
    )
    cancellation_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "cancellationMark",
            "type": "Element",
        },
    )
    payment_method_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "paymentMethodMark",
            "type": "Element",
        },
    )
    authentication_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "authenticationCode",
            "type": "Element",
        },
    )
    reception_providers: Optional[ReceptionProviders] = field(
        default=None,
        metadata={
            "name": "receptionProviders",
            "type": "Element",
        },
    )
    reception_emails: Optional[ReceptionEmails] = field(
        default=None,
        metadata={
            "name": "receptionEmails",
            "type": "Element",
        },
    )
    errors: Optional["Response.Errors"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    status_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Errors:
        error: List[Error] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )
