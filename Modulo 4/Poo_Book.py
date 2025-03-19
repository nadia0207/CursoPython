class Book():
    """
    Clase para trabajar con libros
    """
    def __init__(self, title, author = "",electronic = False):
        self.title = title
        self.author = author
        self.is_electronic = electronic

    def __del__(self):
        print("Acabas de llamar al método destructor. "
        "El objeto acaba de ser eliminado")
        
#Declaración de dos instancias de clase pasándoles
# los parámetros requeridos en el constructor.
libro = Book("Lazarillo de Tormes")
libro.title

#Para eliminar un objeto, utilizamos la palabra reservada del
del libro

#Si intentásemos acceder al objeto libro, obtendríamos error pues ha dejado de ser una
#instancia de la clase Book porque lo hemos eliminado.