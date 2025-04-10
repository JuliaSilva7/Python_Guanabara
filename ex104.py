def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Erro! O valor passado deve ser numérico.')

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
