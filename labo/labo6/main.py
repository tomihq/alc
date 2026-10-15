import numpy as np

from rich.console import Console
from rich.table import Table

console = Console()

def norma(v, p):
    suma = 0
    for i in range(len(v)):
        suma += abs(v[i]) ** p 

    return suma**(1/p) 

def fARandom(A, tol = 1e-12):
    results = []
    for _ in range(5):
        v = np.random.rand(A.shape[0])
        result = fA(A, v, tol)
        results.append((A, v, result))
        
    return results

def fA(A, v, tol = 1e-12):
    w_prima = A @ v 
    w_prima_norma = norma(w_prima, 2)
    if w_prima_norma < tol:
        return None
    w_prima_normalizado = w_prima / w_prima_norma # note that we need to care about err here.
    
    w = w_prima_normalizado if w_prima_norma > 0 else 0

    return w 


matrices = [
    np.array([[1, 1], [0, 1]]),
    np.array([[1/2, 1/2], [1/2, 1/2]]),
    np.array([[0, 1], [-1, 0]])
]

for i, A in enumerate(matrices, start=1):
    table = Table(title=f"Experimento {i}", show_lines=True)

    table.add_column("Iteración", justify="center")
    table.add_column("Vector v", justify="center")
    table.add_column("Resultado fA(A, v)", justify="center")

    for j, (_, v, result) in enumerate(fARandom(A), start=1):
        v_str = np.array2string(v, precision=4)
        result_str = "None" if result is None else np.array2string(
            result, precision=4
        )

        table.add_row(str(j), v_str, result_str)

    console.print(table)