frase = input('Digite uma frase: ').strip().replace(' ', '').lower().split()
lista = ''.join(frase)
palindromo = lista[::-1]
print(lista)
print(palindromo)

"""palindromo = []

for i in range(1, len(frase) + 1):
    letra = frase[len(frase) - i]
    palindromo+=letra

gols = list(frase)"""

if palindromo==lista:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')
