from ex107 import moeda

valor = float(input('Digite um valor: '))
aum = float(input('Digite um percentual de aumento: '))
dim = float(input('Digite um percentual de diminuição: '))
aumento = moeda.aumentar(valor, aum)
diminuicao = moeda.diminuir(valor, dim)
dobro = moeda.dobro(valor)
metade = moeda.metade(valor)

print(f'A moeda tem valor de RS{valor}')
print(f'Ela teve um aumento de {aum}% para R${aumento:.2f}')
print(f'Ela teve diminuição de {dim}% para R${diminuicao}')
print(f'Seu dobro é R${dobro:.2f}')
print(f'A metade é R${metade:.2f}')
