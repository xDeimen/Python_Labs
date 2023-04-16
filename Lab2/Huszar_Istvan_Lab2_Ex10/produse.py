
lista_produse = []

def adaugare_produs(nume_produs, pret_produs, categorie_produs):
    produs = {'nume': nume_produs, 'pret': pret_produs, 'categorie': categorie_produs}
    lista_produse.append(produs)

def stergere_produs(nume_produs):
    for produs in lista_produse:
        if produs['nume'] == nume_produs:
            lista_produse.remove(produs)
            break