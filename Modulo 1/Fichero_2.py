#Para simplificar la iteración manual con __next__,
# Python ofrece la función builtin next que nos permite
# acceder a la iteración manual de __next__ más fácilmente. Lo que hace realmente la función
# next(obj) es llamar directamente a obj.__next()__:
#Si el archivo tiene menos de 5 líneas, el programa dará un error StopIteration.
f = open('short_zen.txt','r')
print(f.__next__())
print(next(f))
print(next(f))
print(next(f))
print(next(f))
#print(next(f))
#print(next(f))

#RECOMENDABLE: para que no salte error es mejor recorrer 
#el archivo con un bucle y asi solo se leera las lineas existentes
with open('short_zen.txt') as g:
    for line in g:
     print(line, end=" ") # end='' evita líneas en blanco extra


