#Faiz Firdaus Priyanto 
#06400230005
#Informatika
#program yang dapat menampilkan hasil perhitungan luas sebuah persegi panjang, 
#dimana panjang dan lebarnya di set sebagai parameter saat pembuatan object (panjang dan lebar persegi panjang bebas).

class Persegi:

    def __init__(self):
          #Identitas
        self.nama  = "Faiz Firdaus Priyanto"
        self.nim   = "064002300005"
        self.studi = "Teknik Informatika"
        self.panjang = int(input("MAsukkan angka : "))
        self.lebar = int(input("MAsukkan angka : "))

    def luas_persegi(self):
        return self.panjang * self.lebar  #rumus persegi 
    
    def tampilan_data(self):  #tampilan user 
        print(self.nama , self.nim , self.studi)  
        print("---->PROGRAM MENGHITUNG PERSEGI PANJANG<----")
        print("Persegi panjang dengan panjang", self.panjang, "cm lebar", self.lebar, "memiliki luas sekitar", self.segitiga(), "cm^2")

def main():  #Pemanggilan fungsi 
    oPersegi = Persegi()
    oPersegi.tampilan_data()

if __name__ == "__main__":
    main()


    

