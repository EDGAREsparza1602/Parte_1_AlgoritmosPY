# Ingenieria en Mecatronica

# Programa_Aprendizaje_por_Refuerzo_Activo

import numpy as np # Importamos NumPy para trabajar con matrices

class Environment: # Creamos la clase
    def __init__(self, num_actions):
        self.num_actions = num_actions

    def step(self, action):
        # Simulamos una recompensa aleatoria entre -1 y 1
        reward = np.random.uniform(-1, 1)
        return reward

class Agent:
    def __init__(self, num_actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.num_actions = num_actions
        self.Q = np.zeros(num_actions)  # Inicializamos los valores Q a 0
        self.learning_rate = learning_rate  # Tasa de aprendizaje
        self.discount_factor = discount_factor  # Factor de descuento
        self.exploration_rate = exploration_rate  # Tasa de exploración

    def choose_action(self):
        # Elige una acción utilizando una política epsilon-greedy
        if np.random.uniform(0, 1) < self.exploration_rate:
            return np.random.choice(self.num_actions)
        else:
            return np.argmax(self.Q)

    def update_Q(self, state, action, reward, next_state):
        # Actualiza los valores Q utilizando el algoritmo Q-Learning
        best_next_action = np.argmax(self.Q[next_state])
        td_target = reward + self.discount_factor * self.Q[next_state, best_next_action]
        td_error = td_target - self.Q[state, action]
        self.Q[state, action] += self.learning_rate * td_error

# Creamos el entorno y el agente
env = Environment(num_actions=3)
agent = Agent(num_actions=3)

# Ejecutamos episodios de juego
num_episodes = 1000
for episode in range(num_episodes):
    state = None  # No hay estado en este ejemplo
    done = False
    while not done:
        action = agent.choose_action()
        reward = env.step(action)
        next_state = None  # No hay estado en este ejemplo
        agent.update_Q(state, action, reward, next_state)
        done = True  # Terminamos el episodio después de una sola acción

# Imprimimos los valores Q aprendidos por el agente
print("Valores Q aprendidos por el agente:")
print(agent.Q)