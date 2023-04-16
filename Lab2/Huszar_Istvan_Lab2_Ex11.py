# primim lista de numere de la utilizator
numere = input("Introduceti numere separate prin spatiu: ")
numere = [int(x) for x in numere.split()]
# transformam sirul de caractere intr-o lista de numere intregi
suma = 0
media = 0
# calculam suma numerelor
print("Numerle pare sunt: ")
for x in numere:
    suma = suma + x
    if x % 2 == 0:
        print(" ", x)

# calculam media numerelor
media = suma / len(numere)

# filtram numerele pare din lista

# afisam suma, media si numerele pare
print("Suma numerelor este:", suma)
print("Media numerelor este:", media)
