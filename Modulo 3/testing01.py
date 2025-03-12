from math import pi

def area(r):
    areaC = pi*(r**2)
    return areaC

valores = [1, 3, 0, -1, -3, 2+3j, True,
'hola']

for v in valores: 
    areaCalculada = area(v)
    print('Para el valor', v, 'el área es', areaCalculada)


#Para hacer el testing poner en consola
#python -m unittest test_testing01.py
#tambien podemos poner
#python -m unittest discover