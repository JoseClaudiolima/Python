from ex111 import moeda,dados
from os import system
system('cls') or None


p = dados.leiaDinheiro("Digite o preço: R$")
moeda.resumo(p,80,35)
