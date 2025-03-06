print("---------------------------------------------------------")
# -------------------------------------
# FUNCIONES
# -------------------------------------
# Definición de una función. Importante la identación:

def my_funcion():
    print("Estamos ejecutando la función.")

# Llamada a la función. En otra parte de mi código, llamamos a la función para que se ejecute:
my_funcion()

print("---------------------------------------------------------")
def suma():
    num1 = 3
    num2 = 5
    print("suma =", num1+num2)

suma()
print("---------------------------------------------------------")

# Otra opción:
def suma2():
    num_1 = 7
    num_2 = 5
    resultado = num_1 + num_2
    return resultado

#print(suma2())
print(f"La suma es: {suma2()}")
print("---------------------------------------------------------")

#El bloque de código que ejecutará la función incluye todas las declaraciones
#con indentación dentro de la función.
def miFunción():
    print('this will print')
    print('so will this')
x = 7
# la asignación de x no es parte de la función ya que no está indentada

print("---------------------------------------------------------")
#Las variables definidas dentro de una función solo existen dentro del ámbito de esa función.

def duplica(num):
    y = num * 2
    return y
#print(y) # error - x no está definida
print(duplica(4)) # muestra 8