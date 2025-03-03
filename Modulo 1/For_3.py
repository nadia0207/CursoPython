print("---------------------------------------")
#Pasarle un diccionario a un FOR (Recorriendo por sus claves)
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'Perez', '60']
d = dict(zip(keys,values))  #Creamos el diccionario y pasamos los datos

for k in d:
    info = '{}: {}'.format(k,d[k]) #Texto formateado con claves y valores
    print(info)
print("---------------------------------------")

#----------------------------------------------
#Pasarle un diccionario a un FOR (Recorriendo todos sus elementos)
#dict.items nos devuelve una tupla (clave, valor)
keys1 = ['nombre', 'apellidos', 'edad']
values1 = ['Jose', 'Maldonado', '70']
dicc = dict(zip(keys1,values1))

for m, n in dicc.items(): #dicc.items devuelve tupla con clave y valor
    print('{}: {}'.format(m,n))
print("---------------------------------------")

#----------------------------------------------
#Recorrer una lista de TUPLAS con FOR
t = [(1,2), (3,4), (5,6)]
for x,y in t:      #desempaquetado en tuplas.
    print(x+y, end=" ")
print("\n---------------------------------------")

#----------------------------------------------
#recorrer dos listas en paralelo con FOR
la = [10, 20, 30, 40]
lb = [5, 25, 50, 10]

for a,b in zip(la,lb):
    m = max(a,b) #max(a,b) devulve el maximo entre a y b
    print(m, end=" ")


