from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from mydata.models.generated.expenses_classification_type import (
    ExpensesClassification,
)
from mydata.models.generated.fuel_codes import FuelCodes
from mydata.models.generated.income_classification_type import (
    IncomeClassification,
)
from mydata.models.generated.ship_type import Ship

__NAMESPACE__ = "http://www.aade.gr/myDATA/invoice/v1.0"


@dataclass
class InvoiceRow:
    """
    Attributes:
        line_number: ΑΑ Γραμμής
        rec_type: Είδος Γραμμής
        taric_no: Κωδικός Taric
        item_code: Κωδικός Είδους
        item_descr: Περιγραφή Είδους
        fuel_code: Κωδικός Καυσίμου
        quantity: Ποσότητα
        measurement_unit: Είδος Ποσότητας
        invoice_detail_type: Επισήμανση
        net_value: Καθαρή Αξία
        vat_category: Κατηγορία ΦΠΑ
        vat_amount: Ποσό ΦΠΑ
        vat_exemption_category: Κατηγορία Αιτίας Εξαίρεσης ΦΠΑ
        dienergia: ΠΟΛ 1177/2018 Αρ. 27
        discount_option: Δικαίωμα Έκπτωσης
        withheld_amount: Ποσό Παρ. Φόρου
        withheld_percent_category: Κατηγορία Συντελεστή  Παρ. Φόρου
        stamp_duty_amount: Ποσό Χαρτοσήμου
        stamp_duty_percent_category: Κατηγορία Συντελεστή  Χαρτοσήμου
        fees_amount: Ποσό Τελών
        fees_percent_category: Κατηγορία Συντελεστή Τελών
        other_taxes_percent_category: Κατηγορία Συντελεστή Λοιπών Φόρων
        other_taxes_amount: Ποσό Φόρου Διαμονης
        deductions_amount: Ποσό Κρατήσεων
        line_comments: Σχόλια Γραμμής
        income_classification: Λίστα Χαρακτηρισμών Εσόδων
        expenses_classification: Λίστα Χαρακτηρισμού Εξόδων
        quantity15: Ποσότητα Θερμοκρασίας 15 βαθμών
        other_measurement_unit_quantity: Πλήθος Μονάδας Μέτρησης Τεμάχια
            Άλλα
        other_measurement_unit_title: Τίτλος Μονάδας Μέτρησης Τεμάχια
            Άλλα
        not_vat195: Ένδειξη μη συμμετοχής στο ΦΠΑ (έσοδα – εκροές)
    """

    class Meta:
        name = "InvoiceRowType"

    line_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "lineNumber",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
        },
    )
    rec_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "recType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 7,
        },
    )
    taric_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaricNo",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "length": 10,
        },
    )
    item_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemCode",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 50,
        },
    )
    item_descr: Optional[str] = field(
        default=None,
        metadata={
            "name": "itemDescr",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 300,
        },
    )
    fuel_code: Optional[FuelCodes] = field(
        default=None,
        metadata={
            "name": "fuelCode",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    quantity: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_exclusive": Decimal("0"),
        },
    )
    measurement_unit: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementUnit",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 7,
        },
    )
    invoice_detail_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "invoiceDetailType",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 2,
        },
    )
    net_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "netValue",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    vat_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "vatCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 10,
        },
    )
    vat_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "vatAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "required": True,
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    vat_exemption_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "vatExemptionCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 31,
        },
    )
    dienergia: Optional[Ship] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    discount_option: Optional[bool] = field(
        default=None,
        metadata={
            "name": "discountOption",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    withheld_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "withheldAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    withheld_percent_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "withheldPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 18,
        },
    )
    stamp_duty_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "stampDutyAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    stamp_duty_percent_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "stampDutyPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 4,
        },
    )
    fees_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "feesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    fees_percent_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "feesPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 22,
        },
    )
    other_taxes_percent_category: Optional[int] = field(
        default=None,
        metadata={
            "name": "otherTaxesPercentCategory",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": 1,
            "max_inclusive": 30,
        },
    )
    other_taxes_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "otherTaxesAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    deductions_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "deductionsAmount",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    line_comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "lineComments",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    income_classification: List[IncomeClassification] = field(
        default_factory=list,
        metadata={
            "name": "incomeClassification",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    expenses_classification: List[ExpensesClassification] = field(
        default_factory=list,
        metadata={
            "name": "expensesClassification",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    quantity15: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "min_exclusive": Decimal("0"),
        },
    )
    other_measurement_unit_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "otherMeasurementUnitQuantity",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
    other_measurement_unit_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "otherMeasurementUnitTitle",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
            "max_length": 150,
        },
    )
    not_vat195: Optional[bool] = field(
        default=None,
        metadata={
            "name": "notVAT195",
            "type": "Element",
            "namespace": "http://www.aade.gr/myDATA/invoice/v1.0",
        },
    )
