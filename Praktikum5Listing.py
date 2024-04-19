#Faiz Firdaus Priyanto 
#064002300005
#Informatika


class List:
    def __init__(self):
        print("Praktikum 5 (Faiz Firdaus Priyanto - 064002300005)")
        self.list_tampung = []

    def masukan(self):
        for i in range(1, 6):
            input_user = str(input(f"Masukkan film Favorit ke {i}: "))
            self.list_tampung.append(input_user)

    def tampilkan(self):
        print("\nDaftar film favorit Anda:")
        for i, film in enumerate(self.list_tampung, 1):  #1 
            print(f"{i}.) {film}")

def main():
    list_film = List()
    
    # Memasukkan 5 film favorit
    list_film.masukan()

    # Menampilkan daftar film favorit
    list_film.tampilkan()

if __name__ == "__main__":
    main()





