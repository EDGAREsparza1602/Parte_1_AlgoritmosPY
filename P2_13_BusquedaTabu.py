import random

def evaluate_solution(x):
    """
    Función de evaluación: f(x) = 2x + 15.
    Queremos maximizar esta función.

    Parámetros:
    - x: Estado actual.

    Retorna:
    - Valor de la función en x.
    """
    return 2 * x + 15

def get_neighbors(current_state):
    """
    Genera vecinos del estado actual.
    En este caso, generamos estados cercanos con un pequeño cambio aleatorio.

    Parámetros:
    - current_state: Estado actual.

    Retorna:
    - Lista de vecinos.
    """
    return [current_state + random.uniform(-1, 1) for _ in range(5)]

def tabu_search(initial_state, max_iterations=100, tabu_tenure=5):
    """
    Realiza la búsqueda tabú.

    Parámetros:
    - initial_state: Estado inicial.
    - max_iterations: Número máximo de iteraciones.
    - tabu_tenure: Tiempo que un movimiento permanece en la lista tabú.

    Retorna:
    - Mejor estado encontrado y su valor.
    """
    current_state = initial_state
    best_state = current_state
    best_value = evaluate_solution(best_state)
    
    # Lista tabú para almacenar soluciones recientes
    tabu_list = []
    
    for iteration in range(max_iterations):
        neighbors = get_neighbors(current_state)
        next_state = None
        next_value = float('-inf')

        # Encontrar el mejor vecino que no esté en la lista tabú
        for neighbor in neighbors:
            if neighbor not in tabu_list:
                neighbor_value = evaluate_solution(neighbor)
                if neighbor_value > next_value:
                    next_value = neighbor_value
                    next_state = neighbor

        # Si encontramos un nuevo estado, actualizamos el estado actual
        if next_state is not None:
            current_state = next_state
            # Actualizamos la mejor solución si es necesario
            if next_value > best_value:
                best_value = next_value
                best_state = next_state
            
            # Agregar el nuevo estado a la lista tabú
            tabu_list.append(current_state)
            # Mantener la lista tabú dentro del tamaño permitido
            if len(tabu_list) > tabu_tenure:
                tabu_list.pop(0)

            print(f"Iteración {iteration}: Mejorado a {current_state} con valor {best_value}")

    return best_state, best_value

# Estado inicial
initial_state = random.uniform(-10, 10)  # Generar un estado inicial aleatorio
print(f"Estado inicial: {initial_state}")

# Ejecutar la búsqueda tabú
best_state, best_value = tabu_search(initial_state)
print(f"Mejor estado encontrado: {best_state} con valor {best_value}")
