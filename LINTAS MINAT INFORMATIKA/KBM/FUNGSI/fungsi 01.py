def luas(alas, tinggi):
    """ini adalah fungsi untuk hitung luas"""
    luas = (alas*tinggi)/2
    return luas

def keliling(panjang, lebar):
    """ini adalah fungsi untuk hitung keliling"""
    keliling = 2*(panjang+lebar)
    return keliling

print("luas segitiga 1 : ",luas(5,6))
print("luas segitiga 2 : ",luas(9,7))
print("luas segitiga 3 : ",luas(19,12))

print("keliling persegi panjang : ",keliling(5,6))