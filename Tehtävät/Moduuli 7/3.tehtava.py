## 3. Tehtävä

lentokentat = {"EFHK" : "Helsinki-Vantaa",}

while True:
    toiminto_kysymys = int(input("Uuden lentoaseman syöttö (1), lentoaseman haku (2), lopetus (3): "))

    if toiminto_kysymys == 1:
        lentoaseman_syotto_koodi = input("Aseta lentoaseman koodi: ")
        lentoaseman_syotto = input("Aseta lentoaseman nimi: ")

        lentokentat[lentoaseman_syotto_koodi] = lentoaseman_syotto

    if toiminto_kysymys == 2:
        lentoaseman_haku_koodi = input("Aseta lentoaseman koodi: ")

        haettava_asema = lentokentat[lentoaseman_haku_koodi]

        print(haettava_asema)

    if toiminto_kysymys == 3:
        break

