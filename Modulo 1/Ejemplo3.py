#Ejemplo 3: ¿Cómo haríamos si quisiéramos guardar este diccionario en un archivo y posteriormente abrirlo
#siempre que queramos consultarlo? Para ello usamos el paquete Path y Pickle
#Pickle nos ofrece procedimientos para poder leer y escribir diccionarios en archivos. 
#El paquete Path lo utilizamos para comprobar si el archivo existe.

import pickle
from pathlib import Path

#create an empty diccionary
d = dict()

#Ask for file name to load dictionary form
file_name = input("Introduce el nombre del archivo con los datos: ")

#comprobamos que existe
path = Path(file_name)
if path.is_file():
    #open file in reading mode
    input_file = open(file_name, 'rb') #'rd' reading lectura
    d = pickle.load(input_file)
    #close de file
    input_file.close()
else:
    print("El file no existe, creamos diccionario vacio")
    print(d)

# check for values or add new ones
document_number = input("Introduce un documento de identidad: ")
if document_number in d: #check whether it is on dict or not
    print("La edad de " + document_number + " es " + str(d[document_number]))
else:
    age = input("DOcumento no existente, Introduce edad: ")
    if age.isnumeric():
        num = int(age)
        d[document_number] = num
        print("Añadido al diccionario")
        print("Diccionario:", d)

#Save dict on file and close
output_file = open(file_name, 'wb') #'wb writing escritura
pickle.dump(d,output_file)
output_file.close()





