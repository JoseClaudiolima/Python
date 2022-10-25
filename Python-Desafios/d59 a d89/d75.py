from os import system
system('cls') or None

num = (int(input(f'Digite um número: ')), int(input(f'Digite um número: ')),
       int(input(f'Digite um número: ')), int(input(f'Digite um número: ')))
print(f'Vc digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'3 apareceu na {num.index(3)+1}° posição')
else:
    print(f'Não tem o valor 3 nos numeros escolhidos.')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:  # n == num[n]
        print(n, end=' ')
