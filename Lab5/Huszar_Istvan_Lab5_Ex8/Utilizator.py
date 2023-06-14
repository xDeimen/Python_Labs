class Utilizator:
    def __init__(self, nume, email):
        self.nume = nume
        self.email = email
        self.carti_imprumutate = []

    def __str__(self):
        return f"Nume: {self.nume}\nEmail: {self.email}\nCarti Imprumutate: {self.carti_imprumutate}"

    def imprumuta_carte(self, carte):
        if(carte.disponibilitate):
            self.carti_imprumutate.append(carte)
            print("Imprumutare cu success!")
        else:
            print("Nu se poate imprumuta aceasta carte deoarece nu este disponibila.")
    def returneaza_carte(self, carte):
        self.carti_imprumutate.remove(carte)


