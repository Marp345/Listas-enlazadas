1. Clase Nodo
Representa un elemento de la lista enlazada.
Atributos:
tarea: Contiene la descripción de la tarea.
fecha_vencimiento: Almacena la fecha límite para completar la tarea.
prioridad: Define el nivel de importancia de la tarea (por ejemplo, "Alta", "Media").
siguiente: Un puntero al siguiente nodo en la lista, inicialmente None.
Constructor (__init__):
Se inicializan los atributos con los valores proporcionados al crear una instancia.
2. Clase ListaEnlazada
Representa una lista enlazada simple que organiza las tareas.
Atributo:
cabeza: Apunta al primer nodo de la lista. Si la lista está vacía, su valor es None.
Métodos de ListaEnlazada
agregar_tarea(tarea, fecha_vencimiento, prioridad):

Crea un nuevo nodo con la información de la tarea.
Si la lista está vacía (cabeza es None), el nodo recién creado se convierte en la cabeza.
Si no está vacía, recorre los nodos existentes hasta llegar al último y lo enlaza al nuevo nodo.
eliminar_tarea(tarea):

Busca un nodo con la tarea especificada.
Si lo encuentra:
Si es el primer nodo (cabeza), actualiza la cabeza para que apunte al siguiente nodo.
Si no es el primero, ajusta el puntero del nodo previo para saltarse el nodo actual.
Si no encuentra la tarea, devuelve un mensaje indicando que no se encontró.
Complejidad: Lineal 
O
(
n
)
O(n), ya que puede necesitar recorrer toda la lista.
mostrar_tareas():

Recorre la lista desde la cabeza hasta el final, acumulando las descripciones de cada tarea en una lista.
Devuelve un string que muestra todas las tareas en un formato legible.
Si la lista está vacía, informa que no hay tareas.
3. Bloque Principal (if __name__ == "__main__":)
Sirve como punto de entrada del programa para demostrar su funcionalidad.
Operaciones realizadas:
Crea una instancia de la lista enlazada: Se inicia con una lista vacía.
Agrega tres tareas:
Cada tarea tiene un título, una fecha de vencimiento y una prioridad.
Muestra las tareas actuales:
Llama a mostrar_tareas() para listar todas las tareas.
Elimina una tarea específica:
Busca y elimina la tarea llamada "Reunión de equipo".
Muestra un mensaje indicando si la tarea fue eliminada o no encontrada.
Vuelve a mostrar las tareas:
Confirma que la tarea eliminada ya no está en la lista.
4. Explicación del Flujo
Este programa organiza tareas usando una lista enlazada, donde cada tarea es un nodo y está conectada al siguiente.
La estructura es dinámica, lo que significa que puede crecer o reducirse según se agreguen o eliminen tareas.
Se destacan las ventajas de la lista enlazada:
No requiere una cantidad fija de memoria.
Es fácil agregar o eliminar elementos.
