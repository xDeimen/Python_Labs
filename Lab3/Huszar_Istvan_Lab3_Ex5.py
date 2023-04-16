'''
În această funcție, folosim "slicing"-ul pentru a inversa șirul de caractere.
Slicing-ul se realizează prin intermediul următorului indice: [::-1],
unde primul index reprezintă începutul intervalului de slice, al doilea index reprezintă sfârșitul intervalului de slice,
iar al treilea index este pașul de incrementare a slice-ului (în cazul nostru, -1 pentru a slice-ui în ordine inversă).
În consecință, text[::-1] va returna text în ordine inversă.
'''

def inverseaza_textul(text):
    return text[::-1]


print(inverseaza_textul("ana are mere"))
print(inverseaza_textul("Python este cool"))
print(inverseaza_textul(inverseaza_textul("Python este cool")))