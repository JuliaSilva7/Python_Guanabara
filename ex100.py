import random


def sorteia():
    for c in range(0, 5):
        numero = random.randint(1, 10)
        numeros.append(numero)
    return numeros


def soma_par():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    return soma


numeros = list()
print(f'Na lista de números {sorteia()}, a soma dos pares é de {soma_par()}')
