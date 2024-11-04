# Ingenieria en Mecatronica

# Programa_Valor_de_la_Informacion

import numpy as np # Nos proporciona soporte para crear y manipular matrices y arrays multidimensionales

def calcular_valor_informacion(dataset, variable): 
    total_entropy = calcular_entropia(dataset)  # Calcular la entropía del conjunto de datos completo

    conditional_entropy = 0  # Calcular la entropía condicional para cada valor único de la variable
    unique_values = np.unique(dataset[:, variable])
    for value in unique_values:
        subset = dataset[dataset[:, variable] == value]
        subset_entropy = calcular_entropia(subset)
        conditional_entropy += (len(subset) / len(dataset)) * subset_entropy

    # Calcular el Valor de la Información
    information_value = total_entropy - conditional_entropy
    return information_value

def calcular_entropia(dataset): # Esta función toma un conjunto de datos como entrada y calcula la entropía del conjunto de datos
    num_instances = len(dataset)
    if num_instances == 0:
        return 0

    _, counts = np.unique(dataset[:, -1], return_counts=True)  # Contar las ocurrencias de cada clase en el conjunto de datos

    probabilities = counts / num_instances  # Calcular la probabilidad de cada clase

    entropy = -np.sum(probabilities * np.log2(probabilities)) # Calcular la entropía
    return entropy

dataset = np.array([ # Se crea el conjunto de datos
    [120, 45, 0],
    [140, 55, 1],
    [130, 60, 1],
    [125, 50, 0],
    [135, 65, 1],
    [128, 48, 0],
    [132, 52, 0],
    [138, 58, 1]
])

information_value = calcular_valor_informacion(dataset, 0) # Calculamos el Valor de la Información para la presión arterial (variable en la columna 0)
print("Valor de la Información de la presión arterial:", information_value) # Imprimimos el valor final
