# isdigit(): Devuelve un boolean, nos dice si el valor introducido es un
# string. Tiene que ser un valor introducido entre comillas o dará error.
s_texto = "6"
print(s_texto.isdigit())
print("-------------------------------")

# ---------------------------------------
# isalum(): Devuelve un boolean, Devuelve verdadero si todos los
# caracteres de la cadena son alfanuméricos es decir, si solo contiene letras (a-z, A-Z) y/o números (0-9)
# y hay al menos un carácter. y False si hay otros caracteres como espacios, 
# signos de puntuación o símbolos especiales.
s_texto1 = "Hola"
s_texto2 = "Hola mundo"

print(s_texto1.isalnum())
print(s_texto2.isalnum())
print("-------------------------------")

# ---------------------------------------
#isalpha(): en Python verifica si una cadena contiene solo letras (mayúsculas o minúsculas)
#  y devuelve True si es así. Si hay números, espacios o símbolos, devuelve False.
s_texto3 = "Holamundo"
s_texto4 = "12345"

print(s_texto3.isalpha())
print(s_texto4.isalpha())
print("-------------------------------")

# ---------------------------------------
# split(): Separa por palabras utilizando espacios. Crea una lista.
s_texto5 = "Vamos a separar esta frase por los espacios"
print(s_texto5.split())
print("-------------------------------")

# ---------------------------------------
#Podemos usar otro carácter como separador, por ejemplo una coma:
s_texto6 = "Esta seria la primera parte, y esta la segunda parte"
print(s_texto6.split(","))