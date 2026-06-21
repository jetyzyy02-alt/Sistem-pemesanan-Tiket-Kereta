class Node:
    def __init__(self, id_tiket, nama, asal, tujuan,
                 tanggal, jam, kelas, harga, status):

        self.id_tiket = id_tiket
        self.nama = nama
        self.asal = asal
        self.tujuan = tujuan
        self.tanggal = tanggal
        self.jam = jam
        self.kelas = kelas
        self.harga = harga
        self.status = status
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, *data):

        node = Node(*data)

        if self.head is None:
            self.head = node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = node

    def tampilkan(self):

        if self.head is None:
            print("\nData kosong")
            return

        temp = self.head

        while temp:
            print("=" * 50)
            print("ID Tiket :", temp.id_tiket)
            print("Nama :", temp.nama)
            print("Asal :", temp.asal)
            print("Tujuan :", temp.tujuan)
            print("Tanggal :", temp.tanggal)
            print("Jam :", temp.jam)
            print("Kelas :", temp.kelas)
            print("Harga :", temp.harga)
            print("Status :", temp.status)

            temp = temp.next

    def cari(self, id_tiket):

        temp = self.head

        while temp:

            if temp.id_tiket == id_tiket:
                return temp

            temp = temp.next

        return None

    def hapus(self, id_tiket):

        temp = self.head

        if temp and temp.id_tiket == id_tiket:
            self.head = temp.next
            return True

        prev = None

        while temp:

            if temp.id_tiket == id_tiket:
                prev.next = temp.next
                return True

            prev = temp
            temp = temp.next

        return False

    def ke_list(self):

        data = []

        temp = self.head

        while temp:

            data.append([
                temp.id_tiket,
                temp.nama,
                temp.asal,
                temp.tujuan,
                temp.tanggal,
                temp.jam,
                temp.kelas,
                temp.harga,
                temp.status
            ])

            temp = temp.next

        return data