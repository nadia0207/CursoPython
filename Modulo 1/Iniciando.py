#Ejemplo de funcion si Return (RETURN no es obligatorio)
def en_pantalla(frase1 , frase2):
    print(frase1,frase2)

en_pantalla("Me gusta", "Python")

#Otro ejemplo de funcion con return
def suma(a,b):
    return a + b
# Aqui termina la funcion


x = suma(2,3)
print(x)

print(suma("Me gusta","Python"))

#******FUNCION ANIDADA*** 
def f1(a):
    print(a)
    b = 100
    def f2(x):
        print (x)
    f2(b)

#llamamos a la funcion f2 desde f1   
f1("JAVA")