from os import system
from random import randint
from time import sleep

system('cls') or None

print('-'*30)
print('JOGA NA MEGA SENA'.center(30,' '))
print('-'*30)
array = []
jogos = input(f'Quanto jogos você quer que eu sorteie? ')
while jogos.isnumeric() is False:
    jogos = input(f'Quanto jogos você quer que eu sorteie? ')
jogos = int(jogos)
print(f'-=-=-= SORTEANDO {jogos} JOGOS'.center(4+len('SORTEANDO 10 JOGOS')),'-='*3)
for i in range (jogos):
    array = []
    for k in range(6):
        random = randint(1,60)
        while random in array:
            random = randint(1,60)
        array.append(random)
    print(f'Jogo {[i+1]}: {array}')
    sleep(0.5)
print(f'-='*5,' < BOA SORTE! > ','-='*5)