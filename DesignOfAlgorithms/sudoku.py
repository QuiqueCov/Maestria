import pdb
def condiciones(tablero, fila, col, num):
    # Condicion 1:
    # Checar la fila
    if num in tablero[fila]:
        return False

    # checar la columna
    for i in range(9):
        if tablero[i][col] == num:
            return False

    # CHECAR LOS CUADRANTES
    start_fila = (fila // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_fila, start_fila + 3):
        for j in range(start_col, start_col + 3):
            if tablero[i][j] == num:
                return False

    return True

def buscar(sudoku):
    for renglon in range(9):
        for columna in range(9):
            # aqui para no dejar vacio, donde es literalmente vacio, 
            # introduje el 0 como valor equivalente a vacio
            if sudoku[renglon][columna] == 0:
                return renglon, columna  # donde se ubica, renglon o columna
    return None  # Si no, regreso none


def resolver_sudoku(sudoku):
    vacia = buscar(sudoku)# busco los 0
    if not vacia:
        return True  # Este lo puse para salir 

    fila, col = vacia

    for num in range(1, 10): # Validos 1 -9
        if condiciones(sudoku, fila, col, num):
            sudoku[fila][col] = num # prueba con el numero 
            if resolver_sudoku(sudoku):
                return True
            sudoku[fila][col] = 0 # si no funciona, se descarta "backstracking"

    return False

def imprimir_sudoku(sudoku): # esta ultima funcion la investigue para que se imprimiera en un formato sudoku
    resolver_sudoku(sudoku)
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Imprime una línea divisoria cada 3 filas
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Imprime una barra vertical cada 3 columnas
            if j == 8:
                print(sudoku[i][j])
            else:
                print(sudoku[i][j], end=" ")

sudoku1 =[
    [5,0,0,9,1,3,7,2,0], # R1
    [3,0,0,0,8,0,5,0,9], # R2
    [0,9,0,2,5,0,0,8,0], # R3
    [6,8,0,4,7,0,2,3,0], #R4
    [0,0,9,5,0,0,4,6,0], #R5
    [7,0,4,0,0,0,0,0,5], #R6
    [0,2,0,0,0,0,0,0,0], #R7row
    [4,0,0,8,9,1,6,0,0], #R8
    [8,5,0,7,2,0,0,0,3]  #R9
]
sudoku2 =[
    [6,9,0,0,0,0,7,0,0], # R1
    [0,0,0,0,9,6,0,0,0], # R2
    [0,8,0,7,5,3,0,9,0], # R3
    [0,2,0,3,7,4,5,6,1], #R4
    [3,6,0,0,0,5,0,2,0], #R5
    [0,0,0,9,6,0,3,7,8], #R6
    [0,0,6,0,3,1,0,8,4], #R7row
    [0,4,5,8,0,7,6,0,0], #R8
    [0,0,0,0,0,0,0,5,7]  #R9
]
print("SUDOKU1")
imprimir_sudoku(sudoku1)
print("\n\nSUDOKU2")
imprimir_sudoku(sudoku2)
