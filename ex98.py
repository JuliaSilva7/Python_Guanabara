def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo = -passo
    if inicio < fim and passo < 0:
        passo = -passo
    if passo > 0:
        fim += 1
    else:
        fim -= 1

    for i in range(inicio, fim, passo):
        print(f'{i}', end=' ')
    print('Fim\n')

contador(1, 11, 1)
contador(10, -1, -2)

print('Personalize a sua contagem')
a = int(input('Insira o valor do início: '))
b = int(input('Insira o valor do fim: '))
c = int(input('Insira o valor do passo: '))

contador(a, b, c)
