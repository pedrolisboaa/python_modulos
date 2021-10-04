from random import randint


def gerar_aleatorio():
    return randint(0, 10000)


if __name__ == '__main__':
    print(gerar_aleatorio())