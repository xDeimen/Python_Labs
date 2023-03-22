class Animal3(object):
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal3("Fat boy", 7)
hippo.description()
print(hippo.health)