## 3. Tehtävä


def nestegallat_litroiksi(x):
    lasku = x * 3.785

    return lasku

while True:
    x = float(input("Bensiinin määrä Yhdysvaltain nestegallonoina: "))

    if x < 0:
        break

    print(f" Litraa: {nestegallat_litroiksi(x)}")

