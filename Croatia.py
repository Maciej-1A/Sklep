from Firma import Firma_base
from random import randint
class Chorwacja(Firma_base):
    def __init__(self, nazwa, produkt, lokacja, workforce, material,ilosc_pracownikow):
        super().__init__(nazwa, produkt, lokacja, workforce, material,ilosc_pracownikow)
        self.produkcja5 = randint(1,2110)
    def info5(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"material {self.material}")
        print(f"{self.nazwa} wyproduktowal {self.produkcja5} water coolerow z dzieci B)")
        print(f"ilosc pracownikow {self.ilosc_pracownikow}")
        self.saldo = 1.5 * self.produkcja5
        print(f"zarobilo {self.saldo}$")
        print("---------------------------")
