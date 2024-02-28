# from oliwer import Pracownik
class Firma_base:
    def __init__(self, nazwa, produkt, lokacja, workforce, material,ilosc_pracownikow):
        self.nazwa = nazwa
        self.produkt = produkt
        self.lokacja = lokacja
        self.workforce = workforce
        self.material = material
        self.ilosc_pracownikow = ilosc_pracownikow
    # def wyplata(self, zarobki):
    #     print(f"{self.nazwa} zarobilo/a {zarobki} \nz czego {self.salery * self.ilosc_pracownikow} wyplacilo/a pracownikom")
    #     zarobki -= self.salery * self.ilosc_pracownikow
    #     self.saldo += zarobki