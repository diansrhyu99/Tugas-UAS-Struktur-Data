def cari_matkul(data, keyword):

    hasil = []

    for jadwal in data:

        if keyword.lower() in jadwal["matkul"].lower():

            hasil.append(jadwal)

    return hasil