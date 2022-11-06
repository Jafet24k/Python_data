from array import Array


def run():
    numero = int(input("Ingresa el numero\n"))
    contador = Array(numero)
    print(f"Representacion en String:\n{contador.__str__()}\n")
    print(f"Lingitud del array:\n{contador.__len__()}\n")
    [contador.__setitems__(i, i+1) for i in range(contador.__len__())]
    print(f"Arreglo con datos secuenciales\n {contador.__str__()}\n")
    print(f"Arreglo con suma:\n {contador.__sum__()}\n")


if __name__ == '__main__':
    run()
