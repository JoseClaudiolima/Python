from os import system
system('cls') or None

# palindromo
# anotaram a data da maratona

n = input(f'Digite um palindromo: ').replace(' ', '')

inverso = []
r = ''
for i in range(len(n)):
    inverso.append(n[len(n)-i-1])

r = r.join(inverso)

if n == r:
    print(f'É um palindromo')
    print('', n, '\n', r)
else:
    print(f'Não é um palindromo')
    print(n, '\n', r)
