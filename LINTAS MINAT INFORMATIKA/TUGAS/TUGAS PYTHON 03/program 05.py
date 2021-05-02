#Definisi Fungsi
def penjumlahan(*vartuple):
    print("Jumlahnya adalah : ")
    jumlah = 0
    for var in vartuple:
        jumlah = jumlah + var
    print(jumlah)

def rata(*vartuple):
    print("Rata-rata adalah : ")
    rerata = 0
    tot = 0
    for var in vartuple:
        tot = tot + var
    rerata = tot / len(vartuple)
    print(rerata)
#Empat Argumen
penjumlahan(10, 30, 50, 70)
rata(10, 30 , 50, 70)