# 📊 Factorización de Enteros en Python

Este proyecto implementa y compara dos algoritmos clásicos de factorización:

* 🔹 Algoritmo de **Fermat**
* 🔹 Factorización por **reducción de raíz cuadrada**

Además, incluye experimentos automáticos cuyos resultados se publican en GitHub Pages.

---

## 🌐 Demo en línea

👉 GitHub Pages:
https://jeancarloscasquin.github.io/factorizacion-python/

---

## 💻 Código fuente

👉 Repositorio en GitHub:
https://github.com/jeancarloscasquin/factorizacion-python

---

## 📌 Descripción

La factorización de números enteros es fundamental en áreas como:

* criptografía (RSA)
* teoría de números
* seguridad informática

En este proyecto se analizan dos enfoques:

### 🔹 Algoritmo de Fermat

Se basa en la identidad:

n = a² - b² = (a - b)(a + b)

✔ Muy eficiente cuando los factores son cercanos.

---

### 🔹 Reducción por raíz cuadrada

Busca divisores desde 2 hasta √n.

✔ Funciona mejor cuando los factores están alejados.

---

## 🧪 Experimentos

El archivo `experimentos.py`:

* ejecuta ambos algoritmos
* mide iteraciones y tiempo
* muestra resultados en consola
* genera automáticamente:

📄 `docs/resultados.html`

Este archivo es consumido por GitHub Pages y mostrado en la web.

---

## ⚙️ Ejecución local

```bash
python experimentos.py
```

Esto generará:

```bash
docs/resultados.html
```

---

## 🚀 Automatización

Se utiliza **GitHub Actions** para:

* ejecutar automáticamente `experimentos.py`
* actualizar los resultados
* reflejar cambios en GitHub Pages

---

## 📁 Estructura del proyecto

```
factorizacion-python/
├── fermat.py
├── sqrt_reduction.py
├── experimentos.py
├── README.md
├── .github/workflows/python.yml
└── docs/
    ├── index.html
    ├── styles.css
    └── resultados.html
```

---

## 📊 Conclusiones

* Fermat es más eficiente cuando los factores son cercanos.
* La reducción por raíz cuadrada es mejor cuando los factores están separados.
* La automatización permite mantener resultados actualizados sin intervención manual.

---

## 👤 Autor

**Jeancarlos Casquín**

---

## 📌 Notas

Este proyecto combina:

* algoritmos matemáticos
* automatización con GitHub Actions
* publicación web con GitHub Pages

con el objetivo de mostrar resultados de forma clara y reproducible.
