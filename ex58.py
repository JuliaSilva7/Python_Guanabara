import random

n = random.randint(1, 10)
escolha = 0
contagem = 1

while escolha != n:
    escolha = int(input('Tente adivinhar o número (entre 1 e 10): '))
    if escolha == n:
        print('Parabéns você acertou!')
    else:
        contagem += 1

print(f'Você precisou de {contagem} tentativas.')
