from dataclasses import dataclass, field
from typing import List, Optional

from mydata.models.generated.invoices_expenses_classification_detail_type import (
    InvoicesExpensesClassificationDetail,
)

__NAMESPACE__ = "https://www.aade.gr/myDATA/expensesClassificaton/v1.0"


@dataclass
class InvoiceExpensesClassification:
    """
    Attributes:
        invoice_mark: Μοναδικός Αριθμός Καταχώρησης Παραστατικού
        classification_mark: Αποδεικτικό Λήψης Χαρακτηρισμού Εξόδων.
            Συμπληρώνεται από την Υπηρεσία
        entity_vat_number: ΑΦΜ Οντότητας Αναφοράς
        transaction_mode: Αιτιολογία Συναλλαγής
        invoices_expenses_classification_details:
        classification_post_mode: Μέθοδος Υποβολής Χαρακτηρισμού
    """

    class Meta:
        name = "InvoiceExpensesClassificationType"

    invoice_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "required": True,
        },
    )
    classification_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "classificationMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    entity_vat_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityVatNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    transaction_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "transactionMode",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 2,
        },
    )
    invoices_expenses_classification_details: List[
        InvoicesExpensesClassificationDetail
    ] = field(
        default_factory=list,
        metadata={
            "name": "invoicesExpensesClassificationDetails",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
        },
    )
    classification_post_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "classificationPostMode",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            "min_inclusive": 0,
            "max_inclusive": 1,
        },
    )
