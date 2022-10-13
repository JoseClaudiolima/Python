from os import system
from random import randint
system('cls') or None

array = [[],
         [],
         []]


for i in range(0, 3):  # vendedores
    for j in range(0, 5):  # dias da semana
        array[i].append(randint(1, 3))

print('Esse é o faturamento da Semana1 da loja:')
print('           Seg  Ter  Quar  Qui  Sex')
print('Sandra:  ', array[0])
print('Vera:    ', array[1])
print('Patrícia:', array[2])


somas = somav = somap = 0

for j in range(0, 5):  # soma da fatura dos vendedores
    somas += array[0][j]
    somav += array[1][j]
    somap += array[2][j]
print(f'\nFaturamento da Sandra na semana foi: {somas}')
print(f'Faturamento da Vera na semana foi: {somav}')
print(f'Faturamento da Patrícia na semana foi: {somap}')
