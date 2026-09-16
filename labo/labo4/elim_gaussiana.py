import numpy as np

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
