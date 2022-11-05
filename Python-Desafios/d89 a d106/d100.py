from os import system
from random import randint
from time import sleep
system('cls') or None

def sortear():
    array = []
    print(f'Foram sorteados os valores',end=' ')
    for i in range (5):
        array.append(randint(1,10))
        print(array[-1],end=' ',flush=True)
        sleep(0.3)
    print()
    return array


def somapar(a):
    soma =0
    for pos, valor in enumerate(a):
        if valor %2==0:
           soma +=valor 
    print(f'Somando os valores pares, temos {soma}.')


lista = sortear()
somapar(lista)


