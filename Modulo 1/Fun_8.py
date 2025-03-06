print("---------------------------------------------------------")
# FUNCIONES RECURSIVAS
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

numero = 6
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')

#---------------------------------------
"""
Imprimir numeros de 5 a 1 de manera
descendente usando funciones recursivas.
Puede ser cualquier valor positivo,
ejemplo, si pasamos el valor de 5, debe
imprimir:
5
4
3"
"2
1
En caso de pasar el valor de 3, debe
imprimir:
3
2
1
Si se pasan valores negativos no imprime
nada
"""