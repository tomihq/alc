import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def pointsGrid(esquinas):
    # crear 10 lineas horizontales
    [w1, z1] = np.meshgrid(np.linspace(esquinas[0,0], esquinas[1,0], 46),
                        np.linspace(esquinas[0,1], esquinas[1,1], 10))

    [w2, z2] = np.meshgrid(np.linspace(esquinas[0,0], esquinas[1,0], 10),
                        np.linspace(esquinas[0,1], esquinas[1,1], 46))

    w = np.concatenate((w1.reshape(1,-1),w2.reshape(1,-1)),1)
    z = np.concatenate((z1.reshape(1,-1),z2.reshape(1,-1)),1)
    wz = np.concatenate((w,z))
                         
    return wz

## Lo que me están pidiendo acá básicamente es: T es una matriz cualquiera. Y wz son puntos.
## Estamos aplicando la transformación lineal T a los puntos contenidos en wz.
def proyectarPts(T, wz):
    assert(T.shape == (2,2)) # chequeo de matriz 2x2
    assert(T.shape[1] == wz.shape[0]) # multiplicacion matricial valida   
    xy = np.matmul(T, wz)
    return xy

          
def vistform(T, wz, titulo=''):
    # transformar los puntos de entrada usando T
    xy = proyectarPts(T, wz)
    if xy is None:
        print('No fue implementada correctamente la proyeccion de coordenadas')
        return
    # calcular los limites para ambos plots
    minlim = np.min(np.concatenate((wz, xy), 1), axis=1)
    maxlim = np.max(np.concatenate((wz, xy), 1), axis=1)

    bump = [np.max(((maxlim[0] - minlim[0]) * 0.05, 0.1)),
            np.max(((maxlim[1] - minlim[1]) * 0.05, 0.1))]
    limits = [[minlim[0]-bump[0], maxlim[0]+bump[0]],
               [minlim[1]-bump[1], maxlim[1]+bump[1]]]             

    fig, (ax1, ax2) = plt.subplots(1, 2)         
    fig.suptitle(titulo)
    grid_plot(ax1, wz, limits, 'w', 'z')    
    grid_plot(ax2, xy, limits, 'x', 'y')

    
def grid_plot(ax, ab, limits, a_label, b_label):
    ax.plot(ab[0,:], ab[1,:], '.')
    ax.set(aspect='equal',
           xlim=limits[0], ylim=limits[1],
           xlabel=a_label, ylabel=b_label)


def main():
    print('Ejecutar el programa')
    # generar el tipo de transformacion dando valores a la matriz T
    T = pd.read_csv('T.csv', header=None).values
    corners = np.array([[0,0],[100,100]])
    # corners = np.array([[-100,-100],[100,100]]) array con valores positivos y negativos
    wz = pointsGrid(corners)
    vistform(T, wz, 'Deformar coordenadas')
    
    
if __name__ == "__main__":
    main()

def multiplicar_matrices(A, B):
    # Verificar si las matrices son compatibles para la multiplicación
    if A.shape[1] != B.shape[0]:
        raise ValueError("Las matrices no son compatibles para la multiplicación")

    matrix = np.zeros((A.shape[0], A.shape[1]))

    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                matrix[i, j] += A[i, k] * B[k, j]

    return matrix

#theta es un ángulo en radianes. Ej.: rota(np.pi/2)
# La matriz de rotación es: (cos angulo -sin angulo, sin angulo cos angulo)
# Devuelve matriz 2x2
def rota(theta): 
  matrix = np.zeros((2,2))
  matrix[0, 0] = np.cos(theta)
  matrix[0, 1] = -np.sin(theta)
  matrix[1, 0] = np.sin(theta)
  matrix[1, 1] = np.cos(theta)
  return matrix


assert(np.allclose(rota(0), np.eye(2)))
assert(np.allclose(rota(np.pi/2), np.array([[0, -1],[1, 0]])))
assert(np.allclose(rota(np.pi), np.array([[-1, 0],[0, -1]])))


## s: es un vector de números. 
# Ej.: (2, 3) es basicamente armar (2x + 3y) = (2 0, 0 3) 
# Retorna matriz cuadrada de n x n.
def escala(s):
  matrix = np.zeros((len(s), len(s)))
  for i in range(len(s)):
        matrix[i][i] = s[i]
  
  return matrix


assert(np.allclose(escala([2,3]), np.array([[2,0],[0,3]])))
assert(np.allclose(escala([1,1,1]), np.eye(3)))
assert(
    np.allclose(escala([0.5,0.25]), np.array([[0.5,0],[0,0.25]]))
)

# Primero rota, y despues escala.
# Tengo que generar primero las dos matrices.
# Después hacer la multiplicación en orden. No es lo mismo escalar y rotar que rotar y escalar.
# Las multiplicaciones de matrices se aplican de DERECHA A IZQUIERDA.
def rota_y_escala(theta, s):
  matrix_rotada = rota(theta)
  matrix_escalada = escala(s)

  return multiplicar_matrices(matrix_escalada, matrix_rotada)

assert(
    np.allclose(rota_y_escala(0,[2,3]), np.array([[2,0],[0,3]]))
)
assert(np.allclose(
    rota_y_escala(np.pi/2,[1,1]), np.array([[0,-1],[1,0]])
))
assert(np.allclose(
    rota_y_escala(np.pi,[2,2]), np.array([[-2,0],[0,-2]])
))


"""
Parámetros
- theta: angulo
- s: vector de numeros (en R2)
- b: vector de números (en R2)

Retorno: matriz transformación de 3x3.
  1. Rotar el vector.
  2. Escalar el vector.
  3. Trasladar el vector.
  4. Extender la transformación de R2 a R3.

  Notar que el truco está en poner en la ultima columna de R3 el b[0] y el b[1]. Entonces después cuando inyectás los valores, los sumás a esos. 
"""
def afin(theta, s, b):
    # 1. Rotar y escalar el vector en R2
    matriz_rotada_escalada = rota_y_escala(theta, s)
    

    # 2. Trasladar el vector en R2
    #    v -> matriz_rotada_escalada @ v + b

    # 3. Extender la transformación de R2 a R3
    matriz = np.array([
        [matriz_rotada_escalada[0, 0], matriz_rotada_escalada[0, 1], b[0]],
        [matriz_rotada_escalada[1, 0], matriz_rotada_escalada[1, 1], b[1]],
        [0, 0, 1]
    ])

    return matriz

    assert(np.allclose(
    afin(0,[1,1],[1,2]),
    np.array([[1,0,1],
              [0,1,2],
              [0,0,1]])))
assert(np.allclose(afin(np.pi/2,[1,1],[0,0]),
    np.array([[0,-1,0],
              [1,0,0],
              [0,0,1]])))
assert(np.allclose(afin(0,[2,3],[1,1]),
    np.array([[2,0,1],
              [0,3,1],
              [0,0,1]])))

"""
  afin(theta, s, b) me devuelve 3x3.
  v es de R2, entonces necesito generar un vector capaz de que pueda multiplicarse con la matriz 3x3. Para eso necesito 3x3 y 3x1. Entonces me queda un vector final de 3x1. 
  Luego, como tengo que devolver en R2, me basta con elimianr la componente que agregue solamente para hacer la multiplicación.

  El truco es extender v, la hacés de 3x1, multiplicás, y después te quedás con los 2 que necesitás.
"""
def trans_afin(v, theta, s, b):
    matriz = afin(theta, s, b)

    v_extendido = np.array([
        [v[0]],
        [v[1]],
        [1]
    ])

    resultado = multiplicar_matrices(matriz, v_extendido)

    return resultado[:2, 0]

assert(np.allclose(
    trans_afin(np.array([1,0]), np.pi/2,[1,1],[0,0]),
    np.array([0,1])
))
assert(np.allclose(
    trans_afin(np.array([1,1]), 0,[2,3],[0,0]),
    np.array([2,3])
))
assert(np.allclose(
    trans_afin(np.array([1,0]), np.pi/2,[3,2],[4,5]),
    np.array([4,7])
))
