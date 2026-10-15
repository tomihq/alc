import numpy as np

from rich.console import Console
from rich.table import Table

console = Console()

########### To import other files ###############
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
#################################################

from lab0.lab0 import traspuesta

def norma(v, p):
    suma = 0
    for i in range(len(v)):
        suma += abs(v[i]) ** p

    return suma ** (1 / p)


def fA(A, v, tol=1e-12):
    w_prima = A @ v
    w_prima_norma = norma(w_prima, 2)

    if w_prima_norma < tol:
        return None

    return w_prima / w_prima_norma

def faRandom(A, tol=1e-12):
    # Generamos los 5 vectores iniciales
    vectores = [np.random.rand(A.shape[0]) for _ in range(5)]
    return fAMultVectores(A, vectores, tol)

def fAMultVectores(A, vectors, tol=1e-12, k = [1, 5, 10, 50, 100]):
    results = []

    for i, v in enumerate(vectors, start=1):
        result = v.copy()
        k_anterior = 0

        for k_ in k:
            # Aplicamos solamente las iteraciones que faltan
            for _ in range(k_ - k_anterior):
                if result is None:
                    break

                result = fA(A, result, tol)

            results.append((i, v.copy(), k_, result))
            k_anterior = k_

    return results



matrices = [
        np.array([[1, 1], [0, 1]]),
        np.array([[1/2, 1/2], [1/2, 1/2]]),
        np.array([[0, 1], [-1, 0]])
    ]

"""
for i, A in enumerate(matrices, start=1):
        table = Table(title=f"Experimento {i}", show_lines=True)

        table.add_column("Vector inicial", justify="center")
        table.add_column("Vector v", justify="center")
        table.add_column("Valor k", justify="center")
        table.add_column("Resultado fA^k(A, v)", justify="center")

        resultados = faRandom(A)

        for id_vector, v, k, result in resultados:
            v_str = np.array2string(v, precision=4)

            result_str = (
                "None"
                if result is None
                else np.array2string(result, precision=4)
            )

            table.add_row(
                f"v{id_vector}",
                v_str,
                str(k),
                result_str
            )

        console.print(table)

    
        matrices = [
                np.array([[1, 1], [0, 1]]),
                np.array([[1/2, 1/2], [1/2, 1/2]]),
                np.array([[0, 1], [-1, 0]])
        ]

        vectores = [
            np.array([1/np.sqrt(2), 1/np.sqrt(2)]),
            np.array([1/np.sqrt(2), -1/np.sqrt(2)]),
            np.array([1, 0]),
            np.array([0, 1])
        ]


        for i, A in enumerate(matrices, start=1):
            table = Table(title=f"Experimento {i}", show_lines=True)

            table.add_column("Vector inicial", justify="center")
            table.add_column("Vector v", justify="center")
            table.add_column("Valor k", justify="center")
            table.add_column("Resultado fA^k(A, v)", justify="center")

            resultados = fAMultVectores(A, vectores)

            for id_vector, v, k, result in resultados:
                v_str = np.array2string(v, precision=4)

                result_str = (
                    "None"
                    if result is None
                    else np.array2string(result, precision=4)
                )

                table.add_row(
                    f"v{id_vector}",
                    v_str,
                    str(k),
                    result_str
                )

            console.print(table)                
"""

def metpot2k(A, tol=1e-8, K=1000):
    v = np.random.rand(A.shape[0])
    v_prima = fAMultVectores(A, [v], tol, [2])[0][3]
    e = v_prima.reshape(1, -1) @ v.reshape(-1, 1)
    k = 0

    while((abs(e-1) > tol) and k < K):
        v = v_prima
        v_prima = fAMultVectores(A, [v], tol, [2])[0][3]
        e = v_prima.reshape(1, -1) @ v.reshape(-1, 1)
        k+=1
    
    _lambda = v_prima.reshape(1, -1) @ A @ v_prima
    _epsilon = e-1 

    return v, _lambda, k