from os import system
from time import sleep
from random import randint, choice
system('cls') or None

s = p1000 = pbarato = nbarato = 0

print('-'*40)
print(' '*10, 'LOJA SUPER BARATÃO ',)
print('-'*40)

while True:
    n = input(f'Nome do produto: ')
    p = randint(1, 10000)

    continuar = input(f'Deseja continuar? [S/N]\t').strip().upper()

    while continuar != 'S' and continuar != 'N':
        continuar = input(f'Deseja continuar? [S/N]\t').strip().upper()

    if continuar == 'N':
        break

    if s == 0:
        nbarato = n
        pbarato = p

    elif p < pbarato:
        nbarato = n
        pbarato = p

    if p > 1000:
        p1000 += 1
    s += p

print('-' * 10, 'FIM DAS COMPRAS', '-' * 10)
print(
    f'O total da compra foi: {s:.2f}\nTemos {p1000} produtos custando acima de 1000.00\nO produto mais barato foi {nbarato} custando {pbarato:.2f}')
