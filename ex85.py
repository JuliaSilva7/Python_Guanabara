lista = [[],[]]

for i in range(1,8):
    n = int(input(f'Escreva o {i}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
    lista[0].sort()
    lista[1].sort()

print(f'Os valores pares são {lista[0]}')
print(f'Os valores ímpares são {lista[1]}')
