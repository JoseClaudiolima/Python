from os import system
system('cls') or None
#O algoritmo de Euclides retorna o MDC (Máximo Divisor Comum) entre números inteiros
a = int(input(f'Entre com um número: '))
b = int(input(f'Entre com um número: '))

if a >b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

menorcopia = menor
while menor !=0:
    menor = maior % menor
    maior = menorcopia
    menorcopia = menor

print(f'O MDC entre {a} e {b} é {maior}!')