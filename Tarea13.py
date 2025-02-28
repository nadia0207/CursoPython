#Modifica la función log para que acepte el siguiente diccionario. 
# Recuerda que hay que pasarlo
#desempaquetándolo con la sintaxis de doble asterisco (**).

def log(*args, prefix, sep):
    print(prefix,sep.join(map(str,args)))

# Crear un diccionario con los valores de 'prefix' y 'sep'
argumentos = {"args":("Hola","Bienvenido",1,2,3),"prefix" :"SALUDO:","sep": "--"} 


# Llamar a la función pasando los valores del diccionario
log(*argumentos["args"],prefix=argumentos["prefix"],sep=argumentos["sep"])


#Explicación: 
# 1- *args permite pasar una cantidad variable de argumentos, y en tu llamada debes pasar esos argumentos con el formato adecuado.
# 2- Se usa el diccionario para separar los valores para prefix y sep, y luego los pasamos a la función directamente.

