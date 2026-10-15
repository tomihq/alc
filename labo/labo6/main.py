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
from lab3.main import norma, normaExacta

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

    return v_prima, _lambda, k

"""
    Este ejercicio hace énfasis en una particularidad del Teorema de Schur. En particular, en el teorema espectral para matrices hermitianas.

    Sea A ∈ R^{nxn} simétrica (A = A^{t}; en complejos es Hermitiana, A = A^{*}).
    
    -- 

    Por Schur, existe la descomposición A = UTU^{*} (vale para cualquier A, no hace falta la simetría para esto).
    Como A es simétrica/hermitiana, T también lo es:
        T^{*} = (U^{*}AU)^{*} = U^{*}A^{*}U = U^{*}AU = T
    Pero T es triangular superior y hermitiana a la vez, entonces T^{*} es triangular inferior e igual a T,
    por lo que todo lo que está arriba de la diagonal es cero. Es decir, T = D es diagonal.

    Entonces A = UDU^{*}, y multiplicando a derecha por U (U^{*}U = I): AU = UD.
    Mirando columna por columna, si u_i es la columna i de U: A u_i = d_ii u_i.
    Por lo tanto, las columnas de U son autovectores de A y los d_ii son sus autovalores.

    Falta justificar por qué los autovectores son reales y ortogonales:

    - Ortogonales: U es unitaria, o sea U^{*}U = I, lo que dice exactamente que u_i^{*} u_j = δ_ij.
      Es decir, las columnas de U (los autovectores) son ortonormales.
      (Notar que esto vale incluso con autovalores repetidos: Schur ya eligió una base ortonormal.)

    - Autovalores reales: D es hermitiana y diagonal, entonces d_ii = conj(d_ii), o sea d_ii ∈ R.
      (Otra forma: si Av = λv, entonces λ||v||² = v^{*}Av. Como A es hermitiana, v^{*}Av = conj(v^{*}Av),
      así que es real, y por lo tanto λ es real.)

    - Autovectores reales: como A es real y los autovalores son reales, la versión real de Schur
      (A ∈ R^{nxn} con autovalores reales ⟹ U se puede tomar real y ortogonal) dice que U ∈ R^{nxn}, U^{t}U = I.
      Entonces las columnas de U son autovectores reales.
      (Otra forma: (A - λI)v = 0 tiene coeficientes reales, así que si v = x + iy es solución,
      también lo son x e y, y el autoespacio tiene una base real.)

    Conclusión: A simétrica ⟹ A = UDU^{t}, con U ortogonal real y D diagonal real, es decir,
    A tiene una base ortonormal de autovectores reales.

"""

def diagRH(A, tol=1e-15, K=1000):
    _v1, _lambda1, _ = metpot2k(A, tol, K)
    n = _v1.shape[0]
    id = np.eye(n)
    w = id[0] - _v1
    _hv1 = np.eye(n) - 2 * (w.reshape(-1, 1) @ w.reshape(1, -1)) / norma(w, 2)**2
    
    if n == 2:
        S = _hv1
        D = S @ A @ traspuesta(S)
    else:
        B = _hv1 @ A @ traspuesta(_hv1)
        A_prime = B[1:n, 1:n]
        S_prime, D_prime = diagRH(A_prime, tol, K)
        
        D = np.zeros((n, n))
        D[0, 0] = _lambda1[0]
        D[1:, 1:] = D_prime

        S_bloque = np.zeros((n, n))
        S_bloque[0, 0] = 1
        S_bloque[1:, 1:] = S_prime
        S = _hv1 @ S_bloque

    D[np.abs(D) < 1e-6] = 0 # sé exactamente que D debe ser diagonal. Los que no están en la diagonal y están cercanos al 0 los hago 0 para evitar el error. Es solamente cosmético.

    return S, D



"""
    S = matriz de autovectores
    D = matriz de autovalores
    
    S_bloque[1:, 1:] = S_prime

    Si n = 4
    S_bloque = [ 1  0  0  0 ]
               [ 0  *  *  * ]
               [ 0  *  *  * ]
               [ 0  *  *  * ]
    
    Las posiciones marcadas con * son [1:, 1:] y ahí se copia S_prime

    El resultado sería
    [ 1   0  ]
    [ 0   S~ ]

    
Dan lo mismo! 

matriz = np.array([[1, 3, 5], [3, 2, 7], [5, 7, 3]])

print(diagRH(matriz)[1]) # ¿es simétrica?
print(np.linalg.eigvalsh(matriz)) #autovalores
"""
