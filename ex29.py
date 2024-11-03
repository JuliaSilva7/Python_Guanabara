vel = float(input('Velocidade do carro: '))
if vel > 80:
    print('Você ultarpassou a velocidade permitida.')
    multa = (vel.__trunc__() - 80) * 7
    print(f'Sua multa é de R${multa}')
else:
    print('Seu carro está em uma velocidade normal.')
