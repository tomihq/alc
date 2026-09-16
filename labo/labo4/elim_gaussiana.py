import numpy as np
import matplotlib.pyplot as plt

def calculaLU(A):
    cant_op = 0

    if A is None:
        return None, None, 0

    m = A.shape[0]
    n = A.shape[1]
    Ac = A.copy()
    
    if m != n:
        return None, None, 0

    for columna in range(m):
        
        if np.isclose(Ac[columna][columna], 0.0, rtol=1e-3):
            return None, None, 0
        print(Ac[columna][columna])
        for fila in range(columna + 1, m):
            val = Ac[fila, columna] / Ac[columna, columna]
            Ac[fila, columna] = val 
            cant_op += 1

            
            for k in range(columna+1, n):
                Ac[fila, k] = Ac[fila, k] - val * Ac[columna, k]
                cant_op += 2
            

    ## La L resultante tiene que ser matriz diagonal. Y después tener lo que está en i > j de Ac
    L  = np.zeros((n, m))

    for i in range(n):
        for j in range(m):
            if i == j:
                L[i][j] = 1
            elif i>j:
                L[i][j] = Ac[i][j]
                Ac[i][j] = 0

    U = Ac.copy()

            
    return L, U, cant_op

"""
    b) Pruebe la descomposición LU para matrices generadas al azar de n x n y grafique el error cometido al aproximar A = LU conforme crece el número de operaciones.
    Para esto realice un gráfico de ||A-LU|| (error absoluto) para una norma de su preferencia, en función de n. 

    Realicen el gráfico en escala log log y estimar visualmente el pendiente de la misma.

    Voy a generar 10 matrices de n x n, y generar para cada una la matriz LU. 
    Luego, mostraré el error absoluto de cada una.

    Lo que muestra el gráfico de este ejercicio es algo importante: en matrices más grandes, necesitamos más operaciones. Por lo tanto, el crecimiento del error se va arrastrando cada vez más.    

    No obstante, al observar el gráfico vemos que si bien el error crece, crece en escala particularmente pequeña. Los valores van desde 10e-16 y 10e-12.

    ¿Por qué nos importa la cantidad de operaciones? Por esto
    Ac[fila, k] = Ac[fila, k] - val * Ac[columna, k]

    Usamos algo que computamos antes, en cada iteración. Si en cada iteración hay error, acumulamos error cada vez más. Notar que si encima los números son feos, entonces peor. 

    
"""

def estimarError(sizes):
    errores = []
    operaciones = []
    for n in sizes:
        matrix = np.random.rand(n, n)
        L, U, cant_ops = calculaLU(matrix)
        matrix_reconstruida = L @ U 
        error = norma1(matrix - matrix_reconstruida) ##la hicimos en el labo3
        errores.append(error)
        operaciones.append(cant_ops)

    plt.figure(figsize=(8, 6))
    plt.loglog(operaciones, errores, marker='o', linestyle='-', color='b')
    
    plt.xlabel("Número de operaciones (cant_ops)")
    plt.ylabel("Error de aproximación ||A - LU|| (Norma Exacta)")
    plt.title("Crecimiento del error en la descomposición LU")
    plt.grid(True, which="both", ls="--")
    plt.show()
    
    return operaciones, errores

print(estimarError([5, 10, 20, 50, 100, 200]))
