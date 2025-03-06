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

imprimir(300)
imprimir(300, 1.08)
print("---------------------------------------------------------")

# Funciones con argumentos variables Me crea una tupla de nombre "otros"
def varios(param1, param2, *otros):
    for val in otros:
        print (val)

varios(1, 2)
varios(1, 2, 3)
varios(1, 2, 3, 4)

