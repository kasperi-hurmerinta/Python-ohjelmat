## 4. Tehtävä

lista = []

def kokonaisluku(luku):
    summa = sum(luku)

    return summa

while True:
    anna_kokonaisluku = input("Anna kokonaisluku: ")

    if anna_kokonaisluku == "":
        print(f"Yhteensä: {kokonaisluku(lista)}")
        break

    lista.append(int(anna_kokonaisluku))












