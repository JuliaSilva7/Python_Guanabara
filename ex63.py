a = 1
b = 1
n = int(input("Escreva quantos números você quer que apareçam na sequência: "))
contador = 1

while contador <= n:
    if contador <= 2:
        print(f'{a},', end=' ')
        contador += 1
    else:
        c = a + b
        a = b
        b = c
        contador += 1
        print(f'{c},', end=' ')

print('Fim')
