def indexador(objeto, indice):
    return objeto[indice]
try:
    print(indexador('Python', 'h'))
except IndexError: # Captura IndexError
    print('Error de índice.')
except TypeError: # Captura TypeError
    print('El índice tiene que ser un número.')
print('Hemos salido del try-catch')