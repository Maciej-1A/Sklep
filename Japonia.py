from Firma import Firma_base
from random import randint
class Japonia(Firma_base):
    def __init__(self, nazwa, produkt, lokacja, workforce, material,ilosc_pracownikow):
        super().__init__(nazwa, produkt, lokacja, workforce, material,ilosc_pracownikow)
        self.produkcja3 = randint(1,13200)
        self.produkcja3a = randint(1,13200)
    def info3(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"material {self.material}")
        print(f"{self.nazwa} wyproduktowal {self.produkcja3} cpu z dzieci :3")
        print(f"{self.nazwa} wyproduktowal {self.produkcja3a} gpu z dzieci ;)")
        print(f"ilosc pracownikow {self.ilosc_pracownikow}")
        self.saldo = 7 * self.produkcja3
        self.saldo1 = 7 * self.produkcja3a
        print(f"zarobilo {self.saldo}$ z cpu\nzarobilo {self.saldo1}$ z gpu")
        print("---------------------------")
