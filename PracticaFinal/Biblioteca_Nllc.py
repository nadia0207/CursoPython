# Creación de la clase Libro
class Libro():
    def __init__(self,titulo,autor,isbn,disponible=True):
        #Definimos los Atributos
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
    
    #Definimos los metodos de la clase
    def agregar(self,titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
           
    def prestar(self, isbn):
        return
        
    def devolver(self,isbn):
        return
    
    def mostrar(self):
        print("Titulo:",self.titulo)
        print("Autor:", self.autor)
        print("ISBN:",self.isbn)
        if(self.disponible == True):
            print("Disponible: SI")
        else:
            print("Disponible: NO")
        print("*******************************")

    def buscar(self, isbn):
        if (self.isbn == isbn):
            self.mostrar()
        else:
            print("NO EXISTE ISBN")


#Creamos instancia a la clase Libro
miLibro = Libro('100 AÑOS DE SOLEDAD','GABRIEL G. MARQUEZ','42444448')
miLibro.agregar('TRADICIONES PERUANAS','RICARDO PALMA','45412541')
miLibro.mostrar()
miLibro.buscar('4444')
miLibro.buscar('45412541')



    
