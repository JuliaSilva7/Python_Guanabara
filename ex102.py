def fatorial(numero,show=False):
    """ A função fatorial() calcula a fatorial de um número.
     Parâmetros: numero(int); show(bool): True ou False
     No parâmetro show, deve ser indicado True, caso se queira mostrar o cálculo da fatorial ou False, caso queira visualizar somente o resultado. Em número deve ser indicado o número da fatorial. """
    n = 1
    for i in range(numero,0,-1):
        if show:
            if i > 1:
                print(f'{i} *', end=' ')
            else:
                print(f'{i} = ', end=' ')
        n*=i
    return n


num = int(input('Escreva o valor de um número para o cálculo da fatorial: '))
calculo_str = input('Deseja mostrar o cálculo da fatorial ? [true/false]: ] ').lower()
calculo = calculo_str == 'true'
res = fatorial(num,calculo)
print(f'{res}')
