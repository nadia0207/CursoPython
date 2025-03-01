# Objetos mutables e inmutables
# Obtener la dirección de memoria de una variable
print("-------------------------------")
a = 65
print("La direccion de memoria es", id(a))
print("-------------------------------")

# ---------------------------------------
# Obtener la dirección de memoria de
# una variable que apunta a otra
miNumero = 65
miNumero2 = miNumero
print("La direccion de memoria es", id(miNumero))
print("La direccion de memoria es segundo Numero", id(miNumero2))
print("-------------------------------")

# ---------------------------------------
# Si cambio la variable, realmente creo
# una copia en otra dirección de memoria:
a = 65
print("La direccion de memoria de",a,"es",id(a))
a +=2
print("La direccion de memoria de",a,"es",id(a))
print("-------------------------------")

# ---------------------------------------
# Obtener la dirección de memoria de una tupla
b=(1,2,3,4,5)
print("La direccion de memoria de la tupla",b,"es",id(b))
print("-------------------------------")

# ---------------------------------------
# Obtener la dirección de memoria de una lista
c = [1,2,3,4,5]
print("La direccion de memoria de la lista",c,"es",id(c))
print("-------------------------------")

# ---------------------------------------
# Obtener la dirección de memoria de un diccionario
d = {"a":1 , "b":2}
print("La direccion de memoria del diccionario",d,"es",id(d))

d["c"] = 3
print("La direccion de memoria del diccionario",d,"es",id(d))
print("-------------------------------")
