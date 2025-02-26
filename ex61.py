pt = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
cont = 0
print(f'O valor da PA é de {pt} -> ',end='')

while cont < 9:
    pa = pt + (razao * (1 + cont))
    cont += 1
    print(f'{pa} -> ',end='')

print('FIM')
