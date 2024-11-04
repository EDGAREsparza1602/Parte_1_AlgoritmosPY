# Ingenieria en Mecatronica

# Programa_Aprendizaje_por_Refuerzo_Pasivo


import numpy as np # Importamos NumPy para trabajar con matrices

class Environment: # Se crea la clase 
    def __init__(self, num_actions):
        self.num_actions = num_actions

    def step(self, action):
        # Simulamos una recompensa aleatoria entre -1 y 1
        reward = np.random.uniform(-1, 1)
        return reward

class Agent:
    def __init__(self, num_actions):
        self.num_actions = num_actions
        self.Q = np.zeros(num_actions)  # Inicializamos los valores de acción a 0
        self.N = np.zeros(num_actions)  # Contador de visitas de cada acción

    def choose_action(self):
        # Elige una acción utilizando una política epsilon-greedy
        epsilon = 0.1
        if np.random.uniform(0, 1) < epsilon:
            return np.random.choice(self.num_actions)
        else:
            return np.argmax(self.Q)

    def update_Q(self, episode):
        # Actualiza los valores de acción utilizando el Método de Monte Carlo
        for (state, action, reward) in episode:
            self.N[action] += 1
            self.Q[action] += (1 / self.N[action]) * (reward - self.Q[action])

# Creamos el entorno y el agente
env = Environment(num_actions=3)
agent = Agent(num_actions=3)

# Ejecutamos episodios de juego
num_episodes = 1000
for episode in range(num_episodes):
    episode_data = []  # Almacenamos los estados, acciones y recompensas de cada episodio
    done = False
    while not done:
        action = agent.choose_action()
        reward = env.step(action)
        episode_data.append((None, action, reward))  # No hay estado en este ejemplo
        done = True  # Terminamos el episodio después de una sola acción
    agent.update_Q(episode_data)

# Imprimimos los valores de acción aprendidos por el agente
print("Valores de acción aprendidos por el agente:")
print(agent.Q)