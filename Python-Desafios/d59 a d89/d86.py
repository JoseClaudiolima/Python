from os import system
from random import randint
system('cls') or None

array = [[], [], []]

for i in range(3):
    for k in range(3):
        #array[i].append(randint(1, 100))
        array[i].append(int(input(f'Digite um valor para [{i},{k}]: ')))
print('-='*30)
for j in range (3):
    for i in range (3):
        print(f'[{array[j][i]:^5}]',end='')
    print()