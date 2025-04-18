def leiadinheiro(numero):
    if numero.isnumeric() and numero != '' and numero >='0':
        numero = int(numero)
        return numero
    else:
        print('Erro: valor inválido')
