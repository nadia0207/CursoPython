print("---------------------------------------")
# Podemos poner un tercer argumento con el que especificamos de cuanto en cuanto
# va el conteo:
for i in range(5,10,2):
    print(f"Valor de la variable {i}")
print("---------------------------------------")

#---------------------------------------------
# validar un mail en función de si tiene
# @ simplemente recorriendo la logitud del string:
valido=False
email=input("Introduce tu email: ")
for i in range(len(email)):
    if email[i]=="@":
        valido=True
if valido:
       print("Email correcto")
else:
       print("Email incorrecto")
print("---------------------------------------")

#---------------------------------------------        
# Las cadenas son objetos iterables,
# contienen una secuencia de caracteres:
for x in "banana":
    print(x)