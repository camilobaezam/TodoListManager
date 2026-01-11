import os  # Para verificar si el archivo existe

def cargar_tareas(archivo='tasks.txt'):
    """Carga las tareas desde un archivo de texto."""
    tareas = []
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            for line in f:
                tareas.append(line.strip())  # Elimina \n al final de cada línea
    return tareas

def guardar_tareas(tareas, archivo='tasks.txt'):
    """Guarda las tareas en un archivo de texto."""
    with open(archivo, 'w') as f:
        for tarea in tareas:
            f.write(tarea + '\n')

def agregar_tarea(tareas):
    """Agrega una nueva tarea a la lista."""
    nueva_tarea = input("Ingresa la nueva tarea: ").strip()
    if nueva_tarea:
        tareas.append(nueva_tarea)
        print(f"Tarea '{nueva_tarea}' agregada.")
    else:
        print("La tarea no puede estar vacía.")

def eliminar_tarea(tareas):
    """Elimina una tarea por índice."""
    listar_tareas(tareas)
    if tareas:
        try:
            indice = int(input("Ingresa el número de la tarea a eliminar: ")) - 1
            if 0 <= indice < len(tareas):
                tarea_eliminada = tareas.pop(indice)
                print(f"Tarea '{tarea_eliminada}' eliminada.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Debe ser un número.")

def listar_tareas(tareas):
    """Lista todas las tareas."""
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def main():
    """Función principal con el menú."""
    tareas = cargar_tareas()
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Listar tareas")
        print("4. Salir")
        opcion = input("Elige una opción: ").strip()
        
        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            eliminar_tarea(tareas)
        elif opcion == '3':
            listar_tareas(tareas)
        elif opcion == '4':
            guardar_tareas(tareas)
            print("Tareas guardadas. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
