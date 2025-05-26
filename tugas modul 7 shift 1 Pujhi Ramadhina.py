def input_data():
    data = []
    n = int(input("\nMasukkan jumlah mahasiswa : "))
    for i in range(n):
        print(f"\nMahasiswa ke-{i+1}")
        nama = input("Nama : ")
        nim = input("NIM : ")
        uts = float(input("Nilai UTS : "))
        uas = float(input("Nilai UAS : "))
        tugas = float(input("Nilai Tugas : "))
        data.append({'nama': nama, 'nim': nim, 'uts': uts, 'uas': uas, 'tugas': tugas})
    return data

def hitung_nilai_akhir(data):
    for i in range(len(data)):
        data[i]['nilai_akhir'] = 0.35 * data[i]['uts'] + 0.35 * data[i]['uas'] + 0.30 * data[i]['tugas']
    return data

def hitung_rata_rata(data, kunci):
    if len(data) > 0:
        total = 0
        for i in range(len(data)):
            total += data[i][kunci]
        return total / len(data)
    return 0

def urutkan_dan_peringkat(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j]['nilai_akhir'] < data[j + 1]['nilai_akhir']:
                data[j], data[j + 1] = data[j + 1], data[j] 
    for i in range(n):
        data[i]['peringkat'] = i + 1
    return data

def tampilkan_tabel(data):
    if len(data) == 0:
        print("\nTidak ada data mahasiswa untuk ditampilkan.")
        return  

    print("-" * 93)
    print("|{:<15}| {:<10}| {:<10}| {:<10}| {:<12}| {:<12}| {:<10}|".format(
        "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Peringkat"))
    print("-" * 93)
    for i in range(len(data)):
        mhs = data[i]
        print("|{:<15}| {:<10}| {:<10.1f}| {:<10.1f}| {:<12.1f}| {:<12.2f}| {:<10}|".format(
            mhs['nama'], mhs['nim'], mhs['uts'], mhs['uas'], mhs['tugas'],
            mhs['nilai_akhir'], mhs['peringkat']))
    print("-" * 93)

    rata_uts = hitung_rata_rata(data, 'uts')
    rata_uas = hitung_rata_rata(data, 'uas')
    rata_tugas = hitung_rata_rata(data, 'tugas')
    rata_akhir = hitung_rata_rata(data, 'nilai_akhir')

    print("|{:<15}| {:<10}| {:<10.2f}| {:<10.2f}| {:<12.2f}| {:<12.2f}| {:<10}|".format(
        "Rata-rata", "", rata_uts, rata_uas, rata_tugas, rata_akhir, ""))
    print("-" * 93)

def menu_utama():
    data_mahasiswa = []
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Input Data Mahasiswa")
        print("2. Hitung Nilai Akhir & Peringkat")
        print("3. Tampilkan Tabel Mahasiswa")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == '1':
            data_mahasiswa = input_data()
            print("\nData mahasiswa berhasil dimasukkan.")
        elif pilihan == '2':
            if len(data_mahasiswa) == 0:
                print("Data kosong! Silakan input data terlebih dahulu.")
            else:
                data_mahasiswa = hitung_nilai_akhir(data_mahasiswa)
                data_mahasiswa = urutkan_dan_peringkat(data_mahasiswa)
                print("Nilai akhir dan peringkat berhasil dihitung.")
        elif pilihan == '3':
            tampilkan_tabel(data_mahasiswa)
        elif pilihan == '4':
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")

menu_utama()