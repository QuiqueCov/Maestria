'''
Usa programación dinámica para encontrar la parentización óptima de la sucesión de 
matrices multiplicándose p=[5, 10, 3, 12, 5, 50, 6]. 
Entrega el mínimo de multiplicaciones escalares con el que se puede ejecutar dicha operación y explicita la parentización usada. Reporta tu código.
'''
import math

def matrix_chain(p):
    n = len(p) - 1  # El número de matrices es len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]  # Inicializa la tabla m con ceros
    s = [[0 for _ in range(n)] for _ in range(n-1)]  # Inicializa la tabla s

    for l in range(2, n + 1):
        for i in range(n - l + 1): 
            j = i + l - 1 
            m[i][j] = math.inf

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i + 1}", end="")  
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j) 
        print(")", end="")


# Ejemplo de clase
#p = [30, 35, 15, 5, 10, 20, 25] 
# ejemplo de tarea
p=[5, 10, 3, 12, 5, 50, 6]
m, s = matrix_chain(p)
print(m)
print_optimal_parens(s, 0, len(p) -2 )
