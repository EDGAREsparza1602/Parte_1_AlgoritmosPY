# Ingenieria en Mecatronica
# Programa_Proceso_de_Decision_de_Markov_(MDP)

import numpy as np # Biblioteca para trabajar con matrices y funciones matemáticas en Python

probabilidades_transicion = np.array([ # Definimos las probabilidades de transición del MDP
    # Desde S0
    [[0.5, 0.5],  # Probabilidades de transición para A0 y A1 desde S0
     [0.9, 0.1],  # Probabilidades de transición para A0 y A1 desde S1
     [0.0, 1.0]], # Probabilidades de transición para A0 y A1 desde S2
    # Desde S1
    [[0.7, 0.3],  # Probabilidades de transición para A0 y A1 desde S0
     [0.0, 1.0],  # Probabilidades de transición para A0 y A1 desde S1
     [0.8, 0.2]], # Probabilidades de transición para A0 y A1 desde S2
    # Desde S2
    [[0.0, 1.0],  # Probabilidades de transición para A0 y A1 desde S0
     [0.0, 1.0],  # Probabilidades de transición para A0 y A1 desde S1
     [0.0, 1.0]]  # Probabilidades de transición para A0 y A1 desde S2
])

recompensas = np.array([ # Definimos las recompensas del MDP
    [0, 0],  # Recompensas para A0 y A1 desde S0
    [0, 0],  # Recompensas para A0 y A1 desde S1
    [0, 1]   # Recompensas para A0 y A1 desde S2
])

# Definimos el número de estados y acciones
num_estados = 3
num_acciones = 2

valor_estado = np.zeros(num_estados) # Inicializamos la función de valor de estado

factor_descuento = 0.9 # Definimos el factor de descuento

max_iteraciones = 1000 # Definimos el número máximo de iteraciones

# Iteramos hasta alcanzar el número máximo de iteraciones
for _ in range(max_iteraciones):
    nuevo_valor_estado = np.zeros(num_estados) # Inicializamos el valor de la nueva función de valor de estado

    # Iteramos sobre cada estado
    for estado in range(num_estados): # Calculamos el valor de acción para cada acción en el estado actual
        valores_accion = np.zeros(num_acciones)

        # Iteramos sobre cada acción
        for accion in range(num_acciones):
            # Calculamos el valor de acción utilizando la función de valor de estado
            valor_accion = 0
            for estado_siguiente in range(num_estados):
                probabilidad_transicion = probabilidades_transicion[estado, estado_siguiente, accion]
                recompensa = recompensas[estado, accion]
                valor_accion += probabilidad_transicion * (recompensa + factor_descuento * valor_estado[estado_siguiente])
            valores_accion[accion] = valor_accion
        
        nuevo_valor_estado[estado] = np.max(valores_accion)    # Elegimos el valor de acción máximo como el nuevo valor de estado

    if np.array_equal(nuevo_valor_estado, valor_estado):  # Si la función de valor de estado no cambia, hemos convergido
        break

    valor_estado = nuevo_valor_estado # Actualizamos la función de valor de estado

print("Función de Valor de Estado óptima:", valor_estado) # Imprimimos la función de valor de estado óptima