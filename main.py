from modules.crud import *
from modules.csv_handler import *
from modules.searching import *
from modules.sorting import *
from modules.queue_jadwal import *
from modules.riwayat import *

FILE_JADWAL = "jadwal.csv"


def menu_cari():

    data = baca_csv(FILE_JADWAL)

    keyword = input("Masukkan Mata Kuliah : ")

    hasil = cari_matkul(data, keyword)

    if len(hasil) == 0:

        print("Data tidak ditemukan")

    else:

        for jadwal in hasil:

            print(
                jadwal["id_jadwal"],
                jadwal["matkul"],
                jadwal["dosen"],
                jadwal["hari"]
            )


def menu_sort():

    data = baca_csv(FILE_JADWAL)

    hasil = bubble_sort_matkul(data)

    print("\nDATA TERURUT")

    for jadwal in hasil:

        print(
            jadwal["id_jadwal"],
            jadwal["matkul"],
            jadwal["dosen"],
            jadwal["hari"]
        )


def tambah_ke_antrian():

    id_jadwal = input(
        "Masukkan ID Jadwal yang akan diverifikasi : "
    )

    tambah_antrian(id_jadwal)

    print("Masuk antrian verifikasi")


def proses_verifikasi():

    data = proses_antrian()

    if data:

        tambah_riwayat(
            f"Jadwal {data} telah diverifikasi"
        )

        print("Verifikasi berhasil")

    else:

        print("Tidak ada antrian")


def tampil_riwayat():

    data = lihat_riwayat()

    if len(data) == 0:

        print("Belum ada riwayat")

    else:

        for item in reversed(data):

            print(item)


while True:

    print("\n===== SISTEM PENJADWALAN KULIAH =====")
    print("1. Tambah Jadwal")
    print("2. Lihat Jadwal")
    print("3. Update Jadwal")
    print("4. Hapus Jadwal")
    print("5. Cari Jadwal")
    print("6. Urutkan Jadwal")
    print("7. Tambah Antrian Verifikasi")
    print("8. Lihat Antrian")
    print("9. Proses Verifikasi")
    print("10. Lihat Riwayat")
    print("11. Keluar")

    pilih = input("Pilih Menu : ")

    if pilih == "1":
        tambah_jadwal()

    elif pilih == "2":
        tampil_jadwal()

    elif pilih == "3":
        update_jadwal()

    elif pilih == "4":
        hapus_jadwal()

    elif pilih == "5":
        menu_cari()

    elif pilih == "6":
        menu_sort()

    elif pilih == "7":
        tambah_ke_antrian()

    elif pilih == "8":

        for item in lihat_antrian():
            print(item)

    elif pilih == "9":
        proses_verifikasi()

    elif pilih == "10":
        tampil_riwayat()

    elif pilih == "11":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")