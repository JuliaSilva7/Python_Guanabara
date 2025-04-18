from ex111.utilidadesCeV import moeda

p = float(input('Digite o preço: R$'))
print(moeda.moeda(p))
print(moeda.moeda(moeda.aumentar(p, 8.5)))
print(moeda.moeda(moeda.diminuir(p, 3)))
print(moeda.moeda(moeda.metade(p)))
print(moeda.moeda(moeda.dobro(p)))