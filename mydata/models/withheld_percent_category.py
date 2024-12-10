from enum import Enum


class WithheldPercentCategory(int, Enum):
    # Περιπτ. β’- Τόκοι - 15%
    TAX_1 = 1
    #  Περιπτ. γ’ - Δικαιώματα - 20%
    TAX_2 = 2
    #  Περιπτ. δ’ - Αμοιβές Συμβουλών Διοίκησης - 20%
    TAX_3 = 3
    #  Περιπτ. δ’ - Τεχνικά Έργα - 3%
    TAX_4 = 4
    #  Υγρά καύσιμα και προϊόντα καπνοβιομηχανίας 1%
    TAX_5 = 5
    #  Λοιπά Αγαθά 4%
    TAX_6 = 6
    #  Παροχή Υπηρεσιών 8%
    TAX_7 = 7
    #  Προκαταβλητέος Φόρος Αρχιτεκτόνων και Μηχανικών επί Συμβατικών Αμοιβών, για Εκπόνηση Μελετών και Σχεδίων 4%
    TAX_8 = 8
    #  Προκαταβλητέος Φόρος Αρχιτεκτόνων και Μηχανικών επί Συμβατικών Αμοιβών, που αφορούν οποιασδήποτε άλλης φύσης έργα 10%
    TAX_9 = 9
    #  Προκαταβλητέος Φόρος στις Αμοιβές Δικηγόρων 15%
    TAX_10 = 10
    #  Παρακράτηση Φόρου Μισθωτών Υπηρεσιών παρ. 1 αρ. 15 ν. 4172/2013 ποσό
    TAX_11 = 11
    #  Παρακράτηση Φόρου Μισθωτών Υπηρεσιών παρ. 2 αρ. 15 ν. 4172/2013 - Αξιωματικών Εμπορικού Ναυτικού 15%
    TAX_12 = 12
    #  Παρακράτηση Φόρου Μισθωτών Υπηρεσιών παρ. 2 αρ. 15 ν. 4172/2013 - Κατώτερο Πλήρωμα Εμπορικού Ναυτικού 10%
    TAX_13 = 13
    #  Παρακράτηση Ειδικής Εισφοράς Αλληλεγγύης ποσό
    TAX_14 = 14
    #  Παρακράτηση Φόρου Αποζημίωσης λόγω Διακοπής Σχέσης Εργασίας παρ. 3 αρ. 15 ν. 4172/2013 ποσό
    TAX_15 = 15
    #  Παρακρατήσεις συναλλαγών αλλοδαπής βάσει συμβάσεων αποφυγής διπλής φορολογίας (Σ.Α.Δ.Φ.) ποσό
    TAX_16 = 16
    #  Λοιπές Παρακρατήσεις Φόρου ποσό
    TAX_17 = 17
    #  Παρακράτηση Φόρου Μερίσματα περ.α παρ. 1 αρ. 64 ν. 4172/2013 5%
    TAX_18 = 18

    @property
    def affects_total_gross_value(self) -> bool:
        return self not in [
            WithheldPercentCategory.TAX_8,
            WithheldPercentCategory.TAX_9,
            WithheldPercentCategory.TAX_10,
        ]
