'''
Usando programacion dinamica:
Resolver el problema  de la mochilka,
Suponga  una capacidad maxima de 140 unidades.
¿Cual es el calor optimo de la mochila?
¿Cuales son los objetos que debemos de tomar?
+--------+-------+------+
| Objeto | Valor | Peso |
+--------+-------+------+
|   1    |   79  |  85  |
|   2    |   32  |  26  |
|   3    |   47  |  48  |
|   4    |   18  |  21  |
|   5    |   26  |  22  |
|   6    |   85  |  95  |
|   7    |   33  |  43  |
|   8    |   40  |  45  |
|   9    |   45  |  55  |
|  10    |   59  |  52  |
+--------+-------+------+
'''
import numpy as np

'''
 n = Numero de elementos
 w = pesos de los elementos
 v = valor de los elementos
 W= capacidad de la mochila
'''
'''
Mochila ejemplo
n = 4
w = [4, 3, 2, 3]
v = [3, 2, 4, 4]
W = 6 
'''
n = 10
w = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
v = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
W = 140
V = np.zeros((n+1, W+1))
for i in range(1, n+1):
    for x in range(0, W + 1):
        j = x - w[i-1]
        if j < 0:
            V[i ,x] = max(V[i-1, x], 0)
        else:
            V[i, x] = max(V[i-1,x], V[i-1, j] + v[i-1])

mochilaOptima = V[n, W]
elementos = []
x = W
'''
Lo que hago aqui es ver si el valor de v[i,x] es diferente de v[i-1,x]
el objeto ya esta incluido en el valor optimo,
'''
for i in range(n,0,-1): # aqui recorro n de atras hacia adelante
    if V[i, x] !=V[i-1, x]:
        elementos.append(i-1) # agergo el objeto
        x-=w[i-1] # aqui hago la resta a la capacidad de la mochila
# Aqui me di cuenta de que debia de sumarle 1 a los elementos, para que las 
#posiciones sean las correctas
for i in range(len(elementos)):
    elementos[i] += 1
# Imprimir los resultados
print(f"El valor optimo de la mochila es: {mochilaOptima}")
print(f"Los objetos que debemos de tomar son: {elementos}")
