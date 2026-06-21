from collections import deque

antrian_jadwal = deque()


def tambah_antrian(id_jadwal):

    antrian_jadwal.append(id_jadwal)


def proses_antrian():

    if len(antrian_jadwal) > 0:
        return antrian_jadwal.popleft()

    return None


def lihat_antrian():

    return list(antrian_jadwal)