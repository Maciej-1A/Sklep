from Firma import Firma_base
class Taiwan(Firma_base):
    def __init__(self, nazwa, produkt, lokacja, workforce, material):
        super().__init__(nazwa, produkt, lokacja, workforce, material)
    def info4(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"material {self.material}")
