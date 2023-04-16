
from produse import lista_produse

def afisare_produse():
    for produs in lista_produse:
        print(f"{produs['nume']}, {produs['pret']} RON, {produs['categorie']}")

def afisare_produse_categorie(categorie_produs):
    for produs in lista_produse:
        if produs['categorie'] == categorie_produs:
            print(f"{produs['nume']}, {produs['pret']} RON")
