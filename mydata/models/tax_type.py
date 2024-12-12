from enum import Enum


class TaxType(int, Enum):
    # Παρακρατούμενος Φόρος
    TYPE_1 = 1
    # Τέλη
    TYPE_2 = 2
    # Λοιποί Φόροι
    TYPE_3 = 3
    # Χαρτόσημο
    TYPE_4 = 4
    # Κρατήσεις
    TYPE_5 = 5
