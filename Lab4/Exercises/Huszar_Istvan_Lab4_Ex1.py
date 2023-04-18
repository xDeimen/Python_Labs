"""
Functia map este utilizata pentru a aplica functia lambda la fiecare element din lista carti.
Functia lambda calculeaza valoarea comenzii pentru fiecare carte si returneaza un tuplu care contine numarul de ordine al cartii si valoarea comenzii.
Daca valoarea comenzii este mai mica de 100 €, pretul comenzii este marit cu 10 €, conform cerintei din enunt.
"""

carti = [
    (34587, "Learning Python", "Mark Lutz", 4, 40.95),
    (98762, "Programming Python", "Mark Lutz", 5, 56.80),
    (77226, "Head First Python", "Paul Barry", 3, 32.95),
    (88112, "Einführung in Python3", "Bernd Klein", 3, 24.99)
]

valoare_comenzi = list(map(lambda c: (c[0], (c[3] * c[4]) if (c[3] * c[4]) >= 100 else (c[3] * c[4] + 10)), carti))

print(valoare_comenzi)
