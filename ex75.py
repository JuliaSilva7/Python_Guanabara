tupla = lista_par = ()
nove = tres = 0

for i in range(4):
    n = int(input('Escreva um número: '))
    tupla += n,
    if tupla[i] == 9:
        nove += 1
    if n % 2 == 0:
        lista_par+=n,

print(tupla)
if tupla.count(3) == 0:
    print('O valor 3 não aparece na tupla')
else:
    print(f'O valor 3 aparece na posição {tupla.index(3)+1}')
print(f'A quantidade de vezes que aparece o valor nove é de {nove}')
if lista_par==():
    print('Essa lista não tem números pares')
else:
    print(f'Os números pares são {lista_par}')