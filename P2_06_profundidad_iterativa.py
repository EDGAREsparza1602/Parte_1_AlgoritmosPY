def iterative_deepening_dfs(graph, start, goal):
    """
    Realiza una búsqueda en profundidad iterativa.

    Parámetros:
    - graph: Diccionario representando el grafo con listas de adyacencia.
    - start: Nodo inicial.
    - goal: Nodo objetivo.

    Retorna:
    - True si encuentra el nodo objetivo.
    - False si no encuentra el nodo objetivo.
    """
    depth = 0
    while True:
        print(f"Buscando con límite de profundidad: {depth}")
        found = depth_limited_search(graph, start, goal, depth)
        if found:
            return True
        depth += 1

def depth_limited_search(graph, current, goal, limit):
    """
    Realiza una búsqueda en profundidad limitada.

    Parámetros:
    - graph: Diccionario representando el grafo con listas de adyacencia.
    - current: Nodo actual.
    - goal: Nodo objetivo.
    - limit: Profundidad máxima permitida.

    Retorna:
    - True si se encuentra el objetivo.
    - False si se alcanza el límite de profundidad o no se encuentra el objetivo.
    """
    # Llamada auxiliar para la recursión con seguimiento de profundidad actual
    return depth_limited_search_recursive(graph, current, goal, limit, 0)

def depth_limited_search_recursive(graph, current, goal, limit, depth):
    # Verificar si el nodo actual es el objetivo
    if current == goal:
        print(f"Encontrado: {current} en profundidad {depth}")
        return True

    # Verificar si se ha alcanzado el límite de profundidad
    if depth >= limit:
        return False

    print(f"Visitando: {current} en profundidad {depth}")

    # Explorar cada vecino del nodo actual
    for neighbor in graph.get(current, []):
        # Llamada recursiva para el vecino, incrementando la profundidad en 1
        if depth_limited_search_recursive(graph, neighbor, goal, limit, depth + 1):
            return True  # Si se encuentra el objetivo en alguna rama, retornar True

    # Si se exploran todas las ramas y no se encuentra el objetivo, retornar False
    return False

# Grafo de ejemplo
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Prueba de búsqueda en profundidad iterativa desde 'A' buscando 'G'
found = iterative_deepening_dfs(graph, 'A', 'G')
print("Resultado:", "Encontrado" if found else "No encontrado")
