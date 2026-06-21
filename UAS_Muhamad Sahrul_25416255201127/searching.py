def cari_tiket(linked):

    id_tiket = input("Masukkan ID Tiket : ")

    data = linked.cari(id_tiket)

    if data:

        print("\n=== DATA DITEMUKAN ===")
        print("Nama :", data.nama)
        print("Asal :", data.asal)
        print("Tujuan :", data.tujuan)
        print("Tanggal :", data.tanggal)

    else:
        print("Data tidak ditemukan")