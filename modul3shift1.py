n = int(input("masukkan nilai n : " ))
i = 1
x = 0
for i in range (1, n+1) :
    if i % 7 == 0 :
        x = x + 1
        print(f'banyaknya kelipatan 7 adalah {x}')
        