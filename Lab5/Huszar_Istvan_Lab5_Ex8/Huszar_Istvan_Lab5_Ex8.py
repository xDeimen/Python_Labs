from Utilizator import Utilizator
class Library:
    def __init__(self):
        self.utilizatori = []

    def __str__(self):
        print("Utilizatorii sunt: ")
        print(len(self.utilizatori))
        for i in range(len(self.utilizatori)):
            print(self.utilizatori[i])


    def add_user(self, user):
        self.utilizatori.append(user)

    def remove_user(self, user):
        self.utilizatori.remove(user)


L = Library()
u = Utilizator("Huszar","ihuszarr@gmail.com")
v = Utilizator("Mike","justin@yahoo.com")
n = Utilizator("Justin","mike@yahoo.com")
L.add_user(u)
L.add_user(v)
L.add_user(n)
L.__str__()
