jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa praktikum ADP : "))
data_mahasiswa = []
for i in range(jumlah_mahasiswa):
    print(f"\nMahasiswa ke-{i+1}  :")
    nama = input("Nama mahasiswa  : ")
    pretest = float(input("Nilai pretest   : "))
    posttest = float(input("Nilai posttest  : "))
    makalah = float(input("Nilai makalah   : "))
    nilai_akhir = (0.4 * pretest) + (0.4 * posttest) + (0.2 * makalah)
    data_mahasiswa.append([nama, nilai_akhir])
print("\nTabel Nilai Mahasiswa :")
print("----------------------------------------")
print("|    Nama Mahasiswa    |  Nilai Akhir  |")
print("----------------------------------------")
for data in data_mahasiswa:
    print(f"| {data[0]:<20} | {data[1]:>9.2f}     |")
print("----------------------------------------")
total_nilai = 0
for data in data_mahasiswa:
    total_nilai += data[1]
rata_rata = total_nilai / jumlah_mahasiswa
print(f"\nRata-rata nilai akhir kelas : {rata_rata:.2f}")
nilai_tertinggi = data_mahasiswa[0]
nilai_terendah = data_mahasiswa[0]
for data in data_mahasiswa:
    if data[1] > nilai_tertinggi[1]:
        nilai_tertinggi = data
    if data[1] < nilai_terendah[1]:
        nilai_terendah = data
print(f"\nNilai tertinggi : {nilai_tertinggi[0]} dengan nilai {nilai_tertinggi[1]:.2f}")
print(f"Nilai terendah  : {nilai_terendah[0]} dengan nilai {nilai_terendah[1]:.2f}")
print("\nMahasiswa yang nilai akhirnya di atas rata-rata kelas : ", end="")
jumlah_di_atas_rata = 0
for data in data_mahasiswa:
    if data[1] > rata_rata:
        print(f"{data[0]} ({data[1]:.2f})")
        jumlah_di_atas_rata += 1
if jumlah_di_atas_rata == 0:
        print("Tidak ada mahasiswa dengan nilai di atas rata-rata.")