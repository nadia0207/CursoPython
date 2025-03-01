la = [1,2,3,4,5] #lista de numeros
lb = list("abcde") # Convierte la cadena "abcde" en una lista de caracteres ['a', 'b', 'c', 'd', 'e']
lc = list("ABCDE") # Convierte la cadena "ABCDE" en una lista de caracteres ['A', 'B', 'C', 'D', 'E']

zlist = list(zip(la,lb,lc)) # AGRUPA elementos de la, lb y lc en tuplas y lo convierte en lista
zlist

print(zlist) #imprime la lista agrupada

a,b,c =zip(*zlist) #El *en zip DESAGRUPA lista de tuplas, # Desempaqueta zlist en tres variables a, b y c

print(la,lb,lc,sep = "\n") # Imprime las listas separadas por saltos de línea
print(la,lb) # Imprime la lista la y lb