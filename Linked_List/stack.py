from linked_list import Node


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0
    # inserta un elemento en la parte superior de la pila

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1
    # Elimina el elemento superior de la fila

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else:
            return "The Stack is empty"
    # Devuelve una referencia al elemento superior de la pila

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The Stack is empty"
    # Limpia el stack por completo

    def clear(self):
        while self.top:
            self.pop()
