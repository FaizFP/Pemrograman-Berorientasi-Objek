#Faiz Firdaus Priyanto
#064002300005
#Informatika 


class Mahasiswa:
    def __init__(self):   #Data data program 
        self.nama1 =  "Faiz Firdaus Priyanto"
        self.nim1 = "064002300005"
        self.nilai1 = "99"

        self.nama2 =  "oji"
        self.nim2 = "06400230000100"
        self.nilai2 = "99"

        self.nama3 =  "boy"
        self.nim3 = "06400230000099"
        self.nilai3 = "99"

        self.nama4 =  "joy"
        self.nim4 = "06400230000098"
        self.nilai4 = "99"

    def set_nim(self,nim):   #mengembalikan fungsi nim 
        return self.nim1 , self.nim2 , self.nim3 , self.nim4
    
    def set_nilai(self,nilai):  #mengembalikan nilai 
        return self.nilai1 , self.nilai2 , self.nilai3 , self.nilai4
    
    def print(self):  #untuk menampilkan data pribadi 
        #Data orang pertama 
        print("---Data Pribadi ---")
        print("Nama :" , self.nama1 )
        print("Nim  :" , self.nim1 )
        print("Nilai:" , self.nilai1 )
        
    
    def print_data_teman(self):
        #Data orang kedua  #menampilkan data teman 
        print("--Data Teman ke 1--")
        print("Nama :" , self.nama2 )
        print("Nim  :" , self.nim2 )
        print("Nilai:" , self.nilai2 )

        print("--Data Teman ke 2--")
        print("Nama :" , self.nama3 )
        print("Nim  :" , self.nim3 )
        print("Nilai:" , self.nilai3 )
        
        print("--Data Teman ke 3--")
        print("Nama :" , self.nama4 )
        print("Nim  :" , self.nim4 )
        print("Nilai:" , self.nilai4 )


def main():#pemanggilan fungsi 
    OMahasiswa = Mahasiswa()
    OMahasiswa.print()   
    OMahasiswa.print_data_teman()     



if __name__ == '__main__':
    main()  