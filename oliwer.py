
class Pracownik:
    def __init__(self,imie, wiek , salery, firma):
        self.imie = imie
        self.wiek = wiek 
        self.salery = salery
        self.firma = firma
    def pracownik_info(self):
            print(f"mam na ime {self.imie}")
            print(f"mam {self.wiek} lat")
            print(f"mam pensje {self.salery}")
            print(f"pracuje dla {self.firma}")
            print("---------------------------")