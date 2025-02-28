G = "Esta variable es de ambito global"
def f1():
    E = "Esta variable es local a f1, englosa a f2"
    def f2():
        L = "L es local de f2"
        E = "E tambien es local de f2"
        G = "G tambien es local de f2"
        print(L ,E,G, sep="\n")
    f2()
f1()
