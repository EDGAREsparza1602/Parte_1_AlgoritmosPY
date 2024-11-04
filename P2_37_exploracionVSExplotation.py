
# Ingenieria en Mecatronica

# Programa_Exploracion_vs_Explotacion

import numpy as np # Importamos NumPy para trabajar con matrices

class EpsilonGreedyAgent: # Se crea la clase 
    def __init__(self, num_actions, epsilon):
        self.num_actions = num_actions
        self.epsilon = epsilon
        self.Q = np.zeros(num_actions)  # Valores de acción inicializados a 0

    def choose_action(self):
        # Elige una acción utilizando una política epsilon-greedy
        if np.random.uniform(0, 1) < self.epsilon:
            # Exploración: elige una acción aleatoria
            return np.random.randint(self.num_actions)
        else:
            # Explotación: elige la acción con el valor Q más alto
            return np.argmax(self.Q)

    def update_Q(self, action, reward):
        # Actualiza el valor Q de la acción elegida
        self.Q[action] += reward

# Creamos un agente con 3 acciones y una política epsilon-greedy con epsilon = 0.1
agent = EpsilonGreedyAgent(num_actions=3, epsilon=0.1)

# Ejecutamos varios episodios de juego
num_episodes = 1000
for episode in range(num_episodes):
    # El agente elige una acción
    action = agent.choose_action()
    # Simulamos una recompensa aleatoria entre -1 y 1
    reward = np.random.uniform(-1, 1)
    # El agente actualiza el valor Q de la acción elegida
    agent.update_Q(action, reward)

# Imprimimos los valores de acción aprendidos por el agente
print("Valores de acción aprendidos por el agente:")
print(agent.Q)