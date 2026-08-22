## 2. Tehtävä

while True:
    tuuma = 2.54
    kysymys = float(input("Tuuma: "))
    lasku = kysymys * tuuma

    if kysymys < 0:
        print("Ohjelmasta poistuttu.")
        break

    print(f"Sentteinä: {lasku}")
