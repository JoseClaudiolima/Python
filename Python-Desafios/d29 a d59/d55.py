from os import system
from random import randint
system('cls') or None


maior = 0
for i in range(1, 6):
    n = randint(50, 120)

    if i == 1:
        menor = n
    if n < menor:
        menor = n

    if n > maior:
        maior = n
    print("Peso:", n, )
print(
    f'A pessoa mais leve pesa {menor}kg e a pessoa mais pesada pesa {maior}kg!')
