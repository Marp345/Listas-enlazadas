
class Nodo:
    def __init__(self, tarea, fecha_vencimiento, prioridad):
        self.tarea = tarea
        self.fecha_vencimiento = fecha_vencimiento
        self.prioridad = prioridad
        self.siguiente = None  # Puntero al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # La lista empieza vacía

    def agregar_tarea(self, tarea, fecha_vencimiento, prioridad):
        nuevo_nodo = Nodo(tarea, fecha_vencimiento, prioridad)
        if not self.cabeza:
            self.cabeza = nuevo_nodo  # Si la lista está vacía, el nuevo nodo es la cabeza
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:  # Navegar hasta el último nodo
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo  # Agregar el nuevo nodo al final

    def eliminar_tarea(self, tarea):
        nodo_actual = self.cabeza
        previo = None
        while nodo_actual:  # Buscar la tarea en la lista
            if nodo_actual.tarea == tarea:
                if previo:  # Si no es el primer nodo
                    previo.siguiente = nodo_actual.siguiente
                else:
                    self.cabeza = nodo_actual.siguiente  # Si es el primer nodo
                return f"Tarea '{tarea}' eliminada."
            previo = nodo_actual
            nodo_actual = nodo_actual.siguiente
        return f"Tarea '{tarea}' no encontrada."

    def mostrar_tareas(self):
        if not self.cabeza:
            return "No hay tareas en la lista."
        nodo_actual = self.cabeza
        tareas = []
        while nodo_actual:
            tareas.append(f"Tarea: {nodo_actual.tarea}, Fecha: {nodo_actual.fecha_vencimiento}, Prioridad: {nodo_actual.prioridad}")
            nodo_actual = nodo_actual.siguiente
        return "\n".join(tareas)

# Ejemplo de ejecución
if __name__ == "__main__":
    lista = ListaEnlazada()
    
    # Agregar tareas
    lista.agregar_tarea("Terminar informe de ventas", "2024-12-01", "Alta")
    lista.agregar_tarea("Reunión de equipo", "2024-11-28", "Media")
    lista.agregar_tarea("Enviar propuesta de cliente", "2024-11-30", "Alta")
    
    # Mostrar tareas
    print("Tareas Pendientes:")
    print(lista.mostrar_tareas())
    
    # Eliminar una tarea
    print("\nEliminar tarea 'Reunión de equipo':")
    print(lista.eliminar_tarea("Reunión de equipo"))
    
    # Mostrar tareas después de eliminar una
    print("\nTareas Pendientes Después de la Eliminación:")
    print(lista.mostrar_tareas())
