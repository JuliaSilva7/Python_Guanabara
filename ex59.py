opcao = 0
a = int(input('Digite um valor:'))
b = int(input('Digite outro valor:'))

while opcao!= 5:
    opcao = int(input(""" 
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Selecione uma das opções acima: """))
    if opcao == 1:
        print(f'Resultado: {a+b}')
    elif opcao == 2:
        print(f'Resultado: {a*b}')
    elif opcao == 3:
        if a > b:
            print(f'O maior é {a}')
        elif b>a:
            print(f'O maior é {b}')
        else:
            print('Os valores são iguais')
    elif opcao == 4:
        a = int(input('Digite um valor:'))
        b = int(input('Digite outro valor:'))
    elif opcao ==5:
        print('Programa finalizado')
    else:
        print('Opção inválida')
