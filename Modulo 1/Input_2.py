#Entrada de datos en listas, conjuntos, tuplas, etc. En el caso de List y Set, la entrada puede tomarse del
#usuario de dos maneras: Solicitando los elementos List/Set uno por uno usando los métodos append()/add().
# Usando los métodos map() y list() / set().
#-------------------------------
#(1) Solicitando elementos de List/Set uno por uno
Lista = list()
Set = set()
l = int(input("Introduzca el tamaño de la lista: ")) #3
s = int(input("Introduzca el tamaño del Set: ")) #2

print("Introduzca los elementos de la lista:")
for i in range(0, l):
    Lista.append(int(input()))

print("Introduzca los elementos del Set:")
for i in range(0, s):
    Set.add(int(input()))

print(Lista)
print(Set)

#Cuando se ingrese los elementos escribir uno y luego enter
#asi se ingresara elemento uno por uno
