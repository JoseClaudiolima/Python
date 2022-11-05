from os import system
from random import randint
system('cls') or None

def notas(*n,sit=False):
    '''
    -> Função para analisar as notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    dict= {}
    dict['total'] = len(*n)
    dict['maior'] = max(*n)
    dict['menor'] = min(*n)
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