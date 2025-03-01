# strip(): Borra los espacios sobrantes
# al principio y al final.
s_texto = "  En este texto habia espacios al principio y al final    "
print(s_texto.strip())
print("-------------------------------")

# ---------------------------------------
# replace(): Cambia una palabra o una letra por otra.
s_texto1 = "Vamos a reemplazar la palabra casa"
print(s_texto1, s_texto1.replace("casa","hogar"), sep="\n")
print("-------------------------------")

# ---------------------------------------
#Entrada de datos input()
s_nombreIntrudido = input("Introducir su nombre:")
print("Bienvenido", s_nombreIntrudido)
print("-------------------------------")

# -------------------------------------
""" IMPORTANTE: Todo lo introducido por input() se considera string, aunque sea
un número, por lo que, si necesitamos operar matemáticamente con números, 
tendremos que hacer un casting:"""
s_edad = int(input("Introduce su edad: "))
print("El año que viene usted tendra", s_edad+1 , "años")