def indexador(objeto, indice):
    return objeto[indice]
try:
    print(indexador('Python', 'h'))
except (IndexError, TypeError): # Captura varios errores
    print('Error.')
print('Hemos salido del try-catch')

try:
    print(indexador('Python', 'h'))
except: # Captura todos los errores. No recomendado.
    print('Error.')
print('Hemos salido del try-catch')