print("---------------------------------------------------------")
#---------------------------------------
# RETURN
#---------------------------------------
#function definiciones de function no pueden estar vacías, pero si por alguna
#razón tiene una definición de function sin contenido, ingrese la instrucción pass
# para evitar un error.
def myfunction():
    pass
#---------------------------------------
print("---------------------------------------------------------")

#---------------------------------------
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f'Resultado sumar: {resultado}')
#Otra forma de llamar
print(f'Resultado sumar: {sumar(5,3)}')
print("---------------------------------------------------------")

# ---------------------------
# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
    return val1 * val2

print(multiplica(3, 5)) 
print("---------------------------------------------------------")
