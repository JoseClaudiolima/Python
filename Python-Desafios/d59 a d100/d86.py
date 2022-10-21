from os import system
from random import randint
system('cls') or None

array = [[], [], []]

for i in range(3):
    for k in range(3):
        #array[i].append(randint(1, 100))
        array[i].append(int(input(f'Digite um valor para [{i},{k}]: ')))
print('-='*30)
print(array[0])
print(array[1])
print(array[2])
