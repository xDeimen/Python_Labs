"""
Mai întâi, funcția transformă textul într-o listă de cuvinte folosind metoda split().

Apoi, pentru fiecare cuvânt din listă, verifică dacă este egal cu cuvântul dat.
Dacă este, înlocuiește cuvântul cu un șir de caractere * de aceeași lungime ca și cuvântul folosind operatorul de multiplicare.

La sfârșit, funcția convertește lista de cuvinte înapoi la un șir de caractere folosind metoda join()
și returnează șirul de caractere rezultat.
"""

def inlocuieste_cuvant(text, cuvant):
    text_lista = text.split()
    for i in range(len(text_lista)):
        if text_lista[i] == cuvant:
            text_lista[i] = '*' * len(cuvant)
    return ' '.join(text_lista)


#imi era foame cand am facut testele :)
print("Textul: pizza burger cuvant astazi maine pizza burger important este text sa fie spatiu intre cuvinte pizza burger")
print(inlocuieste_cuvant("pizza burger cuvant astazi maine pizza burger important este text sa fie spatiu intre cuvinte pizza burger","pizza"))
print(inlocuieste_cuvant("pizza burger cuvant astazi maine pizza burger important este text sa fie spatiu intre cuvinte pizza burger","burger"))