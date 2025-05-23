print("\nSelamat Menggunakan Kalkulator Matriks")
print("\nMasukkan ukuran matriks A:")
m = int(input("Jumlah baris A: "))
n = int(input("Jumlah kolom A: "))
A = []

print("Masukkan elemen-elemen matriks A:")
for i in range(m):
    baris = []
    for j in range(n):
        nilai = float(input(f"Masukkan A[{i+1}][{j+1}]: "))
        baris.append(nilai)
    A.append(baris)
    
print("\nMasukkan ukuran matriks B:")
p = int(input("Jumlah baris B: "))
q = int(input("Jumlah kolom B: "))
B = []

print("Masukkan elemen-elemen matriks B:")
for i in range(p):
    baris = []
    for j in range(q):
        nilai = float(input(f"Masukkan B[{i+1}][{j+1}]: "))
        baris.append(nilai)
    B.append(baris)

while True:
    print("\nMenu Kalkulator Matriks:")
    print("1. Penjumlahan matriks"
          "\n2. Pengurangan matriks"
          "\n3. Perkalian matriks"
          "\n4. Determinan matriks (khusus 2x2)"
          "\n5. Invers matriks (khusus 2x2)"
          "\n6. Transpose matriks"
          "\n7. Keluar")
    
    pil = input("Pilih (1-7): ")
    if pil == "1" and m == p and n == q:
        for i in range(m):
            for j in range(n):
                print(A[i][j] + B[i][j], end=" ")
            print()
            
    elif pil == "2" and m == p and n == q:
        for i in range(m):
            for j in range(n):
                print(A[i][j] - B[i][j], end=" ")
            print()
            
    elif pil == "3" and n == p:
        for i in range(m):
            for j in range(q):
                s = 0
                for k in range(n):
                    s += A[i][k] * B[k][j]
                print(s, end=" ")
            print()
            
    elif pil == "4":
        for nama, M in [("A", A), ("B", B)]:
            if len(M)==2 and len(M[0])==2:
                d = M[0][0]*M[1][1] - M[0][1]*M[1][0]
                print(f"Det {nama} =", d)
                
    elif pil == "5":
        for nama, M in [("A", A), ("B", B)]:
            if len(M)==2 and len(M[0])==2:
                d = M[0][0]*M[1][1] - M[0][1]*M[1][0]
                if d == 0:
                    print(f"{nama} tak punya invers")
                else:
                    print(f"Invers {nama}:")
                    print(M[1][1]/d, -M[0][1]/d)
                    print(-M[1][0]/d, M[0][0]/d)
                    
    elif pil == "6":
        for nama, M in [("A", A), ("B", B)]:
            print(f"Transpose {nama}:")
            for i in range(len(M[0])):
                for j in range(len(M)):
                    print(M[j][i], end=" ")
                print()
                
    elif pil == "7":
        print("Terima kasih telah menggunakan kalkulator. Semoga membantu!")
        break
    else:
        print("Tidak ada di pilihan menu.")