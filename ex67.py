while True:
    n = int(input('Escreva um número (Escreva um número negativo para parar): '))
    if n >= 0:
        for i in range(1, 11):
            tabuada = i * n
            print(f'{i} x {n} = {tabuada}')
    else:
        break

print('Fim do programa')
