def depth_limited_search(graph, start, goal, limit):
    """
    Realiza una búsqueda en profundidad limitada.

    Parámetros:
    - graph: Diccionario representando el grafo con listas de adyacencia.
    - start: Nodo inicial.
    - goal: Nodo objetivo.
    - limit: Profundidad máxima de búsqueda.

    Retorna:
    - True si encuentra el nodo objetivo dentro del límite de profundidad.
    - False si no encuentra el objetivo o si alcanza el límite de profundidad.
    """
    # Llamada recursiva con el límite inicial
    return depth_limited_search_recursive(graph, start, goal, limit, 0)

def depth_limited_search_recursive(graph, current, goal, limit, depth):
    # Verificar si se alcanza el objetivo
    if current == goal:
        print(f"Encontrado: {current} en profundidad {depth}")
        return True
    
    # Si la profundidad actual supera el límite, detenerse
    if depth >= limit:
        return False

    print(f"Visitando: {current} en profundidad {depth}")
    
    # Explorar los vecinos recursivamente
    for neighbor in graph.get(current, []):
        if depth_limited_search_recursive(graph, neighbor, goal, limit, depth + 1):
            return True  # Retorna True si el objetivo se encuentra en alguna rama

    return False  # Si se exploran todas las ramas y no se encuentra el objetivo

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

# Prueba de búsqueda en profundidad limitada desde 'A' buscando 'G' con un límite de profundidad de 3
found = depth_limited_search(graph, 'A', 'G', limit=3)
print("Resultado:", "Encontrado" if found else "No encontrado")
