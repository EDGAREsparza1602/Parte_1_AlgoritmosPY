# Ingenieria en Mecatronica

# Programa_Teoría_de_Juegos_Equilibrios_y_Mecanismos

import numpy as np  # Importamos NumPy para trabajar con matrices
import nashpy as nash  # Importamos la biblioteca nashpy para la Teoría de Juegos

# Definimos las matrices de pagos para dos jugadores en un juego de piedra, papel o tijera
# Cada jugador tiene dos estrategias: 'piedra', 'papel' y 'tijera'
payoff_player1 = np.array([[0, -1, 1],  # Payoffs para jugador 1 cuando elige 'piedra'
                            [1, 0, -1],  # Payoffs para jugador 1 cuando elige 'papel'
                            [-1, 1, 0]]) # Payoffs para jugador 1 cuando elige 'tijera'

payoff_player2 = np.array([[0, 1, -1],   # Payoffs para jugador 2 cuando elige 'piedra'
                            [-1, 0, 1],  # Payoffs para jugador 2 cuando elige 'papel'
                            [1, -1, 0]]) # Payoffs para jugador 2 cuando elige 'tijera'

# Creamos objetos de juego con las matrices de pagos
game_player1 = nash.Game(payoff_player1)
game_player2 = nash.Game(payoff_player2)

# Calculamos los equilibrios de Nash del juego para ambos jugadores
equilibrio_jugador1 = game_player1.support_enumeration()
equilibrio_jugador2 = game_player2.support_enumeration()

# Imprimimos los equilibrios de Nash encontrados
print("Equilibrios de Nash para Jugador 1:")
for eq in equilibrio_jugador1:
    print(eq)

print("\nEquilibrios de Nash para Jugador 2:")
for eq in equilibrio_jugador2:
    print(eq)