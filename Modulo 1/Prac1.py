def maxmin(lista):
    return max(lista),min(lista) #devuelve tupla de 2 elementos

l = [1,3,5,6,0]
maximo, minimo  = maxmin(l) #Desempaquete la tupla en 2 variables

print(minimo, maximo, sep=" ")
    
