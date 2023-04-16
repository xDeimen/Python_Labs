
"""
Funcția extrage_numere_pare primește o listă de numere și creează o listă nouă, numere_pare,
care va conține doar numerele pare din lista inițială.

Pentru fiecare număr din lista dată, funcția verifică dacă acesta este par sau nu. Dacă numărul este par, este adăugat în lista numere_pare.
"""

def extrage_numere_pare(lista):
    numere_pare = []
    for numar in lista:
        if numar % 2 == 0:
            numere_pare.append(numar)
    return numere_pare

list_1 = [1, 2, 3, 4, 5, 6, 7, 10]
list_2 = [1, 3, 5, 7, 11, 17, 1601, 67]

print("list_1: ", list_1)
print("list_1_pare: ", extrage_numere_pare(list_1))
print("list_2: ", list_2)
print("list_2_pare: ", extrage_numere_pare(list_2))
