print("---------------------------------------------------")
#Evaluamos si un mail contiene elcaracter @
miEmail=input("Introduce email: ")
email=False

for i in miEmail:
    if i =="@":
        email=True
if email == True: #Se puedesimplificar if email:
    print("El email es correcto")
else:
    print("EL mail no es correcto")
print("---------------------------------------------------")

#---------------------------------------------------------
# Podemos unir valores de texto con valores de variable a la hora de imprimir:
for j in range(5):
    print(f"Valor de la variable {j}")
print("---------------------------------------------------")

for m in range(5,10):
    print(f"Valor de la variable {m}")

