'''
În această funcție, definim o variabilă vocale care conține o serie de caractere vocale, atât în litere mici, cât și în litere mari.
Apoi, definim o variabilă vidă text_fara_vocale pentru a stoca textul fără vocale.

În blocul de buclă for, iterăm prin fiecare caracter din text.
Pentru fiecare caracter, verificăm dacă acesta este sau nu o vocală,
folosind if caracter not in vocale. Dacă caracterul nu este o vocală, îl adăugăm la text_fara_vocale cu ajutorul operatorului +=.
În final, returnăm text_fara_vocale.
'''


def elimina_vocale(text):
    vocale = "aeiouAEIOU"
    text_fara_vocale = ""
    for caracter in text:
        if caracter not in vocale:
            text_fara_vocale += caracter
    return text_fara_vocale

print("Din acest text vor fi eliminate vocalele")
print(elimina_vocale("Din acest text vor fi eliminate vocalele"))
