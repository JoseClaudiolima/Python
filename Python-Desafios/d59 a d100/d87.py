from os import system
from random import randint
system('cls') or None

array = [[], [], []]
somapar = soma3 = maior2l = 0
for i in range(3):
    for k in range(3):
        #array[i].append(randint(1, 100))
        entrada = int(input(f'Digite um valor para [{i},{k}]: '))
        array[i].append(entrada)
        if entrada % 2 == 0:
            somapar += entrada
        if k == 2:
            soma3 += entrada
        if i == 1 and entrada > maior2l:
            maior2l = entrada
print('-='*30)
print(array[0])
print(array[1])
print(array[2])
print('-='*30)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior2l}')
