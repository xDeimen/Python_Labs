class Animal1(object):
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal1("Hera", 2)
giraffe = Animal1("Bruce", 1)
panda = Animal1("Chad", 7)

print(zebra.name, zebra.age, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_alive)
print(panda.name, panda.age, panda.is_alive)