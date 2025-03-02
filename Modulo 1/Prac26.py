#Bloques else al finalizar bucles
#Por ejemplo, veamos un ejemplo donde hacemos evaluamos 
# si un número es primo o no dentro de un bucle while.
a = int(input("Ingrese numero: "))
b = a // 2  #Division entera ejemplo 13//2 == 6
while b > 1:
    if a % b == 0 :
        print('{} es factor de {}'.format(b,a))
        break
    b -= 1
else:
    print('{} es primo'.format(a))
print('\nFuera del bucle')


