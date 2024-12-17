import os
import sys
from decimal import Decimal
from pathlib import Path

from dotenv import load_dotenv

from mydata import MyDataClient, MyDataClientConfig
from mydata.exceptions import MyDataException, MyDataXMLParseException
from mydata.models import (
    Address,
    Counterpart,
    Country,
    Currency,
    IncomeClassification,
    IncomeClassificationCategory,
    IncomeClassificationValue,
    Invoice,
    InvoiceHeader,
    InvoiceRow,
    InvoiceType,
    Issuer,
    PaymentMethodDetail,
    PaymentMethodType,
    ResponseDoc,
    TaxTotals,
    TaxType,
    VatCategory,
    WithheldPercentCategory,
)

sys.path.append(str(Path(__file__).resolve().parent.parent))
load_dotenv()


def main():
    # Read credentials from environment variables
    user_id = os.getenv("MYDATA_USER", default=None)
    subscription_key = os.getenv("MYDATA_SUBSCRIPTION_KEY", default=None)

    # Configure the client
    config = MyDataClientConfig(environment="sandbox")

    # Initialize the client
    client = MyDataClient(
        user_id=user_id or "your-user-id",
        subscription_key=subscription_key or "your-subscription-key",
        config=config,
    )

    invoice = create_invoice()
    try:
        response_doc = client.send_invoice(invoice=invoice, response_model=ResponseDoc)
        for response in response_doc.response:
            print(
                f"Index: {response.index}  - UUID: {response.invoice_uid} - Mark: {response.invoice_mark} - Status: {response.status_code}"
            )

    except MyDataException as http_err:
        print("HTTP error occurred:", http_err)
    except MyDataXMLParseException as parse_err:
        print("XML parse error occurred:", parse_err)
    except Exception as e:
        print("An unexpected error occurred:", e)


def create_invoice() -> Invoice:
    # Requires a valid VAT number which must be the same as the one of your AADE
    # account if you want canceling/requesting docs to work properly
    issuer = Issuer(vat_number="888888888", country=Country.GR, branch=0)

    a = Address(postal_code="55236", city="Thessaloniki")
    counterpart = Counterpart(
        vat_number="999999999", country=Country.GR, branch=0, address=a
    )

    header = InvoiceHeader()
    header.series = "B"
    header.aa = "12"
    header.issue_date = "2024-12-13"
    header.invoice_type = InvoiceType.VALUE_2_1
    header.currency = Currency.EUR

    payment = PaymentMethodDetail()
    payment.type_value = PaymentMethodType.BANK_ACC_LOCAL
    payment.amount = Decimal(1300)
    payment.payment_method_info = "Some type of info"

    row = InvoiceRow()
    row.line_number = 1
    row.net_value = Decimal(1000)
    row.vat_category = VatCategory.VAT_1
    row.vat_amount = Decimal(240)
    row.income_classification = [
        IncomeClassification(
            classification_type=IncomeClassificationValue.E3_561_001,
            classification_category=IncomeClassificationCategory.CATEGORY1_3,
            amount=Decimal(1000),
        )
    ]
    tax = TaxTotals()
    tax.tax_type = TaxType.TYPE_1
    tax.tax_category = WithheldPercentCategory.TAX_2
    tax.underlying_value = Decimal(1000)
    tax.tax_amount = Decimal(200)

    invoice = Invoice()
    invoice.issuer = issuer
    invoice.counterpart = counterpart
    invoice.invoice_header = header
    invoice.invoice_details = [row]
    invoice.add_payment_method(payment)
    invoice.add_taxes_totals(tax)
    invoice.summarize()

    return invoice


if __name__ == "__main__":
    main()
