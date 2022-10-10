from os import system
system('cls') or None

n = 0
s = 0
t = 0
while n != 999:
    n = int(input(f'Digite 1 valor: '))
    if n == 999:
        continue
    s += n
    t += 1
print(f'{t} numeros foram digitados, {s} é a soma entre eles.')
