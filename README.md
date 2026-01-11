# TodoListManager

Un gestor de tareas simple en Python. Permite agregar, eliminar y listar tareas en una lista, con persistencia en un archivo de texto ("tasks.txt"). Usa listas para almacenar las tareas y bucles para manejar un menú interactivo en la consola.

## Descripción

Este programa es una herramienta básica para gestionar tareas pendientes. Las tareas se almacenan en memoria como una lista de strings y se guardan en un archivo de texto para persistencia entre ejecuciones. No usa bases de datos ni librerías externas avanzadas, solo Python estándar (con `os` para verificar archivos).

Características principales:
- Agregar una nueva tarea.
- Eliminar una tarea por número.
- Listar todas las tareas pendientes.
- Guardar y cargar tareas automáticamente desde "tasks.txt".

## Requisitos

- Python 3.x (probado en Python 3.8+).
- No se requieren librerías externas (usa módulos estándar como `os`).

## Instalación

1. Clona o descarga el repositorio: https://github.com/camilobaezam/TodoListManager.git
2. Navega al directorio: cd TodoListManager

## Uso

Ejecuta el programa desde la consola: python main.py
Aparecerá un menú:
--- Gestor de Tareas ---

Agregar tarea
Eliminar tarea
Listar tareas
Salir

Elige una opción:

- **Opción 1**: Pide el texto de la tarea y la agrega.
- **Opción 2**: Lista las tareas y pide el número para eliminar.
- **Opción 3**: Muestra las tareas numeradas.
- **Opción 4**: Guarda las tareas en "tasks.txt" y sale.

Las tareas se cargan automáticamente al inicio si "tasks.txt" existe.

## Ejemplos de Uso

### Ejemplo 1: Agregar tareas
1. Ejecuta el programa.
2. Elige 1: "Agregar tarea".
3. Ingresa: "Comprar leche".
4. Elige 1 nuevamente: "Llamar a mamá".
5. Elige 3: "Listar tareas".
   - Salida:
Tareas pendientes:
1. Comprar leche
2. Llamar a mamá


### Ejemplo 2: Eliminar una tarea
1. Con las tareas anteriores.
2. Elige 2: "Eliminar tarea".
- Muestra la lista.
- Ingresa "1" para eliminar "Comprar leche".
3. Elige 3: Ahora solo queda "Llamar a mamá".

### Ejemplo 3: Persistencia
1. Sal de la aplicación (opción 4): Guarda en "tasks.txt".
2. Reabre el programa: Carga las tareas desde el archivo automáticamente.

## Notas
- El archivo "tasks.txt" se crea automáticamente si no existe.
- Si el archivo está dañado o vacío, la lista de tareas comienza vacía.
- No maneja errores avanzados (e.g., archivos corruptos), pero es robusto para uso simple.
- Puedes extenderlo agregando más funciones, como editar tareas o buscar.

## Contribuciones
Si quieres contribuir, abre un pull request. ¡Ideas bienvenidas!

## Autor
- Camilo Baeza
