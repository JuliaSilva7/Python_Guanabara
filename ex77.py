palavras = ("carro", "aviao", "bicicleta", "computador", "janela", "telefone", "livro", "mesa", "cadeira", "relogio")

for i in palavras:
    print(f'\nNa palavra {i.upper()} temos', end=' ')
    for j in i:
        if j in 'aeiou':
            print(f'{j}', end=' ')
