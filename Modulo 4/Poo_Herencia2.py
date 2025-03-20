
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
        print("El modelo es un coche:\n",
              "Marca:",self.marca,"\n","Modelo:", self.modelo,"\n",
              "Color:",self.Color,"\n","Está arrancado:", self.arrancado,"\n",
              "Esta parado:",self.parado,"\n")

miCoche = Vehiculo("Renault", "Megane")
miCoche.arrancar()
miCoche.resumen()

class Moto(Vehiculo): #la clase Moto hereda de la clase Vehiculo todos sus atributos y metodos
    is_careando = False #Incorpora otro atributo solo a la clase moto

    #Método propio de la clase Moto, no heredado del padre.
    def poner_carenado(self):
        self.is_careando = True
    
    #La clase Moto sobrescribe el método resumen() heredado del padre
    def resumen(self):
        print("El modelo es una moto:\n",
              "Marca:",self.marca,"\n","Modelo:", self.modelo,"\n",
              "Color:",self.Color,"\n","Está arrancado:", self.arrancado,"\n",
              "Esta parado:",self.parado,"\n","Tiene carenado:",self.is_careando,"\n")

miMoto = Moto("Kawasaki", "Ninjas")
miMoto.poner_carenado()
miMoto.resumen()

class Kwad(Moto): #la clase Kwad hereda de la clase Moto todos sus atributos y metodos
    pass

miKwad = Kwad("Linhai", "LH 500")
miKwad.resumen()
