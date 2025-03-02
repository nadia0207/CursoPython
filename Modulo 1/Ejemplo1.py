#Ejemplo 1: Un usuario introduce texto desde teclado y queremos
# averiguar si es un número entero. Si es entero lo
# añadiremos a una variable tipo lista de números enteros.

lista = list()                 #creamos una lista vacia
x = input("Ingrese numero: ")
if x.isnumeric():              #comprobamos si son nunmeros
    num = int(x)               #convertimos a entero
    lista.append(num)
    print("Numero",str(num), "añadido a la lista")
    print(lista)
else:
    print("No has introducido un numero entero")


