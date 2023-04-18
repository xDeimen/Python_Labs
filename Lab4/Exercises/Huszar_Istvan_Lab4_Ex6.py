
"""
am folosit functia filter() impreuna cu un operator lambda pentru a verifica fiecare element al listei squares si a-l
returna doar daca este intre 30 si 70. Am stocat rezultatul filtrarii intr-o variabila numita filtered_squares si am
afisat aceasta lista utilizand functia print().
"""

squares = [x ** 2 for x in range(1, 11)]
print("Patrate: ", squares)
filtered_squares = list(filter(lambda x: x >= 30 and x <= 70, squares))
print("Lista finala: ", filtered_squares)
