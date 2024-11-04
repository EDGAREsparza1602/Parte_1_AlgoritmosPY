# Ingenieria en Mecatronica

# Programa_Red_Bayesiana_Dinamica

from pgmpy.models import DynamicBayesianNetwork as DBN  # Importamos la clase DBN
from pgmpy.factors.discrete import TabularCPD  # Importamos la clase TabularCPD para definir las CPDs
from pgmpy.inference import VariableElimination  # Importamos la clase VariableElimination para realizar inferencia

# Creamos el objeto DBN
dbn = DBN()

# Definimos los nodos en la DBN
dbn.add_nodes_from(['X0', 'X1'])  # Dos variables en cada período de tiempo

# Definimos las relaciones temporales entre los nodos
dbn.add_edge('X0', 'X1')  # X0 afecta a X1 en cada período de tiempo

# Definimos las probabilidades condicionales para X0
cpd_x0 = TabularCPD(variable='X0', variable_card=2, values=[[0.6], [0.4]])  # Valores arbitrarios

# Definimos las probabilidades condicionales para X1 dado X0
cpd_x1 = TabularCPD(variable='X1', variable_card=2, values=[[0.2, 0.5], [0.8, 0.5]],
                    evidence=['X0'], evidence_card=[2])  # Valores arbitrarios

# Añadimos las CPDs al modelo
dbn.add_cpds(cpd_x0, cpd_x1)

# Verificamos si el modelo es válido
print("¿El modelo es válido?", dbn.check_model())

# Creamos un objeto de inferencia
inference = VariableElimination(dbn)

# Calculamos la probabilidad de X1 dado X0
result = inference.query(variables=['X1'], evidence={'X0': 0})  # Suponiendo que X0 = 0
print("Probabilidad de X1 dado X0=0:", result.values)