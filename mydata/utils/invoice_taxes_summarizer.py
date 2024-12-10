from decimal import Decimal
from typing import List, Optional

from mydata.models.generated.invoice_row_type import InvoiceRow
from mydata.models.generated.invoice_summary_type import InvoiceSummary
from mydata.models.generated.tax_totals_type import TaxTotals
from mydata.models.tax_type import TaxType


class InvoiceTaxesSummarizer:
    def __init__(self, taxes: Optional[List[TaxTotals]] = None):
        self.taxes = taxes
        self.total_withheld_amount: Decimal = Decimal(0)
        self.total_fees_amount: Decimal = Decimal(0)
        self.total_stamp_duty_amount: Decimal = Decimal(0)
        self.total_other_taxes_amount: Decimal = Decimal(0)
        self.total_deductions_amount: Decimal = Decimal(0)
        self.total_informational_tax_amount: Decimal = Decimal(0)

    def summarize_taxes(self) -> None:
        if not self.taxes:
            return

        for tax in self.taxes:
            self.add_taxes_from_tax_totals(tax)

    def add_taxes_from_invoice_row(self, row: InvoiceRow) -> None:
        self.total_withheld_amount += abs(row.withheld_amount or Decimal(0))
        self.total_fees_amount += abs(row.fees_amount or Decimal(0))
        self.total_stamp_duty_amount += abs(row.stamp_duty_amount or Decimal(0))
        self.total_other_taxes_amount += abs(row.other_taxes_amount or Decimal(0))
        self.total_deductions_amount += abs(row.deductions_amount or Decimal(0))

        withheld_category = row.withheld_percent_category
        if withheld_category and not withheld_category.affects_total_gross_value:
            self.total_informational_tax_amount += abs(
                row.withheld_amount or Decimal(0)
            )

    def add_taxes_from_tax_totals(self, tax: TaxTotals) -> None:
        amount = abs(tax.tax_amount or Decimal(0))

        match tax.tax_type:
            case TaxType.TYPE_1:
                self.total_withheld_amount += amount
            case TaxType.TYPE_2:
                self.total_fees_amount += amount
            case TaxType.TYPE_3:
                self.total_other_taxes_amount += amount
            case TaxType.TYPE_4:
                self.total_stamp_duty_amount += amount
            case TaxType.TYPE_5:
                self.total_deductions_amount += amount

    def save_taxes(self, summary: InvoiceSummary) -> None:
        summary.total_withheld_amount = round(
            (summary.total_withheld_amount or Decimal(0)) + self.total_withheld_amount,
            2,
        )
        summary.total_fees_amount = round(
            (summary.total_fees_amount or Decimal(0)) + self.total_fees_amount, 2
        )
        summary.total_stamp_duty_amount = round(
            (summary.total_stamp_duty_amount or Decimal(0))
            + self.total_stamp_duty_amount,
            2,
        )
        summary.total_other_taxes_amount = round(
            (summary.total_other_taxes_amount or Decimal(0))
            + self.total_other_taxes_amount,
            2,
        )
        summary.total_deductions_amount = round(
            (summary.total_deductions_amount or Decimal(0))
            + self.total_deductions_amount,
            2,
        )

    def get_total_taxes(self) -> Decimal:
        return (
            -self.total_withheld_amount
            - self.total_deductions_amount
            + self.total_informational_tax_amount
            + self.total_fees_amount
            + self.total_stamp_duty_amount
            + self.total_other_taxes_amount
        )

    def save_totals(self, summary: InvoiceSummary) -> None:
        self.save_taxes(summary)

        gross_value = round(
            (summary.total_gross_value or Decimal(0)) + self.get_total_taxes(), 2
        )
        summary.total_gross_value = gross_value
