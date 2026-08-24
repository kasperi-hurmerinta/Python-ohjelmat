## 4. Tehtävä

kaupungin_nimet = []
numero = 1

for i in range(1, 5+1):
    anna_nimet = input(f"Anna {numero}. kaupungin nimet: ")
    kaupungin_nimet.append(anna_nimet)
    numero += 1

for tulostus in kaupungin_nimet:
    print(tulostus)


