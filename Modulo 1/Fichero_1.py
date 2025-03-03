print("\n-------------------------------------")
#CREACION Y ESCRITURA EN UN ARCHIVO TXT
zen = '''\
    Bello es mejor que feo.
    Explícito es mejor que implícito.
    Simple es mejor que complejo.
    Complejo es mejor que complicado.
    '''
f = open('short_zen.txt','w')
f.writelines(zen)   #escribe en el fichero
f.close()
print(f)
print("\n-------------------------------------")

#----------------------------------------------
#AHORA QUE TENEMOS CREADO EL FICHERO EN LINEA
#VAMOS A LEER LINEA A LINEA
f = open('short_zen.txt', 'r')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print("\n-------------------------------------")

#----------------------------------------------
for linea in open('short_zen.txt'):
    print(linea.upper(), end=" ")



