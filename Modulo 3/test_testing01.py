import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


#Importamos unittest:
import unittest

#Importamos la función sobre la cual se van a ejecutar los test:
from testing01 import area

#Y en nuestro caso tendremos que importar también PI:
from math import pi

#Lo siguiente será crear una clase que herede de la clase TestCase:
class TestArea(unittest.TestCase):
    #En esta clase es donde vamos a poner nuestros test.
    def test_area(self):
        print('-----Test valores de resultado conocido-----')
        self.assertAlmostEqual(area(1),pi)
        self.assertAlmostEqual(area(0),0)
        self.assertAlmostEqual(area(3),pi*(3**2))

#Para ello debemos invocar al método assertAlmostEqual() pasando como primer
# parámetro nuestra función con el parámetro de entrada y 
# como segundo parámetro el resultado que sabemos que debe dar.

#Recordemos que tenemos que ejecutar nuestro test poniendo en la consola:
#python -m unittest test_testing01.py