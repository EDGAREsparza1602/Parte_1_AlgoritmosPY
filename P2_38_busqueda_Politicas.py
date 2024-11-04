# Ingenieria en Mecatronica
# Programa_Busqueda_de_la_Política

import numpy as np # Importamos NumPy para trabajar con matrices

class Environment: # Se crea la clase
    def __init__(self, num_states, num_actions):
        self.num_states = num_states
        self.num_actions = num_actions
        # Matriz de recompensas R: R[state, action] = reward
        self.R = np.random.rand(num_states, num_actions)
        # Matriz de transiciones P: P[state, action, next_state] = probability
        self.P = np.random.rand(num_states, num_actions, num_states)
        # Política inicial aleatoria
        self.policy = np.random.randint(num_actions, size=num_states)

    def step(self, state, action):
        # Simula un paso en el entorno y devuelve el próximo estado y la recompensa
        next_state = np.random.choice(self.num_states, p=self.P[state, action])
        reward = self.R[state, action]
        return next_state, reward

class PolicyIterationAgent:
    def __init__(self, env, discount_factor=0.9):
        self.env = env
        self.discount_factor = discount_factor

    def evaluate_policy(self, policy):
        # Evalúa la política dada y devuelve los valores de acción
        V = np.zeros(self.env.num_states)
        while True:
            delta = 0
            for s in range(self.env.num_states):
                v = V[s]
                a = policy[s]
                V[s] = np.sum(self.env.P[s, a] * (self.env.R[s, a] + self.discount_factor * V))
                delta = max(delta, np.abs(v - V[s]))
            if delta < 1e-6:
                break
        return V

    def improve_policy(self, V):
        # Mejora la política utilizando los valores de acción dados
        policy_stable = True
        for s in range(self.env.num_states):
            old_action = self.env.policy[s]
            action_values = [np.sum(self.env.P[s, a] * (self.env.R[s, a] + self.discount_factor * V)) for a in range(self.env.num_actions)]
            self.env.policy[s] = np.argmax(action_values)
            if old_action != self.env.policy[s]:
                policy_stable = False
        return policy_stable

    def policy_iteration(self):
        # Iteración de políticas
        while True:
            V = self.evaluate_policy(self.env.policy)
            policy_stable = self.improve_policy(V)
            if policy_stable:
                break

# Creamos el entorno y el agente
env = Environment(num_states=5, num_actions=3)
agent = PolicyIterationAgent(env)

# Ejecutamos la iteración de políticas
agent.policy_iteration()

# Imprimimos la política aprendida por el agente
print("Política aprendida por el agente:")
print(agent.env.policy)