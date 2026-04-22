import time
from fermat import fermat_factor
from sqrt_reduction import sqrt_reduction_factor


def experimentar(n):
    print(f"\nNúmero n = {n}")

    # Fermat
    inicio = time.perf_counter()
    p1, q1, it1 = fermat_factor(n)
    tiempo1 = time.perf_counter() - inicio

    # Raíz cuadrada
    inicio = time.perf_counter()
    p2, q2, it2 = sqrt_reduction_factor(n)
    tiempo2 = time.perf_counter() - inicio

    print("Fermat:")
    print(f"  factores    = ({p1}, {q1})")
    print(f"  iteraciones = {it1}")
    print(f"  tiempo      = {tiempo1:.8f} s")

    print("Reducción sqrt:")
    print(f"  factores    = ({p2}, {q2})")
    print(f"  iteraciones = {it2}")
    print(f"  tiempo      = {tiempo2:.8f} s")


if __name__ == "__main__":
    casos = [
        5959,
        9973 * 10007,
        101 * 10007,
        99991 * 100003,
        5003 * 90001
    ]

    for n in casos:
        experimentar(n)