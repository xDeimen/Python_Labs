'''
Am definit funcția numara_litere_p care primește un argument fisier.
Am definit două variabile: numar_p pentru a număra numărul de litere "p" din fișier și numar_P pentru a număra numărul de litere "P" din fișier.
Am folosit instrucțiunea with open(fisier, "r") as f pentru a deschide fișierul pentru citire și a îl închide automat la finalul blocului with.
Am folosit o buclă for pentru a parcurge fiecare linie din fișier.
Am folosit o altă buclă for pentru a parcurge fiecare literă din fiecare linie și, dacă litera este "p" sau "P", incrementăm variabila corespunzătoare cu 1.
La final, returnăm o tuplă care conține numărul de litere "p" și numărul de litere "P" din fișier.
'''


def numara_litere_p(fisier):
    numar_p = 0
    numar_P = 0

    with open(fisier, "r") as f:
        for linie in f:
            for litera in linie:
                if litera == "p":
                    numar_p += 1
                elif litera == "P":
                    numar_P += 1

    return [numar_p, numar_P]

out = numara_litere_p('fisier.txt')
print("Numarul de litere p: ", out[0])
print("Numarul de litere P: ", out[1])