class Fruit(object):
    """Un exemplu de clasa."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def descriere(self):
        print("Sunt %s %s si am gustul %s" %(self.name, self.color, self.flavor))

    def efect(self):
        if not self.poisonous:
            print("Sunt comestibila")
        else:
            print("Suntr otravitoare")


lemon = Fruit("lamaie","galbena","acru",False)
apple = Fruit("mar", "verde", "dulce", False)

lemon.descriere()
lemon.efect()
apple.descriere()
apple.efect()