n1 = int(input(f'Digite um número: '))
n2 = int(input(f'Digite um número: '))
n3 = int(input(f'Digite um número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'\nO menor valor é {menor}!')

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor é {maior}!')
