from decimal import Decimal
from typing import Dict, List, Optional, Tuple

from mydata.models.generated.expenses_classification_category_type import (
    ExpensesClassificationCategory,
)
from mydata.models.generated.expenses_classification_type import ExpensesClassification
from mydata.models.generated.expenses_classification_value_type import (
    ExpensesClassificationValue,
)
from mydata.models.generated.income_classification_category_type import (
    IncomeClassificationCategory,
)
from mydata.models.generated.income_classification_type import IncomeClassification
from mydata.models.generated.income_classification_value_type import (
    IncomeClassificationValue,
)
from mydata.models.generated.invoice_row_type import InvoiceRow
from mydata.models.vat_category import VatCategory
from mydata.models.vat_exemption import VatExemption


class ClassificationsGrouper:
    def __init__(self, rows=Optional[List[InvoiceRow]]):
        self.rows = rows
        self.income_classifications: Dict[str, Dict[str, Decimal]] = {}
        self.expenses_classifications: Dict[
            str, Dict[str, Dict[str, Dict[str, Dict[str, Decimal]]]]
        ] = {}

    def create_groups(
        self, options: Dict = None
    ) -> Tuple[List[IncomeClassification], List[ExpensesClassification]]:
        if not self.rows:
            return [], []

        for row in self.rows:
            self._group_income_classifications(row)
            self._group_expenses_classifications(row)

        return (
            self._flatten_income_classifications(options),
            self._flatten_expenses_classifications(options),
        )

    def _flatten_income_classifications(
        self, options: Dict = None
    ) -> List[IncomeClassification]:
        flattened_income_classifications = []

        for category_key, types in self.income_classifications.items():
            category = IncomeClassificationCategory(category_key)

            for type_key, amount in types.items():
                classification_type = (
                    IncomeClassificationValue(type_key) if type_key else None
                )

                icls = IncomeClassification(
                    classification_category=category,
                    classification_type=classification_type,
                    amount=round(amount, 2),
                )

                if options and options.get("enableClassificationIds"):
                    icls.id = len(flattened_income_classifications) + 1

                flattened_income_classifications.append(icls)

        return flattened_income_classifications

    def _flatten_expenses_classifications(
        self, options: Dict = None
    ) -> List[ExpensesClassification]:
        flattened_expenses_classifications = []

        for category_key, types in self.expenses_classifications.items():
            category = ExpensesClassificationCategory(category_key)

            for type_key, vat_categories in types.items():
                classification_type = (
                    ExpensesClassificationValue(type_key) if type_key else None
                )

                for vat_category_key, exemptions in vat_categories.items():
                    vat_category = (
                        VatCategory(vat_category_key) if vat_category_key else None
                    )

                    for exemption_key, amounts in exemptions.items():
                        vat_exemption = (
                            VatExemption(exemption_key) if exemption_key else None
                        )

                        ecls = ExpensesClassification(
                            classification_category=category,
                            classification_type=classification_type,
                            vat_category=vat_category,
                            vat_exemption_category=vat_exemption,
                            amount=round(amounts["amount"], 2),
                            vat_amount=round(amounts["vatAmount"], 2),
                        )

                        if options and options.get("enableClassificationIds"):
                            ecls.id = len(flattened_expenses_classifications) + 1

                        flattened_expenses_classifications.append(ecls)

        return flattened_expenses_classifications

    def _group_income_classifications(self, row: InvoiceRow) -> None:
        if not row.income_classification:
            return

        for icls in row.income_classification:
            category_key = icls.classification_category.value or ""
            type_key = icls.classification_type.value or ""

            previous_amount = self.income_classifications.get(category_key, {}).get(
                type_key, Decimal(0)
            )
            new_amount = previous_amount + abs(icls.amount or Decimal(0))

            self.income_classifications.setdefault(category_key, {})[type_key] = (
                new_amount
            )

    def _group_expenses_classifications(self, row: InvoiceRow) -> None:
        if not row.expenses_classification:
            return

        for ecls in row.expenses_classification:
            category_key = ecls.classification_category.value or ""
            type_key = ecls.classification_type.value or ""
            vat_category_key = ecls.vat_category.value or ""
            vat_exemption_key = ecls.vat_exemption_category.value or ""

            previous_amount = self._get_summarized_expenses_classification(
                ecls, "amount"
            )
            previous_vat_amount = self._get_summarized_expenses_classification(
                ecls, "vatAmount"
            )

            new_amount = previous_amount + abs(ecls.amount or Decimal(0))
            new_vat_amount = previous_vat_amount + abs(ecls.vat_amount or Decimal(0))

            self.expenses_classifications.setdefault(category_key, {}).setdefault(
                type_key, {}
            ).setdefault(vat_category_key, {})[vat_exemption_key] = {
                "amount": new_amount,
                "vatAmount": new_vat_amount,
            }

    def _get_summarized_expenses_classification(
        self, ecls: ExpensesClassification, key: str
    ) -> Decimal:
        category_key = ecls.classification_category.value or ""
        type_key = ecls.classification_type.value or ""
        vat_category_key = ecls.vat_category.value or ""
        vat_exemption_key = ecls.vat_exemption_category.value or ""

        return (
            self.expenses_classifications.get(category_key, {})
            .get(type_key, {})
            .get(vat_category_key, {})
            .get(vat_exemption_key, {})
            .get(key, Decimal(0))
        )
