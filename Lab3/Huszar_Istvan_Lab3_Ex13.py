"""
Funcția elimina_duplicate primește o listă de elemente și returnează o listă nouă care
conține aceleași elemente ca lista inițială, dar fără instanțe care au valori identice.

Variabila lista_noua este inițializată cu o listă goală.

Pentru fiecare element din lista dată, funcția numără câte instanțe există în lista inițială.
Dacă numărul este egal cu 1, înseamnă că elementul nu are duplicat și poate fi adăugat la lista nouă.
"""

def elimina_duplicate(lista):
    lista_noua = []
    for element in lista:
        if lista.count(element) == 1:
            lista_noua.append(element)
    return lista_noua

list_1 = [1, 2, 1, 3]
list_2 = [2, 60, 7, 5, 2, 7, 40, 9]

print("list1: ", list_1)
print("list1 fara duplicate: ", elimina_duplicate(list_1))
print("list2: ", list_2)
print("list2 fara duplicate: ", elimina_duplicate(list_2))
