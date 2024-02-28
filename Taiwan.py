from Firma import Firma_base
from random import randint
class Taiwan(Firma_base):
    def __init__(self, nazwa, produkt, lokacja, workforce, material,ilosc_pracownikow):
        super().__init__(nazwa, produkt, lokacja, workforce, material,ilosc_pracownikow)
        self.produkcja4 = randint(1,3470)
    def info4(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"material {self.material}")
        print(f"{self.nazwa} wyproduktowal {self.produkcja4} kart graficznych z dzieci :P")
        print(f"ilosc pracownikow {self.ilosc_pracownikow}")
        self.saldo = 10 * self.produkcja4
        print(f"zarobilo {self.saldo}$")
        print("---------------------------")
