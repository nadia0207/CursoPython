print("---------------------------------------------------------")
# -------------------------------------
# función con un parámetro
# -------------------------------------
# Declaración de una función
def miFuncion(num1, num2):
    return(num1+num2)

#Llamada a la función
print(miFuncion(2, 3))
print("---------------------------------------------------------")

# -------------------------------------
def holaConNombre(name):
    print("Hola " + name + "!")

holaConNombre("Angel") 
print("---------------------------------------------------------")

#---------------------------------------
# Funcion con parametro por defecto
#---------------------------------------
def imprimir(precio, iva = 1.21):
    print(precio * iva)

imprimir(300, 1.08)
print("---------------------------------------------------------")

# Funciones con argumentos variables Me crea una tupla de nombre "otros"
def varios(param1, param2, *otros):
    for val in otros:
        print (val)

varios(1, 2)
varios(1, 2, 3)
varios(1, 2, 3, 4)

"""
También se puede preceder el nombre del último parámetro con **,
en cuyo caso en lugar de una tupla se utilizaría un diccionario.
Las claves de este diccionario serían los nombres de los parámetros
indicados al llamar a la función y los valores del diccionario, los valores
"""