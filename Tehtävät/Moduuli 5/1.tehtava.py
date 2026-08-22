## 1. Tehtävä
import random

arpaluku = int(input("Arpakuutioiden lukumäärä: "))

silmalukujen_summa = 0
for i in range(arpaluku):
    arpakuutio_tulokset = random.randint(1, 6)
    silmalukujen_summa = silmalukujen_summa + arpakuutio_tulokset

print(f"Silmälukujen summa: {silmalukujen_summa}")