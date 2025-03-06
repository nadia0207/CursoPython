print("-----------------------------------------------------------------")
# Recorra el conjunto e imprima los valores:
miSet = {"manzana", "banana", "cereza","fresa","higo","pera","mango","uva"}

for x in miSet:
    print(x, end= " ")

print("\n-----------------------------------------------------------------")
"""
No puede acceder a los elementos de un conjunto haciendo referencia a un índice,
ya que los conjuntos no están ordenados,los elementos no tienen índice.
Porque se paran moviendo de indique cada vez.
"""
# Obtenga la cantidad de elementos en un conjunto:
print(f"Longitud del SET es de: {len(miSet)}")
print("-----------------------------------------------------------------")

# Elimine "banana" utilizando el método remove() :
miSet.remove("banana")
print(f"SET despues de eliminar banana: {miSet}")
print("-----------------------------------------------------------------")

#Elimine "banana" utilizando el método discard() :
miSet.discard("pera")
print(f"SET despues de eliminar pera: {miSet}")
print("-----------------------------------------------------------------")

"""
Si el elemento a eliminar no existe, remove() generará un error.
Si el elemento a eliminar no existe,discard() NO generará un error.
"""
# Elimine el último elemento utilizando el método pop() :
x = miSet.pop()
print(f"Ultimo elemento en este momento: {x}")
print(f"SET despues de eliminar el ultimo elemento: {miSet}")
print("-----------------------------------------------------------------")

# El método clear() vacía el conjunto:
miSet.clear()
print(f"SET despues de vaciar: {miSet}")
