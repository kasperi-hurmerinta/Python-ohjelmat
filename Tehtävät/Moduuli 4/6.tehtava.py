## 6. Tehtävä

import random

pisteiden_maara = int(input("Anna pisteiden maäärä: "))

kierrosten_maara = 0

for i in range(pisteiden_maara):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    lasku = x**2 + y**2

    if lasku < 1:
        kierrosten_maara += 1

piin_likiarvo = 4 * kierrosten_maara / pisteiden_maara
print(piin_likiarvo)








