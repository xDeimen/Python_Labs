"""
Solutia asta este pentru o singura valoare
Pentru mai multe valori am incercat un vector de frecventa mai jos (Dezavantaj: poate ocupa mai mult spatiu si rula pt mai mult)
"""

def contor_valoare_fixa(lista, valoare):
    count = 0
    for element in lista:
        if element == valoare:
            count += 1
    return count

def vector_de_freq(lista):
    #initializare vector freq
    a = [0 for i in range(20)]
    for element in lista:
        a[element] = a[element] + 1
    return a

list = [1, 2 ,3 , 7, 1, 2, 7, 10, 14, 8, 9]
print("Lista este: ", list)
print("Numarul de aparitii al lui 1 in lista: ", contor_valoare_fixa(list, 1))
#indicele reprezinta numarul care apare, si valoarea din vector reprezinta numarul de aparitii
print("Afiseaza numarul de aparitii pentru fiecare valoare: ", vector_de_freq(list))
