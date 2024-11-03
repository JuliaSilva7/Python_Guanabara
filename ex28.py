import random

n = int(input('Escreva um número entre 0 e 5:'))
i = random.randrange(6)
if n == i:
    print('Você acertou o número')
else:
    print(f'Você errou. O número escolhido foi {i}')
