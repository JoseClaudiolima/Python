from array import array
from os import system
system('cls') or None

array = []
ab = 0
fe = 0
while True:
    entrada = input(f'Digite a expressão: ')
    array.append(entrada)
    for i in range(len(array[0])):
        if array[0][i] == '(':
            ab += 1
        elif array[0][i] == ')':
            fe += 1
    break
if ab == fe:
    print(f'Sua expressão está correta!')
else:
    print(f'Sua expressão está errada!')
