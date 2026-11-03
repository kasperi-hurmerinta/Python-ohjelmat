## 1. Tehtävä

import requests

kysymys = input("Anna paikkakunnan nimi: ")

vastaus_koordinaatit = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={kysymys}&limit=5&appid=bc830b1507064402e185e432f3fd6e09").json()

for i in vastaus_koordinaatit:
    if i["name"] == kysymys:
        latitude = i["lat"]
        longitude = i["lon"]
        break

vastaus = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid=bc830b1507064402e185e432f3fd6e09").json()

for x in vastaus:
    a = vastaus["weather"]
    b = a[0]["description"]
    c = vastaus["main"]
    d = c["temp"]


print(f"Säätila: {b} | Lämpötila: {d} °C")