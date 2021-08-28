from random import choice
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
            isbn += choice(it)
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
def show(list):
    for i in range(len(list)):
        print('ISBN: {}, Title: {}, Idiom:{}'.format(list[i].isbn,list[i].title, list[i].idiom))

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


def main():

    op = -1
    while op != 0:
        op = int(input('''
        Menu de opciones:
        0 - Salir
        1 - Generacion y carga  
        2 - Mostrar el genero y el idioma del libro
        3 - Conteo y género más popular
        4 - Búsqueda del mayor
        5 - Búsqueda por ISBN
        6 - Consulta de un género
        7 - Consulta de precio por grupo
        Ingrese su opcion: 
        '''))
        if op == 1:
            auto = int(input('0 si prefiere que la carga de ISBN sea automatica, 1 para que sea manual'))
            tab = lambda x: True if x == 0 else False
            n = int(input('ingrese la cantidad de libros que desea registrar: '))
            intput_book(n, tab(auto))        
        elif op ==2:
            show(library)
        elif op ==3:
            pass
        elif op ==4:
            pass
        elif op ==5:
            i = input('ingrese isbn: ')
            print(search_isbn(i, library))
        elif op == 6:
            pass
        elif op == 7:
            pass
        elif op == 0:
            pass
        else:
            print('esa opcion no existe')
        order_gender(library)

if __name__== "__main__":
    main()