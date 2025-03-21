# Creación de la clase Libro
class Libro():
    #Creamos el constructor 
    def __init__(self,titulo,autor,isbn):
    #Definimos los Atributos
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
    
    #Definimos los metodos de la clase
    @staticmethod #metodo estatico que no se instancia la clase no usa self
    def agregar(titulo, autor, isbn, biblioteca): 
        nuevo_libro = Libro(titulo, autor, isbn)
        biblioteca.append(nuevo_libro)
        print("Libro agregado con éxito.")

    # Método para prestar un libro      
    def prestar(self):
        if self.disponible == True:
            self.disponible = False
            print("Libro prestado con éxito")
        else:
            print("Libro ya esta prestano, No disponible")           
    
    # Método para devolver un libro
    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            print("Libro devuelto correctamente")
        else:
            print("El libro esta disponible")

    # Método para mostrar la información de un libro
    def mostrar(self):
        estado = "Si" if self.disponible else "No"
        return f"-{self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}"
    
    # Función para buscar un libro por ISBN en la biblioteca
    @staticmethod
    def buscar(isbn, biblioteca):
        for libro in biblioteca:
            if libro.isbn == isbn:
                print(libro.mostrar())
                return
        else:
            print("Libro no encontrado.") 
        
# Función para mostrar todos los libros de la biblioteca
def mostrar_libros(biblioteca):
    if not biblioteca:
        print("No hay libros en la biblioteca.")
    else:
        for libro in biblioteca:
            print(libro.mostrar())
   
#------------------------------------------------------------
# Función principal que muestra el menú de opciones
def menu():
    biblioteca = []  # Lista para almacenar los libros
    while True:
        # Mostrar menú de opciones
        print("\nBienvenido al Sistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":  # Agregar un nuevo libro
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            Libro.agregar(titulo, autor, isbn, biblioteca)
        
        elif opcion == "2":  # Prestar un libro por ISBN
            isbn = input("Ingresa el ISBN: ")
            #La función next() devuelve el primer elemento de la expresión generadora.
            #Si no encuentra el libro, devuelve None, evitando errores.
            libro = next((l for l in biblioteca if l.isbn == isbn), None)
            if libro:
                libro.prestar()
            else:
                print("Libro no encontrado.")
        
        elif opcion == "3":  # Devolver un libro por ISBN
            isbn = input("Ingresa el ISBN: ")
            libro = next((l for l in biblioteca if l.isbn == isbn), None)
            if libro:
                libro.devolver()
            else:
                print("Libro no encontrado.")
        
        elif opcion == "4":  # Mostrar todos los libros disponibles
            mostrar_libros(biblioteca)
        
        elif opcion == "5":  # Buscar un libro por ISBN
            isbn = input("Ingresa el ISBN: ")
            Libro.buscar(isbn, biblioteca)
        
        elif opcion == "6":  # Salir del programa
            print("Saliendo del sistema...")
            break
        
        else:  # Manejo de opciones inválidas
            print("Opción inválida. Inténtalo de nuevo.")

# Ejecutar el menú si el script se ejecuta directamente
if __name__ == "__main__":
    menu()