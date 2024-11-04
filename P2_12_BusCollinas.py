import random

def hill_climbing(initial_state, evaluation_function, max_iterations=1000):
    """
    Realiza la búsqueda de ascensión de colinas.

    Parámetros:
    - initial_state: Estado inicial.
    - evaluation_function: Función que evalúa el estado y devuelve su valor.
    - max_iterations: Número máximo de iteraciones.

    Retorna:
    - El estado que representa la mejor solución encontrada.
    """
    current_state = initial_state
    current_value = evaluation_function(current_state)

    for iteration in range(max_iterations):
        # Generar un vecino aleatorio
        neighbor = current_state + random.uniform(-1, 1)  # Pequeño cambio aleatorio
        neighbor_value = evaluation_function(neighbor)

        # Si el vecino es mejor, hacemos el ascenso
        if neighbor_value > current_value:
            current_state = neighbor
            current_value = neighbor_value
            print(f"Iteración {iteration}: Mejorado a {current_state} con valor {current_value}")

    return current_state

def evaluation_function(x):
    """
    Función de evaluación: f(x) = -x^2 + 10, donde queremos maximizar f(x).

    Parámetros:
    - x: Estado actual.

    Retorna:
    - Valor de la función en x.
    """
    return -x**2 + 10

# Estado inicial
initial_state = random.uniform(-10, 10)  # Generar un estado inicial aleatorio
print(f"Estado inicial: {initial_state}")

# Ejecutar la búsqueda de ascensión de colinas
best_state = hill_climbing(initial_state, evaluation_function)
print(f"Mejor estado encontrado: {best_state} con valor {evaluation_function(best_state)}")
