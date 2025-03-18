lista = []
registro = []
maior = menor = 0

while True:
    nome = input('Digite o nome da pessoa: ')
    peso = float(input('Digite o peso da pessoa: '))
    registro.append(nome)
    registro.append(peso)
    lista.append(registro[:])
    registro.clear()
    if len(lista) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar in 'Nn':
        break

print(f'\nForam cadastradas {len(lista)} pessoas')
print(f'O maior peso foi {maior} Kg. Pessoas com esse peso:', end=' ')
for pessoa in lista:
    if pessoa[1] == maior:
        print(pessoa[0], end=', ')

print(f'\nO menor peso foi {menor} Kg. Pessoas com esse peso:', end=' ')
for pessoa in lista:
    if pessoa[1] == menor:
        print(pessoa[0], end=', ')
