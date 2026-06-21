from collections import deque

antrian = deque()


def tambah_antrian():

    nama = input("Nama Penumpang : ")

    antrian.append(nama)

    print("Masuk antrean")


def layani_antrian():

    if len(antrian) == 0:
        print("Antrean kosong")

    else:
        print("Melayani :", antrian.popleft())