total = 0 #variabel global

def jumlah(a,b):
    total = a + b #variabel lokal
    return total

jumlah(100,200) #mengisi fungsi
print("total lokal : ", jumlah(100,200))
print("total : ", total)