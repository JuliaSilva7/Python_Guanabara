salario = float(input('Escreva o salário: '))

if salario > 1250:
    aumento = salario * 1.1
    print(f'Seu novo salário é de {aumento:.2f}')
else:
    aumento = salario * 1.15
    print(f'Seu novo salário é de {aumento:.2f}')
