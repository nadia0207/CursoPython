#El constructor de una clase en Python se llama __init__, 
# con doble guion bajo antes y después.
# Para hacer que un objeto sea iterable en Python, 
# el método debe llamarse __next__ (con doble guion bajo antes y después).
#Para que un objeto sea usado en un bucle for,
#  la clase debe tener el método __iter__ que devuelva self.

class repetidor: #Creando la clase
    def __init__(self,veces,item): #El constructor de la clase de llama init
        self.veces = veces
        self.item = item
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter == self.veces:
            raise StopIteration('Iterador consumido') # Indica que la iteración ha terminado
        self.counter += 1
        return self.item
    
# Uso del iterador
rep = repetidor(3, "hola" )

for palabra in rep:
    print(palabra)
    
