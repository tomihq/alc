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
    if A is None or A.shape[0] != A.shape[1]:
        return None

    n = A.shape[0]
    Q = np.zeros((dimension, dimension))
    R = np.zeros((dimension, dimension))
    nops = 0

    # Columnas de Q
    q1_normalizado = norma(A[:, 0], 2) #Columna 0

    if q1_normalizado < tol:
        return None

    nops += 2*n
    Q[:, 0] = A[:, 0] / q1_normalizado 
    
    # Elementos de R
    nops += n
    R[0][0] = q1_normalizado

    for j in range(1, dimension):
        qjmoño = A[:, j] #Columna j-esima
        for k in range(j):
            qk = Q[:, k]
            R[k][j] = qk @ qjmoño
            nops += 2*n - 1
            qjmoño = qjmoño - (R[k][j] * qk)
            nops += 2*n
        R[j][j] = norma(qjmoño, 2)
        nops += 2*n
        if R[j, j] < tol:
            return None
        Q[:, j] = qjmoño / R[j][j]
        nops += n

    
    R[abs(R) < tol] = 0
    
    if retorna_nops:
        return Q, R, nops
    return Q, R
    

def norma(x, p):
    norma = 0
    for i in range(x.shape[0]):
        norma += abs(x[i]) ** p
    
    return norma**(1/p)

def QR_con_HH(A, tol=1e-12, extras=False):
    if A is None:
        return None
    m, n = A.shape            
    if m < n:
        return None

    R = np.array(A)
    Q = np.eye(m)

    R_matrices = [R.copy()]
    Q_matrices = [Q.copy()]

    for k in range(n):
        x = R[k:, k]
        sign = 1.0 if x[0] >= 0 else -1.0
        alpha = -sign * norma(x, 2)

        e1 = np.zeros(m -k)
        e1[0] = 1.0
        u = x- alpha * e1
        norma_u = norma(u, 2)

        if norma_u > tol:
            u = u/norma_u
            uc = u.reshape(-1, 1)
            Hk = np.eye(m - k) - 2 * (uc @ traspuesta(uc))
            Hkmoño = np.eye(m)
            Hkmoño[k:, k:] = Hk
            R = Hkmoño @ R
            Q = Q @ traspuesta(Hkmoño)
        R_matrices.append(R.copy())
        Q_matrices.append(Q.copy())
    
    R[np.abs(R) < tol] = 0

    if extras:
        return Q, R, {'R_matrices': R_matrices, 'Q_matrices': Q_matrices}

    return Q, R

def calculaQR(A, metodo = 'RH', tol = 1e-12):
    if metodo == 'GS':
        return QR_con_GS(A, tol)
    elif metodo == 'RH':
        return QR_con_HH(A, tol)
    return None
