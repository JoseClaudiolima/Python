from os import system
system('cls') or None

s = 0
for i in range(1, 501):
    if i % 2 == 1:
        if i % 3 == 0:
            s += i
print(f'A soma dos numeros impares multiplos de 3, entre 1 e 500 é: {s}')
