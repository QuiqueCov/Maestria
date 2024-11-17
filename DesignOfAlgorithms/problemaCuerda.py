'''
Encuentra para la cuerda de largo 11 cual sería el precio máximo para venderla, 
así como la descomposición óptima. Reporta tu código.
 +-------+--------+
| Largo | Precio |
+-------+--------+
|   1   |   1    |
|   2   |   4    |
|   3   |   10   |
|   4   |   12   |
|   5   |   15   |
|   6   |   20   |
|   7   |   21   |
|   8   |   32   |
|   9   |   31   |
|  10   |   41   |
|  11   |   51   |
+-------+--------+
    * Principios de la programacion dinamica:
        * 1.- Caracterizar la estructura de la solucion optima
        * 2.- Definir el valor de la solucion optima de forma recursiva
        * 3.- Computar el valor de una solucion optima
        * 4.- Construir la solucion optima con la informacion computada.
'''
import pdb


def cortarCuerda(tablaCuerda, L):
    # aqui creo la tabla donde se guardara la solucion optima
    solucionOptima = [0] * (L + 1)
    # aqui la tabla que guarda las "Coordenadas" de las soluciones optimas
    coordenada = [0] *(L +1)

    for i in range(1, L + 1):
        q = -1
        for j in range(1, i + 1):
            if q <(tablaCuerda[j-1] + solucionOptima[i-j]):
                q = tablaCuerda[j-1] + solucionOptima[i-j]
                coordenada[i] = j
        solucionOptima[j] = q
    # como se hacen los coortes
    print(f'Precio Maximo: {solucionOptima[L]}')
    cortes = []
    while L > 0:
        cortes.append(coordenada[L])
        L = L - coordenada[L]
    print(f'Descomposicion: {cortes}')


if __name__ == "__main__":
    # Esta es la tabla de la tarea
    tabla_Cuerda =[1,4,10,12,15,20,21,32,31,41,51]
    # Esta es la tabla del ejercicio de ejemplo 
    tablacuerdaEjem = [1,5,8,9,10,17,17,20,24,30]
    print(f'\n\nEjercicio de Tarea: \n{tabla_Cuerda}')
    cortarCuerda(tabla_Cuerda, 11)
    print(f'\n\nTabla Ejemplo Clase:\n{tablacuerdaEjem}')
    cortarCuerda(tablacuerdaEjem, 9)
