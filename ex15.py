tempo = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km ele percorreu? '))
pagamento = (tempo*60)+(km*0.15)
print(f'O valor a ser pago é de R${pagamento:.2f}')