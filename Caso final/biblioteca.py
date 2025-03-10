import sys

# Lista de los libros existentes en la biblioteca
libros_biblioteca = []

class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
    
    def agregar(self, new_title, new_autor, new_isbn, disponible):
        # Verificar se el libro ya existe en la biblioteca
        for libro in libros_biblioteca:
            if libro.isbn == new_isbn:
               return print("No es posible agregar libro, ya se encuentra en la biblioteca")
        # Añadir nuevo libro a la biblioteca
        libro = Libro(new_title, new_autor, new_isbn, disponible)
        libros_biblioteca.append(libro)
        print("\n")
        print("Título:", new_title)
        print("Autor:", new_autor)
        print("ISNB:", new_isbn)
        return print("Libro agregado con éxito.")

    def prestar(self, input_isbn):
        for libro in libros_biblioteca:
            if libro.isbn == input_isbn:
                if libro.disponible:
                    libro.disponible = False
                    return print("Libro prestado con éxito.")
                else:
                    return print("El libro no esta disponible.")
        return print("ISBN no encontrado.")

    def devolver(self, input_isbn):
        for libro in libros_biblioteca:
            if libro.isbn == input_isbn and libro.disponible == False:
                libro.disponible = True
                return print("Libro devuelto con exito.")
            if libro.isbn == input_isbn:
                return print("No se puede devolver, libro no prestado.")
        return print("ISBN no encontrado.")

    def mostrar(self):
        for libro in libros_biblioteca:
            disponible = "Sí" if libro.disponible else "No"
            print("- {} ({}) - ISBN:{} - Disponible:{}".format(libro.titulo, libro.autor, libro.isbn, disponible))

    def buscar(self, input_isbn):
        for libro in libros_biblioteca:
            if libro.isbn == input_isbn:
                disponible = "Sí" if libro.disponible else "No"
                print("\n")
                print("Título:", libro.titulo)
                print("Autor:", libro.autor)
                print("ISNB:", libro.isbn)
                print("Disponible:", disponible)
                return ()
        return print("ISBN no encontrado")

# Loop para usuario
while True:
    # Menu de funcionalidades
    print("\n")
    print("Bienvenido al Sistema de Gestión de Biblioteca")
    print("\n")
    print("1. Agegar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar")
    print("6. Salir")
    print("\n")
    opcion = input("Elige una opción:")

    if opcion == "1":
        new_title = input("Introduzca el titulo: ")
        new_autor = input("Introduzca el autor: ")
        new_isbn = input("introduzca ISBN: ")
        libro = Libro(new_title, new_autor, new_isbn)
        libro.agregar(new_title, new_autor, new_isbn, disponible=True)
    elif opcion == "2":
        input_isbn = input("Introduzca ISBN:")
        libro.prestar(input_isbn)
    elif opcion == "3":
        input_isbn = input("Introduzca ISBN:")
        libro.devolver(input_isbn)
    elif opcion == "4":
        libro.mostrar()
    elif opcion == "5":
        input_isbn = input("Introduzca ISBN:")
        libro.buscar(input_isbn)
    elif opcion == "6":
        print("Saliendo del programa...")
        sys.exit()
    else:
        print("Opción no diponible")

        