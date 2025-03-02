total_gasto = mais_que_1000 = menor = cont = produto_mais_barato = 0

while True:
    produto = input('Digite o nome do produto: ')
    preco = int(input('Digite o preco do produto: R$ '))

    total_gasto += preco
    cont += 1

    if cont == 1 or menor > preco:
        menor = preco
        produto_mais_barato = produto

    if preco > 1000:
        mais_que_1000 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]').strip().upper()

    if continuar == 'N':
        break

print(f'Total gasto: R${total_gasto}')
print(f'Produtos que custaram mais que R$1000: {mais_que_1000}')
print(f'O produto mais barato é {produto_mais_barato} e custou R${menor}')
