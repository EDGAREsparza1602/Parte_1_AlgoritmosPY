
# Ingenieria en Mecatronica

# Programa_Busqueda_Local_Mínimos_Conflictos

import random # Genera numeros aleatorios, mezcla secuencias y selecciona elementos aleatorios

class MapColoringMinConflictsProbabilistic: # Se crea la clase
    def __init__(self, countries, neighbors): # Este metodo se manda llamar automáticamente cuando se crea una nueva instancia de la clase de los parametros self
        self.countries = countries # Esta línea asigna el valor del argumento countries que se pasa al inicializador al atributo countries del objeto actual self
        self.neighbors = neighbors # Esta línea asigna el valor del argumento neighbors que se pasa al inicializador al atributo neighbors del objeto actual self
        self.colors = {} #  Esta línea inicializa el atributo colors del objeto actual (self) como un diccionario vacio

    def initial_assignment(self): # Asignación aleatoria inicial de colores a los países
        for country in self.countries:
            self.colors[country] = random.choice(['Red', 'Green', 'Blue'])

    def conflicts(self, country, color): # Calcula el número de conflictos para un país dado si se le asigna un cierto color
        conflicts_count = 0
        for neighbor in self.neighbors[country]:
            if neighbor in self.colors and self.colors[neighbor] == color:
                conflicts_count += 1
        return conflicts_count

    def min_conflicts_color(self, country): # Devuelve el color que minimiza el número de conflictos para un país dado
        current_color = self.colors[country]
        min_conflicts = self.conflicts(country, current_color)
        best_color = current_color

        for color in ['Red', 'Green', 'Blue']:
            if color != current_color:
                conflicts_count = self.conflicts(country, color)
                if conflicts_count < min_conflicts:
                    min_conflicts = conflicts_count
                    best_color = color
                elif conflicts_count == min_conflicts: # Con cierta probabilidad, se elige un color diferente para fomentar la diversidad
                    if random.random() < 0.5:
                        best_color = color

        return best_color

    def min_conflicts(self, max_iterations=1000): # Implementa el algoritmo de Mínimos Conflictos
        self.initial_assignment()  
        for _ in range(max_iterations):
            conflicted_countries = [country for country in self.countries if self.conflicts(country, self.colors[country]) > 0]
            if not conflicted_countries:
                return True  # No hay conflictos, se encontró una solución
            country = random.choice(conflicted_countries)
            new_color = self.min_conflicts_color(country)
            self.colors[country] = new_color
        return False  # No se encontró una solución en el número máximo de iteraciones

countries = ['A', 'B', 'C', 'D', 'E'] # Lista que contiene los nombres de los países o regiones que se estan considerando en el problema
neighbors = { #  Se crea un diccionario que mapea cada país a una lista de sus países vecinos
    'A': ['B', 'C'], # Para el país 'A', los países vecinos son 'B' y 'C
    'B': ['A', 'C', 'D'], # Para el país 'B', los países vecinos son 'A', 'C' y 'D
    'C': ['A', 'B', 'D', 'E'], # Para el país 'C', los países vecinos son 'A', 'B', 'D' y 'E
    'D': ['B', 'C', 'E'], # Para el país 'D', los países vecinos son 'B', 'C' y 'E'
    'E': ['C', 'D'] # Para el país 'E', los países vecinos son 'C' y 'D'
}

solver = MapColoringMinConflictsProbabilistic(countries, neighbors) # Se crea una instancia de la clase MapColoringMinConflictsProbabilistic utilizando el inicializador __init__ de la clase
solution_found = solver.min_conflicts() # Después de crear la instancia solver, se llama al método min_conflicts() en esa instancia

if solution_found: # Verifica si la variable solution_found es verdadera, es decir, si se ha encontrado una solución al problema
    print("Solución encontrada:") # Se imprime el mensaje
    for country, color in solver.colors.items(): # Este bucle for itera sobre cada par clave-valor en el diccionario solver.colors 
        print(f"{country}: {color}") # Se imprime el mensaje
else: # Esta parte de la estructura condicional se ejecuta si la condición del if no se cumple
    print("No se encontró una solución en el número máximo de iteraciones.") # Se imprime el texto