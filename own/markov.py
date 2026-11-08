import numpy as np

"""
Ejemplo de código de mi clase de Markov.
Cada año, 1/10 personas que no están en california se mueven a california y 2/10 personas que están en california se mueven a otro estado. 
"""

P = np.array([[0.8, 0.1], [0.2, 0.9]])
#print(P)

"""
¿Cómo es la probabilidad de que una persona que vive en california se mueva a otro estado después de 3 años?
"""
P3 = np.linalg.matrix_power(P, 3)
#print(P3)

"""
¿Y en 50 años? ¿Y en 100?
"""
P50 = np.linalg.matrix_power(P, 50)
P100 = np.linalg.matrix_power(P, 100)
#print(P50)
#print(P100)

"""
¿Y nuestros datos iniciales? ¿Cómo se distribuyeron? 
"""
v = np.array([0.5, 0.5])
#print(v)

V50 = P50 @ v 
#print(V50)

V100 = P100 @ v 
#print(V100)

P1000 = np.linalg.matrix_power(P, 1000)
V1000 = P1000 @ v
#print(V1000)

"""
Definimos V^{\infty} = lim_{n \to \infty} V^{(n)}.
Por propiedad, tenemos que A v^{\infty} = v^{\infty}. Es decir, v^{\infty} es un autovector de A y está asociado al autovalor 1.
"""

w, V = np.linalg.eig(P) #Devuelve los autovectores normalizados en norma 1, pero nosotros lo buscamos en la norma suma porque es un vector de probabilidad.
v = V[:, np.argmax(w)]   
v = v / v.sum()
print(v)  