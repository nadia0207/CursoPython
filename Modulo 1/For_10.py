print("---------------------------------------")
# Bucle FOR ANIDADO
# Imprime cada color para cada fruta:
color = ["verde", "amarilla", "roja"]
frutas = ["manzana", "banana", "cereza"]
for x in color:
    for y in frutas:
        print(x, y)
print("---------------------------------------")

#-------------------------------------------
# Los bucles for no pueden estar vacíos.
# Si por alguna razón tenemos un bucle for sin contenido, usaremos la
# instrucción pass para evitar un error.
for y in [0, 1, 2]:
    pass