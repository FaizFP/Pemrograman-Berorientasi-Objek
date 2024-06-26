import datetime
import pytz

def my_decorator(inner):
    def inner_decorator():
        print("===================================")
        print("Faiz Firdaus Priyanto")
        print("064002300005")
        print("===================================")
        # Mendapatkan waktu UTC
        utc_now = datetime.datetime.now(pytz.utc)
        # Mengubah waktu UTC menjadi UTC+7 (Jakarta Time)
        jakarta_tz = pytz.timezone('Asia/Jakarta')
        jakarta_now = utc_now.astimezone(jakarta_tz)

        # Menampilkan waktu sebelum menjalankan fungsi
        
        print(f"Timezone: {jakarta_tz.zone}")
        print(f"Tanggal: {jakarta_now.strftime('%Y-%m-%d')}")
        print(f"Waktu: {jakarta_now.strftime('%H:%M:%S.%f')}")
        print()

        # Memanggil fungsi yang dihias
        inner()

        # Mendapatkan waktu UTC lagi setelah pemanggilan fungsi
        utc_now = datetime.datetime.now(pytz.utc)
        jakarta_now = utc_now.astimezone(jakarta_tz)

        # Menampilkan waktu setelah menjalankan fungsi
        print()
        print(f"Tanggal: {jakarta_now.strftime('%Y-%m-%d')}")
        print(f"Waktu: {jakarta_now.strftime('%H:%M:%S.%f')}")
        

    return inner_decorator

@my_decorator
def decorated():
    print("Berubah Menjadi")

if __name__ == "__main__":
    decorated()

