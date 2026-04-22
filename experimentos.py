import math
import time
import os


def fermat_factor(n):
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


def sqrt_reduction_factor(n):
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

    return 1, n, iteraciones


def ejecutar_experimentos():
    casos = [
        5959,
        9973 * 10007,
        101 * 10007,
        99991 * 100003,
        5003 * 90001
    ]

    resultados = []

    print("\n==============================")
    print(" RESULTADOS DE EXPERIMENTOS")
    print("==============================")

    for n in casos:
        inicio = time.perf_counter()
        p1, q1, it1 = fermat_factor(n)
        t1 = time.perf_counter() - inicio

        inicio = time.perf_counter()
        p2, q2, it2 = sqrt_reduction_factor(n)
        t2 = time.perf_counter() - inicio

        resultado = {
            "n": n,
            "fermat_factores": f"({p1}, {q1})",
            "fermat_iteraciones": it1,
            "fermat_tiempo": f"{t1:.8f}",
            "sqrt_factores": f"({p2}, {q2})",
            "sqrt_iteraciones": it2,
            "sqrt_tiempo": f"{t2:.8f}"
        }

        resultados.append(resultado)

        # Mostrar también en terminal
        print(f"\nNúmero n = {n}")
        print("Fermat:")
        print(f"  factores    = {resultado['fermat_factores']}")
        print(f"  iteraciones = {resultado['fermat_iteraciones']}")
        print(f"  tiempo      = {resultado['fermat_tiempo']} s")

        print("Reducción sqrt:")
        print(f"  factores    = {resultado['sqrt_factores']}")
        print(f"  iteraciones = {resultado['sqrt_iteraciones']}")
        print(f"  tiempo      = {resultado['sqrt_tiempo']} s")

    return resultados


def generar_html(resultados):
    filas = ""

    for r in resultados:
        filas += f"""
        <tr>
            <td>{r['n']}</td>
            <td>{r['fermat_factores']}</td>
            <td>{r['fermat_iteraciones']}</td>
            <td>{r['fermat_tiempo']} s</td>
            <td>{r['sqrt_factores']}</td>
            <td>{r['sqrt_iteraciones']}</td>
            <td>{r['sqrt_tiempo']} s</td>
        </tr>
        """

    html = f"""
<section class="card">
    <table>
        <thead>
            <tr>
                <th>Número</th>
                <th>Fermat - Factores</th>
                <th>Fermat - Iteraciones</th>
                <th>Fermat - Tiempo</th>
                <th>Raíz Cuadrada - Factores</th>
                <th>Raíz Cuadrada - Iteraciones</th>
                <th>Raíz Cuadrada - Tiempo</th>
            </tr>
        </thead>
        <tbody>
            {filas}
        </tbody>
    </table>
</section>
"""

    os.makedirs("docs", exist_ok=True)

    with open("docs/resultados.html", "w", encoding="utf-8") as archivo:
        archivo.write(html)

    print("\nArchivo generado correctamente: docs/resultados.html")


if __name__ == "__main__":
    resultados = ejecutar_experimentos()
    generar_html(resultados)