from dataclasses import dataclass, field
from typing import List, Optional

from mydata.models.generated.invoices_income_classification_detail_type import (
    InvoicesIncomeClassificationDetail,
)

__NAMESPACE__ = "https://www.aade.gr/myDATA/incomeClassificaton/v1.0"


@dataclass
class InvoiceIncomeClassification:
    """
    Attributes:
        invoice_mark: Μοναδικός Αριθμός Καταχώρησης Παραστατικού
        classification_mark: Αποδεικτικό Λήψης Χαρακτηρισμού Εσόδων.
            Συμπληρώνεται από την Υπηρεσία
        entity_vat_number: ΑΦΜ Οντότητας Αναφοράς
        transaction_mode: Αιτιολογία Συναλλαγής
        invoices_income_classification_details:
    """

    class Meta:
        name = "InvoiceIncomeClassificationType"

    invoice_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "required": True,
        },
    )
    classification_mark: Optional[int] = field(
        default=None,
        metadata={
            "name": "classificationMark",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )
    entity_vat_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "entityVatNumber",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )
    transaction_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "transactionMode",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 2,
        },
    )
    invoices_income_classification_details: List[
        InvoicesIncomeClassificationDetail
    ] = field(
        default_factory=list,
        metadata={
            "name": "invoicesIncomeClassificationDetails",
            "type": "Element",
            "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        },
    )
