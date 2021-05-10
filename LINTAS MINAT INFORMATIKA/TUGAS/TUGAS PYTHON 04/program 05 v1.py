print("USING RECURSION")

def binerkedesimal(n):
    if n == 0:
        return 0
    else:
        return (n % 10 + 2*binerkedesimal(n // 10))

biner = int(input("Masukkan Bilangan Biner : "))
print("Nilai Desimal dari", biner, "adalah", binerkedesimal(biner))