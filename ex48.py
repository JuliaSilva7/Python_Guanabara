soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i

print(f'Soma dos números ímpares e múltiplos de 3: {soma}')
