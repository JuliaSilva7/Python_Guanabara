cont = soma = 0

while True:
    n = int(input('Escreva um número (Digite 999 para parar): '))
    if n == 999:
        break
    else:
        cont += 1
        soma += n

print(f'Foram somados {cont} números e a soma é {soma}')
