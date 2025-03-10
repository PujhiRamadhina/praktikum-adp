# Tampilan 1 : input data diri
print("=== Struk Pemesanan Tiket Pesawat ===")
nama = input("Masukkan nama: ")
umur = input("Masukkan umur: ")
jenis_kelamin = input("Masukkan jenis kelamin (L/P): ")
# Tampilan 2 : memilih kode maskapai
print("\nPilihan Kode Maskapai:")
print("3012 - Padang-Jakarta")
print("4015 - Padang-Batam")
print("4050 - Padang-Bandung")
kode_maskapai = input("Masukkan pilihan kode maskapai: ")
if kode_maskapai == "3012":
    tujuan = "Padang-Jakarta"
    harga_ekonomi = 800000
    harga_bisnis = 850000
    harga_first = 900000
elif kode_maskapai == "4015":
    tujuan = "Padang-Batam"
    harga_ekonomi = 500000
    harga_bisnis = 550000
    harga_first = 700000
elif kode_maskapai == "4050":
    tujuan = "Padang-Bandung"
    harga_ekonomi = 700000
    harga_bisnis = 750000
    harga_first = 850000
else:
    print("Kode maskapai tidak valid!")
# Tampilan 3 menampilkan menu jenis maskapai
print("\nPilih Kelas Penerbangan:")
print("1. Ekonomi")
print("2. Bisnis")
print("3. First Class")
kelas_input = input("Masukkan pilihan kelas (1/2/3): ")
if kelas_input == "1":
    kelas = "Ekonomi"
    harga_tiket = harga_ekonomi
elif kelas_input == "2":
    kelas = "Bisnis"
    harga_tiket = harga_bisnis
elif kelas_input == "3":
    kelas = "First Class"
    harga_tiket = harga_first
else:
    print("Pilihan kelas tidak valid!")
jumlah = int(input("Jumlah tiket yang dibeli: "))
if jumlah > 3:
    total_harga = harga_tiket * jumlah
    diskon = total_harga * 0.2
    total = int(total_harga - diskon)
else:
    total = int(harga_tiket * jumlah)
# Tampilan 4 menampilkan struk pembelian
print("\n=== Struk Pemesanan Tiket Pesawat ===")
print("Nama:", nama)
print("Umur:", umur)
print("Jenis Kelamin:", jenis_kelamin)
print("Tujuan:", tujuan)
print("Kelas:", kelas)
print("Jumlah Tiket:", jumlah)
print("Total Harga: Rp", (total))
print("=== Tiket pesawat telah berhasil dipesan ===")
print("=======================")