import numpy as np 

def traspuesta(A):
  # More columns than rows
  if(A.shape[0] < A.shape[1]):
    matrix_b = np.zeros((A.shape[1], A.shape[0]))
    for i in range(A.shape[1]): 
        matrix_b[i, :] = A[:, i]
    return matrix_b
  
  # More rows than columns
  if(A.shape[0] > A.shape[1]):
    matrix_b = np.zeros((A.shape[1], A.shape[0]))
    for i in range(A.shape[0]): 
        matrix_b[:, i] = A[i, :]
    return matrix_b
  
  # Equal amount of rows and columns
  matrix_b = np.zeros((A.shape[0], A.shape[1]))
  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        matrix_b[i][j] = A[j][i]
  return matrix_b
        


def QR_con_GS(A, tol=1e-12, retorna_nops= False):
    dimension = A.shape[0]
    if A is None:
        return False 
    if A.shape[0] != A.shape[1]:
        return False
    
    Q = np.zeros((dimension, dimension))

    # Columnas de Q
    q1_normalizado = norma(A[:, 0], 2) #Columna 0
    Q[:, 0] = A[:, 0] / q1_normalizado 
    
    # Elementos de R
    R = np.zeros((dimension, dimension))
    R[0][0] = q1_normalizado

    for j in range(1, dimension):
        qjmoño = A[:, j] #Columna j-esima
        for k in range(j):
            qk = Q[:, k]
            R[k][j] = qk @ qjmoño
            qjmoño = qjmoño - (R[k][j] * qk)
        R[j][j] = norma(qjmoño, 2)
        if R[j, j] < tol:
            return False
        Q[:, j] = qjmoño / R[j][j]
    
    return Q, R
    

def norma(x, p):
    norma = 0
    for i in range(x.shape[0]):
        norma += abs(x[i]) ** p
    
    return norma**(1/p)