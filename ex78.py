lista = []
for n in range(5):
    numero = int(input(f'Digite um valor para a posição {n}: '))
    lista.append(numero)

print(f'Você digitou os valores: {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} nas posições:', end=' ')
for pos, num in enumerate(lista):
    if num == maior:
        print(f'{pos}', end='...')

print(f'\nO menor valor digitado foi {menor} nas posições:', end=' ')
for pos, num in enumerate(lista):
    if num == menor:
        print(f'{pos}', end='...')
