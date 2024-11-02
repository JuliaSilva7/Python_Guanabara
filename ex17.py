import math
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do acateto adjacente? '))
h = math.hypot(co,ca)
print(f'A hipotenusa vai ser {h:.2f}')