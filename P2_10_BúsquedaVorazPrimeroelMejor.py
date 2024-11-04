import heapq

def heuristic(node, goal, heuristics):
    """
    Calcula el valor heurístico de un nodo dado el nodo objetivo.

    Parámetros:
    - node: Nodo actual.
    - goal: Nodo objetivo.
    - heuristics: Diccionario con valores heurísticos para cada nodo.

    Retorna:
    - Valor heurístico del nodo.
    """
    return heuristics.get(node, float('inf'))

def greedy_best_first_search(graph, start, goal, heuristics):
    """
    Realiza una búsqueda voraz primero el mejor usando heurísticas.

    Parámetros:
    - graph: Diccionario representando el grafo con listas de adyacencia.
    - start: Nodo inicial.
    - goal: Nodo objetivo.
    - heuristics: Diccionario con valores heurísticos para cada nodo.

    Retorna:
    - True si encuentra un camino hacia el objetivo.
    - False si no encuentra ningún camino.
    """
    # Cola de prioridad para seleccionar el nodo con el menor valor heurístico
    priority_queue = [(heuristic(start, goal, heuristics), start)]
    # Conjunto de nodos visitados para evitar ciclos
    visited = set()

    while priority_queue:
        # Extrae el nodo con el valor heurístico más bajo
        _, current = heapq.heappop(priority_queue)
        print(f"Visitando: {current}")

        # Si hemos llegado al objetivo, terminamos
        if current == goal:
            print("Objetivo encontrado:", current)
            return True

        # Marcar el nodo como visitado
        visited.add(current)

        # Explorar los vecinos del nodo actual
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic(neighbor, goal, heuristics), neighbor))

    # Si la cola se vacía sin encontrar el objetivo, no hay camino
    return False

# Grafo de ejemplo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

# Heurísticas: estimación de "distancia" al objetivo 'G'
heuristics = {
    'A': 5,
    'B': 4,
    'C': 6,
    'D': 4,
    'E': 1,
    'F': 6,
    'G': 0  # La distancia heurística al objetivo es 0
}

# Prueba de búsqueda voraz primero el mejor desde 'A' hasta 'G'
found = greedy_best_first_search(graph, 'A', 'G', heuristics)
print("Resultado:", "Camino encontrado" if found else "Camino no encontrado")
