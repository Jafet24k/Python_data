from stack_based_queue import Queue

numbers = Queue()


def run():
    for _ in range(4):
        number = input("Numeros: ")
        numbers.enqueue(number)

    print(f"\nPila entrante: {numbers.inbound_stack}")
    print(f"Pila de salida: {numbers.outbound_stack}\n")
    # Sacamos de la Inbound stack y lo mandamos a la outbound stack
    print(f"Sacamos de la Pila entrante: {numbers.dequeue()}\n")
    print(f"Pila entrante: {numbers.inbound_stack}")
    print(f"Pila de salida: {numbers.outbound_stack}\n")


if __name__ == '__main__':
    run()
