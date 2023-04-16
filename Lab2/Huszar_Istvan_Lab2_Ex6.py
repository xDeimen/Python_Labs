'''
Functie cu parametru de input lista de tuple (valoare_carte, culoare_carte)
Pentru fiecare valoarea unica in carti_val verificam cu count() daca avem 2 sau 3 pentru a vedea daca este vorba de o pereche sau un trio
Cazul special pentru ambele situatii este full-house atunci cand perechea si trio-ul se gasesc in acelasi timp intr-o mana
Pentru verificarea de culoare, pt fiecare culoare din mana (printr-un for) se numara cate carti sunt de acea culoare, daca sunt 5 avem culoare
Pe langa asta, o conditie extra, daca cartile ordonate sunt de forma ["10", "A", "J", "K", "Q"] atunci avem chinta roiala
'''

def verifica_mana(carti):
    #lista de tuple
    carti_val = [carte[0] for carte in carti]  # obținem lista de valori ale cărților
    carti_cul = [carte[1] for carte in carti]  # obținem lista de culori ale cărților

    # Verificăm dacă avem o pereche sau un trio
    for valoare in set(carti_val):
        if carti_val.count(valoare) == 2:  # avem o pereche
            for valoare2 in set(carti_val):
                if valoare != valoare2 and carti_val.count(valoare2) == 3:  # avem un trio
                    print("Jucătorul a câștigat o mână cu full!")  # avem un full
                    return True
            print("Jucătorul a câștigat o mână cu o pereche!")
            return True
        elif carti_val.count(valoare) == 3:  # avem un trio
            for valoare2 in set(carti_val):
                if valoare != valoare2 and carti_val.count(valoare2) == 2:  # avem o pereche
                    print("Jucătorul a câștigat o mână cu full!")  # avem un full
                    return True
            print("Jucătorul a câștigat o mână cu un trio!")
            return True

    # Verificăm dacă avem o chintă de culoare
    for culoare in set(carti_cul):
        if carti_cul.count(culoare) == 5:
            valori_carti_culoare = sorted(
                [valoare for index, valoare in enumerate(carti_val) if carti_cul[index] == culoare])
            #sunt ordonate asa pt ca sort le ordoneaza dupa cod
            if valori_carti_culoare == ["10", "A", "J", "K", "Q"]:
                print("Jucătorul a câștigat o mână cu chintă roiala!")
            else:
                print("Jucătorul a câștigat o mână cu o culoare!")
            return True

verifica_mana([("A", "inima"), ("A", "trefla"), ("K", "inima"), ("Q", "inima"), ("J", "inima")]) #Pereche 2
verifica_mana([("A", "inima"), ("A", "trefla"), ("A", "pica"), ("Q", "inima"), ("J", "inima")]) #Pereche 3
verifica_mana([("A", "inima"), ("A", "trefla"), ("A", "pica"), ("Q", "inima"), ("Q", "pica")]) #Full House
verifica_mana([("A", "caro"), ("3", "caro"), ("K", "caro"), ("Q", "caro"), ("J", "caro")]) #Culoare
verifica_mana([("10", "trefla"), ("J", "trefla"), ("Q", "trefla"), ("K", "trefla"), ("A", "trefla")]) #Chinta Roiala

