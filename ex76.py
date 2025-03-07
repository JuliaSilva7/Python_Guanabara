tupla = ('Lápis',5,'Tesoura',10.5,'Caderno',40,'Estojo',9.50)
print('-'*50)
print(f'{"Listagem de preços":^50}')
print('-'*50)
for i in range(0,len(tupla),2):
    item = tupla[i]
    preco = tupla[i+1]
    print(f'{item:.<40} R${preco:>7.2f}')
print('-'*50)