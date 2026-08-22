import numpy as np

# (fila, columna)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr = np.array([1, 2, 3])
non_squared = np.array([[1, 2], [3, 4], [5, 6]])
trasposed_matrix = np.array([[1, 1, 5], [1, 2, 3], [5, 3, 4]])

def esCuadrada(A):
  return A.shape[0] == A.shape[1]

assert(esCuadrada(matrix) == True)
assert(esCuadrada(non_squared) == False)

## Creo nueva Matriz B con misma dimensión que A. Podemos asumir que A es una matriz de numpy y todas sus filas tienen la misma cantidad de elementos.
def crearMatrizConDimensionesDe(A):
  return np.zeros((A.shape[0], A.shape[1]))

def crearMatrizCuadradaConDimension(n):
  return np.zeros((n, n))

def triangSup(A):
  if not(esCuadrada(A)):
    return "Invalid Square Matrix"
  matrix_b = crearMatrizConDimensionesDe(A)

  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      if j > i:
        matrix_b[i][j] = A[i][j]

  print(A)
  print(matrix_b)

print(triangSup(matrix))

def triangInf(A):
  if not(esCuadrada(A)):
    return "Invalid Square Matrix"
  matrix_b = crearMatrizConDimensionesDe(A)

  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      if j <= i:
        matrix_b[i][j] = A[i][j]

  print(A)
  print(matrix_b)

print(triangInf(matrix))

def diagonal(A):
  if not(esCuadrada(A)):
    return "Invalid Square Matrix"
  matrix_b = crearMatrizConDimensionesDe(A)

  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      if j == i:
        matrix_b[i][j] = A[i][j]

    print(A)
    print(matrix_b)

print(diagonal(matrix))

#Traza: solo matrices cuadradas. Es la suma de la diagonal.
def traza(A):
  if not(esCuadrada(A)):
    return "Invalid Square Matrix"
  sum = 0

  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      if j == i:
        sum+= A[i][j]

  return sum

print(traza(matrix))

#Traspuesta: cambiar filas x columnas y viceversa.
def traspuesta(A):
  matrix_b = crearMatrizConDimensionesDe(A)

  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      matrix_b[j][i] = A[i][j]

  print(A)
  print(matrix_b)
  return matrix_b

print(traspuesta(matrix))

#Matriz Simétrica: A = At (t: traspuesta)
def esSimetrica(A):
  return np.array_equal(A, traspuesta(A))

assert(esSimetrica(matrix) == False)
assert(esSimetrica(trasposed_matrix) == True)

## A = n x m, x = m x 1. Devolver el vector resultado de longitud n x 1.
def calcularAx(A, x):
  matrix_b = np.zeros((A.shape[1]))

  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        matrix_b[i] += A[i][j] * x[j]

  print(A)
  print(x)
  print(matrix_b)
  return matrix_b

## (1*1) + (2*2) + (3*3) = 15
## (4*1) + (5*2) + (6*3) = 32
## (7*1) + (8*2) + (9*3) = 50

assert(np.array_equal(calcularAx(matrix, arr), np.array([14, 32, 50])))

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def intercambiarFilas(A, i, j):
  for k in range(A.shape[0]):
    for l in range(A.shape[1]):
      if i == k:
        old = A[j][l]
        A[j][l] = A[i][l]
        A[i][l] = old

  print(A)

print(matrix)
intercambiarFilas(matrix, 0, 1)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

##Multiplicar la fila entera de i, por j*s.
def sumar_fila_multiplo(A, i, j, s):
  for k in range(A.shape[0]):
    for l in range(A.shape[1]):
      if i == k:
        value = A[j][l] * s ##ValFilaColumna*s. Ahora lo sumo con el de i j.
        A[i][l] = A[i][l] + value
  print(A)

sumar_fila_multiplo(matrix, 0, 1, 2)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_dominante = np.array([[100, 0, 0], [0, 150, 0], [0, 0, 200]])

# Si la suma de la diagonal es mayor que la suma de cada fila (con valores absolutos).
def esDiagonalmenteDominante(A):
    sum_filas = np.zeros(A.shape[0])

    for i in range(A.shape[0]):
      sum_fila = 0
      for j in range(A.shape[1]):
        if j!=i:
          sum_fila += (abs(A[i][j]))
      if abs(A[i][i]) <= sum_fila:
        return False
      

    return True

assert(esDiagonalmenteDominante(matrix) == False)
assert(esDiagonalmenteDominante(matrix_dominante) == True)

def crearMatrizCuadradaDesdeVector(A):
  return np.zeros((A.shape[0], A.shape[0]))

# Ej.: v = [1, 2, 3] la matriz es [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
def matriz_circulante(v):
  matrix_circulante = crearMatrizCuadradaDesdeVector(v)

  for i in range(matrix_circulante.shape[0]):
    for j in range(matrix_circulante.shape[1]):
      matrix_circulante[i][j] = v[(i+j) % matrix_circulante.shape[0]]

  print(matrix_circulante)

matriz_circulante(np.array([1, 2, 3]))
# v = [1, 2, 3]
# m = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]

def matrizVandermonde(v):
  matriz_vandermonde = crearMatrizCuadradaDesdeVector(v)
  for i in range(len(v)):
    for j in range(len(v)):
        matriz_vandermonde[i][j] = v[j]**i

"""
Solución 1: más eficiente, puedo ir pisando los valores. No necesito guardar tantas cosas.
Me dan n. Tengo que calcular Fk+1/Fk.
F0 = 0, F1 = 1.
Fk+1 = Fk + Fk-1

Ej.: F2 = F1 + F0 = 1 + 0 = 1, F3 = F2 + F1

Osea me tengo que guardar Fk+1 y Fk. Podria tener los dos valores en una matriz de 1 columna y 2 filas.
Ej.: arranco con (Fk, Fk-1) = (1, 0).
Para F3 tengo = (1, 1).
Para F4 tengo = (2, 1)
Para F5 tengo = (3, 2)

En cada paso hacemos Fk-1 = Fk y Fk = Fk+1.

Preguntar: ¿este lo puedo dejar así o sí o si tengo que usar dos matrices?
"""
def numeroAureo(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  matriz_base = np.array([[1], [0]]);
  for i in range(n):
    val = matriz_base[0][0] + matriz_base[1][0]
    matriz_base[1][0] = matriz_base[0][0]
    matriz_base[0][0] = val

  return matriz_base[0][0]/matriz_base[1][0]

## Solución 2: me fuerzo a usar matrices.
def numeroAureo2(n):
    F = np.array([1, 0])

    for i in range(n):
        F = calcularAx([
            F[0] + F[1],
            F[0]
        ])

    return F[0] / F[1]

assert numeroAureo(1) == 1
assert numeroAureo(2) == 2
assert numeroAureo(3) == 1.5
assert numeroAureo(4) == 5/3
assert numeroAureo(5) == 8/5
assert numeroAureo(6) == 13/8
assert numeroAureo(7) == 21/13
assert numeroAureo(8) == 34/21
assert numeroAureo(9) == 55/34
assert numeroAureo(10) == 89/55

def matrizFibonacci(n):

    matriz = crearMatrizCuadradaConDimension(n)

    if n == 0:
        return matriz

    matriz[0][0] = 0

    if n > 1:
        matriz[0][1] = 1
        matriz[1][0] = 1

        for j in range(2, n):
            matriz[0][j] = matriz[0][j-1] + matriz[0][j-2]

        for i in range(2, n):
            matriz[i][0] = matriz[i-1][0] + matriz[i-2][0]

        for i in range(1, n):
            for j in range(1, n):
                matriz[i][j] = matriz[i-1][j] + matriz[i-1][j-1]

    return matriz

assert np.array_equal(
    matrizFibonacci(1),
    np.array([
        [0]
    ])
)

assert np.array_equal(
    matrizFibonacci(2),
    np.array([
        [0, 1],
        [1, 1]
    ])
)

assert np.array_equal(
    matrizFibonacci(3),
    np.array([
        [0, 1, 1],
        [1, 1, 2],
        [1, 2, 3]
    ])
)

assert np.array_equal(
    matrizFibonacci(4),
    np.array([
        [0, 1, 1, 2],
        [1, 1, 2, 3],
        [1, 2, 3, 5],
        [2, 3, 5, 8]
    ])
)

assert np.array_equal(
    matrizFibonacci(5),
    np.array([
        [0, 1, 1, 2, 3],
        [1, 1, 2, 3, 5],
        [1, 2, 3, 5, 8],
        [2, 3, 5, 8, 13],
        [3, 5, 8, 13, 21]
    ])
)

def matrizHilbert(n):
  matriz_hilbert = crearMatrizCuadradaConDimension(n)

  for i in range(n):
    for j in range(n):
      matriz_hilbert[i][j] = 1/(i+j+1)

  return matriz_hilbert

assert np.allclose(
    matrizHilbert(1),
    np.array([
        [1]
    ])
)

assert np.allclose(
    matrizHilbert(2),
    np.array([
        [1,   1/2],
        [1/2, 1/3]
    ])
)

assert np.allclose(
    matrizHilbert(3),
    np.array([
        [1,   1/2, 1/3],
        [1/2, 1/3, 1/4],
        [1/3, 1/4, 1/5]
    ])
)

"""
17. Usando las funciones previamente desarrolladas donde sea posible, escriba una rutina que calcule los valores entre -1 y 1 de los siguientes polinomios.
a. x**5 - x**4 + x**3 - x**2 + x**1 - 1

Grafique el valor de los polinomios en el rango indicado, y calcule la cantidad de operaciones necesarias y el espacio en memoria para generar 100 puntos equiespaciados entre -1 y 1.
¿Cómo crecen estos valores con n? ¿Qué modificarı́a para hacer el cálculo más eficiente?
Podría armar una matriz con los valores tipo: [(a ** 5, - a ** 4, a ** 3, - a ** 2, a, -1)] [(x)]

No hace falta, puedo usar linspace, pasar la función lambda y plotearlo.

Preguntar: 
1. ¿Más eficiente con respecto a qué? en la diapo del labo dice que nos interesa el "tiempo de cómputo" y "la memoria" utilizada. 
2. ¿Como es como crecen los valores, esto es analizar complejidad también? no entiendo la pregunta.

1. Tenemos que evaluarlo en 100 puntos (-1 a 1). Para un solo x, tenemos m operaciones, mientras que para todos los x tendríamos O(nm) operaciones.
Notar que m serían: m potencias x**k, m multiplicaciones por los coeficientes y m sumas.
Esto crece muy feo si crece n, ya que m estaría fijo en este polinomio. Lo que podría variar es cuantos puntos pedimos evaluar.

En el primer polinomio, m está fijo con m = 5.
En el segundo polinomio, m está fijo con m = 2.
En el tercer polinomio, m está fijo con m = 10.
Si tuviesemos alguna variable tipo x ** k, con k algún número natural, tendríamos que considerar que podría ser muy grande.

"""

import matplotlib.pyplot as plt


def calcular_polinomio():
  p = lambda x: x**5 - x**4 + x**3 - x**2 + x - 1
  q = lambda x: x**2 + 3
  r = lambda x: x**10 - 2

  x = np.linspace(-1, 1, 100)
  y = p(x)
  z = q(x)
  w = r(x)

  plt.plot(x, y)
  plt.plot(x, z)
  plt.plot(x, w)

  plt.show()

calcular_polinomio()



"""
18: Modificar la función row_echelon de manera que evalue en cada pivot si no hay otro elemento de la misma columna con módulo mayor (en valor absoluto). En caso afirmativo, hacer el swap de las filas.
Esta operatoria permite tener mayor estabilidad numérica.
1. Agarro pivot de cada fila.
2. Me fijo si en esa columna no hay otro elemento con módulo mayor. Si hay, detectar esa fila y hacer el swap. Puedo usar: def intercambiarFilas(A, i, j)
"""
def row_echelon(A):
    A = [row[:] for row in A]
    rows = len(A)
    cols = len(A[0])

    pivot_row = 0

    for col in range(cols):
        pivot = None
        for row in range(pivot_row, rows):
          if A[row][col] != 0:
              if pivot is None:
                  pivot = row
              elif abs(A[row][col]) > abs(A[pivot][col]):
                  pivot = row

        if pivot is None:
            continue


        intercambiarFilas(A, pivot_row, pivot)

        for row in range(pivot_row + 1, rows):
            factor = A[row][col] / A[pivot_row][col]

            for j in range(col, cols):
                A[row][j] -= factor * A[pivot_row][j]

        pivot_row += 1

        if pivot_row == rows:
            break

    return A