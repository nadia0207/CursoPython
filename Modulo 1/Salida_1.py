print("---------------------------------------------------")
# Demostración de la función print()
print("GFG")
print("---------------------------------------------------")

# Demostración de la función print() con espacios
print('G', 'F', 'G')
print("---------------------------------------------------")

print("GFG", end = "@")
print("---------------------------------------------------")

print('G', 'F', 'G', sep = "#")
print("---------------------------------------------------")

#-------------Salida de datos con  formato------------
#formato de cadenas de Python usando una cadena F
name = "Antonio"
# Salida
print(f'hola {name}!. Qué tal?')
print("---------------------------------------------------")

#Usando format()
a = 20
b = 10
sum = a+b
sub = a-b

print('El valor de a es {} y b es {}'.format(a,b))
print('{2} es la suma de {0} y {1}'.format(a, b, sum))
print('{sub_value} es la resta de {value_a} y {value_b}'.format(value_a=a, value_b=b,sub_value = sub))
print("---------------------------------------------------")

#----------------Uso del operador %---------------------------------------
#Podemos usar el operador '%'. Los valores de % se reemplazan con cero o más valores de elementos. 
#El formateo usando % es similar al de 'printf' en el lenguaje de programación C.
''''
%d - entero
%f - flotante
%s - cadena
%x - hexadecimal
%o - octal
'''
num = int(input("Introduzca un número: "))
suma = num+5
print("La suma es %d" %suma)