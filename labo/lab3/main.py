from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

"""
  Ejercicio 1:
    a) Realizar una funcion norma(x, p) que reciba un vector x (un objeto iterable) y una norma p, y retorne su norma
    b) Una funcion normaliza(X, p) que reciba una lista de vectores X y una norma p, y retorne una lista Y donde cada elemento corresponde a normalizar
    los elementos de X con la norma p.
    Emplee la función construida para graficar en un mismo plot, los vectores con norma 1 de R2
    segun las normas p = 1, 2, 5, 10, 100, 200.
    Identifique a qué norma funcional converge la norma para valores de p a +inf.

    Muestre gráficamente que ese límite puede expresarse con la norma infinito.

    c) Modifique la función norma(x, p) para que pueda recibir el argumento p='inf'
"""

# Calcula la norma p
def norma(x, p):
  sum = 0
  if p == 'inf':
    return max(abs(xi) for xi in x)
  for i in range(x.shape[0]):
    sum+= abs(x[i])**p

  return sum**(1/p)

print("Ejercicio 1.a.",  norma(np.array([0.1, 0.25, 0.3]), 1))

# Calcula la norma p
def normaliza(X, p):
    x_normalizado = []

    for x in X:
        vector = x / norma(x, p)
        x_normalizado.append(vector)

    return x_normalizado


print("Ejercicio 1.b ", normaliza([np.array([0.1, 0.1, 0.1]), np.array([0.1, 0.2])], 1))



ps = [1, 2, 5, 10, 100, 200]

# Puntos de R2
X = np.random.uniform(-10, 10, (1000, 2))


plt.figure(figsize=(8, 8))

for p in ps:
    # Para cada x, buscamos y tal que ||(x,y)||_p = 1
    Y = normaliza(X, p)

    W = [y[0] for y in Y]
    Z = [y[1] for y in Y]


    plt.plot(W, Z, marker='o', linestyle='', label=f'p = {p}')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Vectores de R² con norma p igual a 1')
plt.axis('equal')
plt.grid()
plt.legend()
plt.show()


# La norma infinito es tomar como norma el ultimo valor
def norma_inf(x, p):
  sum = 0
  if p == np.inf:
        return max(abs(xi) for xi in x)
  for i in range(x.shape[0]):
    sum+= abs(x[i])**p

  return sum**(1/p)

def normalizar_con_inf(X, p):
    x_normalizado = []

    for x in X:
        x_normalizado.append(np.array(x) / norma_inf(x, p))

    return x_normalizado


ps = [1, 2, 5, 10, 100, 200, np.inf]

# Puntos de R2
X = np.random.uniform(-10, 10, (1000, 2))


plt.figure(figsize=(8, 8))

for p in ps:
    # Para cada x, buscamos y tal que ||(x,y)||_p = 1
    Y = normalizar_con_inf(X, p)

    W = [y[0] for y in Y]
    Z = [y[1] for y in Y]


    plt.plot(W, Z, marker='o', linestyle='', label=f'p = {p}')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Vectores de R² con norma p igual a 1')
plt.axis('equal')
plt.grid()
plt.legend()
plt.show()

def normaMatMC(A, q, p, Np):
  max = 0
  n = A.shape[0]
  max_v = np.zeros(n)
  for i in range(0, Np):
    x = np.random.rand(n)

    val = norma(A @ x, q) / norma(x, p)
    if val > max:
      max = val
      max_v = x


  return [max, max_v / norma(max_v, p)]

nMC = normaMatMC(A=np.eye(2),q=2,p=1,Np=100000)

"""
Aclaró un profesor el enunciado: te pueden pedir norma 1, la infinito o ambas.
"""
def normaExacta(A, p=[1, 'inf']):

    def norma1():
        return max(sum(abs(A[i][j]) for i in range(A.shape[0]))
                   for j in range(A.shape[1]))

    def normainf():
        return max(sum(abs(A[i][j]) for j in range(A.shape[1]))
                  for i in range(A.shape[0]))

    if isinstance(p, list):
        resultado = []

        for norma in p:
            if norma == 1:
                resultado.append(norma1())
            elif norma == 'inf':
                resultado.append(normainf())

        return resultado

    if p == 1:
        return norma1()

    if p == 'inf':
        return normainf()

"""
  La definición de condMc(A, p) es la norma de la matriz A * 
  la norma de la matriz inversa A en norma P.

  Notar que condMC es basado en aproximaciones de montecarlo.
"""
def condMC(A, p):
  inv = np.linalg.inv(A)
  norma_a = normaMatMC(A, p, p, 100000)[0]
  norma_inv_a = normaMatMC(inv, p, p, 100000)[0]

  return norma_a * norma_inv_a

"""
    Este utiliza una norma exacta. 
"""
def condExacto(A, p):
  inv = np.linalg.inv(A)
  norma_a = normaExacta(A, p)
  norma_inv_a = normaExacta(inv, p)

  return norma_a * norma_inv_a

