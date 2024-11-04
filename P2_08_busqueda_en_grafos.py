from collections import deque

def graph_search(graph, start, goal):
    """
    Realiza una búsqueda en anchura en un grafo desde un nodo inicial hacia un objetivo.

    Parámetros:
    - graph: Diccionario representando el grafo con listas de adyacencia.
    - start: Nodo inicial.
    - goal: Nodo objetivo.

    Retorna:
    - True si se encuentra un camino al nodo objetivo.
    - False si no se encuentra un camino.
    """
    # Cola de nodos a explorar, comenzando desde el nodo inicial
    queue = deque([start])
    # Conjunto de nodos visitados
    visited = {start}

    while queue:
        # Extrae el primer nodo de la cola
        current = queue.popleft()
        print(f"Visitando: {current}")

        # Verifica si se alcanzó el nodo objetivo
        if current == goal:
            print("Objetivo encontrado:", current)
            return True

        # Expande los vecinos del nodo actual
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

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

# Prueba de búsqueda en grafos desde 'A' hasta 'G'
found = graph_search(graph, 'A', 'G')
print("Resultado:", "Camino encontrado" if found else "Camino no encontrado")
