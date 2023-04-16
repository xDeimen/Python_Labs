import random

# Dictionar cu intrebarile si raspunsurile corespunzatoare
intrebari_si_raspunsuri = {
    "In ce an a inceput al doilea Razboi Mondial?": "1939",
    "Cate sotii a avut Henry al VIII-lea al Angliei?": "6",
    "Cati ani a durat razboiul de 100 de ani dintre Anglia si Franta?": "116",
    "Care dinastie a castigat razboiul rozelor?": "Tudor",
    "Razboiul opiului a fost date intre Mare Britanie si ____?": "China",
    "In ce an a avut loc primul Razboi Mondial?": "1914",
    "Cine a fondat studiourile Disney?": "Walt Disney",
    "Cine a scris seria de carti Harry Potter?": "J. K. Rowling"
}

# Initializare scor la 0
scor = 0

# Parcurgem dictionarul si afisam o intrebare aleatoare la fiecare runda
for i in range(len(intrebari_si_raspunsuri)):
    intrebare = random.choice(list(intrebari_si_raspunsuri.keys()))
    raspuns_corect = intrebari_si_raspunsuri[intrebare]

    # Intrebam utilizatorul si verificam raspunsul
    print("Intrebarea numarul {}: {}".format(i+1, intrebare))
    raspuns_utilizator = input("Raspunsul dumneavoastra: ")
    if raspuns_utilizator.lower() == raspuns_corect.lower():
        print("Raspunsul este corect!")
        scor += 1
    else:
        print("Raspunsul este gresit.")
        print("Raspunsul corect este:", raspuns_corect)

# Afisam scorul final
print("Jocul s-a incheiat! Scorul dumneavoastra este:", scor)
