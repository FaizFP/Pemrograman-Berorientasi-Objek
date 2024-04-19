#Faiz Firdaus Priyanto
#064002300005
#Informatika 



class Masyarakat_kampus:
    def __init__(self, nama):
        self.nama = nama

    def Gaji(self):
        pass

class Dosen(Masyarakat_kampus):
    def __init__(self):
        super().__init__("Dosen")
        print("==============================")

    def Gaji(self, gaji= int(45000)):
        return "Golongan Dosen mendapatkan gaji", gaji

class Karyawan(Masyarakat_kampus):
    def __init__(self):
        super().__init__("STAFF")
        print("Nama : Faiz Firdaus Priyanto||")

    def Gaji(self, gaji= int(35000)):
        return "Golongan STAFF mendapatkan gaji", gaji

class Lain(Masyarakat_kampus):
    def __init__(self):
        super().__init__("Lain")
        print("Nim  : 064002300005         ||")
        print("==============================")

    def Gaji(self, gaji= int(15000)):
        return 'Golongan Lain mendapatkan gaji' , gaji

def main():
    dosen = Dosen()
    karyawan = Karyawan()
    lain = Lain()
    
    
    
    

    print(dosen.Gaji())
    
    print(karyawan.Gaji())
    
    print(lain.Gaji())

if __name__ == "__main__":
    main()
