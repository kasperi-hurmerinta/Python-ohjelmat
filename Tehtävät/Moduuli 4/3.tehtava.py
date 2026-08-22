## 3. Tehtävä
numerot = []

while True:
    kysymys_luku = input("Luku: ")

    if kysymys_luku == "":
        print(f"Suurin numero: {max(numerot)} sekä pienin numero: {min(numerot)}")
        break

    kysymys_luku = int(kysymys_luku)
    numerot.append(kysymys_luku)




