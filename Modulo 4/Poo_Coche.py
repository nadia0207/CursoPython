#Declaracion de la clase
class Coche():
    largo = 250 #Declaracion de los atributos
    ancho = 120
    ruedas = 4
    peso = 900
    color = "rojo"
    is_enMarcha = False

    #Declaracion de métodos
    def arrancar(self): #self hace referencia a la instancia de la clase
        self.is_enMarcha = True  #Es como si pusieramos miCoche.is_enMarca = True
    
    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancando"
        else:
            return "El coche está parado"
            
#Declaracion de una instancia de clase, objeto de clase o ejemplar de clase.
miCoche = Coche()
miCoche2 = Coche()

#Acceso a un atributo de la clase coche.
print("El largo del coche es de", miCoche.largo, "cm.")
print(miCoche.estado())

#Acceso a un metodo de la clase Coche. 
#Nomenclatura del punto.
print("El coche esta arrancando;",miCoche2.arrancar())

#Modificar el valor de una propiedad
miCoche2.ruedas = 10
print("El coche tiene:",miCoche2.ruedas, "ruedas" )