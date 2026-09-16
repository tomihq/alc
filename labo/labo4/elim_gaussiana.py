import numpy as np

def elim_gaussiana(A):
    cant_op = 0
    m = A.shape[0]
    n = A.shape[1]
    Ac = A.copy()
    
    if m != n:
        print('Matriz no cuadrada')
        return

    for columna in range(m):
        
        if np.isclose(Ac[columna, columna], 0.0, rtol=1e-5):
            print('Pivote cero o cercano a cero.')
            return
            
        for fila in range(columna + 1, m):
            val = Ac[fila, columna] / Ac[columna, columna]
            Ac[fila, columna] = val 
            
            for k in range(columna+1, n):
                Ac[fila, k] = Ac[fila, k] - val * Ac[columna, k]
            
            
            cant_op += 1
            
    return Ac, cant_op

    