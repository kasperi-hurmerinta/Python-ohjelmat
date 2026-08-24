## 2. Tehtävä

numero_lista = []

while True:
    kysymys = input("Luku: ")

    if kysymys != "":
        numero_lista.append(kysymys)

    if kysymys == "":
        numero_lista.sort(reverse=True)
        print(f"{numero_lista}")
        break