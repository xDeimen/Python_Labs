class Fiinta:
    def __init__(self, poate_vorbi):
        self.poate_vorbi = poate_vorbi

    def vorbeste(self):
        if self.poate_vorbi:
            print("Buna ziua!")
        else:
            print("...")
