print("*** TERCERA FUNCION*******************")
#****************************************************************

def m(a,*b,c): #Se debe pasar c como Keyword-only. Y "b" puede recibir 0 o muchos valores
    print(a,b,c)

m(1,c=2)
m(1,2,c=3)
m(1,2,3,4,5,6,c=10)