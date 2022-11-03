from os import system
from random import randint
system('cls') or None

def notas(*n,sit=False):
    dict= {}
    dict['total'] = len(*n)
    
    for pos,valor in enumerate(*n):
        if pos ==0:
            maior = valor
            menor = valor
        else:
            if maior <= valor:
                maior = valor
            if menor >= valor:
                menor = valor

    dict['maior'] = maior
    dict['menor'] = menor
    dict['media'] = sum(*n)/len(*n)
    if sit ==True:
        if dict['media'] <5:
            dict['situacao'] = 'Ruim'
        else:
            dict['situacao'] = 'Razoavel' 

    print(dict)



array = []
n = int(input(f'Quantas notas deseja adicionar: '))
for i in range(n):
    array.append(randint(1,10))
notas(array,sit=True)