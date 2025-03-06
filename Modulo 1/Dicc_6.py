print("-----------------------------------------------------------------")
# Copiar un diccionario
miDiccionario4 = {"brand": "Ford","model": "Mustang","year": 1964}
midict = miDiccionario4.copy()
print(midict)
print("-----------------------------------------------------------------")

# Otra forma de copiar un diccionario
miDiccionario5 = {"brand": "Ford","model": "Mustang","year": 1964}
midict = dict(miDiccionario5)
print(midict)
print("-----------------------------------------------------------------")

# Diccionarios anidados
child1 = {"name" : "Emil","year" : 2004}
child2 = {"name" : "Tobias","year" : 2007}
child3 = {"name" : "Linus","year" : 2011}
myfamily = {
"child1" : child1,
"child2" : child2,
"child3" : child3
}
print(myfamily)
print(myfamily["child1"])