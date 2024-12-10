from dataclasses import dataclass, field
from typing import List, Optional

from mydata.models.generated.aade_book_invoice_type import AadeBookInvoice
from mydata.models.generated.cancelled_invoice_type import CancelledInvoice
from mydata.models.generated.continuation_token_type_3 import (
    ContinuationTokenType3,
)
from mydata.models.generated.invoice_expenses_classification_type import (
    InvoiceExpensesClassification,
)
from mydata.models.generated.invoice_income_classification_type import (
    InvoiceIncomeClassification,
)
from mydata.models.generated.payment_method_type import PaymentMethod

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class RequestedDoc:
    class Meta:
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"

    continuation_token: Optional[ContinuationTokenType3] = field(
        default=None,
        metadata={
            "name": "continuationToken",
            "type": "Element",
        },
    )
    invoices_doc: Optional["RequestedDoc.InvoicesDoc"] = field(
        default=None,
        metadata={
            "name": "invoicesDoc",
            "type": "Element",
        },
    )
    cancelled_invoices_doc: Optional["RequestedDoc.CancelledInvoicesDoc"] = field(
        default=None,
        metadata={
            "name": "cancelledInvoicesDoc",
            "type": "Element",
        },
    )
    income_classifications_doc: Optional["RequestedDoc.IncomeClassificationsDoc"] = (
        field(
            default=None,
            metadata={
                "name": "incomeClassificationsDoc",
                "type": "Element",
            },
        )
    )
    expenses_classifications_doc: Optional[
        "RequestedDoc.ExpensesClassificationsDoc"
    ] = field(
        default=None,
        metadata={
            "name": "expensesClassificationsDoc",
            "type": "Element",
        },
    )
    payment_methods_doc: Optional["RequestedDoc.PaymentMethodsDoc"] = field(
        default=None,
        metadata={
            "name": "paymentMethodsDoc",
            "type": "Element",
        },
    )

    @dataclass
    class InvoicesDoc:
        invoice: List[AadeBookInvoice] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass
    class CancelledInvoicesDoc:
        cancelled_invoice: List[CancelledInvoice] = field(
            default_factory=list,
            metadata={
                "name": "cancelledInvoice",
                "type": "Element",
            },
        )

    @dataclass
    class IncomeClassificationsDoc:
        income_invoice_classification: List[InvoiceIncomeClassification] = field(
            default_factory=list,
            metadata={
                "name": "incomeInvoiceClassification",
                "type": "Element",
                "namespace": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
            },
        )

    @dataclass
    class ExpensesClassificationsDoc:
        expenses_invoice_classification: List[InvoiceExpensesClassification] = field(
            default_factory=list,
            metadata={
                "name": "expensesInvoiceClassification",
                "type": "Element",
                "namespace": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
            },
        )

    @dataclass
    class PaymentMethodsDoc:
        payment_methods: List[PaymentMethod] = field(
            default_factory=list,
            metadata={
                "name": "paymentMethods",
                "type": "Element",
            },
        )
