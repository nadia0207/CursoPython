print("---------------------------------------------------------")
""" Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1
En caso de pasar el valor de 3, debe
imprimir:
3
2
1
Si se pasan valores negativos no imprime nada """
def imprimir_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivo(numero - 1)
    elif numero == 0:
        return
    elif numero < 0:
        print('Valor incorrecto...')

imprimir_numero_recursivo(-1)
imprimir_numero_recursivo(8)
print("---------------------------------------------------------")

#---------------------------------------
def cuenta_regresiva(num):
    num -= 1
    if num > 0:
       print (num)
       cuenta_regresiva(num)
    else:
       print ("Boooooooom!")
       print ("Fin de la función"),num

cuenta_regresiva(6)
