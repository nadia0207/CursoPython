#****FUNCION pasando objetos INMUTABLES****
def minimo(l):
    l[0] = 1000 #modificamos la lista en el interior
    return l

l = [1,2,3]
print(l)

print(minimo(l)) #Modifica la lista aqui
print(l)
print("---- Hasta aqui primera funcion")

#*****FUNCION pasando objetos MUTABLES (listas, diccionarios y conjuntos) *****
#*****************************************************************************
def mifuncion(m):
    n = m.copy() #creamos una copia de la lista m
    n[0] = 2000
    return n

m = [3,4,5]
print(m)

print(mifuncion(m))
print(m)