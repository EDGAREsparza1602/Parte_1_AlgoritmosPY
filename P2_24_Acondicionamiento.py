
# Programa_Acondicionamiento_del_Corte

import random # Genera numeros aleatorios, mezcla secuencias y selecciona elementos aleatorios

def conditional_sampling(cutting_probabilities): # Genera un número aleatorio entre 0 y 1
    random_number = random.random()
    
    cumulative_probability = 0  # Inicializa la suma acumulada de probabilidades
    
    for value, probability in cutting_probabilities.items(): # Itera sobre las probabilidades de corte y sus valores asociados
       
        cumulative_probability += probability  # Incrementa la suma acumulada de probabilidades
        
        if random_number <= cumulative_probability: # Si el número aleatorio está dentro del rango de esta probabilidad
            return value # Devuelve el valor asociado a esta probabilidad
            
cutting_probabilities = { # Indica el comienzo de la definición de un diccionario en Python
    'A': 0.1, # 'A': 0.1,: Esto asigna una clave 'A' con un valor de 0.1 dentro del diccionario, cutting_probabilities. Esto significa que el valor 'A' tiene una probabilidad de corte del 10% 
    'B': 0.3, # 'B': 0.3,: De manera similar, esto asigna una clave 'B' con un valor de 0.3 dentro del diccionario cutting_probabilities, lo que indica que el valor 'B' tiene una probabilidad de corte del 30%
    'C': 0.6 # 'C': 0.6: Esto asigna una clave 'C' con un valor de 0.6 dentro del diccionario cutting_probabilities, lo que indica que el valor 'C' tiene una probabilidad de corte del 60%
}

sampled_value = conditional_sampling(cutting_probabilities) # Realiza muestreo condicional utilizando las probabilidades de corte

print("Valor muestreado:", sampled_value) # Imprime el valor muestreado