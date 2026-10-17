import numpy as np

########### To import other files ###############
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
#################################################
from lab3.main import norma
from lab0.lab0 import traspuesta
from labo6.main import diagRH


def numeros_al_azar(n):
    return np.random.rand(n, n)

"""
    Genero matriz nxn con valores entre 0 y 1. 
    Después normalizo cada columna. La suma de los valores de la columna tienen que sumar 1. Ej.: si la columna 1 suma 15 y tengo 3 valores, como hago para que sea 1? El 100% es 15, entonces en cada uno hago val/sumaTotal.
"""
def transiciones_al_azar_continuas(n): 
    A = numeros_al_azar(n)
    for j in range(n):
        A[:, j] = A[:, j] / norma(A[:, j], 1)
    return A
#print(transiciones_al_azar_continuas(3))

"""
    Generar una matriz de probabilidad de nxn. 
    Luego, si el elemento A[i][j] > threshold se hace 0. Notar que acá podría quedar una columna entera de 0's. Hay que tener en cuenta ese caso para poner un 1 por elección (para cumplir Markov)
    Luego, normalizo. 
"""
def transicion_al_azar_uniforme(n, threshold):
    A = numeros_al_azar(n)          

    for i in range(n):
        for j in range(n):
            if A[i][j] > threshold:
                A[i][j] = 0
            else:
                A[i][j] = 1

    for j in range(n):
        if A[:, j].sum() == 0:                  
            A[np.random.randint(n), j] = 1      
        A[:, j] = A[:, j] / norma(A[:, j], 1)

    return A

#print(transicion_al_azar_uniforme(3, 1e-1))

def nucleo(A, tol=1e-5): 
    A_traspose = traspuesta(A)
    B = A_traspose @ A 
    S, D = diagRH(B, tol)
    SKernel = []

    for j in range(D.shape[1]):
        if(abs(D[j][j])<tol):
             SKernel.append(S[:, j]) 

    return np.array(SKernel).reshape(-1, 1)