#Part2

class Book:
    """
    A class to represent a book

    Attributes:
        author (string): Name of the author
        title (string): Title of the book
        
    """
    def __init__(self, author, title):
        """
        Constructs all the necessary attributes for the Book object.
    
        """
        self.author = author
        self.title = title

    def display(self):
        """
    Returns:
        (string) message containing the book's author and title
        
        """
        print(self.title + ", written by " + self.author)

book1 = Book("John Steinbeck", "Of Mice and Men")
book2 = Book("Harper Lee", "To Kill a Mockingbird")


book1.display()
book2.display()
# print(book2.author)