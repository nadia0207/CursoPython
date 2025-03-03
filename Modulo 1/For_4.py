print("------------------------------------------------------------")
#Seguimos con bucles FOR
#en el ejemplo buscamos la posicion de las vocales dentro de letras
import random
letras = list('abcdefghijklmnopqrstuvwxyz')
vocales = 'aeiou'

random.shuffle(letras)
print(''.join(letras))

for i,letra in enumerate(letras): 
    if letra in vocales:
        print('{} en la posicion {}'.format(letra,i))


print("------------------------------------------------------------")
#En este ejemplo buscamos las posiciones de las vocales en un abecedario desordenado. Para ello
# usamos la función ENUMERATE, que nos pide una secuencia y nos devuelve la misma secuencia
# asociada a sus índices:
abcde = sorted(letras)[:5]

print(abcde)
print(list(enumerate(abcde))) #devuelve secuencia con sus indices
print(list(enumerate(abcde,10))) #Podemos decirle en que indice empieza

