# Ingenieria en Mecatronica

# Programa_Propagacion_Restricciones

class MapColoring: # Se crea la clase 
    def __init__(self, countries, neighbors): # Este es el encabezado del método __init__. Toma tres parámetros: self, que hace referencia a la instancia de la clase, countries, que es una lista de nombres de países, y neighbors, que es un diccionario que mapea cada país a una lista de sus vecinos
        self.countries = countries # Se asignan los valores a los argumentos
        self.neighbors = neighbors # Se asignan los valores a los argumentos
        self.colors = {} # Se crea un diccionario vacio 
    
    def is_consistent(self, country, color): #  verifica si asignar un cierto color a un país dado sería consistente con los colores de sus vecinos
        for neighbor in self.neighbors[country]: # Este bucle itera sobre los vecinos del país dado (country). self.neighbors[country] devuelve una lista de los vecinos del país country
            if neighbor in self.colors and self.colors[neighbor] == color: # verifica si el vecino actual (neighbor) ya ha sido coloreado (neighbor in self.colors) y si el color del vecino es igual al color que estamos considerando asignar al país (self.colors[neighbor] == color')
                return False # Si se encuentra que un vecino ya está coloreado con el mismo color, se devuelve False para indicar que la asignación de color no es consistente
        return True # Si no se encuentra ningún vecino ya coloreado con el mismo color, se devuelve True para indicar que la asignación de color es consistente con las restricciones del problema
    
    def ac3(self, queue): # Este método ac3 implementa el algoritmo de AC-3 (Arc-Consistency 3) para propagar restricciones y reducir el dominio de los valores de manera eficiente
        while queue: # Este bucle se ejecuta mientras haya elementos en la cola queue
            (c1, c2) = queue.pop(0) # Se extrae el primer elemento de la cola queue y se desempaqueta en los arcos (c1, c2), donde c1 es el país actual y c2 es uno de sus vecinos
            if self.revise(c1, c2): # Se llama al método revise para verificar si se pueden eliminar valores del dominio de c1 basándose en la restricción impuesta por c2. Si se realizan revisiones (es decir, si se eliminan valores del dominio), el método devuelve True, lo que indica que el dominio se ha modificado
                if len(self.neighbors[c1]) == 0: # Si después de revisar el dominio de c1, se encuentra que el país c1 no tiene vecinos, significa que no se puede cumplir una restricción y el algoritmo termina sin exito
                    return False # Se devuelve False
                for neighbor in self.neighbors[c1]: # Si c1 aún tiene vecinos después de la revision, se agregan todos los arcos que van desde los vecinos de c1 hacia c1 a la cola queue
                    queue.append((neighbor, c1))
        return True # Si todas las revisiones se completan con éxito sin violaciones de restricciones, se devuelve True
    
    def revise(self, c1, c2): # Este es el encabezado del método revise, que toma tres parámetros: self, que hace referencia a la instancia de la clase, c1 que es el país actual y c2 que es uno de los vecinos de c1
        revised = False # Se inicializa la variable revised como False. Esta variable se utiliza para indicar si se ha modificado el dominio del país c1
        for color in self.colors[c1]: # Este bucle itera sobre todos los colores disponibles en el dominio del país c1
            if all(not self.is_consistent(c2, color) for color in self.colors[c2]): # verifica si no existe ningún color en el dominio del país c2 que sea consistente con el color actual (color) del país c1. Si esta condición se cumple para todos los colores en el dominio del país c2, significa que asignar el color actual a c1 violaría la restricción con respecto a c2
                self.colors[c1].remove(color) # Si se encuentra un color en el dominio de c1 que no es consistente con ningún color en el dominio de c2, se elimina este color del dominio del país c1
                revised = True # Se establece la variable revised como True para indicar que se ha modificado el dominio del país c1
        return revised # Finalmente, se devuelve el valor de revised. Si se ha modificado el dominio del país c1, el método devuelve True; de lo contrario, devuelve False
    
    def assign_colors(self): # método assign_colors, que toma un parámetro self, que hace referencia a la instancia de la clase
        for country in self.countries:
            self.colors[country] = ['Red', 'Green', 'Blue']  # Colores disponibles inicialmente
        
        queue = [(country, neighbor) for country in self.countries for neighbor in self.neighbors[country]]
        
        if not self.ac3(queue):
            return "No es posible asignar colores de manera consistente."
        
        return self.colors

def main(): # Este método asigna colores a los países. Inicializa los colores disponibles para cada país y luego llama al algoritmo AC-3 para realizar la propagación de restricciones y garantizar que la asignación de colores sea consistente
    countries = ['A', 'B', 'C', 'D', 'E'] # Contiene los nombres de los países que se deben colorear en el mapa
    neighbors = { # Representa las relaciones de vecindad entre los países en el mapa
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E'],
        'E': ['C', 'D']
    }
    
    coloring = MapColoring(countries, neighbors) # Crea una nueva instancia de la clase MapColoring utilizando los países y los vecinos proporcionados como argumentos
    colors = coloring.assign_colors() # Llama al método assign_colors() en el objeto coloring, que es una instancia de la clase MapColoring
    if isinstance(colors, dict): # verifica si el objeto colors es una instancia de la clase dict
        print("Asignación de colores:") # Se imprime el resultado
        for country, color in colors.items(): # Este bucle itera sobre cada elemento del diccionario colors, desempaquetando cada par clave-valor en las variables country y color
            print(f"{country}: {color}") # Se imprime el resultado
    else:
        print(colors) # Se imprime el resultado del else

if __name__ == "__main__": # Esta línea de codigo comprueba si el script está siendo ejecutado directamente como un programa principal o si está siendo importado como un módulo en otro script
    main()