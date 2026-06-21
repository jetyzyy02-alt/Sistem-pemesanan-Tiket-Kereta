import csv
import os

from linkedlist import LinkedList

FILE_CSV = "tiket.csv"


def buat_file():

    if not os.path.exists(FILE_CSV):

        with open(FILE_CSV, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "id_tiket",
                "nama",
                "asal",
                "tujuan",
                "tanggal",
                "jam",
                "kelas",
                "harga",
                "status"
            ])


def load_csv():

    linked = LinkedList()

    with open(FILE_CSV, "r") as file:

        reader = csv.reader(file)

        next(reader, None)

        for row in reader:

            if len(row) == 9:
                linked.tambah(*row)

    return linked


def simpan_csv(linked):

    with open(FILE_CSV, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "id_tiket",
            "nama",
            "asal",
            "tujuan",
            "tanggal",
            "jam",
            "kelas",
            "harga",
            "status"
        ])

        for data in linked.ke_list():
            writer.writerow(data)