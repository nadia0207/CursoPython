# SETs, conjuntos
"""
Un conjunto es una colección de elementos ÚNICOS que no está ordenada ni indexada,
por lo que no puede estar seguro de en qué orden aparecerán los elementos.
Siempre se cambia de ORDEN los elementos (de manera automatica)
En Python, los conjuntos se escriben entre llaves.
Una vez que se crea un conjunto, no puede cambiar sus elementos, pero puede agregar
nuevos elementos.
"""
print("-----------------------------------------------------------------")
# Declaración:
mi_conjunto = {"Angel", "Sara", "Pilar","Angel"}
mi_conjunto2 = {"Angel", "Manolo","Juan"}

#Otra forma de declararlo
mi_conjunto3 = set(("Angel", "Sara","Pilar","Angel")) #Asi este 2 veces Angel solo considera 1
print(mi_conjunto3)
print("-----------------------------------------------------------------")

#Para añadir un nuevo elemento:
mi_conjunto.add("Antonio")
# Para añadir varios elementos:
mi_conjunto.update({"Fran", "María"})
print(mi_conjunto)
print("-----------------------------------------------------------------")


#Unión de colecciones. Si hay algún valor repetido sólo aparecerá una vez.
union= mi_conjunto | mi_conjunto2
print(union)
print("-----------------------------------------------------------------")

#Intersección de conjuntos, Nos crea otro conjunto con los
#valores que estaban duplicados en ambos conjuntos. En nuestro caso sólo Angel.
interseccion= mi_conjunto & mi_conjunto2
print(mi_conjunto)
print(mi_conjunto2)
print(interseccion)
print("-----------------------------------------------------------------")

# Diferencia de conjuntos. Nos crea otro conjunto con los elementos que no
# están duplicados.
diferencia= mi_conjunto - mi_conjunto2
print(mi_conjunto)
print(mi_conjunto2)
print(diferencia)
print("-----------------------------------------------------------------")

# Para comprobar si un elemento está en un conjunto:
"Angel" in mi_conjunto #devuelve true o false