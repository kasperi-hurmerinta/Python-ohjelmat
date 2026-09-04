## 2. Tehtävä

nimet = set()

while True:
    x = input("Anna nimi: ").capitalize()

    if x == "":
        for tulostus in nimet:
            print(tulostus)
        break
    elif x in nimet:
        print("Aiemmin syötetty nimi!")
    else:
        nimet.add(x)
        print("Uusi nimi!")

