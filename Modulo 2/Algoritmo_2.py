#------------------CODIGO 2----------------------------------------
def codigo_2():
    a = 0
    a -= 1
    a *= 2
# En el Código 2 la complejidad sería: F(x) = 3
print("-----------------------------------------------------")


#------------------CODIGO 3----------------------------------------
def codigo_3( number ):
    a = 0                              #Instrucciones = 1
    for j in range(1, number+1):       #Instrucciones = (n)(n)
        for k in range(1, number+1):
            a += a + ( k*j )
    return a
#En el código 3 tenemos un bucle anidado. Cada vez que ejecute un ciclo el otro se ejecuta n veces
# también. Lo cual sería n veces n. La complejidad quedaría: F(x) = n^2+1
