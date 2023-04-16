def produs(lista):
    produs = 1
    for numar in lista:
        if isinstance(numar, int):
            produs *= numar
    return produs

list_1 = [1, 2, 4 , 7, 9]
list_2 = [9, 0, 2, 6]

print("Produs lista1: ", produs(list_1))
print("Produs lista2: ", produs(list_2))