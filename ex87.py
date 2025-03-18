lista = [[], [], []]
soma = coluna = 0

for i in range(3):
    for j in range(3):
        n = int(input(f'Digite um valor para {[i]},{[j]}: '))
        lista[i].append(n)
        if n % 2 == 0:
            soma += n
        if j == 2:
            coluna+=n

print('-=' * 30, end='')
for i in range(3):
    print(f'')
    for j in range(3):
        print(f'[ {lista[i][j]} ]', end=' ')

print(f'\nA soma de todos os valores é de {soma}')
print(f'A soma dos valores da 3ª coluna é de {coluna}')
print(f'O maior valor da 2ª linha é {max(lista[1])}')
