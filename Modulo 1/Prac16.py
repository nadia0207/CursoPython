# Forzado de tipo, CASTING:
# ---------------------------------------
# Forzado de tipo Enteros:
x = int(1)     # x valdra 1
y = int(2.8)   # y valdra 2
z = int("3")   # z valdra 3

print(x,y,z,sep="-")

# ---------------------------------------
# Forzado de tipo Float:
m = float(1)     # m valdra 1.0
n = float(2.8)   # n valdra 2.8
l = float("3")   # l valdra 3.0
o = float("4.2") # o valdra 4.2

print(m,n,l,o,sep="-")

# ---------------------------------------
# CASTING. Reconversión de tipos:
# Casting de int a float:
n_numero = 13
n_numero2 = float(n_numero)
print(n_numero, n_numero2, sep="-")

# ---------------------------------------
# Casting de float a int:
n_numero3 = 24.876
n_numero4 = int(n_numero3)
print(n_numero3, n_numero4, sep="-")

# ---------------------------------------
# Casting de string a int
s_texto = "13"
n_numero5 = int(s_texto)
print(s_texto, n_numero5, sep="-")