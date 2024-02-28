
class Pracownik:
    def __init__(self,imie, wiek , salery, firma):
        self.imie = imie
        self.wiek = wiek 
        self.salery = salery
        self.firma = firma
    # def budowa_komp(self):
    #     if self.wiedza_na_temat_komputerow == True:
    #         print("zbudowales komputer chuj ci w pizde")
    #     else:
    #          print("jestem gluptasem")
            # self.produkt += ilosc
    def pracownik_info(self):
            print(f"mam na ime {self.imie}")
            print(f"mam {self.wiek} lat")
            print(f"mam pensje {self.salery}")
            print(f"pracuje dla {self.firma}")
            print("---------------------------")