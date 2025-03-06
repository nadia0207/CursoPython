print("---------------------------------------------------------")
#Entrada por parte del usuario como número entero
num = int(input('Introduce un número: '))
add = num+1
# Salida
print(add)
print("---------------------------------------------------------")

#Cómo pedir varios valores de una sola vez
a, b, c = map(int, input("Introduzca los números: ").split())
print("Los números son: ", end = " ")
print(a, b, c)
