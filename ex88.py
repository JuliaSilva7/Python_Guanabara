import random

lista = []
sorteio = int(input('Quantos jogos você quer sortear? '))
for i in range(sorteio):
    num = range(1,61)
    n = random.sample(num,6)
    lista.append(n)

for c in range(len(lista)):
    print(f'Jogo {c+1}: {sorted(lista[c])}')
