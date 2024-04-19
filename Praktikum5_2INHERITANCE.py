##Faiz Firdaus Priyanto 
#064002300005
#Informatika

import math 
class BangunRuang:
    def __init__(self,nama ):
        print("Faiz Firdaus Priyanto ")
        self.nama = nama 
        

    def luas(self):
        pass

    def volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__("Kubus")
        self.sisi = sisi

    def luas(self):
        return 6 * self.sisi ** 2

    def volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__("Balok")
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def luas(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)

    def volume(self):
        return self.panjang * self.lebar * self.tinggi

class Bola(BangunRuang):
    def __init__(self, jari_jari):
        super().__init__("Bola")
        self.jari_jari = jari_jari

    def luas(self):
        return 4 * math.pi * self.jari_jari ** 2

    def volume(self):
        return (4/3) * math.pi * self.jari_jari ** 3

class Silinder(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        super().__init__("Silinder")
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def luas(self):
        return 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)

    def volume(self):
        return math.pi * self.jari_jari ** 2 * self.tinggi

class PrismaSegitiga(BangunRuang):
    def __init__(self, alas, tinggi_prisma, tinggi_segitiga):
        super().__init__("Prisma Segitiga")
        self.alas = alas
        self.tinggi_prisma = tinggi_prisma
        self.tinggi_segitiga = tinggi_segitiga

    def luas(self):
        luas_segitiga = 0.5 * self.alas * self.tinggi_segitiga
        return 2 * luas_segitiga + self.alas * 3 * self.tinggi_prisma

    def volume(self):
        return 0.5 * self.alas * self.tinggi_segitiga * self.tinggi_prisma    



def main():
    kubus = Kubus(5)
    print("Bangun Ruang:", kubus.nama)
    print("Luas Permukaan:", kubus.luas())
    print("Volume:", kubus.volume())
    print()

    balok = Balok(4, 3, 6)
    print("Bangun Ruang:", balok.nama)
    print("Luas Permukaan:", balok.luas())
    print("Volume:", balok.volume())
    print()

    bola = Bola(7)
    print("Bangun Ruang:", bola.nama)
    print("Luas Permukaan:", bola.luas())
    print("Volume:", bola.volume())
    print()

    silinder = Silinder(5, 10)
    print("Bangun Ruang:", silinder.nama)
    print("Luas Permukaan:", silinder.luas())
    print("Volume:", silinder.volume())
    print()

    prisma_segitiga = PrismaSegitiga(6, 8, 10)
    print("Bangun Ruang:", prisma_segitiga.nama)
    print("Luas Permukaan:", prisma_segitiga.luas())
    print("Volume:", prisma_segitiga.volume())
    print()

if __name__ == "__main__":
    main()



