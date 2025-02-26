sexo = input("Digite a letra inicial do seu sexo: ").upper()

while sexo not in 'FM':
    sexo = input("Digite seu sexo novamente: ").upper()

print(f'Seu sexo é {sexo}')