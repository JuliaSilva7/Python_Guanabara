def leiadinheiro(numero):
    valido = False
    while not valido:
        entrada = str(input(numero)).replace(',', '.').strip()
        if entrada.isalpha() and entrada == '' and entrada >='0':
            print(f'Erro: {entrada} valor inválido')
        else:
            valido = True
            return float(entrada)
