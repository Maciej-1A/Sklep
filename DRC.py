from Firma import Firma_base
from random import randint
class DRC(Firma_base):
    def __init__(self, nazwa, produkt, lokacja, workforce, material,ilosc_pracownikow):
        super().__init__(nazwa, produkt, lokacja, workforce, material,ilosc_pracownikow)
        self.produkcja2 = randint(1,12000)
    def info2(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"material {self.material}")
        print(f"{self.nazwa} wyproduktowal {self.produkcja2} power suply z dzieci uwu")
        print(f"ilosc pracownikow {self.ilosc_pracownikow}")
        self.saldo = 0.5 * self.produkcja2
        print(f"zarobilo {self.saldo}$")
        print("---------------------------")

