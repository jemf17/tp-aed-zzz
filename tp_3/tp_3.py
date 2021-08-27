import random 
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
    if isbn[0] != '-' and isbn[-1] != '-':
        return rta
    else:
        return False

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

def create_isbn():
    it = ['0','1','2','3','4','5','6','7','8','9','-']
    a = False
    isbn = ''
    while a == False:
        for i in range(14):
            isbn += random.choice(it)
        if isbn_condition_1(isbn) and isbn_condition_2(isbn) and isbn_condition_3(isbn):
            return isbn
        else:
            isbn = ''
def intput_book(n, auto):
    while n != 0:
        if auto:
            isbn = create_isbn()
        else:
            isbn = input('isbn: ')
        title = input('title: ')
        gender = input('gender: ')
        idiom = input('idiom: ')
        price = int(input('price: '))
        if isbn_condition_1(isbn) and isbn_condition_2(isbn) and isbn_condition_3(isbn):
            register_book(isbn,title,gender,idiom,price)
            n -= 1
        else:
            print('el isbn no es valido')
n = int(input('numero de libros a agregar: '))
intput_book(n, True)



def order_gender(v):
    n = len(v)
    for i in range(n-1):
        ordenado = True
        for j in range(n-i-1):
            if v[j].title[0].lower() > v[j+1].title[0].lower():
                ordenado = False
                v[j].title, v[j+1].title = v[j+1].title, v[j].title
            if ordenado:
                break
order_gender(library)
def show(list):
    for i in range(len(list)):
        print('ISBN: {}, Title: {}, Idiom:{}'.format(list[i].isbn,list[i].title, list[i].idiom))
show(library)

def search_isbn(isbn, vec):
    price = lambda p: p+(p/10)
    pos = 0
    for i in range(len(vec)):
        if vec[i].isbn == isbn:
            pos = i
            break
    if vec[pos].isbn == isbn:       
        return 'ISBN:{}, Title: {}, Gender:{}, Idiom:{}, Price:{}'.format(vec[pos].isbn,vec[pos].title,vec[pos].gender,vec[pos].idiom,price(vec[pos].price))
    else:
        return 'no se encontro :('
i = input('ingrese isbn: ')

print(search_isbn(i, library))