def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-2) + fibo(n-1))

deret = 1

if deret <= 0:
    print("Masukkan bilangan positif")
else:
    print("Deret fibo")
    for i in range(deret):
        print(fibo(i), end=' ')