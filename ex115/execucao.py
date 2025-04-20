from ex115 import cadastro

arquivo = 'registro.txt'
while True:
    if not cadastro.abrirarquivo(arquivo) :
        cadastro.criararquivo(arquivo)


    cadastro.cabecalho('Menu Principal')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar pessoas')
    print('3 - Sair do programa')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        cadastro.listar()
    elif opcao == '2':
        nome = input('Digite o nome da pessoa: ')
        idade = input('Digite a idade da pessoa: ')
        cadastro.registrar(nome,idade)
    elif opcao == '3':
        break
    else:
        print(f'\033[31mOpção inválida. Tente novamente.\033[m')
