## 3. Tehtävä
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

def paa_ohjelma():
    lista = []
    for i in range(1, 11):
        huippu_nopeus = random.randint(100, 200)
        auto = Auto(f"ABC-{i}", max_speed=huippu_nopeus)
        lista.append(auto)

    print("Luodut ajoneuvot: \n")
    for auto in lista:
        print(f" Rekisterikilpi: {auto.licenseplate} : Huippunopeus: {auto.max_speed} km/h ")

    kilpailu_kaynnissa = True

    while kilpailu_kaynnissa:
        # peli looppi
        print("Ajoneuvot lähtee liikenteeseen...")
        sleep(1)
        print("Ajoneuvot ovat ajaneet tunnin. Nopeudet vaihtuvat.")

        for auto in lista:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

            print(f" Rekisterikilpi: {auto.licenseplate} : Nopeus : {auto.current_speed} km/h : Kuljettu matka: {auto.traveled_distance}")

            if auto.traveled_distance >= 10000:
                print(f"{auto.licenseplate} : {auto.max_speed} : {auto.current_speed} : {auto.traveled_distance}")
                kilpailu_kaynnissa = False

        print("Autot ovat ajaneet yhden tunnin.")

    print("Kilpailu päättyi! Tässä kilpailijat: ")
    for auto in lista:
        print(f"{auto.licenseplate} : {auto.max_speed} : {auto.current_speed} : {auto.traveled_distance}")


paa_ohjelma()