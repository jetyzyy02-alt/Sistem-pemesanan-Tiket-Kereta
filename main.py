from database import buat_file, load_csv
from crud import (
    pesan_tiket,
    update_tiket,
    batalkan_tiket
)

from searching import cari_tiket
from sorting import sorting_nama

from queue_tiket import (
    tambah_antrian,
    layani_antrian
)


def menu():

    buat_file()

    linked = load_csv()

    while True:

        print("\n")
        print("=" * 45)
        print(" SISTEM PEMESANAN TIKET KERETA API ")
        print("=" * 45)

        print("1. Pesan Tiket")
        print("2. Lihat Data Pemesanan")
        print("3. Update Tiket")
        print("4. Batalkan Tiket")
        print("5. Cari Tiket")
        print("6. Sorting Nama Penumpang")
        print("7. Tambah Antrean")
        print("8. Layani Antrean")
        print("9. Keluar")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            pesan_tiket(linked)

        elif pilih == "2":
            linked.tampilkan()

        elif pilih == "3":
            update_tiket(linked)

        elif pilih == "4":
            batalkan_tiket(linked)

        elif pilih == "5":
            cari_tiket(linked)

        elif pilih == "6":
            sorting_nama(linked)

        elif pilih == "7":
            tambah_antrian()

        elif pilih == "8":
            layani_antrian()

        elif pilih == "9":
            print("Program selesai")
            break

        else:
            print("Menu tidak tersedia")


if __name__ == "__main__":
    menu()