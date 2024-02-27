from Firma import Firma_base
class Taiwan(Firma_base):
    def __init__(self, nazwa, produkt, lokacja, workforce, material):
        super().__init__(nazwa, produkt, lokacja, workforce, material)
        self.nazwa = "Linkou Chang Gung Memorial Hospita"
        self.produkt = "karta graficzna"
        self.lokacja = "Taiwan"
        self.workforce = "chirurgi"
        self.material = "oczy"
    def info(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"material {self.material}")
