def log(*args):
    print("LOG: ", *args)

log("Hola","mundo","2025",1234)

print("**************Hasta aqui la funcion 1****************")
#*********************************************************

def log1(pref,*args):
    print(pref, *args)

log1("INFO:", "Hola", "otra vez",1234)

print("**************Hasta aqui la funcion 2****************")
#*********************************************************

def log2(*args, prefix ="LOG:"):
    print(prefix, *args)

log2("Mensaje")
log2("Hi","Bienvenidos")
log2("dato",prefix="INFO:")




