print("---------------------------------------------------")
# Programa que pide una nota por consola y
# valora si el alumno ha aprobado o no.
nota=int(input("Introduce tu nota: "))
if nota<5:
    print("Suspenso")
elif nota<7:
    print("Aprobado")
elif nota<9:
    print("Notable")
else:
    print("Sobresaliente")
print("---------------------------------------------------")

#--------------------------------------------------------
#Programa que pide una edad por
# consola y valora si el usuario es mayor de edad o no.
edad=int(input("Introduce edad: "))
if edad<18:
    print("No puedes pasar")
elif edad>100:
    print("Edad incorrecta")
else:
    print("Adelante")