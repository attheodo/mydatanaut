from enum import Enum


class WithheldPercentCategory(Enum):
    TAX_1 = 1
    TAX_2 = 2
    TAX_3 = 3
    TAX_4 = 4
    TAX_5 = 5
    TAX_6 = 6
    TAX_7 = 7
    TAX_8 = 8
    TAX_9 = 9
    TAX_10 = 10
    TAX_11 = 11
    TAX_12 = 12
    TAX_13 = 13
    TAX_14 = 14
    TAX_15 = 15
    TAX_16 = 16
    TAX_17 = 17
    TAX_18 = 18

    def affects_total_gross_value(self) -> bool:
        return self not in [
            WithheldPercentCategory.TAX_8,
            WithheldPercentCategory.TAX_9,
            WithheldPercentCategory.TAX_10,
        ]

    def __str__(self) -> str:
        labels = {
            WithheldPercentCategory.TAX_1: "Περιπτ. β’ - Τόκοι - 15%",
            WithheldPercentCategory.TAX_2: "Περιπτ. γ’ - Δικαιώματα - 20%",
            WithheldPercentCategory.TAX_3: "Περιπτ. δ’ - Αμοιβές Συμβουλών Διοίκησης - 20%",
            WithheldPercentCategory.TAX_4: "Περιπτ. δ’ - Τεχνικά Έργα - 3%",
            WithheldPercentCategory.TAX_5: "Υγρά καύσιμα και προϊόντα καπνοβιομηχανίας 1%",
            WithheldPercentCategory.TAX_6: "Λοιπά Αγαθά 4%",
            WithheldPercentCategory.TAX_7: "Παροχή Υπηρεσιών 8%",
            WithheldPercentCategory.TAX_8: "Προκαταβλητέος Φόρος Αρχιτεκτόνων και Μηχανικών επί Συμβατικών Αμοιβών, για Εκπόνηση Μελετών και Σχεδίων 4%",
            WithheldPercentCategory.TAX_9: "Προκαταβλητέος Φόρος Αρχιτεκτόνων και Μηχανικών επί Συμβατικών Αμοιβών, που αφορούν οποιασδήποτε άλλης φύσης έργα 10%",
            WithheldPercentCategory.TAX_10: "Προκαταβλητέος Φόρος στις Αμοιβές Δικηγόρων 15%",
            WithheldPercentCategory.TAX_11: "Παρακράτηση Φόρου Μισθωτών Υπηρεσιών παρ. 1 αρ. 15 ν. 4172/2013",
            WithheldPercentCategory.TAX_12: "Παρακράτηση Φόρου Μισθωτών Υπηρεσιών παρ. 2 αρ. 15 ν. 4172/2013 - Αξιωματικών Εμπορικού Ναυτικού 15%",
            WithheldPercentCategory.TAX_13: "Παρακράτηση Φόρου Μισθωτών Υπηρεσιών παρ. 2 αρ. 15 ν. 4172/2013 - Κατώτερο Πλήρωμα Εμπορικού Ναυτικού 10%",
            WithheldPercentCategory.TAX_14: "Παρακράτηση Ειδικής Εισφοράς Αλληλεγγύης",
            WithheldPercentCategory.TAX_15: "Παρακράτηση Φόρου Αποζημίωσης λόγω Διακοπής Σχέσης Εργασίας παρ. 3 αρ. 15 ν. 4172/2013",
            WithheldPercentCategory.TAX_16: "Παρακρατήσεις συναλλαγών αλλοδαπής βάσει συμβάσεων αποφυγής διπλής φορολογίας (Σ.Α.Δ.Φ.)",
            WithheldPercentCategory.TAX_17: "Λοιπές Παρακρατήσεις Φόρου",
            WithheldPercentCategory.TAX_18: "Παρακράτηση Φόρου Μερίσματα 5% [περ.α παρ. 1 αρ. 64 ν. 4172/2013]",
        }
        if self not in labels:
            raise ValueError(f"Undefined for: {self.name}")
        return labels[self]
