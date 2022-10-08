from os import system
system('cls') or None

s = 0
for i in range(1, 7):
    n = int(input(f'Digite um numero:\t'))
    if n % 2 == 0:
        s += n
print(s)
