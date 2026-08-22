## 4. Tehtävä
import random

satunnainen_luku = (random.randint(1, 10))

while True:
    kysymys = int(input("Kokonaisluku: "))

    if kysymys == satunnainen_luku:
        print("Oikea luku!")
        break
    elif kysymys > satunnainen_luku:
        print("Liian suuri arvaus")
    elif kysymys < satunnainen_luku:
        print("Liian pieni arvaus")




