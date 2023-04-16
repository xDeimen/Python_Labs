'''
În această funcție, am folosit funcția încorporată isinstance() pentru a verifica dacă numărul este un întreg sau un float.
Dacă este un întreg, funcția va returna True imediat.
Dacă este un float, vom folosi metoda is_integer() pentru a verifica dacă partea fracționară a numărului este 0.
Dacă este 0, funcția va returna True. În orice alt caz, funcția va returna False.
'''

def este_int_float(numar):
    if isinstance(numar, int):
        return True
    elif isinstance(numar, float) and numar.is_integer():
        return True
    else:
        return False

print("5 este intreg? ", este_int_float(5))
print("3.0 este intreg? ", este_int_float(3.0))
print("10.7 este intreg? ", este_int_float(10.7))