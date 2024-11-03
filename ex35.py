a = float(input('Escreva o comprimento da 1ª reta: '))
b = float(input('Escreva o comprimento da 2ª reta: '))
c = float(input('Escreva o comprimento da 3ª reta: '))

if a + b > c and b + c > a and a + c > b:
    print('Essas medidas podem formar um triângulo')
else:
    print('Essas medidas não podem formar um triângulo')
