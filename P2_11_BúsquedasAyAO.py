import heapq

def heuristic(node, goal, heuristics):
    """
    Calcula el valor heurístico de un nodo dado el nodo objetivo.
    formula: f(n)=g(n)+h(n)
    Parámetros:
    - node: Nodo actual.
    - goal: Nodo objetivo.
    - heuristics: Diccionario con valores heurísticos para cada nodo.

    Retorna:
    - Valor heurístico del nodo.
    """
    return heuristics.get(node, float('inf'))

def a_star_search(graph, start, goal, heuristics):
    """
    Realiza la búsqueda A*.

    Parámetros:
    - graph: Diccionario representando el grafo con listas de adyacencia y costos.
    - start: Nodo inicial.
    - goal: Nodo objetivo.
    - heuristics: Diccionario con valores heurísticos para cada nodo.

    Retorna:
    - Lista del camino desde el nodo inicial al objetivo si se encuentra, de lo contrario, None.
    """
    # Cola de prioridad para seleccionar el nodo con el menor costo estimado
    priority_queue = [(0 + heuristic(start, goal, heuristics), start)]
    # Costos acumulados desde el inicio a cada nodo
    g_costs = {start: 0}
    # Mapa de nodos padres para reconstruir el camino
    came_from = {}

    while priority_queue:
        # Extrae el nodo con el menor costo estimado
        current_f, current = heapq.heappop(priority_queue)

        # Si hemos llegado al objetivo, reconstruimos el camino
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Regresar el camino en orden desde inicio a objetivo

        # Explorar los vecinos del nodo actual
        for neighbor, cost in graph.get(current, {}).items():
            tentative_g_cost = g_costs[current] + cost

            # Si el vecino no ha sido visitado o se encontró un mejor camino
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                priority_queue.append((tentative_g_cost + heuristic(neighbor, goal, heuristics), neighbor))
                came_from[neighbor] = current

    # Si la cola se vacía sin encontrar el objetivo, no hay camino
    return None

# Grafo de ejemplo con costos
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'G': 1},
    'E': {'B': 5, 'G': 3},
    'F': {'C': 3, 'G': 6},
    'G': {'D': 1, 'E': 3, 'F': 6}
}

# Heurísticas: estimación de "distancia" al objetivo 'G'
heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 3,
    'F': 4,
    'G': 0  # La distancia heurística al objetivo es 0
}

# Prueba de búsqueda A* desde 'A' hasta 'G'
path = a_star_search(graph, 'A', 'G', heuristics)
print("Camino encontrado:", path if path else "No se encontró camino")
