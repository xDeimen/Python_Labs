# Ex 1
class robotica:
    def __init__(self):
        print("ROBOTICA")
obiect_robotica = robotica()
print("\n")
# -----------------------------------------
# Ex 2
class inginer:
    IR=type('inginer',(),{})()
    IR.__class__.__str__ = lambda self: "Inginer robotician"
    print(IR)
print("\n")
# ------------------------------------------
# Ex 3
class student:
    def __init__(self, an_studii, nume):
        self.an_studii = an_studii
        self.nume = nume


studentul_meu = student(1, "John Doe")

print(f"An de studii: {studentul_meu.an_studii}")
print(f"Nume: {studentul_meu.nume}")

studentul_meu.an_studii = 2

print(f"An de studii actualizat: {studentul_meu.an_studii}")

print("\n")
# ------------------------------------------
# Ex 4
class student:
    def __init__(self, an_studii, nume):
        self.an_studii = an_studii
        self.nume = nume

studentul_meu = student(1, "John Doe")

del studentul_meu.an_studii

#print(f"An de studii: {studentul_meu.an_studii}")
print(f"Nume: {studentul_meu.nume}")

studentul_meu = student(1, "John Doe")

del studentul_meu

#print(studentul_meu)

print("\n")
# ------------------------------------------
# Ex 5
class student:
    def __init__(self, an_studii, nume):
        self.an_studii = an_studii
        self.nume = nume

class student_modificat(student):
    def __init__(self, stare, nume):
        self.stare = stare
        self.nume = nume

studentul_meu = student_modificat('absolvent', 'John Doe')

print(f"Stare: {studentul_meu.stare}")
print(f"Nume: {studentul_meu.nume}")

print("\n")
# ------------------------------------------
# Ex 6
class ClasaA:
    pass
class ClasaB:
    pass

obiect1 = ClasaA()
obiect2 = ClasaB()

if isinstance(obiect1, ClasaA) and isinstance(obiect2, ClasaA):
    print("Ambele obiecte sunt de acelasi tip")
else:
    print("Obiectele nu sunt de acelasi tip")

print("\n")
# ------------------------------------------
# Ex 7
class ObiectSursa:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

obiect_sursa = ObiectSursa("John Doe", 30)

obiect_destinatie = ObiectSursa("", 0)

proprietati_sursa = vars(obiect_sursa)
for atribut, valoare in proprietati_sursa.items():
    setattr(obiect_destinatie, atribut, valoare)

print(f"Nume obiect sursă: {obiect_sursa.nume}, Varsta obiect sursă: {obiect_sursa.varsta}")
print(f"Nume obiect destinație: {obiect_destinatie.nume}, Varsta obiect destinație: {obiect_destinatie.varsta}")

print("\n")
# ------------------------------------------
# Ex 8
class Exemplu:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def metoda(self):
        pass

obiect = Exemplu("John Doe", 30)
atribute = dir(obiect)
print(atribute)
proprietati = vars(obiect).keys()
print(proprietati)

print("\n")
# ------------------------------------------
# Ex 9
class robotica:
    pass
setattr(robotica, "tip_roboti", ["robot1", "robot2", "robot3"])
setattr(robotica, "producatori", ["producator1", "producator2", "producator3"])
print(robotica.tip_roboti)
print(robotica.producatori)

print("\n")
# ------------------------------------------
# Ex 10
class student:
    def __init__(self, an_studii, nume):
        self.an_studii = an_studii
        self.nume = nume
class student:
    def __init__(persoana, an_studii, nume):
        persoana.an_studii = an_studii
        persoana.nume = nume
class student1:
    def __init__(self, an_studii, nume):
        self.an_studii = an_studii
        self.nume = nume
student1_obj = student1(1, "John Doe")
print(student1_obj.an_studii)
print(student1_obj.nume)
class student2:
    def __init__(persoana, an_studii, nume):
        persoana.an_studii = an_studii
        persoana.nume = nume
student2_obj = student2(2, "Jane Smith")
print(student2_obj.an_studii)
print(student2_obj.nume)

print("\n")
# ------------------------------------------
# Ex 11
class student:
    def __init__(self, universitatea, an_studii, nume):
        self.__universitatea = universitatea
        self.an_studii = an_studii
        self.nume = nume

    def get_universitatea(self):
        return self.__universitatea

    def set_universitatea(self, universitatea):
        raise AttributeError("Modificarea stării universității nu este permisă.")

    universitatea = property(get_universitatea, set_universitatea)

print("\n")
# ------------------------------------------
# Ex 12

class student:
    universitate = "NumeUniversitate"

    def __init__(self, an_studii, nume):
        self.an_studii = an_studii
        self.nume = nume

print(student.universitate)
studentul_meu = student(1, "John Doe")

print(f"An de studii: {studentul_meu.an_studii}")
print(f"Nume: {studentul_meu.nume}")
print(f"Universitate: {student.universitate}")

print("\n")
# ------------------------------------------
# Ex 13

class student('''invatamant_tertiar'''):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

print("\n")
# ------------------------------------------
# Ex 14

class student:
    def __init__(self, n):
        self._nume = []
        for i in range(0, n):
            s = input("Introdu un nume: ")
            self._nume.append(s)

    def __call__(self, t):
        self._date = []
        for k in range(0, t):
            s = input("Introdu un nume: ")
            self._date.append(s)

s1 = student(3)
print(s1._nume)

s1(2)
print(s1._date)

print("\n")
# ------------------------------------------
# Ex 15

class robot_fix:
    def __init__(self, model):
        self.model = model

    def move(self):
        print("Robot fix nu se poate deplasa.")

    def display(self):
        print(f"Model robot fix: {self.model}")


class robot_mobil:
    def __init__(self, model):
        self.model = model

    def move(self):
        print("Robot mobil se poate deplasa.")

    def display(self):
        print(f"Model robot mobil: {self.model}")


class robot:
    def __new__(cls, baza, *args, **kwargs):
        if baza == "fixa":
            return robot_fix(*args, **kwargs)
        else:
            return robot_mobil(*args, **kwargs)


print("\n")
# ------------------------------------------
# Ex 16

class Incrementare:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            current = self.start
            self.start += 1
            return current
        else:
            raise StopIteration

a = 0
b = 5

print("Utilizând range:")
for x in range(a, b):
    print("robotica")
print("Utilizând clasa Incrementare:")
for x in Incrementare(a, b):
    print("robotica")

print("\n")
# ------------------------------------------
# Ex 17

class Inversare:
    def __init__(self, cuvant):
        self.cuvant = cuvant
        self.index = len(cuvant)

    def __iter__(self):
        return self

    def __reversed__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.cuvant[self.index]
        else:
            raise StopIteration


cuvant = input("Introduceți un cuvânt: ")
invers = Inversare(cuvant)

print("Inversul cuvântului:")
for litera in invers:
    print(litera, end="")

print("\nInversul cuvântului utilizând reversed:")
for litera in reversed(invers):
    print(litera, end="")


print("\n")
# ------------------------------------------
# Ex 18

class Afisare:
    def __init__(self, dimensiune):
        self.dimensiune = dimensiune
        self.elemente = [''] * dimensiune

    def __getitem__(self, index):
        return self.elemente[index]

    def __setitem__(self, index, valoare):
        self.elemente[index] = valoare


indice = Afisare(4)
indice[0] = 'robot mobil'
indice[1] = 'robot serial'
indice[2] = 'robot paralel'
indice[3] = 'robot pentru servicii'

print("Elementele din indice:")
for i in range(4):
    print(indice[i])


print("\n")
# ------------------------------------------
# Ex 19

class Student:
    def __init__(self, atribute):
        self.atribute = atribute

    def __getattr__(self, nume_atribut):
        if nume_atribut in self.atribute:
            return self.atribute[nume_atribut]
        else:
            raise AttributeError(f"Atributul '{nume_atribut}' nu există.")

    def __setattr__(self, nume_atribut, valoare):
        if hasattr(self, "atribute") and nume_atribut in self.atribute:
            self.atribute[nume_atribut] = valoare
        else:
            super().__setattr__(nume_atribut, valoare)


MP = Student({'an_studii': 2, 'nume': 'Mihai Pop'})

print(MP.an_studii)
print(MP.nume)
#print(MP.data)

MP.nota = 10
print(MP.nota)


print("\n")
# ------------------------------------------
# Ex 20

class Student:
    def __init__(self, nume):
        self.nume = nume

    def __del__(self):
        print(f"Obiectul Student cu numele '{self.nume}' a fost distrus.")


SM = Student('Mihai Pop')
print(SM)
SM = 'Dan Pop'
print(SM)

print("\n")
# ------------------------------------------
# Ex 21

class MyClass:
    def __init__(self, public_var, private_var):
        self.public_var = public_var
        self.__private_var = private_var

    def public_method(self):
        print("Aceasta este o metodă publică")
        self.__private_method()

    def __private_method(self):
        print("Aceasta este o metodă privată")

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, new_value):
        self.__private_var = new_value

print("\n")
# ------------------------------------------
# Ex 22
   # Incapsularea
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

   # Agregarea
class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

employee1 = Employee("John", "Manager")
employee2 = Employee("Jane", "Developer")

department = Department("IT Department", [employee1, employee2])

    # Compozitia
class Car:
    def __init__(self, engine):
        self.engine = engine

class Engine:
    def __init__(self, capacity):
        self.capacity = capacity

engine = Engine(2000)
car = Car(engine)


print("\n")
# ------------------------------------------
# Ex 23
    # Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog("Buddy")
dog.eat()
dog.bark()
    # Multiple Inheritance
class Bird:
    def fly(self):
        print("Flying...")

class Mammal:
    def walk(self):
        print("Walking...")

class Bat(Bird, Mammal):
    pass

bat = Bat()
bat.fly()
bat.walk()