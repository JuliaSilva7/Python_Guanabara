import random
n = ()
cont = maior = menor = 0

while cont < 5:
    numero = random.randint(1, 10)
    n += numero,
    if cont == 0:
        maior = numero
    elif numero > maior:
        maior = numero

    if cont == 0:
        menor = numero
    elif numero < menor:
        menor = numero

    cont += 1

print(n)
print(f'O maior é {maior}')
print(f'O menor é {menor}')
