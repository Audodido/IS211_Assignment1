#Part2

class Book:

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(self.title)

book1 = Book("Will Chancellor", "7 Storeys")
book2 = Book("Andy Warhol", "Popism")

#book2.display()
print(book2.author)