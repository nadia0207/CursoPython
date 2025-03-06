# Recorrer una tupla
miTupla = ("manzana", "banana", "cereza")
for x in miTupla:
    print(x)
print("-------------------------------")


# Comprobar si existe un elemento
# Compruebe si "manzana" está presente en la tupla:
miTupla1 = ("manzana", "banana", "cereza")
if "manzana" in miTupla1:
    print("Si, 'manzana' esta en la Tupla")
print("-------------------------------")

#Otra forma de comprobar si existe un elemento, simplemente con un boolean
print("manzana" in miTupla1)
print("-------------------------------")

# Longitud de la tupla
print(f"la longitud de la Tupla es: {len(miTupla1)}")
print("-------------------------------")

# Unir dos tuplas
tupla1 = ("a","b","c")
tupla2 = (1,2,3)

tupla3 = tupla1 + tupla2
print(tupla3)