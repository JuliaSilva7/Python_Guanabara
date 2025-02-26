contador = somador = media = menor = maior = 0
continuar = True

while continuar:
    n = int(input("Escreva um número: "))
    somador += n
    contador += 1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

    continuar = input(f'Deseja continuar? [S/N]').strip().upper()[0]
    if continuar in 'nN':
        continuar = False

media = somador / contador
print(f'A média dos números é {media:.2f}. O maior {maior} e o menor {menor}. Foram digitados {contador} números.')
