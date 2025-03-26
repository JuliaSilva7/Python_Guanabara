import random
from operator import itemgetter

jogo = {}
ranking = []
for i in range(1,5):
    jogo[f'Jogador {i}'] = random.randint(1, 6)

print('\nValores Sorteados\n')
for jogador,jogada in jogo.items():
    print(f'O {jogador} jogou {jogada}')

print('\nRanking de Jogadores\n')
ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)
for j,k in enumerate(ranking, start=1):
    print(f'{j}ºlugar: {k[0]} que jogou {k[1]}')
