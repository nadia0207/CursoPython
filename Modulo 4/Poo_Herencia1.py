
class Vehiculo():

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.Color = "negro"
        self.arrancado = False
        self.parado = True
        
    def arrancar (self):
        self.arrancado = True
        self.parado = False

    def parar (self):
        self.arrancado = False
        self.parado = True

    def resumen(self):
        print("Marca:",self.marca)
        print("Modelo:", self.modelo)
        print("Color:",self.Color,"\n")
        print("Está arrancado:", self.arrancado)
        print("Esta parado:",self.parado)


miCoche = Vehiculo("Renault","Megane")
miCoche.arrancar()
miCoche.resumen()

class Moto(Vehiculo): #Aquí la clase Moto hereda de Vehículo. Se heredan atributos y métodos,incluido el constructor.
    pass    #Nota: Usaremos la palabra clave pass cuando no deseemos agregar otras propiedades o métodos a la
            #clase, es decir, cuando vayamos a dejar la clase vacía (de momento).

miMoto = Moto("Kawasaki","Ninja")
miMoto.resumen()




            


