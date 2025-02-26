n = int(input('Escreva um número: '))
cont = somador = n = 0

while n != 999:
    somador += n
    cont += 1
    n = int(input('Escreva um número: '))

print(f'A soma dos valores é {somador}. Foram somados {cont} números.')
