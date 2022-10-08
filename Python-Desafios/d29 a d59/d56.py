from os import system
from random import randint, choice
system('cls') or None

sexo = ['Masculino', 'Feminino']
midade = 0
sidade = 0
maioridade = 0
a = 0
for i in range(1, 5):
    nome = input(f'Nome da pessoa: ')
    idade = randint(18, 60)
    sexoi = choice(sexo)
    sidade += idade
    if idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexoi == 'Feminino' and idade < 20:
        a += 1
    print(idade)
    print(sexoi)
midade = sidade/5


print(
    f'A média da idade é {midade}, o nome da pessoa mais velha é {nomevelho} e dapa-dale em {a}')
