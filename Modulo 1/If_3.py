print("---------------------------------------------------")
# Operadores AND y OR
distancia = int(input("Introduce distancia: "))
numHermanos = int(input("Introduce número de hermanos en el centro: "))
notaMedia = int(input("Introduce notaMedia: "))

if distancia>20 or numHermanos<2 or notaMedia<=5:
    print("NO eres candidato a la beca")
else:
    print("Sí eres candidato a la beca")