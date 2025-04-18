from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(moeda.moeda(p))
print(moeda.aumentar(p, 8.5, True))
print(moeda.diminuir(p, 3, True))
print(moeda.metade(p,True))
print(moeda.dobro(p, True))
