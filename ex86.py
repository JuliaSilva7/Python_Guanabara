lista = [[],[],[]]

for i in range(3):
    for j in range(3):
        n = int(input(f'Digite um valor para {[i]},{[j]}: '))
        lista[i].append(n)

print('-='*30, end='')
for i in range(3):
    print(f'')
    for j in range(3):
        print(f'[ {lista[i][j]:^5} ]', end=' ' )
