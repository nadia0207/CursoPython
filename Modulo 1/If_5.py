a = 10
b = int(input('Ingrese numero: '))
if a > b:
    print('Se ha cumplido la condicion')
else:
    print('No se ha cumplido la condicion')

print ('Ya estamos fuera del if')

print("-------------------------------")

# ---------------------------------------
c = 10
d = int(input('Ingrese numero D: '))
if c > d:
    print('C es mayor que D')
elif c == d: #elif es (else if)
    print('C es igual a D')
else:
    print('C es menor que D')

print ('Ya estamos fuera del if')
print("-------------------------------")

# ---------------------------------------
# Condicional if en una sola linea no es necesario poner :
x = 20 if c > d else 30 #Si se cumple la condicion x sera 20 y sino sera 30
print("el valor de x es" ,x)






