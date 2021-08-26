class Libro:
    def __init__(self,isbn,title,gender,idiom,price):
        self.isbn = isbn
        self.title = title
        self.gender = gender
        self.idiom = idiom
        self.price = price
library = []
def register_book(isbn,title,gender,idiom,price):
    book = Libro(isbn,title,gender,idiom,price)
    library.append(book)
def isbn_condition_1(isbn):
    cont = 0
    for i in isbn:
        if i == '-':
            cont += 1
    if cont == 3:
        return True
    else :
        return False

def isbn_condition_2(isbn):
    rta = True
    cont = 0
    for i in isbn:
        if i == '-' and isbn[cont-1] == '-':
            rta = False
        cont += 1
    return rta

def isbn_condition_3(isbn):
        expo = 10
        rta = 0
        for i in isbn:
            if i != '-' and i != ' ':
                rta += int(i)*expo
                expo -= 1
        if rta % 11 == 0:
            return True
        else :
            return False

def intput_book(n):
    while n != 0:
        isbn = input('isbn: ')
        title = input('title: ')
        gender = input('gender: ')
        idiom = input('idiom: ')
        price = input('price: ')
        if isbn_condition_1(isbn) and isbn_condition_2(isbn) and isbn_condition_3(isbn):
            register_book(isbn,title,gender,idiom,price)
            n -= 1
        else:
            print('el isbn no es valido')

n = int(input('numero de libros a agregar: '))
intput_book(n)
 
print(library[0].title, library[0].isbn)