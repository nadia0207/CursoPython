#-------------------CODIGO 1------------------------
def codigo_1(number): 
    a = 0                             #Instrucciones = 1
    for j in range(1, number+1):      
        a += a + j                    #Instrucciones = (1)+(n) =n+1

    for k in range(number, 0, -1):
        a -= 1                       #Instrucciones = 2n+n+1 = 3n+1
        a *= 2                    
    
    return a

#se realiza una instrucción n veces. Por ejemplo, si $number tiene el valor de 3 entonces las
# instrucciones que se realizan son 3 veces.

print(codigo_1(8))
