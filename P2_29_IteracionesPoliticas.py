# Ingenieria en Mecatronica

# Programa_Iteracion_de_Políticas

import numpy as np # Biblioteca para trabajar con matrices y funciones matemáticas

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

politica = np.random.randint(num_acciones, size=num_estados) # Inicializamos la política aleatoriamente

factor_descuento = 0.9 # Definimos el factor de descuento

max_iteraciones = 1000 # Definimos el número máximo de iteraciones

# Iteramos hasta alcanzar el número máximo de iteraciones
for _ in range(max_iteraciones):
    nueva_politica = np.zeros(num_estados) # Inicializamos el valor de la nueva política

    # Iteramos sobre cada estado
    for estado in range(num_estados):
        valores_accion = np.zeros(num_acciones) # Calculamos el valor de acción para cada acción en el estado actual

        # Iteramos sobre cada acción
        for accion in range(num_acciones):
            # Calculamos el valor de acción utilizando la función de valor de estado-acción
            valor_accion = 0
            for estado_siguiente in range(num_estados):
                probabilidad_transicion = probabilidades_transicion[estado, estado_siguiente, accion]
                recompensa = recompensas[estado, accion]
                valor_accion += probabilidad_transicion * (recompensa + factor_descuento * nueva_politica[estado_siguiente])
            valores_accion[accion] = valor_accion
        
        # Elegimos la acción con el mayor valor
        mejor_accion = np.argmax(valores_accion)
        nueva_politica[estado] = mejor_accion

    # Si la política no cambia, hemos convergido
    if np.array_equal(nueva_politica, politica):
        break

    politica = nueva_politica  # Actualizamos la política

print("Política óptima:", politica) # Imprimimos la política óptima