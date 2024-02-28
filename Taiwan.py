from Firma import Firma_base
from random import randint
class Taiwan(Firma_base):
    def __init__(self, nazwa, produkt, lokacja, workforce, material):
        super().__init__(nazwa, produkt, lokacja, workforce, material)
        self.produkcja = randint(1,3470)
    def info4(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"material {self.material}")
        print(f"sigma#69 wyproduktowal {self.produkcja} kart graficznych z dzieci :P")
        print("---------------------------")
