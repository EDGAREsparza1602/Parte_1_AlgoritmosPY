# Ingenieria en Mecatronica

# Programa_Busqueda_Online

import random # El módulo random proporciona funciones para la generación de números aleatorios
import time # El módulo time proporciona funciones relacionadas con la manipulación del tiempo, como la medición del tiempo transcurrido, la conversión entre representaciones de tiempo y la suspensión del proceso durante un período de tiempo

def online_search(target, stream):
    for i, num in enumerate(stream): # Este bucle for itera sobre todos los elementos en el flujo de datos stream. enumerate(stream) proporciona tanto el índice i como el valor num de cada elemento en el flujo de datos
        print("Número actual:", num) #  Imprime el número actual del flujo de datos en cada iteración, lo que permite visualizar el progreso de la búsqueda
        if num == target: # Compara el número actual del flujo de datos con el objetivo que estamos buscando
            return f"¡El número {target} fue encontrado en la posición {i + 1}!"
        time.sleep(1)  # Simulación de procesamiento en tiempo real
    return f"El número {target} no fue encontrado en la secuencia."

def main():
    target_number = random.randint(1, 10)  # Número objetivo a buscar
    print("Número objetivo a buscar:", target_number)
    
    stream_of_numbers = iter(random.randint(1, 10) for _ in range(10))  # Secuencia de números generada de forma continua
    result = online_search(target_number, stream_of_numbers)
    print(result)

if __name__ == "__main__":
    main()