def area(largura,comprimento):
    res = largura * comprimento
    print(f'A área de um terreno {largura} * {comprimento} =  {res:.2f}m²')


print('Controle de terrenos')
print('-'*40)
a = float(input('Insira a largura do terreno (m): '))
b = float(input('Insira o comprimento do terreno (m): '))
area(a,b)
