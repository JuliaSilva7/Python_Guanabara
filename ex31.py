km = float(input('Quantos km você percorreu na viagem: '))
if km <= 200:
    preco = km * 0.5
    print(f'O gasto da viagem foi RS{preco:.2f}')
else:
    preco = km * 0.45
    print(f'O gasto da viagem foi RS{preco:.2f}')
