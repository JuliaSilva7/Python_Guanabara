lista = []

for c in range(5):
    n = int(input('Escreva um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista) and n > lista[posicao]:
                posicao += 1
        lista.insert(posicao, n)

print(lista)
