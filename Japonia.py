from Firma import Firma_base
from random import randint
class Japonia(Firma_base):
    def __init__(self, nazwa, produkt, lokacja, workforce, material):
        super().__init__(nazwa, produkt, lokacja, workforce, material)
        self.produkcja = randint(1,13200)
        self.produkcja2 = randint(1,13200)
    def info3(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"material {self.material}")
        print(f"sigma#9/11 wyproduktowal {self.produkcja} cpu z dzieci :3")
        print(f"sigma#18/22 wyproduktowal {self.produkcja2} gpu z dzieci ;)")
        print("---------------------------")
