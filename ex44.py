preco = float(input('Qual o preço do produto: '))
print(
    """Selecione a forma de pagamento: \n 1 - À vista (Dinheiro ou cheque)\n 2 - Em até 2 vezes no cartão\n 3 - 3 vezes ou mais no cartão \n 4 - à vista no cartão""")
pag = int(input('Qual a forma de pagamento: '))

if pag == 1:
    preco_final = preco * 0.9
    print(f'O preço final vai ser de R${preco_final:.2f}')
elif pag == 2:
    preco_final = preco
    print(f'O preço final vai ser de R${preco_final:.2f}')
elif pag == 3:
    preco_final = preco * 1.2
    print(f'O preço final vai ser de R${preco_final:.2f}')
elif pag == 4:
    preco_final = preco * 0.95
    print(f'O preço final vai ser de R${preco_final:.2f}')
else:
    print('Essa opção não existe. Escreva novamente.')

