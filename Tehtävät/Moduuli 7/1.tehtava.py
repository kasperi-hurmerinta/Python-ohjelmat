## 1. Tehtävä

vuodenajat = ("Kevät", "Kesä", "Syksy", "Talvi")

x = int(input("Anna viikonpäivän järjestysnumero (1-12): "))

def monikko_tarkistus():
    if x <= 3 and x > 0:
        print(vuodenajat[0])
    elif x <= 6:
        print(vuodenajat[1])
    elif x <= 9:
        print(vuodenajat[2])
    elif x <= 12:
        print(vuodenajat[3])
    else:
        print("Noo mään")


monikko_tarkistus()

