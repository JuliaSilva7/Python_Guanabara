import random
from time import sleep

print("""Suas opções: 
[0]PEDRA
[1]TESOURA
[2]PAPEL
""")

opcoes = ['pedra', 'papel', 'tesoura']
jogador = int(input('Escolha uma das opções acima: '))
computador = random.randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if computador == 0:
    if jogador == 0:
        print(f'O jogador e o computador jogaram {opcoes[0]} Eles empataram!')
    elif jogador == 1:
        print(f'O computador jogou {opcoes[0]} e o jogador jogou {opcoes[1]}. O jogador venceu!')
    elif jogador == 2:
        print(f'O computador jogou {opcoes[0]} e o jogador jogou {opcoes[2]}. O computador venceu!')
    else:
        print('Opção inválida. Tente novamente.')
elif computador == 1:
    if jogador ==0:
        print(f'O computador jogou {opcoes[1]} e o jogador jogou {opcoes[0]}. O computador venceu!')
    elif jogador == 1:
        print(f'O computador jogou {opcoes[1]} e o jogador jogou {opcoes[1]}. Eles empataram!')
    elif jogador == 2:
        print(f'O computador jogou {opcoes[1]} e o jogador jogou {opcoes[2]}. O jogador venceu!')
    else:
        print('Opção inválida. Tente novamente.')
elif computador == 2:
    if jogador == 0:
        print(f'O computador jogou {opcoes[2]} e o jogador jogou {opcoes[0]}. O jogador venceu!')
    elif jogador==1:
        print(f'O computador jogou {opcoes[2]} e o jogador jogou {opcoes[1]}. O computador venceu!')
    elif jogador == 2:
        print(f'O computador jogou {opcoes[2]} e o jogador jogou {opcoes[2]}. Eles empataram!')
    else:
        print('Opção inválida. Tente novamente.')

