#Para capturar excepciones utilizamos el bloque de sentencias try/except:
def indexador1(objeto1, indice1):
    return objeto1[indice1]
try:
    print(indexador1('Python', 10))
except IndexError: # Captura Indexerror
    print('Has puesto un índice muy grande.')
print('Hemos salido del try-catch')