
#Indicando n cantidades de argumentos
#Si usamos la sintaxis de doble asterisco, especificamos que le pasaremos los argumentos por nombre

def otrafuncion(**args):
    print(args)

otrafuncion() #si no hay argumentos , args es una tupla vacia
otrafuncion(a=1)
otrafuncion(a=1,b=2)
otrafuncion(a=1,b=2,c=3,d=4)


