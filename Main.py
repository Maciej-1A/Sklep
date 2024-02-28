from Chiny import Chiny
from DRC import DRC
from Japonia import Japonia
from Taiwan import Taiwan
from Croatia import Chorwacja
from oliwer import Pracownik

China = Chiny("Chiny.inc", "case", "Chiny", "dzieci (z Chin)", "kosc udowa", 1)
China.info1()
DRoC = DRC("Bare hands mine", "power source", "Democratic Republic of the Congo", "dzieci (z Demokratycznej Republiki Kongo? czy Congo nie wiem ja tylko koduje)", "Kobalt", 2)
DRoC.info2()
japan = Japonia("Nada High School", "cpu i gpu","Japonia","chirurgi","mozg",2)
japan.info3()
Taiwann = Taiwan("Linkou Chang Gung Memorial Hospital", "karta graficzna", "Taiwan", "chirurg", "oczy", 1)
Taiwann.info4()
Chorwacjaa = Chorwacja("the University Hospital Zagreb", "watter cooling", "Chorwacja", "chirurgi", "serce", 2)
Chorwacjaa.info5()
Eggman = Pracownik("Egg Head", "6.9", "370$ na miesac", "Chiny.inc")
Eggman.pracownik_info()
Jamal = Pracownik("Jamal Jankins", "4,2", "0.61$ na dzien :D", "Bare hands mine")
Jamal.pracownik_info()
Jankins = Pracownik("Jankins Jamal", "2,4", "0.60$ na dzien :(", "Bare hands mine")
Jankins.pracownik_info()
Bio = Pracownik("アドルフ・ドリプラー", "911", "248$ na godzine", "Nada High School jako nauczyciel biologi")
Bio.pracownik_info()
BioA = Pracownik("アドルフ・ヒトラー・ジュニア", "42", "0$ na rok (jestem internem)", "Nada High School jako asytent nauczycila biologi nauczyciela biologi")
BioA.pracownik_info()
Mama_Mateusza = Pracownik("ฉันชอบทเวิร์ก", "50", "690$ na godzine", "Linkou Chang Gung Memorial Hospital")
Mama_Mateusza.pracownik_info()
Buczy = Pracownik("Buczy Slaw", "18", "140$ na godzine", "the University Hospital Zagreb")
Buczy.pracownik_info()
Mateusz = Pracownik("Mateusz Wajche Przeloz", "14", "0 nie mam 16 lat", "the University Hospital Zagreb")

