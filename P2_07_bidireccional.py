from collections import deque

def bidirectional_search(graph, start, goal):
    """
    Realiza una búsqueda bidireccional entre un nodo inicial y un nodo objetivo.

    Parámetros:
    - graph: Diccionario representando el grafo con listas de adyacencia.
    - start: Nodo inicial.
    - goal: Nodo objetivo.

    Retorna:
    - True si se encuentra un camino entre el nodo inicial y el nodo objetivo.
    - False si no se encuentra ningún camino.
    """

    # Si el nodo inicial es el mismo que el objetivo, no hay búsqueda que realizar
    if start == goal:
        return True

    # Inicializar las colas de búsqueda para ambos lados
    start_queue = deque([start])
    goal_queue = deque([goal])

    # Inicializar los conjuntos de visitados
    start_visited = {start}
    goal_visited = {goal}

    while start_queue and goal_queue:
        # Expansión desde el lado del inicio
        if expand_frontier(graph, start_queue, start_visited, goal_visited):
            return True

        # Expansión desde el lado del objetivo
        if expand_frontier(graph, goal_queue, goal_visited, start_visited):
            return True

    return False  # Si se terminan las búsquedas sin encontrarse

def expand_frontier(graph, queue, visited, other_visited):
    """
    Expande el frente de búsqueda desde un lado (inicio o objetivo).

    Parámetros:
    - graph: Diccionario representando el grafo.
    - queue: Cola de nodos a explorar en este lado.
    - visited: Conjunto de nodos visitados desde este lado.
    - other_visited: Conjunto de nodos visitados desde el otro lado.

    Retorna:
    - True si el frente de búsqueda se encuentra con el otro.
    - False si no se encuentra el otro frente.
    """
    current = queue.popleft()
    print(f"Visitando: {current}")

    for neighbor in graph.get(current, []):
        if neighbor in other_visited:  # Se encontró el otro frente
            print(f"Encuentro en: {neighbor}")
            return True
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
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

# Prueba de búsqueda bidireccional desde 'A' hasta 'G'
found = bidirectional_search(graph, 'A', 'G')
print("Resultado:", "Camino encontrado" if found else "Camino no encontrado")
