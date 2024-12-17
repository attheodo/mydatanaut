from mydata.models.generated.invoice_summary_type import InvoiceSummary
from mydata.utils.classifications_grouper import ClassificationsGrouper
from mydata.utils.invoice_rows_summarizer import InvoiceRowsSummarizer
from mydata.utils.invoice_taxes_summarizer import InvoiceTaxesSummarizer


class InvoiceSummarizer:
    def __init__(self, invoice):
        self.invoice = invoice

    def summarize(self) -> InvoiceSummary:
        summary = InvoiceSummary()

        rows_summarizer = InvoiceRowsSummarizer(rows=self.invoice.invoice_details)
        rows_summarizer.summarize_rows()
        rows_summarizer.save_totals(summary)

        if (
            getattr(self.invoice, "taxes_totals", None)
            and self.invoice.taxes_totals.taxes
        ):
            taxes_summarizer = InvoiceTaxesSummarizer(
                taxes=self.invoice.taxes_totals.taxes
            )
            taxes_summarizer.summarize_taxes()
            taxes_summarizer.save_totals(summary)

        classifications_group = ClassificationsGrouper(
            rows=self.invoice.invoice_details
        )
        icls, ecls = classifications_group.create_groups()

        summary.income_classification = icls
        summary.expenses_classification = ecls

        return summary
