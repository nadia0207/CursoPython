print("-------------------------------------------------")
# WHILE
# Imprime edad cuando el contador llegue a 18
edad = 0
while edad < 18:
    edad=edad+1
    print("Tienes "+str(edad))
print("-------------------------------------------------")

#--------------------------------------------------------
# Pregunta la edad mientras sea negativa
edad1 =int(input("Introduce edad: "))
while edad1<0:
    print("Edad incorrecta")
    edad1=int(input("Introduce edad: "))
print("tu edad es: "+str(edad1))
