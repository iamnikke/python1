class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def tulosta_tiedot(self):
        print(f"Kirja: {self.name}")
        print(f"Kirjoittaja: {self.author}")
        print(f"Sivumäärä: {self.pages}")


class Magazine(Publication):
    def __init__(self, name, editor_in_chief):
        super().__init__(name)
        self.editor_in_chief = editor_in_chief

    def tulosta_tiedot(self):
        print(f"Lehti: {self.name}")
        print(f"Päätoimittaja: {self.editor_in_chief}")


# Pääohjelma

julkaisu1 = Magazine("Aku Ankka", "Aki Hyyppä")
julkaisu2 = Book("Hytti n:o 6", "Rosa Liksom", 200)

julkaisu1.tulosta_tiedot()
print("")
julkaisu2.tulosta_tiedot()