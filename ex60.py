n = int(input('Escreva um número: '))
fatorial = 1

while n > 1:
    fatorial *= n
    n = n - 1

print(f'Fatorial: {fatorial}')
