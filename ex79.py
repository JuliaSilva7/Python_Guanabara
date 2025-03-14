lista = []

while True:
    n = int(input('Digite um número: '))
    if n in lista:
        print('Esse número já foi adicionado')
    else:
        lista.append(n)
    continuar = ' '
    while continuar not in 'NnSs':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

lista_ordenada = sorted(lista)
print(lista_ordenada)
