stats = list()
copia = dict()
gols = []
dados = None

while True:
    copia['nome'] = input('Digite o nome do jogador: ')
    partidas = int(input('Digite a quantidade de partidas: '))
    for i in range(partidas):
        gols.append(int(input(f'Digite os gols marcados na partida {i}: ')))
    copia['gols marcados'] = gols[:]
    gols.clear()
    copia['total'] = sum(copia['gols marcados'])
    stats.append(copia.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-='*40)
print(stats)
print('*='*40)
print(f'{"Código": <10}', end='')
print(f'{"Nome": <15}', end='')
print(f'{"Gols": <20}', end='')
print(f'{f'"Total"\n'}', end='')
for k,l in enumerate(stats):
    print(f'{k:<10}{l["nome"]:<15}{str(l["gols marcados"]):<20}{l["total"]}')

print("\n" + "*=" * 40)
while True:
    dados = int(input('Levantamento de dados de qual jogador ( Digite 999 para sair ):'))
    if dados == 999:
        break
    elif dados>= len(stats):
        print('O seu valor está fora do alcance, digite novamente.')
    for n in range(len(stats)):
        if n == dados:
            print(f'Levantamento do jogador {stats[n]['nome']:}')
            for o in range(len(stats[n]['gols marcados'])):
                print(f'No jogo {o} fez {stats[n]['gols marcados'][o]} gols')
