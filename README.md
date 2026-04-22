# Factorización en Python

Este proyecto implementa dos métodos de factorización:

- Algoritmo de Fermat
- Factorización por reducción de raíz cuadrada

## Descripción

El algoritmo de Fermat es eficiente cuando el número `n = p*q` tiene factores cercanos entre sí.  
La reducción por raíz cuadrada busca divisores desde 2 hasta `sqrt(n)` y resulta útil cuando los factores están más separados.

## Archivos

- `factorizacion.py`: implementación de ambos algoritmos
- `experimentos.py`: pruebas comparativas de rendimiento

## Requisitos

Python 3.10 o superior.

## Ejecución

```bash
python factorizacion.py