# Programa_Teoría_de_la_Utilidad_Función_de_Utilidad


class UtilityFunction: # Se crea la clase
    def __init__(self, coefficients): #  Inicializa la Función de Utilidad con los coeficientes dados, Los coeficientes deben ser una lista de números que representan los pesos de cada opcion en el cálculo de la utilidad
        self.coefficients = coefficients

    def calculate_utility(self, options): # Calcula la utilidad de un conjunto de opciones dados. Se asume que options es una lista de números que representan las opciones disponibles para el agente
        utility = 0 # Inicializa la variable utility como 0
        for coefficient, option in zip(self.coefficients, options): # Inicia un bucle for que itera simultáneamente sobre los elementos de dos listas: self.coefficients y options. self.coefficients contiene los coeficientes de la función de utilidad, mientras que options contiene los valores de las opciones para calcular la utilidad
            utility += coefficient * option # En cada iteración del bucle, multiplica el coeficiente correspondiente por el valor de la opción y lo agrega al valor actual de utility. Esto se hace para calcular la contribución de cada opción a la utilidad total, basada en su peso (coeficiente) en la función de utilidad
        return utility # Una vez que se han calculado las contribuciones de todas las opciones a la utilidad total, el bucle termina y la función devuelve el valor total de la utilidad calculada

utility_function = UtilityFunction([0.5, 0.3, 0.2]) # Creamos una instancia de la Función de Utilidad con coeficientes dados

options = [10, 5, 8] # Definimos un conjunto de opciones para calcular la utilidad

resulting_utility = utility_function.calculate_utility(options) # Calculamos la utilidad utilizando la Función de Utilidad

print("La utilidad calculada es:", resulting_utility) # Imprimimos el resultado