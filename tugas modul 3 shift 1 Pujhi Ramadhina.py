print ("\nPERMAINAN TEBAK ANGKA BOM")
print("pemain 1")
n = int(input("pilih angka positif sampai berapa : "))
k = int(input("Angka bom: "))
print("\nderetan angka : ")
i = 1
output = ""
while i <= n  :
    if i % k == 0 :
        output += "BOM "
    else :
        output += str(i) + " "
    i += 1
print (output)  
print ("\npemain 2")
for i in range (n) :
    tebak = int(input(f"tebak angka dari 1 - {n} : "))
    if tebak < 1 or tebak > n :
        print(f"angka harus antara 1 dan {n}, coba lagi!")
        continue
    elif tebak % k == 0 :
        print(f"angka {tebak} adalah bom, anda kalah!")
        break
    else :
        print(f"angka {tebak} bukan bom, anda menang!!")
        break
print ("\nPERMAINAN SELESAI")