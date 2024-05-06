from abc import ABC, abstractmethod
import math 

class Abstrak(ABC):
    @abstractmethod
    def luas(self):
        pass

class Persegi(ABC):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

class Segitiga(ABC):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

class Lingkaran(ABC):
    def __init__(self, r):
        self.r = r

    def luas(self):
        return math.pi * self.r * self.r

class PersegiPanjang(ABC):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

class JajarGenjang(ABC):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return self.alas * self.tinggi

