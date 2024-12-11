from enum import Enum


class PaymentMethod(Enum):
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
            PaymentMethod.BANK_ACC_LOCAL: "Επαγ. Λογαριασμός Πληρωμών Ημεδαπής",
            PaymentMethod.BANK_ACC_FOR: "Επαγ. Λογαριασμός Πληρωμών Αλλοδαπής",
            PaymentMethod.CASH: "Μετρητά",
            PaymentMethod.CHEQUE: "Επιταγή",
            PaymentMethod.CREDIT: "Επί Πιστώσει",
            PaymentMethod.WEB_BANKING: "Web Banking",
            PaymentMethod.POS: "POS / e-POS",
            PaymentMethod.IRIS: "Άμεσες Πληρωμές IRIS",
        }
        return labels.get(self, "Unknown Payment method type")
