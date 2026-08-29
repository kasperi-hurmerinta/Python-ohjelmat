## 2. Tehtävä

import random

tahkojen_maara = int(input("Syötä tahkojen määrä: "))

def satunnainen_silmaluku(tahkojen_maara):
    return random.randint(1,tahkojen_maara)


while True:
    tulos = satunnainen_silmaluku(tahkojen_maara)

    print(f"Silmäluku: {tulos}")

    if tulos == tahkojen_maara:
        break

