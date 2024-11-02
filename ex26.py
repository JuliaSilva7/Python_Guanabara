f = input('Escreva uma frase: ').lower().strip()
print(f'A letra A aparece {f.count('a')} vezes na frase.')
print(f'A primeira letra A aparece na posição {f.find('a') + 1} ')
print(f'A última letra A aparece na posição {f.rfind('a') + 1}')
