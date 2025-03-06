print("-----------------------------------------------------------------")
# La palabra clave del borrará completamente el conjunto:
miSet2 = {"manzana", "banana", "cereza","fresa","higo"}
del miSet2
#print(f"SET despues de borrar {miSet2}") #ESTO GENERA ERROR
print("-----------------------------------------------------------------")

#Unión de conjuntos: El método union() devuelve un nuevo
# conjunto con todos los elementos de ambos conjuntos:
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)
print("-----------------------------------------------------------------")

# El método update() inserta los elementos en set2 en set1:
set1.update(set2)
print(set1)

# NOTA: Tanto union() como update() excluirán cualquier elemento duplicado.