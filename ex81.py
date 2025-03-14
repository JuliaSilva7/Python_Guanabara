lista = []

while True:
    n = int(input('Escreva um número: '))
    lista.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print(f'A lista tem {len(lista)} elementos')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
