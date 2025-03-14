lista = []
par = []
impar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print(f'A lista de números é {lista}')
print(f'A lista de números pares é {par}')
print(f'A lista de números ímpares é {impar}')
