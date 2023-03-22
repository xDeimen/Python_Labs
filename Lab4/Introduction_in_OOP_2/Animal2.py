class Animal2(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal2("Fat boy", 7)
hippo.description()