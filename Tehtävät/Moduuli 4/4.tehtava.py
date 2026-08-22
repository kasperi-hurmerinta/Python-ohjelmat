## 4. Tehtävä
import random

satunnainen_luku = (random.randint(0, 10))
oikea_luku = satunnainen_luku

while True:
    kysymys = int(input("Kokonaisluku: "))

    if kysymys == oikea_luku:
        print("Oikea luku!")
        break
    elif kysymys > satunnainen_luku:
        print("Liian suuri arvaus")
    elif kysymys < satunnainen_luku:
        print("Liian pieni arvaus")




