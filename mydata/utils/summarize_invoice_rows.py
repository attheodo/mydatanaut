from decimal import Decimal
from typing import List, Optional

from mydata.models.generated.invoice_row_type import InvoiceRow
from mydata.models.generated.invoice_summary_type import InvoiceSummary


class SummarizeInvoiceRows:
    def __init__(self):
        self.total_net_value = Decimal(0)
        self.total_vat_amount = Decimal(0)
        self.total_taxes = Decimal(0)

    def handle(self, rows: Optional[List[InvoiceRow]], options: dict = None) -> None:
        """
        Process a list of invoice rows and calculate totals.
        :param rows: List of InvoiceRow objects or None.
        :param options: Additional options (not used in this implementation).
        """
        if not rows:
            return

        for row in rows:
            self.total_net_value += abs(row.net_value or Decimal(0))
            self.total_vat_amount += abs(row.vat_amount or Decimal(0))
            self.total_taxes += abs(row.vat_amount or Decimal(0))

    def save_totals(self, summary: InvoiceSummary) -> None:
        """
        Save calculated totals into the invoice summary.
        :param summary: InvoiceSummary object.
        """
        net_value = self.round(
            (summary.total_net_value or Decimal(0)) + self.total_net_value
        )
        summary.total_net_value = net_value

        vat_amount = self.round(
            (summary.total_vat_amount or Decimal(0)) + self.total_vat_amount
        )
        summary.total_vat_amount = vat_amount

        self.save_taxes(summary)

        summary.total_gross_value = self.get_total_gross_value()

    def save_taxes(self, summary: InvoiceSummary) -> None:
        """
        Save calculated taxes into the invoice summary (implementation placeholder).
        :param summary: InvoiceSummary object.
        """
        # Logic for saving taxes to the summary, depending on its structure
        pass

    def get_total_gross_value(self) -> Decimal:
        """
        Calculate and return the total gross value.
        """
        return self.round(
            self.total_net_value + self.total_vat_amount  # + self.get_total_taxes()
        )

    def get_total_taxes(self) -> Decimal:
        """
        Return the total taxes calculated.
        """
        return self.total_taxes

    @staticmethod
    def round(value: Decimal) -> Decimal:
        """
        Round the given value to 2 decimal places.
        :param value: Decimal value.
        """
        return value.quantize(Decimal("0.01"))
