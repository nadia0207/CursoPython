print("-------------------------------------------------")
#--------------------------------------------------------
# Calcula la raiz cuadrada de un número.
#  Tenemos tres intentos y el número no puede ser negativo.
import math
intentos = 0 
num = int(input("Introduce numero: ")) 

while num < 0:                                  
    if intentos==2:
        print("Demasiados intentos")
        break    
    print("Incorrecto")
    num=int(input("Introduce numero nuevamente: "))    
    intentos=intentos+1 # 2

if intentos<= 2:
    intentos=intentos+1
    solucion=math.sqrt(num)
    print("la raiz cuadrada de "+str(num)+ " es: "+str(solucion))
    print("En el intento",intentos)
print("-------------------------------------------------")

#--------------------------------------------------------
# Bucle while con un if anidado y un break
# Salga del bucle cuando num sea 3:
num1 = 1
while num1 < 6:
    print(num1)
    if num1 == 3:
        break
    num1 += 1
