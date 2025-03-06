print("---------------------------------------------------------")
#---------------------------------------
# VALORES POR DEFECTO
#---------------------------------------
# esta es una función básica de suma con valores predeterminados
def suma(a, b=3):
    return a + b

result = suma(1)
print(result)
print("---------------------------------------------------------")

#---------------------------------------
# Indicio de qué tipo de dato vamos amanejar:
#---------------------------------------
def sumar(a:int = 0, b:int = 0) -> int: #def sumar(a = 0, b = 0):
    return a + b

resultado = sumar()
print(f'Resultado sumar: {resultado}')
print(f'Resultado sumar: {sumar(45,654)}')

#uanque le hemos dicho el tipo de los parámetros no estamos obligados acumplirlo.
print(f'Resultado sumar: {sumar("aNGEL","Garcia")}')