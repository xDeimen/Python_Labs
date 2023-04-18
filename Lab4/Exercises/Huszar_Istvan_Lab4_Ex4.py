"""
Aceasta clasa Human are un constructor care primeste trei parametri: name, age si gender. Clasa contine de asemenea patru metode:

say_hello(): afiseaza un mesaj de salut cu numele si varsta omului
say_gender(): afiseaza genul persoanei
have_birthday(): incrementeaza varsta persoanei cu 1 si afiseaza un mesaj de la multi ani
introduce(): apeleaza metodele say_hello() si say_gender() pentru a se prezenta
"""


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def say_gender(self):
        print(f"I am {self.gender}.")

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age} years old.")

    def introduce(self):
        self.say_hello()
        self.say_gender()


person = Human("John", 25, "male")

person.say_hello()  # va afisa "Hello, my name is John and I am 25 years old."
person.say_gender()  # va afisa "I am male."
person.have_birthday()  # va afisa "Happy birthday! You are now 26 years old."
person.introduce()  # va afisa "Hello, my name is John and I am 26 years old. I am male."
