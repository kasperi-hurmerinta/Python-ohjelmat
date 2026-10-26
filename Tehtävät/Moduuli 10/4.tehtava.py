## 4. Tehtävä

import random
from time import sleep


class Auto:
    def __init__(self, licenseplate, max_speed, current_speed=0, traveled_distance=0):
        self.licenseplate = licenseplate
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.traveled_distance = traveled_distance

    def kiihdyta(self, nopeuden_muutos):

        self.current_speed += nopeuden_muutos

        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def kulje(self, tuntimaara):
        matka = tuntimaara * self.current_speed

        self.traveled_distance += matka

class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_km):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_km = pituus_km
        self.osallistujat = []
        self.kuinka_monta_kertaa = 0

        for i in range(1, 11):
            huippu_nopeus = random.randint(100, 200)
            uusi_auto = Auto(f"ABC-{i}", max_speed=huippu_nopeus)
            self.osallistujat.append(uusi_auto)

        print("Luodut ajoneuvot: \n")
        for i in self.osallistujat:
            print(f" Rekisterikilpi: {i.licenseplate} : Huippunopeus: {i.max_speed} km/h ")

    def tunti_kuluu(self):

        sleep(1)
        print("Ajoneuvot ovat ajaneet tunnin. Nopeudet vaihtuvat.")

        for i in self.osallistujat:
            i.kiihdyta(random.randint(-10, 15))
            i.kulje(1)

        self.kuinka_monta_kertaa += 1

        if self.kuinka_monta_kertaa == 10:
            Suuri_romuralli.tulosta_tilanne()
            self.kuinka_monta_kertaa = 0

    def tulosta_tilanne(self):

        sleep(1)
        for i in self.osallistujat:
            print(f" Rekisterikilpi: {i.licenseplate} : Nopeus : {i.current_speed} km/h : Kuljettu matka: {i.traveled_distance}")

    def kilpailu_ohi(self):

        sleep(1)
        for i in self.osallistujat:
            if i.traveled_distance >= self.pituus_km:
                print(f"{i.licenseplate} : {i.max_speed} : {i.current_speed} : {i.traveled_distance}")
                return False

        return True

Suuri_romuralli = Kilpailu("Suuri Romuralli", 1000)
kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    Suuri_romuralli.tunti_kuluu()

    if Suuri_romuralli.kilpailu_ohi() == False:
        Suuri_romuralli.tulosta_tilanne()
        kilpailu_kaynnissa = False