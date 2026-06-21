from database import simpan_csv


def pesan_tiket(linked):

    print("\n=== PESAN TIKET KERETA ===")

    id_tiket = input("ID Tiket : ")
    nama = input("Nama Penumpang : ")
    asal = input("Stasiun Asal : ")
    tujuan = input("Stasiun Tujuan : ")
    tanggal = input("Tanggal Berangkat : ")
    jam = input("Jam Berangkat : ")

    kelas = input("Kelas (Ekonomi/Bisnis/Eksekutif): ").lower()
    if kelas == "ekonomi":
        harga = 100000
    elif kelas == "bisnis":
        harga = 200000
    elif kelas == "eksekutif":
        harga = 300000
    else:
        print("Kelas Tidak ada")

    status = "Lunas"

    linked.tambah(
        id_tiket,
        nama,
        asal,
        tujuan,
        tanggal,
        jam,
        kelas,
        harga,
        status
    )
    print(linked.ke_list())
    simpan_csv(linked)

    print("Harga Tiket: Rp", harga)
    print("Pemesanan berhasil")


def update_tiket(linked):

    id_tiket = input("Masukkan ID Tiket : ")

    data = linked.cari(id_tiket)

    if data:

        data.nama = input("Nama Baru : ")
        data.tanggal = input("Tanggal Baru : ")
        data.jam = input("Jam Baru : ")
        data.kelas = input("Kelas Baru : ")

        simpan_csv(linked)

        print("Data berhasil diperbarui")

    else:
        print("Data tidak ditemukan")


def batalkan_tiket(linked):

    id_tiket = input("Masukkan ID Tiket : ")

    if linked.hapus(id_tiket):

        simpan_csv(linked)

        print("Tiket berhasil dibatalkan")

    else:
        print("Data tidak ditemukan")