def siswa(nama = "tanpa nama", umur = None):
    print("nama :",nama)
    print("umur :",umur)

def nilai(*data):
    for n in data:
        print("nilai : ", n)
    print("------------")
    rata = sum(data)/len(data)
    print("rata-rata : ",rata)

siswa(nama ="susi") #argumen default
nilai(80,78,90,95)