primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro_termo
contador = 1
total_termos = 10

while total_termos !=0:
    contador = 1
    while contador <= total_termos:
        print(f'{termo}', end=' -> ')
        termo+=razao
        contador+=1
    total_termos = int(input('Quantos termos mais você deseja que sejam calculados (digite 0 para parar): '))

print('Programa finalizado com sucesso')
