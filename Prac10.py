print("*** PRIMERA FUNCION****************")
#****************************************************************
def f(a,b,c,d):
    print(a,b,c,d)

argumentos = {'b':20 , "a":1, "c":300, "d":4000}
print(argumentos)
f(**argumentos) # Desempaquetando diccionario argumentos con **

argumentos = {'b':200 , "c":300, "d":400}
print(argumentos)
f(10,**argumentos) #podemos posicionar argumentos posicionales con dict
