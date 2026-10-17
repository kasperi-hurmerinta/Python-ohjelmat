## 1. Tehtävä

class Auto:
    def __init__(self, licenseplate, max_speed, current_speed=0, traveled_distance=0):
        self.licenseplate = licenseplate
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.traveled_distance = traveled_distance

auto = Auto("ABC-123", 142)

print(f"{auto.licenseplate}, {auto.max_speed}, {auto.current_speed}, {auto.traveled_distance}")