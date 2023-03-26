
class Stack:
    def __init__(self) -> None:
        self.data = []
        self.size = 0
        self.names = []

    def add(self, data):
        num1 = data
        num = self.data.append(num1)
        self.size += 1
        return num

    def list(self):
        return self.data

    def listSize(self):
        return self.size

    def sum(self):
        date = self.data
        for j in date:
            if j <= 17:
                edad = 18 - j
                position = date.index(j)
                # print(position)
                # print(date[position]+edad)
                date[position] += edad
        return date

    def delete(self):
        while self.data:
            self.data.pop()

    def __str__(self, data) -> str:
        String = "["
        Current = self.size
        while Current != None:
            String += str(Current)
            String += str(", ")
            # Current = Current.Next
        String += "]"

        return String
