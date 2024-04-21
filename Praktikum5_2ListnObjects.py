#Faiz Firdaus Priyanto
#064002300005
#Informatika

class Film:
    def __init__(self, nama, tahun_rilis, director):
         # Konstruktor untuk inisialisasi objek Film 
        self.nama = nama   #attribute 
        self.tahun_rilis = tahun_rilis
        self.director = director


class ListFilm:
    def __init__(self):
        print("Prak 5 (Faiz Firdaus Priyanto - 064002300005)")
        print("-----------------------ELKOM 2 ----------------")
        self.list_film = [] #list 

    def tambah_film(self, film):
        self.list_film.append(film)  #menambahkan   objek Film ke dalam list_film

    def tampilkan_film(self):
        for index, film in enumerate(self.list_film, start=1):
             print(f"film favorit ke-{index} \n judul : {film.nama} \n  Rilis : {film.tahun_rilis} \n Director :{film.director}")

# Membuat objek-objek film favorit
film1 = Film("Inception", 2010, "Christopher Nolan")
film2 = Film("The Shawshank Redemption", 1994, "Frank Darabont")
film3 = Film("The Godfather", 1972, "Francis Ford Coppola")

# Membuat list film
list_film = ListFilm()
list_film.tambah_film(film1)
list_film.tambah_film(film2)
list_film.tambah_film(film3)

# Menampilkan daftar film
list_film.tampilkan_film()
