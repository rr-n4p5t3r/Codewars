def criba_eratostenes(n):
    """
    Implementación del algoritmo de la Criba de Eratóstenes para encontrar todos los números primos hasta n.
    
    Parámetros:
        n (int): El límite superior hasta el cual se buscan los números primos.
        
    Retorna:
        primos (list): Una lista que contiene todos los números primos hasta n.
    """
    # Inicializar una lista de booleanos para marcar si un número es primo o no
    es_primo = [True] * (n + 1)
    # 0 y 1 no son primos
    es_primo[0] = es_primo[1] = False
    
    # Empezar desde el primer número primo (2)
    p = 2
    while p * p <= n:
        # Si es_primo[p] es True, entonces p es primo
        if es_primo[p]:
            # Marcar como no primo todos los múltiplos de p, comenzando desde p^2
            for i in range(p * p, n + 1, p):
                es_primo[i] = False
        p += 1
    
    # Recoger los números primos en una lista
    primos = [i for i in range(n + 1) if es_primo[i]]
    return primos

# Pedir al usuario que ingrese el límite
limite = int(input("Ingrese el límite para encontrar los números primos: "))

# Obtener los números primos hasta el límite dado
primos = criba_eratostenes(limite)
print("Los números primos hasta", limite, "son:", primos)
