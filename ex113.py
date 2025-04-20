def leiaint(inteiro):
    while True:
        try:
            valor = int(input(inteiro))
            return valor
        except (ValueError, TypeError):
            print('Erro no valor digitado. O valor deve ser inteiro.')
            continue
        except KeyboardInterrupt:
            print(f'O usuário preferiu não digitar esse valor')
            return 0


def leiafloat(real):
    while True:
        try:
            valor = float(input(real))
            return valor
        except ValueError or TypeError:
            print('Erro no valor digitado. O valor deve ser real.')
            continue
        except KeyboardInterrupt:
            print(f'O usuário preferiu não digitar esse valor')
            return 0

n1 = leiaint('Digite um valor: ')
n2 = leiafloat('Digite um valor: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')