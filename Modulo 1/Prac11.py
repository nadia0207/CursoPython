print("*** SEGUNDA FUNCION*******************")
#****************************************************************
def g(a, *,b,c): # Define b y c como keyword-only con el *
    print(a,b,c)

g(1,b=10,c=100)
#g(1,10,100)   #ERROR al no pasar argumentos Keyword-only
