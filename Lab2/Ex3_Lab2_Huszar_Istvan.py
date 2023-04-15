'''
Am definit funcția numara_info_text care primește un argument text.
Am definit trei variabile:
-cuvinte_python pentru a număra numărul de cuvinte "Python",
-spatii_libere pentru a număra numărul total de spații libere și
-caractere_totale pentru a număra numărul total de caractere din text.
Am folosit o buclă for pentru a parcurge fiecare cuvânt din textul dat. Dacă cuvântul este "Python", incrementăm cuvinte_python cu 1.
Am folosit o altă buclă for pentru a parcurge fiecare caracter din text și, dacă caracterul este un spațiu liber, incrementăm spatii_libere cu 1.
La final, returnăm o tuplă care conține numărul de cuvinte "Python", numărul total de spații libere și numărul total de caractere din text.
'''

def numara_info_text(t):

    cuvinte_python = 0
    spatii_libere = 0
    caractere_totale = len(t)

    for cuvant in t.split():
        if cuvant == "Python" or cuvant == "Python,":
            cuvinte_python += 1

    for caracter in t:
        if caracter == " ":
            spatii_libere += 1

    return [cuvinte_python, spatii_libere, caractere_totale]

text = "In Python, any line that begins with a hash mark (#) " \
       "is known as a comment and is ignored by the Python interpreter. " \
       "Comments are intended to allow programmers to communicate with one another " \
       "(or to remind themselves of what their code does when they sit down with it a few months later). " \
       "In a larger sense, programs themselves are typically written and formatted in a way " \
       "that makes it easier for programmers to communicate with one another. " \
       "Code that is closer to the requirements of the machine is referred to as low-level, " \
       "whereas code that is closer to natural language is high-level. " \
       "One of the benefits of using a language like Python is that it is very high-level, " \
       "making it easier for us to communicate with you (at some cost in terms of computational efficiency)."

rezultat = numara_info_text(text)
print("Aparitii Python: ", rezultat[0])
print("Aparitii spatii libere: ", rezultat[1])
print("Caractere totale: ", rezultat[2])
