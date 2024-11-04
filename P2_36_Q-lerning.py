# Ingenieria en Mecatronica

# Programa_Q-Learning

import numpy as np # Importamos NumPy para trabajar con matrices

class Environment: # Creamos la clase
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.goal = (grid_size - 1, grid_size - 1)  # La meta está en la esquina inferior derecha
        self.obstacles = [(1, 1), (2, 2)]  # Posiciones de los obstáculos

    def step(self, state, action):
        # Calcula la nueva posición después de tomar una acción
        x, y = state
        if action == 0:  # Mover hacia arriba
            x -= 1
        elif action == 1:  # Mover hacia abajo
            x += 1
        elif action == 2:  # Mover hacia la izquierda
            y -= 1
        elif action == 3:  # Mover hacia la derecha
            y += 1
        
        # Verifica si la nueva posición está dentro del grid
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            # Verifica si la nueva posición es un obstáculo
            if (x, y) in self.obstacles:
                reward = -10  # Penaliza al agente por golpear un obstáculo
                next_state = state  # El estado no cambia
            else:
                reward = 0  # No hay recompensa por moverse sin llegar a la meta
                next_state = (x, y)
        else:
            reward = -1  # Penaliza al agente por salir del grid
            next_state = state  # El estado no cambia
        
        return next_state, reward

class QLearningAgent:
    def __init__(self, grid_size, num_actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.grid_size = grid_size
        self.num_actions = num_actions
        self.Q = np.zeros((grid_size, grid_size, num_actions))  # Inicializa los valores Q a 0
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

    def choose_action(self, state):
        # Elige una acción utilizando una política epsilon-greedy
        if np.random.uniform(0, 1) < self.exploration_rate:
            return np.random.randint(self.num_actions)  # Exploración aleatoria
        else:
            return np.argmax(self.Q[state])

    def update_Q(self, state, action, reward, next_state):
        # Actualiza los valores Q utilizando el algoritmo Q-Learning
        best_next_action = np.argmax(self.Q[next_state])
        td_target = reward + self.discount_factor * self.Q[next_state][best_next_action]
        td_error = td_target - self.Q[state][action]
        self.Q[state][action] += self.learning_rate * td_error

# Creamos el entorno y el agente
grid_size = 5
num_actions = 4  # Arriba, abajo, izquierda, derecha
env = Environment(grid_size)
agent = QLearningAgent(grid_size, num_actions)

# Ejecutamos episodios de juego
num_episodes = 1000
for episode in range(num_episodes):
    state = (0, 0)  # El agente comienza en la esquina superior izquierda
    done = False
    while not done:
        action = agent.choose_action(state)
        next_state, reward = env.step(state, action)
        agent.update_Q(state, action, reward, next_state)
        state = next_state
        if state == env.goal:
            done = True

# Imprimimos los valores Q aprendidos por el agente
print("Valores Q aprendidos por el agente:")
print(agent.Q)