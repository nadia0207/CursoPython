#----------------------SIN USA SUPER()----------------------------------
#Mismo ejemplo llamando al constructor de la clase padre (Archivo Poo_Super2.py)

class Padre(object): #Creamos la clasePadre
    def __init__(self, ojos, cejas):
    #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas

class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas,cara): #creamos el constructor de la clase especificando atributos
        Padre.__init__(self, ojos, cejas)
        #Especificamos la clase y llamamos a su constructor + Atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo


Tomas = Hijo('Marrones', 'Negras','Larga')
print (Tomas.ojos, Tomas.cejas,Tomas.cara)