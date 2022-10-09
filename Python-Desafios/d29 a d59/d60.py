from os import system
system('cls') or None

n = int(input(f'Digite um numero: '))

fact = 1
while n != 1:
    fact *= n
    n -= 1
print(fact)
