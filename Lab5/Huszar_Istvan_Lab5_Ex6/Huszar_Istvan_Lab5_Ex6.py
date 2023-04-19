import json

def citeste_tranzactii(nume_fisier):
        with open(nume_fisier, 'r') as f:
            tranzactii = f.read()
            return tranzactii

def calculeaza_total_vanzari(tranzactii, data):
    total = 0
    if data in tranzactii:
        for i in tranzactii[data]:
            total += i['suma']
    return total

def calculeaza_categorii_vandute(tranzactii, data):
    categorii = {}
    if data in tranzactii:
        for tranzactie in tranzactii[data]:
            categorie = tranzactie['categorie']
            if categorie in categorii:
                categorii[categorie] += tranzactie['cantitate']
            else:
                categorii[categorie] = tranzactie['cantitate']
    return categorii

def calculeaza_top_3(tranzactii, data):
    top = {}
    if data in tranzactii:
        for tranzactie in tranzactii[data]:
            produs = tranzactie['produs']
            if produs in top:
                top[produs] += tranzactie['cantitate']
            else:
                top[produs] = tranzactie['cantitate']
    return sorted(top.items(), key=lambda x: x[1], reverse=True)[:3]

def calculeaza_media_preturilor(tranzactii, data):
    """
    Calculeaza media preturilor pentru produsele vandute intr-o anumita zi.

    Args:
        tranzactii (dict): Dictionarul cu toate tranzactiile.
        data (str): Data pentru care se calculeaza media preturilor (format: 'dd-mm-yyyy').

    Returns:
        float: Media preturilor pentru produsele vandute in ziua respectiva.
    """
    total_preturi = 0
    total_produse = 0

    for tranzactie in tranzactii.values():
        if tranzactie['data'] == data:
            total_preturi += tranzactie['pret'] * tranzactie['cantitate']
            total_produse += tranzactie['cantitate']

    if total_produse == 0:
        return 0

    return total_preturi / total_produse

def selecteaza_tranzactii_interval(tranzactii, inceput, sfarsit):
    """
    Returnează o listă cu toate tranzacțiile din intervalul specificat.
    """
    tranzactii_interval = []
    for tranzactie in tranzactii:
        data_tranzactie = tranzactie['data']
        if inceput <= data_tranzactie <= sfarsit:
            tranzactii_interval.append(tranzactie)
    return tranzactii_interval


def genereaza_raport(tranzactii, data, nume_fisier):
    """
    Generează un raport text cu informații relevante despre tranzacțiile dintr-o anumită zi și îl salvează în fișierul
    specificat de utilizator.
    """
    # Calculează totalul vânzărilor în ziua specificată
    total_vanzari = calculeaza_total_vanzari(tranzactii)

    # Calculează categoriile de produse vândute în ziua specificată și numărul de produse vândute per categorie
    categorii_vandute = calculeaza_categorii_vandute(tranzactii)

    # Calculează cele mai vândute 3 produse din ziua specificată
    top_3_produse_vandute = calculeaza_top_3(tranzactii, data)

    # Calculează media prețurilor produselor vândute în ziua specificată
    media_preturilor = calculeaza_media_preturilor(tranzactii)

    # Generează raportul text
    raport = f"Raport pentru data de {data}\n"
    raport += f"Total vânzări: {total_vanzari:.2f} lei\n\n"
    raport += "Categorii de produse vândute:\n"
    for categorie in categorii_vandute:
        raport += f"- {categorie}\n"
    raport += "\nTop 3 cele mai vândute produse:\n"
    for i, produs in enumerate(top_3_produse_vandute, start=1):
        raport += f"{i}. {produs['denumire']} ({produs['categorie']}) - {produs['numar_vanzari']} vânzări\n"
    raport += f"\nMedia prețurilor: {media_preturilor:.2f} lei\n"

    # Salvează raportul în fișier
    try:
        with open(nume_fisier, 'w') as file:
            file.write(raport)
        print(f"Raportul pentru data de {data} a fost generat și salvat în fișierul {nume_fisier}!")
    except IOError:
        print(f"Eroare la scrierea fișierului {nume_fisier}.")

def main():
    # citirea datelor din fisier
    tranzactii = citeste_tranzactii(f'S:\III\Sem II\POO\Python_Labs\Lab5\Huszar_Istvan_Lab5_Ex6\Vanzari.txt')
    print(tranzactii)

    # afisarea totalului vanzarilor pentru o anumita zi
    zi = '2023-04-18'
    total_vanzari = calculeaza_total_vanzari(tranzactii, zi)
    print(f'Totalul vanzarilor din data de {zi} este: {total_vanzari}')

    # afisarea categoriilor de produse vandute intr-o anumita zi
    zi = '2022-03-11'
    categorii_produse = calculeaza_categorii_vandute(tranzactii, zi)
    print(f'Categoriile de produse vandute in data de {zi} sunt: {categorii_produse}')

    # afisarea numarului de produse vandute per categorie intr-o anumita zi
    zi = '2022-03-12'
    numar_produse_categorie = calculeaza_categorii_vandute(tranzactii, zi)
    print(f'Numarul de produse vandute per categorie in data de {zi} este: {numar_produse_categorie}')

    # afisarea top 3 cele mai vandute produse intr-o anumita zi
    zi = '2022-03-13'
    top_3_produse = calculeaza_top_3(tranzactii, zi)
    print(f'Top 3 cele mai vandute produse in data de {zi} sunt: {top_3_produse}')

    # afisarea mediei preturilor pentru produsele vandute intr-o anumita zi
    zi = '2022-03-14'
    media_preturilor = calculeaza_media_preturilor(zi, tranzactii)
    print(f'Media preturilor produselor vandute in data de {zi} este: {media_preturilor:.2f}')

    # afisarea tranzactiilor realizate intr-un interval de timp specificat
    data_inceput = '2022-03-11'
    data_sfarsit = '2022-03-13'
    tranzactii_interval = selecteaza_tranzactii_interval(data_inceput, data_sfarsit, tranzactii)
    print(f'Tranzactiile realizate in intervalul {data_inceput} - {data_sfarsit} sunt:')
    for tranzactie in tranzactii_interval:
        print(tranzactie)

    # generarea unui raport in format text pentru o anumita zi
    zi = '2022-03-15'
    genereaza_raport(tranzactii, zi, )
    print('Programul a fost executat cu succes!')


main()



