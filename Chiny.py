from Firma import Firma_base
from random import randint
class Chiny(Firma_base):
    def __init__(self, nazwa, produkt, lokacja, workforce, material,ilosc_pracownikow):
        super().__init__(nazwa, produkt, lokacja, workforce, material,ilosc_pracownikow)
        self.produkcja1 = randint(1,1000)
    def info1(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"material {self.material}")
        print(f"{self.nazwa} wyproduktowal {self.produkcja1} casow do komuterow z dzieci :D")
        print(f"ilosc pracownikow {self.ilosc_pracownikow}")
        self.saldo = 4 * self.produkcja1
        print(f"zarobilo {self.saldo}$")
        print("---------------------------")
