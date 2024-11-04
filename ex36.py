cor = {
    "vermelho-e-preto": "\033[30;101m"
}
print(f'{cor["vermelho-e-preto"]}CONDIÇÕES PARA EMPRÉSTIMO BANCÁRIO\033[0m')

salario = float(input('Escreva o seu salário: '))
preco = float(input('Escreva o preço da casa: '))
anos = int(input('Escreva em quantos anos você planeja pagar o empréstimo: '))

prestacao = (preco / anos) / 12
minimo = salario * 0.3

if prestacao > minimo:
    print(f'Empréstimo negado.')
else:
    print(f'Empréstimo aceito. A prestacao será de R${prestacao:.2f}')

