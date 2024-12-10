from enum import Enum


class PaymentMethodType(Enum):
    BANK_ACC_LOCAL = 1
    BANK_ACC_FOR = 2
    CASH = 3
    CHEQUE = 4
    CREDIT = 5
    WEB_BANKING = 6
    POS = 7
    IRIS = 8

    def __str__(self) -> str:
        labels = {
            PaymentMethodType.BANK_ACC_LOCAL: "Επαγ. Λογαριασμός Πληρωμών Ημεδαπής",
            PaymentMethodType.BANK_ACC_FOR: "Επαγ. Λογαριασμός Πληρωμών Αλλοδαπής",
            PaymentMethodType.CASH: "Μετρητά",
            PaymentMethodType.CHEQUE: "Επιταγή",
            PaymentMethodType.CREDIT: "Επί Πιστώσει",
            PaymentMethodType.WEB_BANKING: "Web Banking",
            PaymentMethodType.POS: "POS / e-POS",
            PaymentMethodType.IRIS: "Άμεσες Πληρωμές IRIS",
        }
        return labels.get(self, "Unknown Payment method type")
