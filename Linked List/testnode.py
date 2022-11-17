from node import Node

node1 = None
node2 = Node("A", None)
node3 = Node("B", node2)
node4 = Node("C", node1)

# print(node3.next.data)

head = None
for count in range(1, 10):
    head = Node(count, head)


while head != None:
    print(head.data)
    head = head.next
