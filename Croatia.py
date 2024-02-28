from Firma import Firma_base
from random import randint
class Chorwacja(Firma_base):
    def __init__(self, nazwa, produkt, lokacja, workforce, material):
        super().__init__(nazwa, produkt, lokacja, workforce, material)
        self.produkcja = randint(1,2110)
    def info5(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"material {self.material}")
        print(f"sigma#2137 wyproduktowal {self.produkcja} water coolerow z dzieci B)")
        print("przez Macieja Brzezinskiego <3")
        print("---------------------------")
