print("---------------------------------------------------")
#Operador IN
opcion = input("ELige opcion: opcion1, opcion2, opcion3, opcion4 ")
pasoMinusculas = opcion.lower()
if pasoMinusculas in("opcion1","opcion2", "opcion3", "opcion4"):
    print("Opción válida: " + pasoMinusculas)
else:
    print("Opción inválida: " + pasoMinusculas)

print("---------------------------------------------------")
#---------------------------------------------------------
#OPERADOR TERNARIO
num = int(input("Ingrese numero: "))
var = "par" if (num % 2 == 0) else "impar"
print(var)