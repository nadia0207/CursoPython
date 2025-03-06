print("-----------------------------------------------------------------")
# La palabra clave del también puede eliminar completamente el diccionario:
miDiccionario2 = {"brand": "Ford","model": "Mustang","year": 1964}
print("Eliminando completamente el Diccionario ")
del miDiccionario2
#print(miDiccionario2) #Saldra error porque ya no existe diccionario
print("-----------------------------------------------------------------")

#La palabra clave clear() vacía el diccionario:
miDiccionario3 = {"brand": "Ford","model": "Mustang","year": 1964}
print(miDiccionario3)
print("Vaciando el diccionario")
miDiccionario3.clear()
print(miDiccionario3)
