peso = float(input('Qual seu peso: '))
altura = float(input('Qual sua altura: '))
imc = peso/(pow(altura,2))

if imc < 18.5:
    print(f'Seu Imc é de {imc:.2f}. Você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print(f'Seu Imc é de {imc:.2f}. Você está no peso ideal.')
elif 25 < imc <=30:
    print(f'Seu Imc é de {imc:.2f}. Você está com sobrepeso.')
elif 30 <imc <= 40:
    print(f'Seu Imc é de {imc:.2f}. Você está obeso.')
else:
    print(f'Seu Imc é de {imc:.2f}. Você está com obesidade mórbida.')