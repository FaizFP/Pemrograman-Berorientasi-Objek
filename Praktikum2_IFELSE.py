# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:27:46 2024

@author: faiz
"""

#Faiz Firdaus Priyanto 
#064002300005
#Informatika 
#"Program menghitung keliling dan luas segitiga"

class Segitiga:
    def __init__(self, sisi1, sisi2, sisi3):
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        self.sisi3 = sisi3

    def keliling(self):      #Mengitung keliling segitiga
        if self.sisi1 and self.sisi2 and self.sisi3:
            return self.sisi1 + self.sisi2 + self.sisi3
        

    
    def hitung_luas(alas, tinggi):      #Menghitung luas segitiga
        return 0.5 * alas * tinggi

while True:
    print("Nama : Faiz Firdaus Priyanto ")  #Tampilan untuk user
    print("Nim : 064002300005s")
    print("Program menghitung keliling dan luas:")
    print("1. Hitung Keliling Segitiga")
    print("2. Hitung Luas Segitiga")
    
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "":   #tidak mengisi apapun akan program berhenti 
        print("Terima kasih telah menggunakan program ini.")
        break
    
    elif pilihan == "1":  #user input
        sisi1 = float(input("Masukkan panjang sisi pertama: "))
        sisi2 = float(input("Masukkan panjang sisi kedua: "))
        sisi3 = float(input("Masukkan panjang sisi ketiga: "))
        segitiga = Segitiga(sisi1, sisi2, sisi3)
        print(f"Keliling segitiga : {segitiga.keliling():.2f} cm")

    elif pilihan == "2":  #user input
        tinggi = float(input("Masukkan tinggi segitiga: "))
        alas = float(input("Masukkan alas segitiga: "))
        luas_segitiga = Segitiga.hitung_luas(alas, tinggi)
        print(f"Luas segitiga : {luas_segitiga:.2f} cm^2")





        
        
    