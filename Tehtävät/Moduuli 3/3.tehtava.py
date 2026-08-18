## 3. Tehtävä

x = input("Sukupuoli M/N: ")
y = float(input("Hemoglobiiniarvo (g/l): "))

if x == "M" and y < 134:
    print("Hemoglobiiniarvo (g/l): alhainen")
elif x == "M" and y <= 195:
    print("Hemoglobiiniarvo (g/l): normaali")
elif x == "N" and y < 117:
    print("Hemoglobiiniarvo (g/l): alhainen")
elif x == "N" and y <= 175:
    print("Hemoglobiiniarvo (g/l): normaali")
else:
    print("Hemoglobiiniarvo (g/l): korkea")