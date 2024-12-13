from typing import Dict

from mydata.models.generated.invoice_summary_type import InvoiceSummary
from mydata.utils.group_classifications import GroupClassifications
from mydata.utils.summarize_invoice_rows import SummarizeInvoiceRows
from mydata.utils.summarize_invoice_taxes import SummarizeInvoiceTaxes


class SummarizeInvoice:
    def handle(self, invoice, options: Dict = None) -> InvoiceSummary:
        """
        Summarizes the details, taxes, and classifications of an invoice.
        :param invoice: An Invoice object.
        :param options: Additional options (default: None).
        :return: An InvoiceSummary object.
        """
        if options is None:
            options = {}

        summary = InvoiceSummary()

        # Summarize invoice rows
        sum_invoice_rows = SummarizeInvoiceRows()
        sum_invoice_rows.handle(invoice.invoice_details, options)
        sum_invoice_rows.save_totals(summary)

        # Summarize invoice taxes
        sum_invoice_taxes = SummarizeInvoiceTaxes()
        sum_invoice_taxes.handle(invoice.taxes_totals.taxes, options)
        sum_invoice_taxes.save_totals(summary)

        # Group classifications
        classifications_group = GroupClassifications()
        icls, ecls = classifications_group.handle(invoice.invoice_details, options)

        summary.income_classification = icls
        summary.expenses_classification = ecls

        return summary
