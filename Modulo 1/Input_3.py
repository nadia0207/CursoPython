#Entrada de datos en listas, conjuntos, tuplas, etc. En el caso de List y Set, la entrada puede tomarse del
#usuario de dos maneras: Solicitando los elementos List/Set uno por uno usando los métodos append()/add().
# Usando los métodos map() y list() / set().
#-------------------------------
#(2) Uso de los métodos map() y list() /set()


List = list(map(int, input("Introduzca los elementos de la lista: ").split()))
Set = set(map(int, input("Introduzca los elementos del Set: ").split()))
print(List)
print(Set)

#Cuando se ingresen los elementos debe hacer un elemento luego espacio
#y al finalizar de ecsribir todos los elementos presionar enter