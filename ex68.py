import random

cont = soma = n = 0

while True:
    n = int(input('Escolha um número: '))
    n_computador = random.randint(0, 10)
    soma = n + n_computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Escolha par ou impar: [P/I] ').upper().strip()[0]
    if tipo == 'P':
        if soma % 2 == 0:
            cont += 1
            print(f'Você ganhou. Você jogou {n} e o computador {n_computador}.')
        else:
            print(f'Você perdeu. Você jogou {n} e o computador {n_computador}.')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            cont += 1
            print(f'Você perdeu. Você jogou {n} e o computador {n_computador}.')
        else:
            print('Você perdeu')
            break

print(f'Você venceu {cont} vezes.')
