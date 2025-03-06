print("-----------------------------------------------------------------")
# Usar una tupla dentro de un diccionario:
miDiccionario3 = {"nombre":"Jordan", "Equipo":"Bulls", "Anillos": [1991,1992,
               1993, 1996,1997, 1998]}
print(miDiccionario3["Anillos"])
print("-----------------------------------------------------------------")


#Quitar valores de un diccionario
peliculas = {"Love Actually": "Richard Curtis",
"Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet"}
print(peliculas)
peliculas.pop("Love Actually")
print(peliculas)
print("-----------------------------------------------------------------")

# Crear un diccionario a partir de dos listas:
ListaLlaves = ["nombre","edad"]
ListaValores = ["Angel",43]
diccionario = dict(zip(ListaLlaves,ListaValores))
print(diccionario)
print("-----------------------------------------------------------------")

#Para comprobar si una clave está en el diccionario:
"nombre" in diccionario  #Devuelve true o false
print("nombre" in diccionario)