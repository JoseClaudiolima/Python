from ex107 import moeda
from os import system
system('cls') or None


p = float(input(f'Digite o preço: '))
print(f'A metade de {p} é {moeda.metade(p,1)}')
print(f'O dobro de {p} é {moeda.dobro(p,1)}')
print(f'Aumentando 10% de {p}, temos {moeda.aumentar(p,10,1)}')
print(f'Reduzindo 13% de {p},  temos {moeda.reduzir(p,13,1)}')
