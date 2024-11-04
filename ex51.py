primeiro_termo = int(input('Digite o primeiro termo da pa: '))
razao = int(input('Digite a razão da pa: '))

for i in range (1,11):
    pa = primeiro_termo + (i-1) * razao
    print(pa,end=' -> ')

print('Fim')