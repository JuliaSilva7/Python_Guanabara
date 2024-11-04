a = float(input('Escreava o 1º lado do triângulo: '))
b = float(input('Escreva o 2º lado do triângulo: '))
c = float(input('Escreva o 3º lado do triângulo: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Esse triângulo é equilátero.')
    elif a == b or a == c or b == c:
        print('Esse triângulo é isósceles')
    else:
        print('Esse triângulo é escaleno')
else:
    print('Esses lados não conseguem formar um triângulo.')
