
# Ingenieria en Mecatronica

# Programa_Redes_de_Decision

class DecisionNode:
    def __init__(self, name, decision_values):
        self.name = name  # Nombre del nodo de decisión
        self.decision_values = decision_values  # Valores posibles de la decisión
        self.children = {}  # Almacena los nodos hijos de este nodo

    def add_child(self, value, node):
        self.children[value] = node  # Añade un nodo hijo para un valor de decisión dado


class ChanceNode:
    def __init__(self, name, probabilities):
        self.name = name  # Nombre del nodo de probabilidad
        self.probabilities = probabilities  # Probabilidades condicionales de cada valor
        self.children = {}  # Almacena los nodos hijos de este nodo

    def add_child(self, value, node):
        self.children[value] = node  # Añade un nodo hijo para un valor de probabilidad dado


class DecisionNetwork:
    def __init__(self, root_node):
        self.root = root_node  # Nodo raíz de la red de decisión

    def infer(self, evidence):
        marginal_probabilities = {}

        # Itera sobre todos los valores posibles de la raíz (nodo de decisión)
        for decision_value in self.root.decision_values:
            # Realiza la recursión para calcular la probabilidad marginal para cada valor de decisión
            marginal_probabilities[decision_value] = self._infer_recursive(self.root, evidence, decision_value)

        return marginal_probabilities

    def _infer_recursive(self, node, evidence, decision_value):
        """
        Realiza una inferencia recursiva en la red de decisión.
        """
        if isinstance(node, DecisionNode):
            # Si el nodo es un nodo de decisión, selecciona el nodo hijo correspondiente al valor de la decisión
            node = node.children[decision_value]

        if isinstance(node, ChanceNode):
            # Si el nodo es un nodo de probabilidad
            probability = 1.0

            # Multiplica las probabilidades de los hijos dados los valores de las variables observadas
            for child_value, child_node in node.children.items():
                if child_node.name in evidence:
                    probability *= node.probabilities[child_value][evidence[child_node.name]]
                else:
                    # Si el valor del hijo no está observado, recursivamente calcula la probabilidad
                    probability *= self._infer_recursive(child_node, evidence, decision_value)

            return probability

        return None


# Creamos los nodos de decisión y de probabilidad
decision_node = DecisionNode("Destination", ["Beach", "Mountain"])
weather_node = ChanceNode("Weather", {"Beach": {"Sunny": 0.8, "Rainy": 0.2},
                                      "Mountain": {"Sunny": 0.6, "Rainy": 0.4}})

# Añadimos los nodos hijos a los nodos de decisión y de probabilidad
decision_node.add_child("Beach", weather_node)
decision_node.add_child("Mountain", weather_node)

# Creamos la red de decisiones con el nodo raíz
decision_network = DecisionNetwork(decision_node)

# Realizamos inferencias en la red de decisiones con evidencia
evidence = {"Weather": "Sunny"}
marginal_probabilities = decision_network.infer(evidence)

# Imprimimos las probabilidades marginales
print("Probabilidades marginales:", marginal_probabilities)