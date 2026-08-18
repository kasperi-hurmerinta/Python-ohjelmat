## 5. Tehtävä

x = float(input("Anna leiviskät: "))
y = float(input("Anna naulat: "))
z = float(input("Anna luodit: "))

luoti_lasku =  x * 20 * 32 + y * 32 + z
luoteja_yhteensa = luoti_lasku * 13.3
grammat = luoteja_yhteensa
kilogrammat = grammat // 1000
grammoja_jaljella = grammat % 1000

print(f"{kilogrammat:.3} Kilogrammaa ja {grammoja_jaljella:.5} grammaa")



