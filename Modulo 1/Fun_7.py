print("---------------------------------------------------------")
#---------------------------------------
"""
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la suma de todos los valores pasados como argumentos.
"""
# Definimos nuestra funcion para sumar valores
def sumar(*args):
    resultado = 0
    for x in args:
        resultado += x
    return resultado

print(sumar(3,4,7,6,15))
print("---------------------------------------------------------")

#---------------------------------------
# Distintos tipos de datos como argumentos en Python
def desplegarNombres(nombres):
    for nombre in nombres:
        #print(nombre)
        print(nombre,end=" ")

nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
print("\n")
desplegarNombres('Carlos')
print("\n")
desplegarNombres((8, 9))
print("\n")
desplegarNombres([10, 11])