from grid import Grid


def run():
    # matrix = Grid(3, 3)
    primero = int(input("Primer numero: "))
    segundo = int(input("Segundo numero: "))

    matrix = Grid(primero, segundo)

    for row in range(matrix.get_heigth()):
        for col in range(matrix.get_width()):
            matrix[row][col] = row * col

    print(matrix)


if __name__ == '__main__':
    run()
