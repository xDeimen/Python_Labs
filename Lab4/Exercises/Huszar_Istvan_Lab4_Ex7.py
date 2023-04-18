"""
am creat un obiect de tip range cu valorile numerice intre 1 si 15 folosind functia range().
Apoi, am folosit functia filter() impreuna cu un operator lambda pentru a verifica fiecare element al acestui obiect
si a-l returna doar daca este divizibil cu 3 sau 5.
"""

divisible_by_3_or_5 = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, 16)))
print(divisible_by_3_or_5)
