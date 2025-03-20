#El polimorfismo es una propiedad de la herencia por
# la que objetos de distintas subclases pueden responder a una misma acción.

class Poligono():
    def __init__(self,lados,color=None):
        self.lados = lados
        self.color = color
    
    def show(self):
        print("color:", self.color)

class Cuadrado(Poligono):
    def __init__(self, lado,color=None):
        Poligono.__init__(self,4,color) # Llama correctamente al constructor de Poligono
        self.lado = lado

    def show(self):
        super().show() # Llama a show() de Poligono
        print(f'lados: {self.lados}')

class Triangulo(Poligono):
    def __init__(self, base, altura,color=None):
        super().__init__(3, color)
        self.base = base
        self.altura = altura
    
    def show(self):
        super().show()
        print(f'Base: {self.base}, Altura: {self.altura}, Lados: {self.lados}')

#crear objetos
t1 = Triangulo(3,4)
t2 = Triangulo(10,6,"azul")
c1 = Cuadrado(2,"verde")

# Crear tupla con los polígonos
poligonos = (t1,t2,c1)

# Iterar sobre los polígonos
for i in poligonos:
    i.show()
    print()