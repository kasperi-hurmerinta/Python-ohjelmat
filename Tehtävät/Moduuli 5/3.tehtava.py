## 3. Tehtävä

alkuluku_kysymys = int(input("Kokonaisluku: "))

jakaja = 2
alkuluku = True

if alkuluku_kysymys > 1:
    alkuluku = False
    for i in range(alkuluku_kysymys - 2):
        if alkuluku_kysymys % jakaja == 0:
            alkuluku = False

        jakaja += 1

if alkuluku == True:
    print("Yees mään")
else:
    print("No määän")