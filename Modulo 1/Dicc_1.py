print("----------------------------------------------------------------")
# DICCIONARIOS
"""Los diccionarios, también llamados matrices asociativas, deben su nombre a
que son colecciones que relacionan una clave y un valor.
Un diccionario es una colección desordenada, modificable e indexada.
En Python, los diccionarios se escriben entre llaves y tienen claves y valores.
"""
# Declaración de un diccionario
miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(miDiccionario)
print("-----------------------------------------------------------------")


#A los valores almacenados en un diccionario se accede por su clave
peliculas = {"Love Actually": "Richard Curtis",
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
print(peliculas)
print(peliculas["Love Actually"])
print("-----------------------------------------------------------------")

# Reasignar valores a un diccionario
peliculas["Kill Bill"] = "Nadia Llamoca"
print(peliculas)
