from Firma import Firma_base
from random import randint
class Chiny(Firma_base):
    def __init__(self, nazwa, produkt, lokacja, workforce, material):
        super().__init__(nazwa, produkt, lokacja, workforce, material)
        self.produkcja = randint(1,1000)
    def info1(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"material {self.material}")
        print(f"sigma#420 wyproduktowal {self.produkcja} casow do komuterow z dzieci :D")
        print("---------------------------")
