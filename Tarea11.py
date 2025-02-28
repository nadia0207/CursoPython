print("**************FUNCION 4****************")
#*********************************************************
#Modificar la función para que el usuario pueda establecer el prefijo 
# y el separador (sep y prefix), pero solo por nombre
def log(*args,prefix,sep):
    print(prefix,sep.join(map(str,args)))

log(1,2,4,5,prefix="BLOG:",sep="-")
log("Hola","como","estas",prefix="SALUDO:",sep="/")

'''
1- map(str, args)
Convierte cada elemento de args en una cadena (str).
Si args = (1, 2, 3), esto genera ["1", "2", "3"].

2-sep.join(...)
Une los elementos convertidos en cadena usando el separador sep.
Si sep = "-", el resultado sería "1-2-3".
'''