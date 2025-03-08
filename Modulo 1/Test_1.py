#encontrar el mínimo de estos dos números
def minimo(a,b):
    if a<b:
        return a
    else:
        return b

print(f"El menor numero de {minimo(2,4)}")
print(f"El menor numero de {minimo(-1,-4)}")
print("------------------------------------------------------")

#Invertir palabras de una cadena dada.
def reverse(frase):
    letra = frase.split(" ")
    nueva_frase= ' '.join(reversed(letra))
    return nueva_frase

if __name__ == "__main__":
    p = input("Ingrese frase: ")
    print(reverse(p))
print("------------------------------------------------------")

#Realizar una suma de los elementos de una tupla
mitupla = (7,8,9,10,11)
print("mi tupla original es: ", str(mitupla))

suma = sum(list(mitupla))
print("La suma de mi tupla es:",str(suma))
print("------------------------------------------------------")        

#Escriba un código que calcule una lista de números proporcionados.
def lista_numero(milista1):
    if len(milista1) == 1:
        return milista1[0]
    else:
        return milista1[0] + lista_numero(milista1[1:])

print(lista_numero([3,5,8,9,9]))

print("------------------------------------------------------")   
#5 Escriba un código que desordene al azar una lista.
from random import shuffle
x = ['Shyner','Pertenece','a','los','Nordidos']
shuffle(x)
print(x)