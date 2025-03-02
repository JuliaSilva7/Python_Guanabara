print('Caixa Eletrônico\n')
while True:

    dinheiro = int(input('Digite o valor do dinheiro que você deseja sacar: '))
    if dinheiro == 0:
        break
    nota_50 = dinheiro // 50
    nota_20 = dinheiro % 50 // 20
    nota_10 = dinheiro % 50 % 20 // 10
    nota_1 = dinheiro % 50 % 20 % 10 // 1

    print(
        f'Os R${dinheiro} foram sacados em notas {nota_50} notas de 50, {nota_20} notas de 20, e {nota_10} de 10 e {nota_1} de 1.')

# total = int(input('digite um valor inteiro: '))
# for i in (50, 20, 10, 1):
#     tced = 0
#     while total >= i:
#         total -= i
#         tced += 1
#     if tced != 0:
#         print(f'Total de cédulas de R$ {i}: {tced}')

# din = int(input('Digite o valor do dinheiro: '))
# total = din
# nota = 50
# cedula = 0
#
# while True:
#     if total >= nota:
#         total -= nota
#         cedula += 1
#     else:
#         if cedula > 0:
#             print(f'Total de notas de cedula de R${nota}: {cedula}')
#         if nota == 50:
#             nota = 20
#         elif nota == 20:
#             nota = 10
#         elif nota == 10:
#             nota = 1
#         cedula = 0
#         if total == 0:
#             break
