## 2. Tehtävä

class Hissi:
    def __init__(self,  alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.missa_kerroksessa_ollaan = self.alin_kerros

    def siirry_kerrokseen(self, kerros):

        if self.missa_kerroksessa_ollaan < kerros:
            print(f"Menet hissillä ylöspäin! \n")
            for i in range(self.missa_kerroksessa_ollaan, kerros, +1):
                self.kerros_ylos()


        if self.missa_kerroksessa_ollaan > kerros:
            print(f"Menet hissillä alaspäin! \n")
            for i in range(self.missa_kerroksessa_ollaan, kerros, -1):
                self.kerros_alas()

    def kerros_ylos(self):

        self.missa_kerroksessa_ollaan += 1

        print(f"Olet kerroksessa: {self.missa_kerroksessa_ollaan}")

    def kerros_alas(self):

        self.missa_kerroksessa_ollaan -= 1

        print(f"Olet kerroksessa: {self.missa_kerroksessa_ollaan}")

class Talo:
    def __init__(self, talo_alin_kerros, talo_ylin_kerros, hissien_lukumaara=0):
        self.hissien_lista = []
        self.hissien_lukumaara = hissien_lukumaara

        for i in range(self.hissien_lukumaara):
            hissit = Hissi(talo_alin_kerros, talo_ylin_kerros)
            self.hissien_lista.append(hissit)

    def aja_hissia(self, hissin_numero, kohdekerros):

hissi = Hissi(0, 10)

hissi.siirry_kerrokseen(7)
hissi.siirry_kerrokseen(3)