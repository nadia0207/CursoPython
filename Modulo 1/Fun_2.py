print("---------------------------------------------------------")
#---------------------------------------
#Si la definición de una función incluye parámetros, debe proporcionar el mismo número
# de parámetros cuando llame a la función.
def multiplica(arg1, arg2):
    return arg1 * arg2

#print(multiplica(3)) # TypeError: multiplica() utiliza exactamente 2 argumentos (0 proporcionados)
print(multiplica('a', 5)) 
#print(multiplica('a', 'b')) #TypeError: Python no puede multiplicar dos strings
print("---------------------------------------------------------")

#---------------------------------------
#Puedes pasar los parámetros en el orden que desees, utilizando el nombre del parámetro.
def suma(a, b):
    return a + b
    
result = suma(b=2, a=3)
print(result)
print("---------------------------------------------------------")

#---------------------------------------
#También podríamos pasar varios valores que retornar a return.
def f(x, y):
    return x * 2, y * 2

a, b = f(5, 3)
print(a,b,sep= " ")
""" Sin embargo, esto no quiere decir que las funciones Python puedan de-volver
varios valores, lo que ocurre en realidad es que Python crea una tupla al vuelo cuyos elementos
son los valores a retornar, y esta única variable es la que se devuelve.
"""