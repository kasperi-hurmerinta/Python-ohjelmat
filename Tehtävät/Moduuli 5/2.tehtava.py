## 1. Tehtävä

numero_lista = []

while True:
    kysymys = input("Luku: ")
    numero_lista.append(kysymys)

    if kysymys == "":
        numero_lista.sort(reverse=True)
        print(numero_lista)
        break