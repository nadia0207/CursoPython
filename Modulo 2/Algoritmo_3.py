#------------------Escenario de peor caso----------------------------------------
#El siguiente código tiene como fin encontrar el primer
# número par de una lista de números:
def codigo_4(array):
    for k in range(len(array)):
        if( array[k] % 2 == 0 ):
            return k
    #return null

#En el mejor de los escenarios el número par será el primero de la lista, lo que concluiría el algoritmo.
#  En el peor caso ni siquiera tenga un número par, porque recorrería todas las instrucciones.

#Para el mejor caso tendríamos una complejidad algorítmica: F(x)=1
#Para el peor de los casos la complejidad algorítmica sería: (x)=n
#Para expresar el peor caso usaremos una notación conocida como:
#“O Grande” y se escribe: O(n)
#Que significa complejidad en el peor caso