from stack import Stack

food = Stack()
food.push('egg')
food.push('ham')
food.push('spam')

print(food.pop())

# El ultimo en entrar es el primero en salir

print(food.peek())
