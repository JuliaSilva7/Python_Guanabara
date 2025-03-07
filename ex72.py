n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Escreva um número entre 0 e 20: '))
    if  20 >= numero >= 0 :
        break

print(f'O número {numero} por extenso é {n[numero]}')
