#Faiz Firdaus Priyanto 
#06400230005
#Informatika


#identitas
class Identitas:

    def __init__(self):
          #Identitas
        self.nama  = "Faiz Firdaus Priyanto"
        self.nim   = "064002300005"
        self.studi = "Teknik Informatika"
        self.hobi  = "Nyangkul"
    
    def nama(self):
        return  self .nama  #Mengembalikan nama 
    
    def fakultas(self):
        return self.studi #Mengembalikan fakultas
    
    def hobi(self):
        return self.hobi  #mengembalikan hobi
               
    def tampilan(self):  #Tampilan 
        print(self.nama ,"\n" ,self.nim)
        print("-------------")
        #Tampilan 
        print("Nama Saya adalah :" , self.nama ,"Nim saya adalah :" , self.nim )
        print("Saya dari fakultas :" , self.studi)
        print("Hobi saya adalah :", self.hobi)

   

def main():   #MEnjalankan program 
    OIdentitas = Identitas()  #
    OIdentitas.tampilan()
    
    

if __name__ == "__main__":
    main()     