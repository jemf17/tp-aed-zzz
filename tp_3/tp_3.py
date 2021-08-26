class Libro:
    def __init__(self,isbn,title,gender,idiom,price):
        self.isbn = isbn
        self.title = title
        self.gender = gender
        self.idiom = idiom
        self.price = price
library = []
def input_book(isbn,title,gender,idiom,price):
    book = Libro(isbn,title,gender,idiom,price)
    library.append(book)
def isbn_to_accept():
    pass
