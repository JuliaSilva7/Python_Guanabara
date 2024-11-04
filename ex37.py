n = int(input('Digite um número inteiro: '))
escolha = int(input(
    """Escolha um número para converter em tipo binário, octal ou hexadecimal:
    [1 - Binário] 
    [2 - Octal]
    [3 - Hexadecimal]: """))

binario = bin(n)
octal = oct(n)
hexa = hex(n)

if escolha == 1:
    print(f'O número convertido para binário é {binario[2:]}')
elif escolha == 2:
    print(f'O número convertido para octal é {octal[2:]}')
elif escolha == 3:
    print(f'O número convertido para hexadecimal é {hexa[2:]}')
else:
    print('Opção inválida. Tente novamente.')
