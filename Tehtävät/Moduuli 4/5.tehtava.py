## 5. Tehtävä

oikea_kayttajatunnus = "python"
oikea_salasana = "rules"

yritykset = 0

while True:
    kayttajatunnus_kysymys = input("Käyttäjätunnus: ")
    salasana_kysymys = input("Salasana: ")
    yritykset = yritykset + 1

    if kayttajatunnus_kysymys == oikea_kayttajatunnus and salasana_kysymys == oikea_salasana:
        print("Tervetuloa!")
        break
    elif yritykset == 2:
        break
    else:
        print("Pääsy evätty.")





