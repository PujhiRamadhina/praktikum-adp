# data = ISBN,Judul Buku,Penulis,Stok,Harga Beli,Harga Jual.
data = """9786021514712,Kalkulus 1,E. Purcell,15,70000,110000
9786021514729,Kalkulus 2,E. Purcell,12,75000,115000
9786029324122,Geometri Analitik,Sukino,20,60000,95000
9789792902251,Analisis Data,Dr. Sugiyono,18,80000,115000
9786022894127,Matematika Diskrit,Edi Suryanto,15,78000,110000
9786024531235,Algoritma dan Pemrograman,Ir. Adi Nugroho,18,85000,125000
9786024531341,Aljabar Linier Elementer,Dr. Rinaldi Munir,15,82000,118000
9786028650833,Kimia Dasar,Ebbing & Gammon,12,95000,140000
9786023743486,Fisika Dasar,Ertanto Setyo,18,80000,120000
9786022897654,Pengantar Matematika,E. Purcell,12,75000,110000
"""
with open("inventaris_buku.txt", "w") as file:
    file.write(data)
buku_list = []

with open("inventaris_buku.txt", "r") as file:
    for baris in file:
        bagian = []
        kata = ""
        for huruf in baris:
            if huruf == "," or huruf == "\n":
                bagian.append(kata)
                kata = ""
            else:
                kata += huruf
        if kata != "":
            bagian.append(kata)
        buku = {
            "ISBN": bagian[0],
            "Judul": bagian[1],
            "Penulis": bagian[2],
            "Stok": int(bagian[3]),
            "Harga Beli": int(bagian[4]),
            "Harga Jual": int(bagian[5])
        }
        buku_list.append(buku)

with open("laporan_inventaris.txt", "w") as laporan:
    laporan.write("ISBN,Judul,Penulis,Stok,Harga Beli,Harga Jual,Potensi Keuntungan\n")
    for buku in buku_list:
        keuntungan = (buku["Harga Jual"] - buku["Harga Beli"]) * buku["Stok"]
        buku["Potensi"] = keuntungan
        laporan.write(buku["ISBN"] + "," + buku["Judul"] + "," + buku["Penulis"] + "," +
                      str(buku["Stok"]) + "," + str(buku["Harga Beli"]) + "," +
                      str(buku["Harga Jual"]) + "," + str(keuntungan) + "\n")

buku_tertinggi = buku_list[0]
buku_terendah = buku_list[0]
total_nilai = 0
butuh_restock = []
for buku in buku_list:
    total_nilai += buku["Harga Beli"] * buku["Stok"]
    if buku["Potensi"] > buku_tertinggi["Potensi"]:
        buku_tertinggi = buku
    if buku["Potensi"] < buku_terendah["Potensi"]:
        buku_terendah = buku
    if buku["Stok"] < 5:
        butuh_restock.append(buku)

print("\n---LAPORAN ANALISIS INVENTARIS BUKU---\n")
print("Buku dengan Potensi Keuntungan Tertinggi :")
print(buku_tertinggi["Judul"] + " oleh " + buku_tertinggi["Penulis"] +
      " - Rp" + str(buku_tertinggi["Potensi"]))
print("\nBuku dengan Potensi Keuntungan Terendah :")
print(buku_terendah["Judul"] + " oleh " + buku_terendah["Penulis"] +
      " - Rp" + str(buku_terendah["Potensi"]))
print("\nTotal Nilai Inventaris (berdasarkan harga beli): Rp" + str(total_nilai))
print("\nBuku yang Perlu Restock (Stok < 5) :")
if len(butuh_restock) == 0:
    print("Tidak ada buku yang perlu direstock.\n")
else:
    for buku in butuh_restock:
        print(buku["ISBN"] + ", " + buku["Judul"] + ", " + buku["Penulis"] +
              ", Stok: " + str(buku["Stok"]))