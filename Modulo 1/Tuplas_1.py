# TUPLAS
"""Una tupla es una colección ordenada e inmutable.
En Python, las tuplas se escriben entre paréntesis.
Una vez creada no se puede modificar es como una constatnte
pero si modificas algo (eliminas o agregas), en automatico crea otra Tupla
"""
# Declaración de una tupla
miTupla = ("manzana", "banana", "cereza")
print(miTupla[1])
print("-------------------------------")

# Otra forma de declararla
miTupla2 = tuple(("manzana", "banana","cereza"))
print(miTupla)
print(miTupla[2])
print("-------------------------------")

# Indexación Negativa
mitupla3 = ("manzana","banana","cereza")
print(mitupla3[-1])
print("-------------------------------")

# Rango de índices
mitupla4 = ("manzana","banana","cereza","naranja","kiwi","melon","mango")
print(mitupla4[2:5])
print(mitupla4[1:3])
print(mitupla4[3:5])
print("-------------------------------")

# Convierta la tupla en una lista para poder cambiarla:
mitupla5 = ("manzana","banana","cereza")
miLista = list(mitupla5) #convertimos la tupla a lista
miLista[1] = "kiwi"
mitupla5 = tuple(miLista) #convertimos la lista a tupla
print(mitupla5)