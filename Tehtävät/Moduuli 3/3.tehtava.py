## 3. Tehtävä

x = input("Sukupuoli M/N: ")
y = float(input("Hemoglobiiniarvo (g/l): "))

if x == "M" and y >= 117 and y <= 130:
    print("Hemoglobiiniarvo (g/l): alhainen")
elif x == "M" and y >= 131 and y <= 160:
    print("Hemoglobiiniarvo (g/l): normaali")
elif x == "N" and y >= 117 and y <= 130:
    print("Hemoglobiiniarvo (g/l): alhainen")
elif x == "N" and y >= 131 and y <= 160:
    print("Hemoglobiiniarvo (g/l): normaali")
else:
    print("Hemoglobiiniarvo (g/l): korkea")