import math
graus = float(input('Digite o ângulo que você deseja: '))
ang = math.radians(graus)
print(f'O seno de {graus} é {math.sin(ang):.2f}; o cosseno é {math.cos(ang):.2f};a tangente é {math.tan(ang):.2f}')