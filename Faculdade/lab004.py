import os

# 2
num = int(input(f'Digite um valor:\t'))
nini = num

if num < 0:
    print("Não existe fatorial de numero negativo")

elif num == 0 or num == 1:
    fact = 1

else:
    fact = 1
    while (num > 1):
        fact *= num
        num -= 1

print(f'O fatorial de {nini} é {fact}')

# 3

# 4
