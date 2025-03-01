# VARIABLES
# Lo ideal es declara e inicializar siempre las variables.
# ---------------------------------------
# En Python podemos asignar una variable a otra variable diferente.
var = "Hola mundo"
var2 = var
print(var2)

# ---------------------------------------
#Los nombres de las variables en Python pueden tener cualquier longitud y
# pueden consistir en letras mayúsculas y minúsculas (A-Z, a-z), dígitos (0-9) y
# el carácter de subrayado (_). Cualquier otro carácter dará error:
var& = "HOLA MADRID" #Esto dara error por el simbolo &

# ---------------------------------------
#Aunque el nombre de una variable puede contener dígitos, el primer carácter de
# un nombre de variable no puede ser un dígito.
2var = "Hola mundo" #Esto daria error

# ---------------------------------------
# Declaración de variable de tipo string en varias líneas:
s_textoLargo =  """Esto es un ejemplo de mensaje
con tres saltos
de linea"""
print(s_textoLargo)