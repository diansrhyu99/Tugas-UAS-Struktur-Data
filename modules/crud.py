from modules.csv_handler import baca_csv, tulis_csv

FILE_JADWAL = "jadwal.csv"


def tambah_jadwal():

    data = baca_csv(FILE_JADWAL)

    id_jadwal = input("ID Jadwal : ")
    matkul = input("Mata Kuliah : ")
    dosen = input("Dosen : ")
    hari = input("Hari : ")
    jam = input("Jam : ")
    ruangan = input("Ruangan : ")

    data.append({
        "id_jadwal": id_jadwal,
        "matkul": matkul,
        "dosen": dosen,
        "hari": hari,
        "jam": jam,
        "ruangan": ruangan
    })

    tulis_csv(
        FILE_JADWAL,
        [
            "id_jadwal",
            "matkul",
            "dosen",
            "hari",
            "jam",
            "ruangan"
        ],
        data
    )

    print("Data berhasil ditambahkan")


def tampil_jadwal():

    data = baca_csv(FILE_JADWAL)

    print("\nDATA JADWAL")

    for jadwal in data:

        print(
            jadwal["id_jadwal"],
            jadwal["matkul"],
            jadwal["dosen"],
            jadwal["hari"],
            jadwal["jam"],
            jadwal["ruangan"]
        )


def update_jadwal():

    data = baca_csv(FILE_JADWAL)

    id_cari = input("Masukkan ID Jadwal : ")

    ditemukan = False

    for jadwal in data:

        if jadwal["id_jadwal"] == id_cari:

            jadwal["matkul"] = input("Mata Kuliah Baru : ")
            jadwal["dosen"] = input("Dosen Baru : ")
            jadwal["hari"] = input("Hari Baru : ")
            jadwal["jam"] = input("Jam Baru : ")
            jadwal["ruangan"] = input("Ruangan Baru : ")

            ditemukan = True
            break

    if ditemukan:

        tulis_csv(
            FILE_JADWAL,
            [
                "id_jadwal",
                "matkul",
                "dosen",
                "hari",
                "jam",
                "ruangan"
            ],
            data
        )

        print("Data berhasil diupdate")

    else:

        print("Data tidak ditemukan")


def hapus_jadwal():

    data = baca_csv(FILE_JADWAL)

    id_cari = input("Masukkan ID Jadwal : ")

    data_baru = []

    for jadwal in data:

        if jadwal["id_jadwal"] != id_cari:

            data_baru.append(jadwal)

    tulis_csv(
        FILE_JADWAL,
        [
            "id_jadwal",
            "matkul",
            "dosen",
            "hari",
            "jam",
            "ruangan"
        ],
        data_baru
    )

    print("Data berhasil dihapus")