from ex107 import moeda
from os import system
system('cls') or None


p = float(input(f'Digite o preço: '))
opcao = input(f'Deseja formatação? 0 para não, 1 para sim! ')
while opcao not in '01':
    opcao = input(f'Deseja formatação? 0 para não, 1 para sim! ')
opcao = int(opcao)
print(f'A metade de {p} é {moeda.metade(p,opcao)}')
print(f'O dobro de {p} é {moeda.dobro(p,opcao)}')
print(f'Aumentando 10% de {p}, temos {moeda.aumentar(p,10,opcao)}')
print(f'Reduzindo 13% de {p},  temos {moeda.reduzir(p,13,opcao)}')
