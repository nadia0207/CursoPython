def factores_primos(n):
    factores = []
    divisor = 2
    
    while n % divisor == 0:  # Dividir por 2 tantas veces como sea posible
        factores.append(divisor)
        n //= divisor  # n = n // divisor (// es division entera redonada sin decimales)    
    
    divisor = 3
    while divisor * divisor <= n:  # Probar con números impares
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
        divisor += 2
    
    if n > 2:  # Si queda un número mayor que 2, es primo
        factores.append(n)
    
    return factores

print(factores_primos(1050)) 