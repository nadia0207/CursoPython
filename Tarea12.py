#Hacer que sep y prefix tengan valores por defecto
def log(*args, prefix ="COMENTARIO:", sep = "--"):
    print(prefix,sep.join(map(str,args)))

log("Hola")
log("Hola","mundo")
log(1,2,3)

'''
1- map(str, args)
Convierte cada elemento de args en una cadena (str).
Si args = (1, 2, 3), esto genera ["1", "2", "3"].

2-sep.join(...)
Une los elementos convertidos en cadena usando el separador sep.
Si sep = "-", el resultado sería "1-2-3".
'''