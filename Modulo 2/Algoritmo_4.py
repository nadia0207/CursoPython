#------------------CONSTANTE O(1)----------------------------------------
#Es la más sencilla y siempre presenta un tiempo de ejecución constante. Ejemplo:
def constante():
    y = 50
    ++y
    return y

print(constante())
print("---------------------------------------------------------------------")


#------------------LINEAL O(X)----------------------------------------
#El tiempo crece linealmente mientras crece los datos.Ejemplo:
def lineal(number):
    result = 0
    for x in range(0, number):
        result +=1
    return result
print(lineal(5))
print("---------------------------------------------------------------------")

#------------------POLINOMICO: O(X^c), c>0----------------------------------------
#Son los algoritmos más comunes. Cuando c es 2 se le llama cuadrático, 
# cuando es 3 se le llama cúbico, y en general, polinómico. Cuando n es muy grande
# suelen ser muy complicados. Estos algoritmos suelen tener bucles anidados. 
# Si tienen 2 bucles anidados sería un cuadrático. Ejemplos:
def polinomico(number):
    m = 0
    for i in range(1,number):
        for j in range(1,number):
            m += i + j

    for i in range(1,number):
        for j in range(1,number):
            for k in range(1,number):
                m += i * j * k
    return m
print(polinomico(5))
print("---------------------------------------------------------------------")

#------------------LOGARITMICO: O(log x)----------------------------------------
#No suelen ser muchos. Estos algoritmos indican que el tiempo es menor que 
# el tamaño de los datos de entrada. No importa indicar la base del logaritmo. 
# Un ejemplo es una búsqueda dicotómica.