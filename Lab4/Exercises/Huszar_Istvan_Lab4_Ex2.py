"""
Aceasta functie utilizeaza operatorul biti "si" (&) pentru a determina valoarea bitului cel mai din dreapta al lui n.
Daca acest bit este setat (adica are valoarea 1), atunci numarul de biti setati este incrementat.
Apoi, numarul n este mutat cu o pozitie spre dreapta prin operatia biti de deplasare (>>) si procesul se repeta pentru urmatorul bit.
"""


def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


numar = 4510295
print("Numarul de biti al numarului ", numar," este:", count_bits(numar))