from enum import Enum


class VatCategory(int, Enum):
    # ΦΠΑ συντελεστής 24%
    VAT_1 = 1
    # ΦΠΑ συντελεστής 13%
    VAT_2 = 2
    # ΦΠΑ συντελεστής 6%
    VAT_3 = 3
    # ΦΠΑ συντελεστής 17%
    VAT_4 = 4
    # ΦΠΑ συντελεστής 9%
    VAT_5 = 5
    # ΦΠΑ συντελεστής 4%
    VAT_6 = 6
    # Άνευ Φ.Π.Α. 0%
    VAT_7 = 7
    # Εγγραφές χωρίς ΦΠΑ (πχ Μισθοδοσία, Αποσβέσεις)
    VAT_8 = 8
    # ΦΠΑ συντελεστής 3% (αρ.31 ν.5057/2023)
    VAT_9 = 9
    # ΦΠΑ συντελεστής 4% (αρ.31 ν.5057/2023)
    VAT_10 = 10