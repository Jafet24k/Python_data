class Node():
    def __init__(self, Value) -> None:
        self.Value = Value
        self.Next = None

    def __str__(self) -> str:
        return str(self.Value)


class LinkedList():
    def __init__(self) -> None:
        self.Firts = None
        self.Size = 0

    def Append(self, Value):
        mynode = Node(Value)
        if self.Size == 0:
            self.Firts = mynode
        else:
            # Nodo current para recorrer la lista
            Current = self.Firts
            while Current.Next != None:
                Current = Current.Next
            Current.Next = mynode

        self.Size += 1

        return mynode

    def Remove(self, Value):
        if self.Size == 0:
            return False

        else:
            Current = self.Firts
            while Current.Next.Value != Value:
                if Current.Next == None:
                    return False
                else:
                    Current = Current.Next
            DeletedNode = Current.Next
            Current.Next = DeletedNode.Next

        self.Size -= 1

        return DeletedNode

    def __len__(self):
        return self.Size

    def __str__(self) -> str:
        String = "["
        Current = self.Firts
        while Current != None:
            String += str(Current)
            String += str(", ")
            Current = Current.Next
        String += "]"

        return String
