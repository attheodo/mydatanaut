from enum import Enum


class IncomeClassificationCategory(str, Enum):
    CATEGORY_1_1 = "category1_1"
    CATEGORY_1_2 = "category1_2"
    CATEGORY_1_3 = "category1_3"
    CATEGORY_1_4 = "category1_4"
    CATEGORY_1_5 = "category1_5"
    CATEGORY_1_6 = "category1_6"
    CATEGORY_1_7 = "category1_7"
    CATEGORY_1_8 = "category1_8"
    CATEGORY_1_9 = "category1_9"
    CATEGORY_1_10 = "category1_10"
    CATEGORY_1_95 = "category1_95"
    CATEGORY_3 = "category3"

    def __str__(self) -> str:
        labels = {
            IncomeClassificationCategory.CATEGORY_1_1: "Έσοδα από Πώληση Εμπορευμάτων",
            IncomeClassificationCategory.CATEGORY_1_2: "Έσοδα από Πώληση Προϊόντων",
            IncomeClassificationCategory.CATEGORY_1_3: "Έσοδα από Παροχή Υπηρεσιών",
            IncomeClassificationCategory.CATEGORY_1_4: "Έσοδα από Πώληση Παγίων",
            IncomeClassificationCategory.CATEGORY_1_5: "Λοιπά Έσοδα / Κέρδη",
            IncomeClassificationCategory.CATEGORY_1_6: "Αυτοπαραδόσεις / Ιδιοχρησιμοποιήσεις",
            IncomeClassificationCategory.CATEGORY_1_7: "Έσοδα για λογαριασμό τρίτων",
            IncomeClassificationCategory.CATEGORY_1_8: "Έσοδα προηγούμενων χρήσεων",
            IncomeClassificationCategory.CATEGORY_1_9: "Έσοδα επομένων χρήσεων",
            IncomeClassificationCategory.CATEGORY_1_10: "Λοιπές Εγγραφές Τακτοποίησης Εσόδων",
            IncomeClassificationCategory.CATEGORY_1_95: "Λοιπά Πληροφοριακά Στοιχεία Εσόδων",
            IncomeClassificationCategory.CATEGORY_3: "Διακίνηση",
        }
        if self not in labels:
            raise ValueError(f"Undefined for: {self.name}")
        return labels[self]
