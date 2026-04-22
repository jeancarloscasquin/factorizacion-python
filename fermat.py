import math

def fermat_factor(n):
    """
    Factorización de Fermat.
    Retorna (p, q, iteraciones)
    """
    if n <= 0:
        raise ValueError("n debe ser positivo")

    if n % 2 == 0:
        return 2, n // 2, 1

    a = math.isqrt(n)
    if a * a < n:
        a += 1

    iteraciones = 0

    while True:
        b2 = a * a - n
        b = math.isqrt(b2)
        iteraciones += 1

        if b * b == b2:
            return a - b, a + b, iteraciones

        a += 1