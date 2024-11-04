# Ingenieria en Mecatronica

# Programa_Comprobación_Hacia_Delante

tasks = { # Definición de las tareas del proyecto y sus requerimientos de recursos

    'Tarea A': {'Recursos': 3, 'Duración': 5}, # 'Tarea A' requiere 3 recursos y tiene una duración estimada de 5 unidades de tiempo
    'Tarea B': {'Recursos': 2, 'Duración': 3}, # 'Tarea B' requiere 2 recursos y tiene una duración estimada de 3 unidades de tiempo
    'Tarea C': {'Recursos': 4, 'Duración': 7}, # 'Tarea C' requiere 4 recursos y tiene una duración estimada de 7 unidades de tiempo
    'Tarea D': {'Recursos': 2, 'Duración': 4}  # 'Tarea D' requiere 2 recursos y tiene una duración estimada de 4 unidades de tiempo
}

def forward_checking(tasks, available_resources): # Función para realizar la comprobación hacia adelante
    for task, details in tasks.items():
        
        if details['Recursos'] <= available_resources: # Verificar si hay suficientes recursos para la tarea
            print(f"Se pueden asignar recursos a {task}")
            available_resources -= details['Recursos']  # Actualizar recursos disponibles
        else:
            print(f"No hay suficientes recursos para {task}. Requiere {details['Recursos']} recursos.") # Se imrpime el else


def main(): # Función principal
    
    available_resources = 8 # Recursos disponibles para asignación
    
    print("Comprobación hacia adelante para la asignación de recursos en el proyecto:") # Se imprime el resultado final 
    forward_checking(tasks, available_resources)

if __name__ == "__main__": # Verifica si el modulo se está ejecutando como el programa principal
    main() # Contiene el codigo principal que se debe ejecutar cuando el script se inicias