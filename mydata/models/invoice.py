from typing import Optional

from xsdata.formats.dataclass.models.elements import XmlType

from mydata.utils.invoice_summarizer import InvoiceSummarizer

from .counterpart import Counterpart
from .generated.aade_book_invoice_type import AadeBookInvoice
from .generated.invoice_summary_type import InvoiceSummary
from .generated.payment_method_detail_type import PaymentMethodDetail
from .generated.tax_totals_type import TaxTotals
from .issuer import Issuer


class Invoice(AadeBookInvoice):
    issuer: Optional[Issuer]
    counterpart: Optional[Counterpart]

    class Meta:
        name = "invoice"
        nillable = False
        namespace = "http://www.aade.gr/myDATA/invoice/v1.0"
        type = XmlType.ELEMENT

    def add_payment_method(self, method: PaymentMethodDetail):
        if not self.payment_methods:
            self.payment_methods = AadeBookInvoice.PaymentMethods()
        self.payment_methods.payment_method_details.append(method)

    def add_taxes_totals(self, tax: TaxTotals):
        if not self.taxes_totals:
            self.taxes_totals = AadeBookInvoice.TaxesTotals()
        self.taxes_totals.taxes.append(tax)

    def summarize(self) -> InvoiceSummary:
        s = InvoiceSummarizer(self).summarize()
        self.invoice_summary = s
        return s
