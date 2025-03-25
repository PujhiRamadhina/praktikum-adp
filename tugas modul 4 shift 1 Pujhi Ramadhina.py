while True:
    r = int(input("Masukkan jumlah baris kursi (minimal 4): "))
    c = int(input("Masukkan jumlah kolom kursi (minimal 4): "))
    if r >= 4 and c >= 4:
        break
    print("Ukuran minimal bioskop adalah 4x4! Silakan masukkan ulang.")
teater = ()
for i in range(r):
    baris_kursi = ()
    for j in range(c):
        nomor_kursi = i * c + j + 1
        baris_kursi = baris_kursi + (nomor_kursi,)  
    teater = teater + (baris_kursi,)
kursi_dipesan = ()
while True:
    print("\nLayout Kursi Bioskop:")
    for baris in teater:
        for kursi in baris:
            if kursi in kursi_dipesan:
                print(" X ", end=" ")
            else:
                print(f"{kursi:3}", end=" ")
        print()   
    pilihan = int(input("\nMasukkan nomor kursi yang ingin dipesan (atau 0 untuk selesai): "))
    if pilihan == 0:
        print("Terima kasih telah memesan tiket!")
        break
    if pilihan < 1 or pilihan > r * c:
        print("Nomor kursi tidak valid!")
        continue
    if pilihan in kursi_dipesan: 
        print("Kursi sudah dipesan! Pilih kursi lain.")
    else:
        kursi_dipesan = kursi_dipesan + (pilihan,)  
        print(f"Kursi {pilihan} berhasil dipesan!")
print("\nProses selesai. Berikut adalah layout kursi terakhir:")
for baris in teater:  
    for kursi in baris:
        if kursi in kursi_dipesan:
            print(" X ", end=" ")
        else:
            print(f"{kursi:3}", end=" ")
    print()