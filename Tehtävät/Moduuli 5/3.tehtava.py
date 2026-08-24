## 3. Tehtävä

alkuluku_kysymys = int(input("Luku: "))

for i in range(2, alkuluku_kysymys):
    if alkuluku_kysymys % i == 0:
        print("Naa mään")
        break
else:
    print("Yee mään")