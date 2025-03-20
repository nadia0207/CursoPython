"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos
Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )
Coche (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de
Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )
Bicicleta (Clase Hija de Vehículo) (Además de los atributos y métodos heredados de
Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        print (f'Color: {self.color}, ruedas: {self.ruedas}')

class Coche(Vehiculo):
    def __init__(self,color, ruedas,velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        print (super().__str__(), ',Velocidad (km/hr):' , str(self.velocidad))

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        print (super().__str__() , 'Tipo: ', str(self.tipo))

# Creamos un objeto de la clase Vehiculo
mi_vehiculo = Vehiculo('Rojo', 4)
mi_vehiculo.__str__()
print("----------------------------")

# Creamos un objeto de la clase hija Coche
mi_coche = Coche('Azul', 4, 150)
mi_coche.__str__()
print("----------------------------")

# Creamos un objeto de la clase hija Bicicleta
mi_bicicleta = Bicicleta('Blanca', 2, 'Urbano')
mi_bicicleta.__str__()
