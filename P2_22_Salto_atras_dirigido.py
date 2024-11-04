# Ingenieria en Mecatronica

# Programa_Salto_Atras_Dirigido_por_Conflictos

class MapColoring: # Se crea la clase 
    def __init__(self, countries, neighbors): # Este es el encabezado del método __init__. Toma tres parámetros: self, que hace referencia a la instancia de la clase, countries, que es una lista de nombres de países, y neighbors, que es un diccionario que mapea cada país a una lista de sus vecinos
        self.countries = countries # Se asignan los valores a los argumentos
        self.neighbors = neighbors # Se asignan los valores a los argumentos
        self.colors = {} # Se crea un diccionario vacio 
    
    def is_consistent(self, country, color): #  verifica si asignar un cierto color a un país dado sería consistente con los colores de sus vecinos
        for neighbor in self.neighbors[country]: # Este bucle itera sobre los vecinos del país dado (country). self.neighbors[country] devuelve una lista de los vecinos del país country
            if neighbor in self.colors and self.colors[neighbor] == color: # # verifica si el vecino actual (neighbor) ya ha sido coloreado (neighbor in self.colors) y si el color del vecino es igual al color que estamos considerando asignar al país (self.colors[neighbor] == color')
                return False # Si se encuentra que un vecino ya está coloreado con el mismo color, se devuelve False para indicar que la asignación de color no es consistente
        return True # Si no se encuentra ningún vecino ya coloreado con el mismo color, se devuelve True para indicar que la asignación de color es consistente con las restricciones del problema
    
    def backjumping(self, country):
        if country not in self.countries:
            return True  # Si ya se han coloreado todos los países, retornamos True (solución encontrada)
        
        for color in ['Red', 'Green', 'Blue']:
            if self.is_consistent(country, color):
                self.colors[country] = color  # Asignamos el color si es consistente con los vecinos
                
                # Intentamos colorear el siguiente país recursivamente
                if self.backjumping(self.get_next_country(country)):
                    return True
                
                # Si llegamos aquí, significa que no se pudo colorear el siguiente país con el color actual
                # Entonces, deshacemos la asignación de color y probamos el siguiente color
                del self.colors[country]
        
        return False  # No se encontró una solución
        
    def get_next_country(self, country):
        # Función auxiliar para obtener el siguiente país a colorear
        for c in self.countries:
            if c not in self.colors:
                return c
        return None  # Retorna None si ya se han coloreado todos los países
    
    def assign_colors(self):
        return self.backjumping(self.get_next_country(None))

def main(): # Este método asigna colores a los países. Inicializa los colores disponibles para cada país y luego llama al algoritmo AC-3 para realizar la propagación de restricciones y garantizar que la asignación de colores sea consistente
    countries = ['A', 'B', 'C', 'D', 'E'] # Contiene los nombres de los países que se deben colorear en el mapa
    neighbors = { # # Representa las relaciones de vecindad entre los países en el mapa
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E'],
        'E': ['C', 'D']
    }
    
    coloring = MapColoring(countries, neighbors) # Crea una instancia de la clase MapColoring con los datos proporcionados y la asigna a la variable coloring
    if coloring.assign_colors(): # Esta línea de código ejecuta el método assign_colors() en el objeto coloring, que es una instancia de la clase MapColoring 
        print("Asignación de colores:") # Se imprime el resultado
        for country, color in coloring.colors.items(): # itera sobre cada par clave-valor en el diccionario colors dentro del objeto coloring, que almacena la asignación de colores a cada país
            print(f"{country}: {color}") # Se imprime el resultado
    else:
        print("No se encontró una solución.") # Se imprime el resultado

if __name__ == "__main__": # # Esta línea de codigo comprueba si el script está siendo ejecutado directamente como un programa principal o si está siendo importado como un módulo en otro script
    main()