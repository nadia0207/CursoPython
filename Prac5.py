def suma(a,b):  #modificamos a y b en el ascope de suma()
    a = 3
    b = 4
    return a + b

a , b = 5,10
print(suma (a , b))
print (a,b)  #a y b no han cambiado fuera de la funcion

