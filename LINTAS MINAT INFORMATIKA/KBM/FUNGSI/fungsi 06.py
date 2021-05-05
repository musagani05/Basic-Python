def faktorial(bil):
    if bil == 1:
        return 1
    else:
        return (bil * faktorial(bil - 1))
input = 5
print("Faktorial dari", input, "adalah :", faktorial(input))