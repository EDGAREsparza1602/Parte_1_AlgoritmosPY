from constraint import Problem, AllDifferentConstraint

def map_coloring():
    problem = Problem()

    # Definimos los países y los colores posibles
    countries = ["A", "B", "C", "D", "E"]
    colors = ["Rojo", "Verde", "Azul"]

    # Agregamos las variables al problema (países)
    for country in countries:
        problem.addVariable(country, colors)

    # Agregamos restricciones para asegurar que países adyacentes no tengan el mismo color
    problem.addConstraint(AllDifferentConstraint(), [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")])

    # Encuentra una solución
    solution = problem.getSolution()

    if solution is None: # Esta línea verifica si la variable solution es None, lo que indica que no se encontró ninguna solución al problema de asignación de colores
        print("No se encontró solución.") #  Si no se encontró ninguna solución, esta línea imprime un mensaje indicando que no se encontró una solución válida para el problema de asignación de colores
    else: # Si hay una solución en el diccionario solution, esta línea se ejecutara
        print("Asignación de colores:") #  Esta línea imprime un encabezado indicando que se mostrará la asignación de colores para cada país
        for country, color in solution.items(): # Este bucle itera a través de los elementos del diccionario solution, donde cada elemento representa la asignación de color para un país en particular. country es la clave que representa el país y color es el valor que representa el color asignado a ese país
            print(f"{country}: {color}") # Dentro del bucle, esta línea imprime la asignación de colores para cada país en el formato "país: color". Utiliza una cadena formateada (f-string) para incluir el nombre del país y el color asignado en el mensaje de impresión

if __name__ == "__main__":
    map_coloring()