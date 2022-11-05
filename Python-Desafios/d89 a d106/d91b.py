from random import randint
from time import sleep
from operator import itemgetter
from os import system
system('cls') or None

jogos = {'jogador1': randint(1,20),'jogador2': randint(1,20),'jogador3': randint(1,20),'jogador4': randint(1,20),}
ranking = list()
print('Valores sorteados: ')
for k, v in jogos.items():
    print(f'{k} tirou {v} no dado.')
    sleep(.5)
ranking = sorted(jogos.items(),key=itemgetter(1),reverse=True)
print(f'-='* 30)
print(f'  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(.5)


#pesquisar como funciona o sorted(),especificamente o seus parametros, como key= itemgetter().