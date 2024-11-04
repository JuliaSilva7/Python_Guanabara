maior = 0
menor = 0

for i in range(5):
    peso = float(input('Escerav o seu peso: '))
    if i == 0:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Maior peso: {maior:.2f}')
print(f'Menor peso: {menor:.2f}')
