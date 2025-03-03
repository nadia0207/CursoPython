print("---------------------------------------")
# Con la instrucción break podemos detener el ciclo antes de que haya pasado
#por todos los elementos:
# Salga del bucle cuando x es "banana"
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    print(x)
    if x == "banana":
        break
print("---------------------------------------")

#--------------------------------------------
# Salga del bucle cuando x es "banana",
# pero esta vez el corte se produce antes de la impresión:
frutas2 = ["manzana", "banana", "cereza"]
for y in frutas2:
    if y == "banana":
        break
    print(y)
print("---------------------------------------")

#--------------------------------------------
# Con la instrucción continue podemos detener la iteración actual del ciclo y
# continuar con la siguiente:
# En este caso no me imprimiría "banana"
frutas3 = ["manzana", "banana", "cereza"]
for z in frutas3:
    if z == "banana":
        continue
    print(z)