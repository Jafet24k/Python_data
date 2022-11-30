
class Node():
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None) -> None:
        # instanciamos Node para usar sus caracteristicas
        Node.__init__(self, data, next)
        # Agregamos una nueva caracteristica
        self.previous = previous


# https://www.geeksforgeeks.org/introduction-and-insertion-in-a-doubly-linked-list/
