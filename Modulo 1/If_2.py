print("---------------------------------------------------")
# Otro ejemplo de operadores de comparación concatenados
salarioPresidente = int(input("Introduce salario presidente: "))
print("El salario del presidente es de" , salarioPresidente)

salarioDirector = int(input("Introduce salario Director: "))
print("El salario del director es de" ,salarioDirector)

salarioJefe = int(input("Introduce salario jefe: "))
print("El salario del jefe es de" ,salarioJefe)

salarioOperario = int(input("Introduce salario operario: "))
print("El salario del operario es de" ,salarioOperario)

if salarioOperario<salarioJefe<salarioDirector<salarioPresidente:
    print("Todo ok")
else:
    print("Algo no va bien")