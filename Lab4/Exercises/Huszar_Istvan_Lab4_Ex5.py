
"""
am folosit functia filter() impreuna cu operatorul lambda pentru a verifica fiecare element al listei languages si a-l
returna numai pe cel care este egal cu "Python".
Am stocat rezultatul intr-o variabila numita filtered_languages si am afisat aceasta lista utilizand functia print().
Rezultatul va fi o lista cu un singur element: ["Python"].
"""

languages = ["HTML", "JavaScript", "Python", "Ruby"]
filtered_languages = list(filter(lambda x: x == "Python", languages))
print(filtered_languages)
