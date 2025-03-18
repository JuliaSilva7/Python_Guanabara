lista = []
aluno = []
media = notas = 0

while True:
    nome = input('Digite o nome do aluno: ')
    n1 = float(input('Digite a primeira nota do aluno: '))
    n2 = float(input('Digite a segunda nota do aluno: '))
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    lista.append(aluno[:])
    aluno.clear()
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Deseja continuar? [s/n] ').lower().strip()
    if continuar == 'n':
        break

print('-=' * 30)
print(f'{"Nº":<5}', end='')
print(f'{"Nome":<10}', end='')
print(f'{"Média":>8}', end='')
for n in range(len(lista)):
    print(f'\n{n:<5}', end='')
    print(f'{lista[n][0]:<10}', end='')
    media = ((lista[n][1]) + (lista[n][2])) / 2
    print(f'{media:>8}', end='')
print(f'\n{'-=' * 30}')

while notas!=999:
    notas = int(input('\nMostrar notas de qual aluno?(Escreva 999 para sair) '))
    if notas == 999:
        break
    elif lista[notas] not in lista:
        print('O valor inserido foi inválido. Tente novamente.')
    else:
        print(f'Aluno: {lista[notas][0]}')
        print(f'Nota 1: {lista[notas][1]}')
        print(f'Nota 2: {lista[notas][2]}')
        print(f'\n{'-=' * 30}')
