from time import sleep
import os
# 1
'''
fórmula: J = C . i . t
C-> Capital, i -> índice e t -> tempo
Taxa para 2 meses de empréstimo = 6.9% ao mês
Taxa para 6 meses de empréstimo = 7.14% ao mês
Taxa para 12 meses de empréstimo = 9.21% ao mês
Taxa para 24 meses de empréstimo = 12.46% ao mês
'''

c = int(input(f'Digite o valor que deseja pegar emprestado:\t'))
t = int(input(f'Digite a quantidade de meses para pagar:\t'))

i = 0.069
if t < 12:
    i = 0.0714
elif t < 24:
    i = 0.0921
else:
    i = 0.1246

print(f'O valor que irá pagar em {t} meses será: {c+(c*i*t):.2f}')


# 2
sleep(1)
os.system('cls') or None

print(f'''Valores das bebidas:
1- Coca Cola (R$3.75)
2- Mate Leão (R$2.45)
3- Guaraná Antártica  (R$3.55)
4- Citrus Schweppes (R$3.15)
5- Garrafa de Água  (R$1.35)
6- long neck Spaten (R$5.75)
7- long neck Stella (R$5.85)
8- long neck Heineken (R$6.50)
''')


saldo = int(input(f'Digite quanto dinheiro você tem:\t'))
escolha = int(input(f'Digite o código do produto que vc deseja comprar:\t'))
c = 0

if escolha == 1 and saldo >= 3.75:
    c += 1
    produto = "Coca Cola"
    troco = saldo - 3.75

elif escolha == 2 and saldo >= 2.45:
    c += 1
    produto = "Mate Leão"
    troco = saldo - 2.45

elif escolha == 3 and saldo >= 3.55:
    c += 1
    produto = "Guaraná Antártica"
    troco = saldo - 3.55

elif escolha == 4 and saldo >= 3.15:
    c += 1
    produto = "Citrus Schweppes"
    troco = saldo - 3.15

elif escolha == 5 and saldo >= 1.35:
    c += 1
    produto = "Garrafa d'agua"
    troco = saldo - 1.35

elif escolha == 6 and saldo >= 5.75:
    c += 1
    produto = "long neck Spaten"
    troco = saldo - 5.75

elif escolha == 7 and saldo >= 5.85:
    c += 1
    produto = "long neck Stella"
    troco = saldo - 5.85

elif escolha == 8 and saldo >= 6.50:
    c += 1
    produto = "long neck Heineken"
    troco = saldo - 6.50

elif escolha < 1 or escolha > 8:
    print(f'\nVocê inseriu o código do produto errado!\ntente novamente')
else:
    print(f'\nVocê não tem dinheiro suficiente para comprar esse produto!')


if c > 0:
    print(f'\nVocê comprou um(a) {produto} e sobrou {troco:.2f}')
