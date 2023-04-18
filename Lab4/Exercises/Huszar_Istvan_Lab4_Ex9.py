"""
random pentru a genera doua numere aleatoare, intre 1 si numarul maxim de pe fetele zarului
(6 pentru un zar cu 6 fete, 12 pentru un zar cu 12 fete, etc).
Apoi, putem cere utilizatorului sa introduca un numar intre 1 si numarul maxim posibil si sa comparam suma
celor doua numere generate cu numarul introdus. Daca numarul introdus este mai mare sau egal cu suma celor
doua numere generate, atunci afisam ca utilizatorul a castigat, altfel afisam ca a pierdut.
"""

import random

# generam doua numere aleatoare intre 1 si 6 (pentru un zar cu 6 fete)
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

# calculam suma celor doua aruncari
dice_sum = dice1 + dice2

# cerem utilizatorului sa introduca un numar intre 1 si 6
max_num = 6
user_num = int(input(f"Introdu un numar intre 1 si 12: "))

# comparam numarul introdus cu suma celor doua aruncari
if user_num >= dice_sum:
    print(f"Ai castigat! Ai aruncat {dice1} si {dice2} si suma este {dice_sum}.")
else:
    print(f"Ai pierdut! Ai aruncat {dice1} si {dice2} si suma este {dice_sum}.")
