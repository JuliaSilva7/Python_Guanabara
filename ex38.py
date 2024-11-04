a = int(input('Escreva um número: '))
b = int(input('Escreva outro número: '))

if a > b:
    print(f'{a} é maior que {b}')
elif b > a:
    print(f'{b} é maior que {a}')
else:
    print('Os números são iguais')
