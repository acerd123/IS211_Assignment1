
class Book:
    def __init__(self, author, title):
        """

        Constructor of a Book class

        :param author: The author of the book
        :param title: The title of the book
        """
        self.author = author
        self.title = title
    
    def display(self):
        """Display the Book's author title"""
        print(f"{self.title} written by {self.author}")
        

if __name__ == "__main__":
    book1 = Book("JK. Rowling", "Harry Potter and the Goblet of Fire")
    book2 = Book("Walter Scott", Ivanhoe: A Romance")

    book1.display()
    book2.display()
