class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
        
    def __str__(self):
        return f'{self.descripcion} - Prioridad: {self.prioridad} - Completada: {self.completada}'
        
    def completar(self):
        self.completada = True


class ListaTareas:
    def __init__(self):
        self.tareas = []
        
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        
    def mostrar_tareas(self):
        for tarea in self.tareas:
            print(tarea)
            
    def mostrar_tareas_completadas(self):
        for tarea in self.tareas:
            if tarea.completada:
                print(tarea)
            
    def mostrar_tareas_pendientes(self):
        for tarea in self.tareas:
            if not tarea.completada:
                print(tarea)


lista_tareas = ListaTareas()

tarea1 = Tarea("Comprar leche", 1)
tarea2 = Tarea("Ir al gimnasio", 2)
tarea3 = Tarea("Hacer la tarea de matemáticas", 3)

lista_tareas.agregar_tarea(tarea1)
lista_tareas.agregar_tarea(tarea2)
lista_tareas.agregar_tarea(tarea3)

# lista_tareas.mostrar_tareas()

tarea2.completar()

lista_tareas.mostrar_tareas_completadas()

lista_tareas.mostrar_tareas_pendientes()
