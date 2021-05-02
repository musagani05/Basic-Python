bil = int(input('bilangan : '))

if bil > 0:
    if bil % 2 == 0:
        print('bilangan genap')
    else:
        print('bilangan ganjil')
else:
    print('bilangan negatif atau nol')
    