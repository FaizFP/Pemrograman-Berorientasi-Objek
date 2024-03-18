#Faiz Firdaus Priyanto 
#06400230005
#Informatika
#Menampilkan deret 


class Deret:
    def bilangan(nim):
       for i in range(1,51):
           if i % 100 != nim :
            print(i, end=" ")

nim = int(input("Masukkan 2 digit terakhir : "))  #input nim 

#Pemanggilan fungsi 
Deret.bilangan(nim) 

