from ex107 import moeda
from os import system
system('cls') or None


p = float(input(f'Digite o preço: '))
moeda.resumo(p,80,35)
