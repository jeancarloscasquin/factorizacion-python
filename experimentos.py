import math
import time
import os


def fermat_factor(n):
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

    for n in casos:
        # Fermat
        inicio = time.perf_counter()
        p1, q1, it1 = fermat_factor(n)
        t1 = time.perf_counter() - inicio

        # sqrt
        inicio = time.perf_counter()
        p2, q2, it2 = sqrt_reduction_factor(n)
        t2 = time.perf_counter() - inicio

        resultados.append({
            "n": n,
            "fermat": f"({p1},{q1}) - it:{it1} - t:{t1:.6f}",
            "sqrt": f"({p2},{q2}) - it:{it2} - t:{t2:.6f}"
        })

    return resultados


def generar_html(resultados):
    filas = ""

    for r in resultados:
        filas += f"""
        <tr>
            <td>{r['n']}</td>
            <td>{r['fermat']}</td>
            <td>{r['sqrt']}</td>
        </tr>
        """

    html = f"""
    <section class="card">
        <h2>🧪 Resultados Automáticos</h2>
        <table>
            <thead>
                <tr>
                    <th>Número</th>
                    <th>Fermat</th>
                    <th>Raíz cuadrada</th>
                </tr>
            </thead>
            <tbody>
                {filas}
            </tbody>
        </table>
    </section>
    """

    # Guardar en docs
    os.makedirs("docs", exist_ok=True)

    with open("docs/resultados.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    resultados = ejecutar_experimentos()
    generar_html(resultados)