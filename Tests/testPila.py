from pilaNumbers import Stack
from clearWindow import borrarPantalla

num = Stack()
ageList = []
nameList = []
# listaNumbers = [12, 34, 22, 21, 19, 17, 18, 9, 5, 6, 7]


def run():
    for _ in range(3):
        borrarPantalla()
        print(""" 
            Welcome to get your first passport to travel anywhere 
                            ▓▓░░▓▓░░▓▓░░▓▓░░
                            ░░▓▓░░▓▓░░▓▓░░▓▓
                            ▓▓░░▓▓░░▓▓░░▓▓░░
                            ░░▓▓░░▓▓░░▓▓░░▓▓
        """)
        name = input("Add your name: ")
        age = int(input("Add your age: "))
        ageList.append(age)
        nameList.append(name)

    for i in ageList:
        num.add(i)
    # bucle para iterar en los nombres
    # for j in nameList:
    #    num.__str__(j)

    borrarPantalla()
    print(f"This' your list = {num.list()}")
    print(f"This' the size of your list = {num.listSize()}")
    print(f"This' the new list = {num.sum()}")
    # print(f"This' the names = {num.__str__()}")
    # print(num.__str__())
    # print(num.delete())


if __name__ == '__main__':
    run()
