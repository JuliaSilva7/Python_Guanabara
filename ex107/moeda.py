def aumentar(numero, aumento, formatar=False):
    """ Acrescenta um aumento percentual a um valor numérico.
    Parâmetros:
    numero (float): valor numérico
    aumento (float): valor percentual do aumento
    Return (float): valor resultado do aumento. """
    if numero >= 0:
        res = (numero * (100 + aumento)) / 100
        if formatar:
            return f'R${res:.2f}'
        else:
            return res
    else:
        print('Valor inválido')


def diminuir(numero, decrescimo, formatar=False):
    """ Decresce uma diminuição percentual a um valor numérico.
    Parâmetros:
    numero (float): valor numérico
    decrescimo (float): valor percentual da diminuição
    Return (float): retorna o valor resultante após o decréscimo."""
    if 100 >= decrescimo >= 0:
        res = (numero * (100 - decrescimo)) / 100
        if formatar:
            return f'R${res:.2f}'
        else:
            return res
    else:
        print('Valor inválido')


def dobro(numero, formatar=False):
    """ Dobra o valor
    Parâmetros:
    numero (float): valor numérico
    return (float): retorna o valor resultado do dobro."""
    res = numero * 2
    if formatar:
        return f'R${res:.2f}'
    else:
        return res


def metade(numero, formatar=False):
    """ Calcula a metade do valor
    Parâmetros:
    numero (float) : valor numérico
    return (float) : retorna o valor resultado da metade do valor."""
    res = numero / 2
    if formatar:
        return f'R${res:.2f}'
    else:
        return res


def moeda(numero):
    """
    Formata o número para dinheiro
    :param numero: o preço do produto
    :return: o valor formatado
    """
    return f'R${numero:.2f}'

