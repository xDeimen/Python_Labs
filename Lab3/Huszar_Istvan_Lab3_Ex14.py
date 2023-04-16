"""
Dacă numărul de elemente din listă este par (lungime % 2 == 0), mediana se calculează ca media aritmetică a celor două elemente din mijloc,
adică mediana = (lista[mijloc - 1] + lista[mijloc]) / 2.
Dacă numărul de elemente din listă este impar, mediana este pur și simplu elementul din mijloc, adică mediana = lista[mijloc].
"""

def mediana(lista):
    mijloc = len(lista)// 2

    if len(lista) % 2 == 0:
        mediana = (lista[mijloc - 1] + lista[mijloc]) / 2
    else:
        mediana = lista[mijloc]

    return mediana

list_1 = [1, 2, 1, 3, 5]
list_2 = [2, 60, 7, 5, 2, 7, 40, 9]

print("list1: ", list_1)
print("list1 fara duplicate: ", mediana(list_1))
print("list2: ", list_2)
print("list2 fara duplicate: ", mediana(list_2))