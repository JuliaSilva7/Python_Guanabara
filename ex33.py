n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva um número: '))
n3 = int(input('Escreva um número: '))

menor = n1
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3

print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')
