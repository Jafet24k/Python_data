from list_based_queue import ListQueue

# food = ListQueue()
# food.enqueue("eggs")
# food.enqueue("ham")
# food.enqueue("parrot")
# food.enqueue("spam")


# print(food.dequeue())
# print(food.traverse())


food = ListQueue()


def run():
    # Usamos for _ para iterar por la cantidad de veces elegida
    for _ in range(3):
        foods = str(input('Foods Names: '))
        food.enqueue(foods)
    print(food.traverse())
    print('El primer elemento en ingresar es el primer elemento en salir (FIFO)')
    print(f"Eliminamos como primer elemento: {food.dequeue()}")


if __name__ == '__main__':
    run()
