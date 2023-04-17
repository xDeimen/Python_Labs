
"""
Aceasta aplicatie utilizeaza biblioteca cryptography pentru a genera si utiliza cheia de criptare.
Functia generare_cheie genereaza o cheie de criptare dintr-o parola data, utilizand algoritmul Fernet.
Functia criptare cripteaza un text folosind o cheie de criptare data si functia decriptare decripteaza un text criptat folosind o cheie de criptare data.

In aplicatia principala, citim parola de la tastatura si generam cheia de criptare utilizand functia generare_cheie.
Apoi, afisam optiunile disponibile pentru operator si citim optiunea de la tastatura.
"""

import base64
from cryptography.fernet import Fernet

def generare_cheie(parola):
    """Genereaza o cheie de criptare dintr-o parola data."""
    b_parola = parola.encode()
    b_cheie = base64.urlsafe_b64encode(b_parola)
    return Fernet(b_cheie)

def criptare(text, cheie):
    """Cripteaza un text folosind o cheie de criptare data."""
    b_text = text.encode()
    b_text_criptat = cheie.encrypt(b_text)
    return b_text_criptat

def decriptare(b_text_criptat, cheie):
    """Decripteaza un text criptat folosind o cheie de criptare data."""
    b_text = cheie.decrypt(b_text_criptat)
    text = b_text.decode()
    return text

# citim parola de la tastatura
parola = input("Introduceti o parola pentru generarea cheii de criptare: ")

# generam cheia de criptare
cheie = generare_cheie(parola)

# afisam optiunile disponibile pentru operator
print("Alegeti optiunea:")
print("1. Criptare")
print("2. Decriptare")
optiune = input("Optiunea dvs: ")

if optiune == "1":
    # citim textul de la tastatura
    text = input("Introduceti textul de criptat: ")
    # criptam textul
    b_text_criptat = criptare(text, cheie)
    # scriem textul criptat intr-un fisier
    with open("criptat.txt", "wb") as f:
        f.write(b_text_criptat)
    print("Textul a fost criptat si salvat in fisierul 'criptat.txt'.")
elif optiune == "2":
    # citim textul criptat din fisier
    with open("criptat.txt", "rb") as f:
        b_text_criptat = f.read()
    # decriptam textul
    text_decriptat = decriptare(b_text_criptat, cheie)
    # afisam textul decriptat
    print("Textul decriptat este:")
    print(text_decriptat)
else:
    print("Optiune invalida.")
