
#*****Indicando n cantidades de argumentos
def mifuncion(*args): #acepta un numero arbitrario de argumentos
    print(args)

mifuncion() #si no hay argumentos , args es una tupla vacia
mifuncion(1)
mifuncion(1,2)
mifuncion(1,2,3,4,5,6)

