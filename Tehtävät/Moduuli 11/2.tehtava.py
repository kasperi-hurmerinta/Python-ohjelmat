## 2. Tehtävä

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

class Sahkoauto(Auto):
    def __init__(self, licenseplate, max_speed, current_speed=0, traveled_distance=0, akkukapasiteetti=52.5):
        self.akkukapasiteetti = akkukapasiteetti
        Auto.__init__(self, licenseplate, max_speed, current_speed, traveled_distance)

class Polttomoottoriauto(Auto):
    def __init__(self, licenseplate, max_speed, current_speed=0, traveled_distance=0, bensatankki_litroina = float()):
        self.bensatankki_litroina = bensatankki_litroina
        Auto.__init__(self, licenseplate, max_speed, current_speed, traveled_distance)

auto_luokka_sahko = Auto("ABC-15", 180, 30, 0)
auto_luokka_bensa = Auto("ACD-123", 165, 30, 0)

sahkoauto = Sahkoauto(auto_luokka_sahko.licenseplate, auto_luokka_sahko.max_speed, auto_luokka_sahko.current_speed, auto_luokka_sahko.traveled_distance, 625)
sahkoauto.kulje(3)
bensa_auto = Polttomoottoriauto(auto_luokka_bensa.licenseplate, auto_luokka_bensa.max_speed, auto_luokka_bensa.current_speed, auto_luokka_bensa.traveled_distance, 32.3)
bensa_auto.kulje(3)

print(f"{sahkoauto.licenseplate} : {sahkoauto.max_speed} km/h : {sahkoauto.current_speed} km/h : {sahkoauto.traveled_distance} km : {sahkoauto.akkukapasiteetti} kw/h")
print(f"{bensa_auto.licenseplate} : {bensa_auto.max_speed} km/h : {bensa_auto.current_speed} km/h : {bensa_auto.traveled_distance} km : {bensa_auto.bensatankki_litroina} kw/h")