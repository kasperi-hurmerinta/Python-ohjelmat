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



def paa_ohjelma():
    auto = Auto("ABC-123", 142)

    auto.kiihdyta(30)
    auto.kiihdyta(70)
    auto.kiihdyta(50)

    print(f" Ennen hidastusta: {auto.current_speed}")

    auto.kiihdyta(-200)

    print(f" Hidastuksen jälkeen: {auto.current_speed}")



paa_ohjelma()