from decimal import Decimal
from typing import List, Optional

from mydata.models.generated.invoice_row_type import InvoiceRow
from mydata.models.generated.invoice_summary_type import InvoiceSummary
from mydata.utils.invoice_taxes_summarizer import InvoiceTaxesSummarizer


class InvoiceRowsSummarizer:
    def __init__(self, rows: Optional[List[InvoiceRow]]):
        self.rows = rows
        self.total_net_value = Decimal(0)
        self.total_vat_amount = Decimal(0)
        self.total_taxes = Decimal(0)
        self.tax_summarizer = InvoiceTaxesSummarizer()

    def summarize_rows(self) -> None:
        if not self.rows:
            return

        for row in self.rows:
            self.total_net_value += abs(row.net_value or Decimal(0))
            self.total_vat_amount += abs(row.vat_amount or Decimal(0))
            self.tax_summarizer.add_taxes_from_invoice_row(row)

    def save_totals(self, summary: InvoiceSummary) -> None:
        net_value = round(
            (summary.total_net_value or Decimal(0)) + self.total_net_value, 2
        )
        summary.total_net_value = net_value

        vat_amount = round(
            (summary.total_vat_amount or Decimal(0)) + self.total_vat_amount, 2
        )
        summary.total_vat_amount = vat_amount

        self.save_taxes(summary)

        summary.total_gross_value = self.get_total_gross_value()

    def save_taxes(self, summary: InvoiceSummary) -> None:
        self.tax_summarizer.save_taxes(summary)

    def get_total_gross_value(self) -> Decimal:
        return round(self.total_net_value + self.total_vat_amount, 2)

    def get_total_taxes(self) -> Decimal:
        return self.total_taxes
