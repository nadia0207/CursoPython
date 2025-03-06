print("-----------------------------------------------------------------")
# Agregar elementos a un diccionario:
miDiccionario = {"brand": "Ford","model": "Mustang","year": 1964}
print(miDiccionario)
print("-----------------------------------------------------------------")
print("Agregando elementos")
miDiccionario["color"] = "red"
print(miDiccionario)
print("-----------------------------------------------------------------")

# Eliminar el último elemento insertado:
print("Eliminando el ultimo elemento")
miDiccionario.popitem()
print(miDiccionario)
print("-----------------------------------------------------------------")

# La palabra clave del elimina el elemento con el nombre de clave especificado:
print("Eliminando elemento de la clave 'Model'")
del miDiccionario["model"]
print(miDiccionario)
