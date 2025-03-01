# Para concatenar textos se hace con “+” o simplemente con una coma.
# Si ponemos coma nos pone entre los textos un espacio, con + no lo hace.
print("Esta frase" + "Termina aca")
print("Esta frase" , "Termina aca")

# ---------------------------------------
# Contatenación y multiplicación de strings
a = "uno"
b = "dos"
c = a + b  #Aqui sale "unodos"
d = a * 3  #Aqui sale "unounouno"
print(a, b, c ,d , sep="-")
print("-------------------------------")

# ---------------------------------------
# MÉTODOS DE LOS STRINGS:
# lower(): Convierte en minúsculas un string.
s_texto = "ESTE TEXTO ESTA INICIALMENTE EN MAYUSCULA"
print(s_texto, s_texto.lower(), sep="\n")
print("-------------------------------")

# ---------------------------------------
# capitalize(): Pone la primera letra en mayúscula.
s_texto1 = "este texto esta inicialemnte en minuscula"
print(s_texto1, s_texto1.capitalize(), sep="\n")
print("-------------------------------")

# ---------------------------------------
# count(): Cuenta cuantas veces aparece una letra o una cadena de caracteres.
s_texto2 = "Vamos a ver cuantas veces aparece la letra c"
print(s_texto2,s_texto2.count("c"),sep="\n")
print("-------------------------------")

# ---------------------------------------
# find(): Representa el índice o la posición en el cual aparece un carácter o
# un grupo de caracteres. Si aparece varias veces me dice sólo el primero.
s_texto3 = "Vamos a ver en que posicion aparece primero la letra e"
print(s_texto3, s_texto3.find("e"),sep="\n")
print("-------------------------------")

# ---------------------------------------
# rfind(): Igual que find() perocontando desde atrás.
s_texto4 = "Vamos a ver en qué posición aparece la palabra desde, contando desde atrás"
print(s_texto4,s_texto4.rfind("desde"),sep="\n")