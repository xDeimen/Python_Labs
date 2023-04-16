"""
În primul rând, funcția is_prime primește un argument x.
În primul rând, se verifică dacă x este mai mic decât 2, caz în care False este returnat automat pentru că 2 este cel mai mic număr prim.
Dacă x este egal sau mai mare decât 2, continuăm cu verificarea sa dacă este prim.
Se execută o buclă for care iterează prin fiecare număr întreg n începând de la 2 până la x-1.
Pentru fiecare valoare de n din bucla for, se verifică dacă x este divizibil cu n (adică x modulo n este zero).
Dacă este adevărat, atunci False este returnat deoarece x nu este prim.
Dacă x nu este divizibil cu niciun număr întreg cuprins între 2 și x-1, atunci True este returnat deoarece x este prim.
"""
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print ("13 este prim? ", is_prime(13))
print ("15 este prim? ", is_prime(15))
print ("7 este prim? ", is_prime(7))
print ("230 este prim? ", is_prime(230))