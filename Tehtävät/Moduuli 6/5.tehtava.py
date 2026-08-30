## 5. Tehtävä

normaali_lista = []

def lista_tarkistus(luku):
    karsittu_lista = []

    for tarkistus in luku:
        if tarkistus % 2 == 0:
            karsittu_lista.append(tarkistus)

    return karsittu_lista

while True:
    anna_kokonaisluku = input("Anna kokonaisluku: ")

    if anna_kokonaisluku == "":
        karsittu_lista = lista_tarkistus(normaali_lista)
        print(f"Yhteensä: {normaali_lista}, {karsittu_lista}")
        break

    normaali_lista.append(int(anna_kokonaisluku))
