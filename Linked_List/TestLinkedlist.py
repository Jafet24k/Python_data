from linked_list import SinglyLinkedList

words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')
words.append('soap')
current = words.tail


while current:
    print(current.data)
    current = current.next

for word in words.iter():
    print(word)

# usamos la funcion search para buscar proveniente del archivo linked_list.py
words.search('soap')
