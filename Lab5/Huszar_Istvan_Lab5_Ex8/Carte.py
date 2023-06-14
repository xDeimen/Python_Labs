class Carte:
    def __init__(self, titlu, autor, editura, an_publicare, isbn, disponibilitate=True):
        self.titlu = titlu
        self.autor = autor
        self.editura = editura
        self.an_publicare = an_publicare
        self.isbn = isbn
        self.disponibilitate = disponibilitate

    def __str__(self):
        return f"Titlu: {self.titlu}\nAutor: {self.autor}\nEditura: {self.editura}\nAn Publicare: {self.an_publicare}\nISBN: {self.isbn}\nDisponibilitate: {'Disponibil' if self.disponibilitate else 'Indisponibil'}"


