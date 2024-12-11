from enum import Enum


class VatCategory(Enum):
    VAT_1 = 1  # ΦΠΑ συντελεστής 24%
    VAT_2 = 2  # ΦΠΑ συντελεστής 13%
    VAT_3 = 3  # ΦΠΑ συντελεστής 6%
    VAT_4 = 4  # ΦΠΑ συντελεστής 17%
    VAT_5 = 5  # ΦΠΑ συντελεστής 9%
    VAT_6 = 6  # ΦΠΑ συντελεστής 4%
    VAT_7 = 7  # ΦΠΑ συντελεστής 0%
    VAT_8 = 8  # Εγγραφές χωρίς ΦΠΑ (πχ Μισθοδοσία, Αποσβέσεις)
    VAT_9 = 9  # ΦΠΑ συντελεστής 3% (αρ.31 ν.5057/2023)
    VAT_10 = 10  # ΦΠΑ συντελεστής 4% (αρ.31 ν.5057/2023)

    @property
    def date(self) -> float:
        rates = {
            VatCategory.VAT_1: 24.0,
            VatCategory.VAT_2: 13.0,
            VatCategory.VAT_3: 6.0,
            VatCategory.VAT_4: 17.0,
            VatCategory.VAT_5: 9.0,
            VatCategory.VAT_6: 4.0,
            VatCategory.VAT_7: 0.0,
            VatCategory.VAT_8: 0.0,
            VatCategory.VAT_9: 3.0,
            VatCategory.VAT_10: 4.0,
        }
        if self not in rates:
            raise ValueError(f"Undefined VAT rate for: {self.name}")
        return rates[self]

    @property
    def is_zero(self) -> bool:
        return self == VatCategory.VAT_7 or self == VatCategory.VAT_8

    @property
    def is_exemption(self) -> bool:
        return self == VatCategory.VAT_7

    def __str__(self) -> str:
        labels = {
            VatCategory.VAT_1: "ΦΠΑ συντελεστής 24%",
            VatCategory.VAT_2: "ΦΠΑ συντελεστής 13%",
            VatCategory.VAT_3: "ΦΠΑ συντελεστής 6%",
            VatCategory.VAT_4: "ΦΠΑ συντελεστής 17%",
            VatCategory.VAT_5: "ΦΠΑ συντελεστής 9%",
            VatCategory.VAT_6: "ΦΠΑ συντελεστής 4%",
            VatCategory.VAT_7: "Άνευ Φ.Π.Α. 0%",
            VatCategory.VAT_8: "Εγγραφές χωρίς ΦΠΑ",
            VatCategory.VAT_9: "ΦΠΑ συντελεστής 3% (αρ.31 ν.5057/2023)",
            VatCategory.VAT_10: "ΦΠΑ συντελεστής 4% (αρ.31 ν.5057/2023)",
        }
        if self not in labels:
            raise ValueError(f"Undefined for: {self.name}")
        return labels[self]
