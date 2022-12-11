from node_based_queue import TwoWayNode, Queue


def run():
    food = Queue()

    for _ in range(3):
        names = str(input("Nombre de alimentos: "))
        food.enqueue(names)

    print(f"Segundo nodo: {food.head.next.data}")
    print(f"Ultimo nodo: {food.tail.data}")
    print(f"Nodo anterior: {food.tail.previous.data}")
    print(f"Contar nodos: {food.count}")
    print(f"Removemos el primer nodo: {food.dequeue()}")
    print(f"El que era el segundo ahora es primero: {food.head.data}")


if __name__ == '__main__':
    run()
