#--------------------------------------------------------------------------------------------------------
#---------------------------------     HERENCIA MULTIPLE ------------------------------------------------
class Vehiculo():

    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.Color = "negro"
        self.arrancado = False
        self.parado = True

    def estado(self):
        print("Marca:",self.marca, "Modelo",self.modelo)
    

class V_electricos():

    def __init__(self):
        pass


class B_electrica(Vehiculo,V_electricos):
    #poniendo entre paréntesis las clases de las que hereda, nuestra clase hija
    #  ya tiene todos los métodos y las propiedades de ambas clases.

    # Muy importante: Se da preferencia siempre a la primera clase que se indique entre paréntesis.
    # Hereda el constructor de la primera clase que pusimos en el paréntesis, y en caso de que haya
    # métodos comunes, también hereda el del primero.

    #Para sobrescribir un método heredado de la clase padre, simplemente volvemos a escribir el método
    #con todos sus argumentos y añadimos el nuevo argumento.
    
    #def cilindrada(self):
    cilindrada = 3000
    
    def estado(self):
        print("Marca:",self.marca, "Modelo:",self.modelo, "Cilindrada:", self.cilindrada)


Mibici = B_electrica("MarcaLoquesea","Modelo2")
Mibici.estado()