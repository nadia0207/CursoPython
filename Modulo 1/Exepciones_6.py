#-------------Acciones de finalización y limpieza-------------
#Este tipo de operaciones suelen ser, por ejemplo, asegurarnos 
# que cerramos un fichero, una conexión,etc.
#Para esto tenemos la sentencia finally:
def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10)
finally:
    print('Esto se ejecuta incluido cuando salta la excepción')