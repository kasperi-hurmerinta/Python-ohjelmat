## 1. Tehtävä

class Julkaisu:

    def __init__(self, julkaisu_tyyppi, julkaisu_nimi):
        self.julkaisu_tyyppi = julkaisu_tyyppi
        self.julkaisu_nimi = julkaisu_nimi

    def tulosta_tiedot(self):
        print(f"{self.julkaisu_tyyppi} : {self.julkaisu_nimi}")

class Lehti(Julkaisu):

    def __init__(self, julkaisu_tyyppi, julkaisu_nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(julkaisu_tyyppi, julkaisu_nimi)

    def tulosta_tiedot(self):
        print(f"{self.julkaisu_tyyppi} : {self.julkaisu_nimi} : {self.paatoimittaja}")

class Kirja(Julkaisu):

    def __init__(self, julkaisu_tyyppi, julkaisu_nimi, kirjoittaja, sivumaara):
        self.sivumaara = sivumaara
        self.kirjoittaja = kirjoittaja
        super().__init__(julkaisu_tyyppi, julkaisu_nimi)

    def tulosta_tiedot(self):
        print(f"{self.julkaisu_tyyppi} : {self.julkaisu_nimi} : {self.kirjoittaja} : {self.sivumaara}")

aku_ankka = Lehti("Lehti", "Aku Ankka", "Aki Hyyppä")
hytti_nro_6 = Kirja("Kirja", "Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti_nro_6.tulosta_tiedot()