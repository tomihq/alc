import numpy as np 

def error(x, y):
    x = np.float64(x)  
    return abs(x - y)

def error_relativo(x, y):
  x = np.float32(x)

  return abs(x-y) / abs(x)

def matricesIguales(A, B):

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if error(A[i, j], B[i, j]) > np.float64(0.7e-1):
                return False

    return True

def multiplicar_matrices(A, B):
    matrix = np.zeros((A.shape[0], A.shape[1]))

    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                matrix[i, j] += A[i, k] * B[k, j]

    return matrix


def rota(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

def escala(s):
  matrix = np.zeros((len(s), len(s)))
  for i in range(len(s)):
        matrix[i][i] = s[i]
  
  return matrix

def rota_y_escala(theta, s):
  matrix_rotada = rota(theta)
  matrix_escalada = escala(s)

  return multiplicar_matrices(matrix_escalada, matrix_rotada)


def afin(theta, s, b):
    matriz_rotada_escalada = rota_y_escala(theta, s)
    
    matriz = np.array([
        [matriz_rotada_escalada[0, 0], matriz_rotada_escalada[0, 1], b[0]],
        [matriz_rotada_escalada[1, 0], matriz_rotada_escalada[1, 1], b[1]],
        [0, 0, 1]
    ])

    return matriz

def trans_afin(v, theta, s, b):
    matriz = afin(theta, s, b)

    v_extendido = np.array([
        [v[0]],
        [v[1]],
        [1]
    ])

    resultado = multiplicar_matrices(matriz, v_extendido)

    return resultado[:2, 0]
