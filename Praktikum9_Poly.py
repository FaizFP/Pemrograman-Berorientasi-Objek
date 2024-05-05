#Faiz Firdaus Priyanto
#064002300005
#Informatika



import math 

class Over:
    def __init__(self):  #constructor 
        print("======================")
        print("Faiz Firdaus Priyanto ")
        print("064002300005")
        print("======================")
        self.sisi = 5    #atribut 
        self.panjang = 4
        self.lebar = 3 
        self.tinggi_balok = 6
        self.tinggi_tabung = 8
        self.jari_jari = 2

    def method(self, *args): # method 
        if len(args) == 1:  #ngitung panjang parameter 
            return self.sisi * self.sisi * self.sisi
        elif len(args) == 3:
            return self.panjang * self.lebar * self.tinggi_balok
        elif len(args) == 2:
            return math.pi * (self.jari_jari ** 2) * self.tinggi_tabung

def main():
    Oover = Over()
    print("Volume kubus dengan sisi 5 :", Oover.method(5),"cm^3") #1 parameter 
    print("Volume balok dengan panjang = 4 , lebar = 3, tinggi = 6 :", Oover.method(4, 3, 6),"cm^3")  #3 parameter 
    print("Volume tabung dengan jari jari dan tinggi 8 :", Oover.method(2, 8),"cm^3") #2 parameter 

if __name__ == "__main__":
    main()
