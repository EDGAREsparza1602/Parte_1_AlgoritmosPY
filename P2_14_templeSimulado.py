

# Programa_Busqueda_de_Temple_Simulado

import random
import math

class TSPProblem:
    def __init__(self, distances): # Este es el constructor de la clase. Recibe una matriz de distancias que representa las distancias entre todas las ciudades en el problema TSP y la almacena en el atributo self.distances
        self.distances = distances

    def initial_solution(self): # Este método genera una solución inicial aleatoria para el problema TSP. Crea una lista de ciudades en orden secuencial y luego la mezcla aleatoriamente utilizando random.shuffle()
        cities = list(range(len(self.distances)))
        random.shuffle(cities)
        return cities

    def evaluate(self, solution): # Este método calcula la evaluación de una solución dada, es decir, la distancia total recorrida para completar la ruta. Itera sobre las ciudades en la solución y suma las distancias entre cada par de ciudades consecutivas
        total_distance = 0
        for i in range(len(solution)):
            total_distance += self.distances[solution[i - 1]][solution[i]]
        return total_distance

    def neighbor(self, solution): # Este método genera un vecino de una solución dada realizando un intercambio entre dos ciudades en la ruta. Elige dos índices aleatorios en la solución y revierte el orden de las ciudades entre esos dos índices
        new_solution = solution[:]
        i, j = sorted(random.sample(range(len(solution)), 2))
        new_solution[i:j+1] = reversed(new_solution[i:j+1])
        return new_solution

def simulated_annealing(problem, initial_temperature=1000, cooling_rate=0.99, max_iterations=1000):
    current_solution = problem.initial_solution()
    current_energy = problem.evaluate(current_solution)
    best_solution = current_solution
    best_energy = current_energy
    temperature = initial_temperature

    for _ in range(max_iterations):
        new_solution = problem.neighbor(current_solution)
        new_energy = problem.evaluate(new_solution)

        if new_energy < current_energy or random.random() < math.exp((current_energy - new_energy) / temperature):
            current_solution = new_solution
            current_energy = new_energy

        if new_energy < best_energy:
            best_solution = new_solution
            best_energy = new_energy

        temperature *= cooling_rate

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
    best_solution = simulated_annealing(problem)

    print("Mejor solución encontrada:", best_solution)
    print("Distancia de la mejor solución:", problem.evaluate(best_solution))

if __name__ == "__main__":
    main()