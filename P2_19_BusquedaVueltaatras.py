
# Ingenieria en Mecatronica

# Programa_Busqueda_Vuelta_Atras

def is_safe(board, row, col, n):
    # Verifica si es seguro colocar una reina en la posición (row, col)
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, n, solutions): # Esta función toma cuatro parámetros: board, que representa el tablero actual, row, que representa la fila actual en la que se está colocando una reina, n, que es el tamaño del tablero, y solutions, que es una lista para almacenar todas las soluciones encontradas
    if row == n: # Se verifica si se ha llegado al final del tablero (es decir, si row es igual a n). En este caso, todas las reinas se han colocado en posiciones válidas en el tablero y se ha encontrado una solución. Se copia el tablero actual en la lista de soluciones y se retorna
        solutions.append(board[:])
        return
    for col in range(n): # Se itera sobre todas las columnas del tablero (para la fila row actual)
        if is_safe(board, row, col, n): # Se verifica si es seguro colocar una reina en la posición (row, col) del tablero. Esto se hace llamando a una función is_safe, que aún no se proporciona, pero se espera que devuelva True si es seguro colocar una reina en esa posición y False de lo contrario
            board[row] = col # Si es seguro colocar una reina en la posición (row, col), se actualiza el tablero para reflejar esta colocación
            solve_n_queens_util(board, row + 1, n, solutions) # Se llama recursivamente a la función solve_n_queens_util para avanzar a la siguiente fila (row + 1) y continuar colocando reinas en el tablero

def solve_n_queens(n):
    solutions = [] # Se inicializa una lista solutions para almacenar todas las soluciones encontradas
    board = [-1] * n # Se inicializa una lista board de longitud n con -1, donde cada índice representa una fila del tablero y el valor en el índice representa la columna en la que se coloca una reina en esa fila
    solve_n_queens_util(board, 0, n, solutions) # Se llama a una función auxiliar solve_n_queens_util para encontrar todas las soluciones al problema de las N reinas. Se pasa el tablero inicializado, la fila actual (0 al principio), el tamaño del tablero (n) y la lista de soluciones
    return solutions # Se devuelven todas las soluciones encontradas

if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)
    print(f"Solutions for {n}-Queens:")
    for solution in solutions:
        print(solution)