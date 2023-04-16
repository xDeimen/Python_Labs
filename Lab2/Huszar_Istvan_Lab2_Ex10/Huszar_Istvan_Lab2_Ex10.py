# programul principal

import produse
import afisare_produse

produse.adaugare_produs('Laptop', 3000, 'electronice')
produse.adaugare_produs('Mouse', 50, 'electronice')
produse.adaugare_produs('Pantaloni', 150, 'imbracaminte')

afisare_produse.afisare_produse()
print()
print("Afisare electornice: ")

afisare_produse.afisare_produse_categorie('electronice')

produse.stergere_produs('Mouse')
print()
print("Afisare dupa stergere Mouse: ")
afisare_produse.afisare_produse()
