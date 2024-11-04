# Ingenieria en Mecatronica
# Programa_Iteración_de_Valores

def funcion_objetivo(x, y, z): # Definimos la función objetivo
    return x**2 + y**2 + z**2

def iteracion_valores(x, y, z, learning_rate): # Definimos una función que actualiza los valores de las variables en cada iteración
    # Calculamos el gradiente de la función objetivo respecto a cada variable
    gradiente_x = 2 * x
    gradiente_y = 2 * y
    gradiente_z = 2 * z

    # Actualizamos los valores de las variables usando el gradiente descendiente
    x_nuevo = x - learning_rate * gradiente_x
    y_nuevo = y - learning_rate * gradiente_y
    z_nuevo = z - learning_rate * gradiente_z

    return x_nuevo, y_nuevo, z_nuevo

max_iteraciones = 1000 # Definimos la condición de parada: el numero máximo de iteraciones

x_actual, y_actual, z_actual = 1.0, 1.0, 1.0 # Definimos los valores iniciales de las variables

learning_rate = 0.1 # Definimos el tamaño del paso de aprendizaje (learning rate)

for i in range(max_iteraciones): # Iteramos hasta alcanzar el numero máximo de iteraciones
    x_actual, y_actual, z_actual = iteracion_valores(x_actual, y_actual, z_actual, learning_rate) # Actualizamos los valores de las variables en cada iteracion

# Imprimimos el valor optimo de las variables y el valor de la función objetivo
print("Valor óptimo de x:", x_actual)
print("Valor óptimo de y:", y_actual)
print("Valor óptimo de z:", z_actual)
print("Valor óptimo de la función objetivo:", funcion_objetivo(x_actual, y_actual, z_actual))