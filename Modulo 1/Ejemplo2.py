#Ejemplo 2: Tenemos un diccionario en el que asociamos los 
# números de los documentos de identidad de ciertas personas con su edad.
# Queremos realizar un programa en el que el usuario introduzca un el
# número de un documento de identidad. Si dicho número ya está en el diccionario
#  debe mostrar la edad, en caso contrario debe solicitarnos que 
# introduzcamos la edad, que posteriormente añadiremos al diccionario.

dic = {"50869888":37 , "12345678":32} #creamos el diccionario
print("Diccionario: ",dic)
documento = input("Introduce numero documento: ")
if documento in dic: #Comprobamos que esta en el diccionario
    print("La edad de " + documento + " es: " + str(dic[documento]))
else:
    edad = input("Documento no existe, Ingrese edad: ")
    if edad.isnumeric():       #comprobamos si son nunmeros
        num = int(edad)        #convertimos a entero
        dic[documento] = num
        print("Edad añadida al diccionario")
        print("Diccionario actualizado: ", dic)
    else:
        print("La edad ingresada no es numero entero")
