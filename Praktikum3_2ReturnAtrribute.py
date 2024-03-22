#Faiz Firdaus Priyanto 
#06400230005
#Informatika



class Persegi:

    def __init__(self):
          #Identitas
        self.nama  = "Faiz Firdaus Priyanto"
        self.nim   = "064002300005"
        self.studi = "Teknik Informatika"
        self.panjang = int(input("MAsukkan angka : "))
        self.lebar = int(input("MAsukkan angka : "))

    def segitiga(self):
        return self.panjang * self.lebar  #rumus persegi 
    
    def tampilan(self):  #tampilan user 
        print(self.nama , self.nim , self.studi)  
        print("---->PROGRAM MENGHITUNG PERSEGI PANJANG<----")
        print("Persegi panjang dengan panjang", self.panjang, "cm lebar", self.lebar, "memiliki luas sekitar", self.segitiga(), "cm^2")

def main():  #Pemanggilan fungsi 
    obj_persegi = Persegi()
    obj_persegi.tampilan()

if __name__ == "__main__":
    main()


    

