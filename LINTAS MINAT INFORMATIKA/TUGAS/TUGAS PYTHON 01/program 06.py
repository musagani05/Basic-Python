num1 = float(input('Masukkan Bilangan Pertama: '))
num2 = float(input('Masukkan Bilangan Kedua: '))
num3 = float(input('Masukkan Bilangan Ketiga: '))

if (num1 >= num2) and (num1 >= num3):
    terbesar = num1
elif (num2 >= num1) and (num2 >= num3):
    terbesar = num2
else:
    terbesar = num3

print('nilai terbesar =', terbesar)