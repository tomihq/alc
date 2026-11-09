import numpy as np

m_ratones = np.array([[0.25, 0.5, 0.5, 0.5],
                      [0.25, 0.5, 0,   0  ],
                      [0.25, 0,   0.5, 0  ],
                      [0.25, 0,   0,   0.5]])
v_0 = np.array([20, 0, 0, 0])

# Inciso b: v^{4} = P^4 v^0
v_4 = np.linalg.matrix_power(m_ratones, 4) @ v_0
print("v_4 =", v_4)

# Inciso c: estado de equilibrio (autovector de lambda = 1, normalizado a suma 1)
autovalores, autovectores = np.linalg.eig(m_ratones)
print("autovalores =", np.round(autovalores, 6))

i = np.argmin(np.abs(autovalores - 1))   # índice del autovalor 1
w = np.real(autovectores[:, i])
w = w / w.sum()                          # normalizar: suma 1 (también arregla el signo)
print("w =", w)                          # esperado: [0.4, 0.2, 0.2, 0.2]
print("P w == w ?", np.allclose(m_ratones @ w, w))

# Inciso d: P^∞ (todas las columnas iguales a w)
P_inf = np.tile(w.reshape(-1, 1), (1, 4))
print("P_inf =\n", P_inf)

