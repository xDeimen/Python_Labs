
"""
Se defineste un set predefinit de litere corespunzatoare pentru fiecare litera a alfabetului, in cadrul unei chei secrete.
Se citeste textul de la tastatura.
Pentru fiecare litera din text, se inlocuieste cu litera corespunzatoare din cheia secreta.
Se salveaza textul criptat intr-un fisier.
Pentru a decripta textul, se va folosi aceeasi cheie secreta si se vor inversa operatiile:

Se citeste textul criptat din fisier.
Pentru fiecare litera din text, se inlocuieste cu litera corespunzatoare din cheia secreta.
Se afiseaza textul decriptat la consola.
"""

# Cheia secreta
key = {'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'}

# Functie pentru criptarea unui text dat
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char in key:
            encrypted_text += key[char]
        else:
            encrypted_text += char
    return encrypted_text

# Functie pentru decriptarea unui text dat
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char in key.values():
            for k, v in key.items():
                if v == char:
                    decrypted_text += k
        else:
            decrypted_text += char
    return decrypted_text

# Criptarea unui text si salvarea acestuia intr-un fisier
text = input("Introduceti textul de criptat: ").lower()
encrypted_text = encrypt(text, key)

"""
Utilizarea sintaxei "with open as f" ofera o modalitate mai sigura si mai eficienta de a deschide un fisier si de a-l manipula. 
In aceasta sintaxa, Python va automatiza procesul de inchidere a fisierului, 
astfel incat sa nu mai fie necesara apelarea metodei close() explicit. 
Acest lucru se realizeaza prin utilizarea unui context, care este definit prin blocul "with".

In acest exemplu, "nume_fisier.txt" este numele fisierului pe care dorim sa-l deschidem, iar "r" este modul de deschidere, 
care specifica ca dorim sa citim din fisier. Variabila "f" este variabila prin care putem accesa fisierul deschis
"""

with open("text_criptat.txt", "w") as f:
    f.write(encrypted_text)

# Decriptarea textului din fisier
with open("text_criptat.txt", "r") as f:
    encrypted_text = f.read()
decrypted_text = decrypt(encrypted_text, key)
print("Textul decriptat este:", decrypted_text)
