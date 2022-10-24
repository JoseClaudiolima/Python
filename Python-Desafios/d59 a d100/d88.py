from os import system
from random import randint
from time import sleep

system('cls') or None

print('-'*30)
print('JOGA NA MEGA SENA'.center(30,' '))
print('-'*30)
jogos = input(f'Quanto jogos você quer que eu sorteie? ')
while jogos.isnumeric() is False:
    jogos = input(f'Quanto jogos você quer que eu sorteie? ')
jogos = int(jogos)
print(f'-='*3,'SORTEANDO 10 JOGOS'.center(4+len('SORTEANDO 10 JOGOS')),'-='*3)
for i in range (jogos):
    array = [randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)]
    print(f'Jogo {[i+1]}: {array}')
    sleep(0.5)
print(f'-='*5,' < BOA SORTE! > ','-='*5)