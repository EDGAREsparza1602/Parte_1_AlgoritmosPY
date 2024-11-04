
# Programa_Algoritmos_Geneticos

import random # importa el módulo random de la biblioteca estándar de Python, que se utiliza para generar números aleatorios

# Parámetros del algoritmo genético
TARGET_SEQUENCE = "110101101010101" # La secuencia objetivo que el algoritmo genético intentará encontrar
POPULATION_SIZE = 100 # El tamaño de la población de individuos en cada generación
MUTATION_RATE = 0.01 # La tasa de mutación que determina la probabilidad de que ocurra una mutación en un individuo durante la reproducción
MAX_GENERATIONS = 1000 # El número máximo de generaciones que el algoritmo genético ejecutará antes de terminar

def initialize_population(size, sequence_length): #  inicializa y devuelve una población de individuos aleatorios. Recibe dos parámetros: size (el tamaño de la población) y sequence_length (la longitud de cada individuo). Utiliza la función random.choice("01") para generar de manera aleatoria una secuencia de bits de la longitud especificada
    return [''.join(random.choice("01") for _ in range(sequence_length)) for _ in range(size)]

def fitness(individual): # calcula la aptitud de un individuo. Recibe un individuo (una cadena de bits) y compara cada bit con el bit correspondiente en la secuencia objetivo (TARGET_SEQUENCE). Por cada bit que coincide, incrementa el puntaje en uno. Retorna el puntaje tota
    score = 0
    for i in range(len(TARGET_SEQUENCE)):
        if individual[i] == TARGET_SEQUENCE[i]:
            score += 1
    return score

def crossover(parent1, parent2): # realiza el cruce de dos padres (individuos) para producir dos hijos. Se elige aleatoriamente un punto de cruce entre 1 y la longitud de los individuos menos 1. Luego, se intercambian las porciones de los padres antes y después del punto de cruce para crear dos nuevos individuos hijos
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mutation_rate): # realiza la mutación de un individuo con una cierta tasa de mutación (mutation_rate). Recorre cada bit del individuo y, si un número aleatorio es menor que la tasa de mutación, cambia el bit por su opuesto (de 0 a 1 o de 1 a 0). Retorna el individuo mutado
    mutated_individual = ''
    for bit in individual:
        if random.random() < mutation_rate:
            mutated_individual += '1' if bit == '0' else '0'
        else:
            mutated_individual += bit
    return mutated_individual

def genetic_algorithm(): #  implementa el algoritmo genético para resolver el problema de encontrar la secuencia objetivo
    population = initialize_population(POPULATION_SIZE, len(TARGET_SEQUENCE))
    generation = 0

    while generation < MAX_GENERATIONS:
        population = sorted(population, key=fitness, reverse=True)

        if fitness(population[0]) == len(TARGET_SEQUENCE):
            print("Solution found in generation", generation)
            print("Target sequence:", population[0])
            return population[0]

        mating_pool = population[:10]

        for _ in range(POPULATION_SIZE - len(mating_pool)):
            parent1, parent2 = random.choices(mating_pool, k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, MUTATION_RATE)
            child2 = mutate(child2, MUTATION_RATE)
            population.append(child1)
            population.append(child2)

        generation += 1

    print("Maximum generations reached. Best solution found:")
    print("Target sequence:", population[0])
    return population[0]

if __name__ == "__main__":
    genetic_algorithm()