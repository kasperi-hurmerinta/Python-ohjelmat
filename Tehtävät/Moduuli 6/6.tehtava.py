## 5. Tehtävä

def pitsa_lasku(pitsa_hinta, pitsa_halkaisija):
    sentit_metreiksi = pitsa_halkaisija / 100
    sade = sentit_metreiksi / 2
    pinta_ala = 3.14 * sade**2

    hinta = pitsa_hinta / pinta_ala

    return hinta

def paa_ohjelma():
    hinta_kysymys = int(input("Anna pitsan hinta: "))
    halkaisija_kysymys = int(input("Anna pitsan halkaisija: "))

    x1 = float(pitsa_lasku(hinta_kysymys, halkaisija_kysymys))

    hinta_kysymys = int(input("Anna pitsan hinta: "))
    halkaisija_kysymys = int(input("Anna pitsan halkaisija: "))

    x2 = float(pitsa_lasku(hinta_kysymys, halkaisija_kysymys))

    print(f" 1. Pitsa: {x1:.3} €/m² ja  2. Pitsa: {x2:.3} €/m²")

    if x1 > x2:
        print(f"{x2:.3} €/m² on parempi vastine rahalle!")
    if x2 > x1:
        print(f"{x1:.3} €/m² on parempi vastine rahalle!")

paa_ohjelma()





