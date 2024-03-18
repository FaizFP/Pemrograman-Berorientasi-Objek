#Faiz Firdaus Priyanto 
#06400230005
#Informatika
#Menampilkan deret 


class Deret:
    def bilangan(nim):
       for angka in range(1,51):  #start #stop
           if angka  != nim :
            print(angka, end=" ")

nim = int(input("Masukkan 2 digit terakhir : "))  #input nim 

#Pemanggilan fungsi 
Deret.bilangan(nim) 

