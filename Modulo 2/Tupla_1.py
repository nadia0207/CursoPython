
miTupla=("Angel", 4, 5.345, True, 4)
tuplaUnitaria=("Sara",) #Tupla unitaria.Hay que poner al final ","
print(miTupla[2]) #Igual que en las listas
miLista=list(miTupla) #Con list convierto una tupla en una lista
miTupla2=tuple(miLista) #Con tuple convierto una lista en una tupla.
print("Angel" in miTupla) #Está "Angel" enmiTupla?,devuelve True o False
print(miTupla.count(4)) #Cuantas veces se encuentra el elemento 4 en miTupla?
print(len(miTupla)) #Longitud de miTupla