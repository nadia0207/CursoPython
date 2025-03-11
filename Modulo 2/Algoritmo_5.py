import time
import math

# Iniciar medición de tiempo
start_time = time.time()

def iterador_incremento_exponencial(x:list) -> list:
    iterador = len(x)
    incremento = 1
    while(iterador > 0):
        iterador -= pow(incremento, 2)
        incremento += 1
    return x

# Definir x como una lista de tamaño 5
#Define x correctamente como una lista de tamaño 5 ([0, 0, 0, 0, 0])
x = [0] * 5 

# Ejecutar la función
iterador_incremento_exponencial(x)

# Finalizar medición de tiempo
end_time = time.time()

# Calcular tiempo transcurrido
elapsed_time = end_time - start_time
print(f"Tiempo de ejecución: {elapsed_time:.6f} segundos")

