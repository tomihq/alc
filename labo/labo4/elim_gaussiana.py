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

def norma1(A):
        return max(sum(abs(A[i][j]) for i in range(A.shape[0]))
                   for j in range(A.shape[1]))

def normainf(A):
        return max(sum(abs(A[i][j]) for j in range(A.shape[1]))
                  for i in range(A.shape[0]))

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

"""
    2. Estudiar la relación entre la cantidad de operaciones para encontrar la factorización LU y el tamaño de la matriz.

    Propongo tomar una matriz sencilla que tenga LU y nos permita hacer operaciones triviales.
        -1 si i>j
        1 si i==j o j == n-1
        0 cc


    El algoritmo de la factorización LU aparenta ser determinístico en cantidad de pasos. Es decir, la decomposición es única, y por ende, la cantidad de operaciones para una misma matriz de dimensión n siempre será la misma.

    (Notar que la norma infinito de U_n de casualidad es 2^{n-1} porque la ultima columna va creciendo a su valor, y como la norma infinito es el valor más grande lo agarra cuando termina).

    ¿Podemos encontrar una función que nos diga en base al tamaño la cantidad de operaciones? hagamos matemática en base a mis datos de prueba.

    C(100) = 661650
    C(200) = 5313300

    Dupliqué el n, ¿por cuánto se multipla C(n)?
    C(200) / C(100) = 5313300 / 661650 aprox 8.03

    Ahora

    C(300) = 17954950

    C(300) / C(100) =  17954950 / 661650 aprox 27.14

    n -> 2n => C(n) -> 8C(n)
    n -> 3n => C(n) -> 27C(n)

    Entonces C(n) es aprox kC(n)

    ¿Pero cuánto vale k? ¡Despejemos para varios valores de n! Aprox para 10 valores me dió 0.6

    Entonces, la función aproximada es: C(n) = 0.665n^3 (véase el = como un aproximado, no como igualdad estricta)
    
"""
def relacionLUMatriz(sizes):
    cantidad_operaciones = []

    for n in sizes:
        matrix = np.zeros((n, n)) 

        for i in range(n):
            for j in range(n): 
                if i == j or j == n-1:
                    matrix[i][j] = 1
                elif i>j:
                    matrix[i][j] = -1
                else:
                    matrix[i][j] = 0
        
        L, U, cant_operaciones = calculaLU(matrix)
        print(n)
        norma_inf = normainf(U)
        cantidad_operaciones.append([n, cant_operaciones, norma_inf, 2**(n-1)])

    return cantidad_operaciones



#print(relacionLUMatriz([1, 2, 3, 4, 5, 10, 50, 100, 200, 250, 300]))

"""
    3. Calcular la solución de un sistema
        a) Ly = b, siendo L triangular inferior (forward sustitution)
        b) Ux = y, siendo U triangular superior (backward sustitution)
        c) Resolver un sistema Ax = b, utilizando las funciones de los ítems anteriores.

    Algunas aclaraciones: L y U son cuadradas.

    Si L es nxn, y se multiplica por y entonces y tiene dimensión n x 1 (es un vector). Por lo tanto, b es n x 1.

    Tuve que hacerme una formula para ver como hacer lo de forward sustitution, la dejo acá.
        A. coefx1A x1 = b[0]
        B. coefx1B x1 + coefx2B x2 = b[1]
        C. coefx1C x1 + coefx2C x2 + coefx2C x3 = b[2]

        y[0] = (b[0] / coefx1A)
        y[1] = (b[1] - coefx1B (y[0])) / coefx2B
        y[2] = (b[2] - coefx1C(y[0]) + coefx2C (y[1])

        Pienso directo en código ahora, usando las variables.
        y[2] = (b[2] - (L[2, 0] * y[0]) + (L[2, 1] * y[1])) / L[2][2]

        2 = fila
        0 = columna
        1 = moverte en otra columna

"""

def forward_sustitution(L, b):
    n = L.shape[0]
    y = np.zeros((n, 1))

    for i in range(n):
        der = b[i]
        acum = 0
        for j in range(n):
            acum += L[i][j] * y[j]
        y[i] = (der - acum) / L[i][i]
    
    return y

"""res = forward_sustitution(np.array([[2, 0, 0], [3, 1, 0], [4, 2, 5]]), np.array([[4], [7], [20]]))
print("L:", res[0])
print("y:", res[1])
print("b:", res[2])"""


def backward_sustitution(U, y):
    n = U.shape[0]
    x = np.zeros((n, 1))

    for j in range(n-1, -1, -1): #arranco en ultima columna
        der = y[j]
        acum = 0
        for i in range(j+1, n): #arranco en ultima fila
            acum += U[j][i] * x[i]

        x[j] = (der - acum) / U[j][j]
    
    return x
"""backward_sustitution(np.array([[2, 1, -1], [0, 3, 2], [0, 0, 4]]), np.array([[5], [7], [8]]))"""

def resolver_sistema(A, b):
    L, U, _ = calculaLU(A)

    y = forward_sustitution(L, b)
    x = backward_sustitution(U, y)

    vx = np.array([x[i][0] for i in range(x.shape[0])])
    return vx
