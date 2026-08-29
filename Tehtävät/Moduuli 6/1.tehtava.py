## 1. Tehtävä

import random

def satunnainen_silmaluku():
    return random.randint(1,6)


while True:
    tulos = satunnainen_silmaluku()

    print(f"Silmäluku: {tulos}")

    if tulos == 6:
        break

