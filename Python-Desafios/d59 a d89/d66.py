from os import system
system('cls') or None

t = s = 0
while True:
    n = int(input(f'Digite um valor (999 para parar): '))
    if n == 999:
        break
    t += 1
    s += n

print(f'A soma dos {t} valores é {s}')
