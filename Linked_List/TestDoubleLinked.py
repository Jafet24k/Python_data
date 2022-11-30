from double_linked_list import Node, TwoWayNode

head = TwoWayNode(1)
tail = head

for data in range(2, 6):
    tail.next = TwoWayNode(data, tail)
    tail = tail.next

probe = tail

while probe != None:
    print(f"This {probe.data}")
    probe = probe.previous
