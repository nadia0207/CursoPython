print("---------------------------------------------------------")
"""
También se puede preceder el nombre del último parámetro con **,
en cuyo caso en lugar de una tupla se utilizaría un diccionario.
Las claves de este diccionario serían los nombres de los parámetros
indicados al llamar a la función y los valores del diccionario, los valores
"""
def varios(param1, param2, **otros):
    for i in otros.items():
        print (i)

varios(1, 2, tercero = 3)
print("---------------------------------------------------------")

#---------------------------------------
#ARGUMENTOS VARIABLES EN FUNCIONES. EL ARGUMENTO CON * SERÁ UNA TUPLA
# PYTHON NO TIENE SOBRECARGA DE FUNCIONES
#---------------------------------------
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Karla', 'María','Ernesto')
listarNombres('Laura', 'Carlos')
print("---------------------------------------------------------")

#---------------------------------------
# hACER LO MISMO PERO PASANDO DICCIONARIOS COMO ARGUMENTOS. 
def listarTerminos(**KWARGS):
    for clave, valor in KWARGS.items():
        print(f"{clave}: {valor}")

listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')
print("---------------------------------------------------------")

#---------------------------------------
def mi_funcion(nombre, apellido):
    print('saludos desde mi función')
    print(f'Nombre: {nombre}, Apellido: {apellido}')
# Sería como imprimir así:
    print('Nombre:', nombre, 'Apellido:',apellido)

mi_funcion('Juan', 'Perez')
mi_funcion('Karla','Lara')