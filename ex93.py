stats = dict()
lista = list()

stats['nome'] = input('Digite o nome do jogador: ')
partidas = int(input('Digite a quantidade de partidas: '))
for i in range(partidas):
    lista.append(int(input(f'Digite os gols marcados na partida {i}: ')))
stats['gols marcados'] = lista[:]
stats['total'] = sum(stats['gols marcados'])
print('-='*40)
print(stats)
print('*='*40)
for k,l in stats.items():
    print(f'O campo {k} tem o valor {l}')
print('*='*40)
print(f'O jogador {stats["nome"]} jogou {partidas} partidas')
for o,p in enumerate(stats['gols marcados']):
    print(f'    -> Na partida {o} fez {p} gols')
print(f'Fez um total de {stats["total"]} gols')
