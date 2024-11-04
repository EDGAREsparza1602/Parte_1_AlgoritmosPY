
# Programa_Busqueda_Haz

import random # importa el módulo random de la biblioteca estándar de Python, que se utiliza para generar números aleatorios

class TSPProblem:
    def __init__(self, distances): # Este es el constructor de la clase. Recibe una matriz de distancias que representa las distancias entre todas las ciudades en el problema TSP y la almacena en el atributo self.distances
        self.distances = distances

    def initial_solutions(self, k): # Este método genera k soluciones iniciales aleatorias para el problema TSP. Utiliza la matriz de distancias para calcular la distancia total de cada solución
        cities = list(range(len(self.distances)))
        return [random.sample(cities, len(cities)) for _ in range(k)]

    def evaluate(self, solution): # Este método calcula la evaluación de una solución dada, es decir, la distancia total recorrida para completar la ruta. Itera sobre las ciudades en la solución y suma las distancias entre cada par de ciudades consecutivas
        total_distance = 0
        for i in range(len(solution)):
            total_distance += self.distances[solution[i - 1]][solution[i]]
        return total_distance

    def neighbors(self, solution): # Este método genera todos los vecinos de una solución dada intercambiando dos ciudades en la ruta
        neighbors = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                neighbor = solution[:]
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

def local_beam_search(problem, k, max_iterations=1000):
    current_solutions = problem.initial_solutions(k)

    for _ in range(max_iterations):
        neighbors = []
        for solution in current_solutions:
            neighbors.extend(problem.neighbors(solution))

        sorted_neighbors = sorted(neighbors, key=problem.evaluate)
        current_solutions = sorted_neighbors[:k]

    best_solution = min(current_solutions, key=problem.evaluate)
    return best_solution

def main():
    # Distancias entre ciudades (ejemplo)
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    problem = TSPProblem(distances)
    best_solution = local_beam_search(problem, k=3)

    print("Mejor solución encontrada:", best_solution)
    print("Distancia de la mejor solución:", problem.evaluate(best_solution))

if __name__ == "__main__":
    main()