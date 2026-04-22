import math

def sqrt_reduction_factor(n):
    """
    Factorización por reducción de raíz cuadrada.
    Retorna (p, q, iteraciones)
    """
    if n <= 0:
        raise ValueError("n debe ser positivo")

    if n % 2 == 0:
        return 2, n // 2, 1

    limite = math.isqrt(n)
    iteraciones = 0

    for d in range(3, limite + 1, 2):
        iteraciones += 1
        if n % d == 0:
            return d, n // d, iteraciones

    return 1, n, iteraciones  # número primo