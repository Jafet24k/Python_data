

class Queue:
    def __init__(self) -> None:
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        #  Agreamos datos en inbound stack
        self.inbound_stack.append(data)

    def dequeue(self):
        # si no hay nada en outbound stack entonces:
        if not self.outbound_stack:
            # mientras haya algo en inbound stack
            while self.inbound_stack:
                # a outbound stack le agregamos los valores de inbound stack
                self.outbound_stack.append(self.inbound_stack.pop())
        # Por ultimo sacamos el primer elemento del inbound stack
        return self.outbound_stack.pop()
