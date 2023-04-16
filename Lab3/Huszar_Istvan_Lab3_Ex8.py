


#se poate face un joc similar cu scrabble
def suma_puncte(cuvant):
    #dictionar cu puncte
    punctaje = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}
    total = 0

    """
    punctaje.get(litera.lower(), 0) obține punctajul pentru fiecare literă din cuvânt. 
    Funcția lower() este utilizată pentru a asigura că literele majuscule și minuscule sunt tratate la fel, 
    iar valoarea implicită 0 este returnată dacă litera nu există în dicționar.
    """

    for litera in cuvant:
        total += punctaje.get(litera.lower(), 0)
    return total

print("Suma cuvantului mama : ", suma_puncte("mama"))
print("Suma cuvantului Robotica: ", suma_puncte("Robotica"))
print("Suma cuvantului robotica: ", suma_puncte("robotica"))
print("Suma cuvantului UTCN: ", suma_puncte("UTCN"))