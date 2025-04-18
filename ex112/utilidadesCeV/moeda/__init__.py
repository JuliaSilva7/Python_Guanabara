def aumentar(numero=0, aumento=0, formatar=False):
    """ Acrescenta um aumento percentual a um valor numérico.
    Parâmetros:
    numero (float): valor numérico
    aumento (float): valor percentual do aumento
    Return (float): valor resultado do aumento. """
    if numero >= 0:
        res = (numero * (100 + aumento)) / 100
        return res if formatar == False else moeda(res)
    else:
        print('Valor inválido')


def diminuir(numero=0, decrescimo=0, formatar=False):
    """ Decresce uma diminuição percentual a um valor numérico.
    Parâmetros:
    numero (float): valor numérico
    decrescimo (float): valor percentual da diminuição
    Return (float): retorna o valor resultante após o decréscimo."""
    if 100 >= decrescimo >= 0:
        res = (numero * (100 - decrescimo)) / 100
        return res if formatar == False else moeda(res)


def dobro(numero=0, formatar=False):
    """ Dobra o valor
    Parâmetros:
    numero (float): valor numérico
    return (float): retorna o valor resultado do dobro."""
    res = numero * 2
    return res if formatar == False else moeda(res)


def metade(numero=0, formatar=False):
    """ Calcula a metade do valor
    Parâmetros:
    numero (float) : valor numérico
    return (float) : retorna o valor resultado da metade do valor."""
    res = numero / 2
    return res if formatar == False else moeda(res)


def moeda(numero=0,tipo_moeda = 'R$'):
    """
    Formata o número para dinheiro
    :param numero: o preço do produto
    :param tipo_moeda: tipo do moeda
    :return: o valor formatado
    """
    return f'{tipo_moeda}{numero:>8.2f}'.replace('.',',')


def resumo(numero=0, aumento=0, decrescimo=0):
    print('-' * 30)
    texto = 'RESUMO DO VALOR'
    print(f'{texto.center(30)}')
    print('-' * 30)
    print(f'Preço analisado: {moeda(numero)}')
    print(f'Dobro do preço: {dobro(numero, True)}')
    print(f'Metade do preço: {metade(numero, True)}')
    print(f'{aumento}% de aumento: {aumentar(numero, aumento, True)}')
    print(f'{decrescimo}% de desconto: {diminuir(numero, decrescimo, True)}')
