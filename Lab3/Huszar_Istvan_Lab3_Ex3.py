x = int(input("Introduceti un numar: "))
suma = 0
while x != 0:
    suma = suma + x%10
    x = int(x/10)

print("Suma cifrelor numarului este: ", suma)