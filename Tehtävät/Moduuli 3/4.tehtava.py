## 4. Tehtävä

x = int(input("Vuosiluku: "))

if x % 4 == 0:
    print("Vuosi on karkausvuosi!")
elif x % 400 == 0:
    print("Vuosi on karkausvuosi!")
else:
    print("Vuosi ei ole karkausvuosi!")