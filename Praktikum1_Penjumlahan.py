# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:20:59 2024

@author: faiz
#Faiz Firdaus Priyanto
#Informatika 
#064002300005
#program untuk menerima input berupa dua buah angka 
#(integer/float) yang nantinya akan menerima output penjumlahan dari kedua input tersebut
"""


class Penjumlahan:
    def pertambahan(self):      
        angka_1 = float(input("Masukkan angka 1 : "))
        angka_2 = float(input("Masukkan angka 2 : "))
        
        hasil = angka_1 + angka_2    #Penjumlahan
        
        print(f"hasilnya = {hasil}")
        
        
calculator = Penjumlahan()  
calculator.pertambahan()
        
                      
                      
                      
                      