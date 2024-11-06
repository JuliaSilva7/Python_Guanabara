soma = 0

for i in range(6):
    n = int(input('Escreva um número: '))
    if n % 2 == 0:
        soma += n

print(f'A soma dos números é igual à {soma}')
