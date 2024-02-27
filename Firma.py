class Firma:
    def __init__(self, nazwa, produkt, lokacja, workforce, material):
        self.nazwa = nazwa
        self.produkt = produkt
        self.lokacja = lokacja
        self.workforce = workforce
        self.material = material
    def info(self):
        print(f"nazwa firmy {self.nazwa}")
        print(f"produkt {self.produkt}")
        print(f"lokacja {self.lokacja}")
        print(f"sila robocza {self.workforce}")
        print(f"czesc dizeci {self.material}")

