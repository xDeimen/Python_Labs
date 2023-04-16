x = int(input("Introduceti un numar intreg pozitiv: "))
produs = 1
while x != 0:
    produs = produs * x
    x = x - 1

print("Factorialul numarului introdus este: ", produs)