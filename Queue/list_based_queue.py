

class ListQueue:
    def __init__(self) -> None:
        # Creamos una lista
        self.items = []
        # Definimos el tamaño de la lista
        self.size = 0

    # Agregamos los metodos
    def enqueue(self, data):
        # Con el metodo insert() en la posicion 0 agregamos el valor
        self.items.insert(0, data)
        # Incrementamos el tamaño de la lista
        self.size += 1

    def dequeue(self):
        # Usamos el metodo pop() para eliminar el primer elemento
        # ubicado en el front del stack
        data = self.items.pop()
        # Reducimos el tamaño de la lista restanto 1
        self.size -= 1
        # Retornamos el valor eliminado de la lista
        return data

    # Metodo de recorrido para ver cuando elementos hay
    def traverse(self):
        total_items = self.size

        for item in range(total_items):
            print(self.items[item])
