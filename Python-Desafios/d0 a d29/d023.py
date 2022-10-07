n1 = input(f'Digite um valor inteiro dentro de 0 a 9999: ')
print(f'Unidade: {n1[len(n1)-1]}')
if len(n1) > 1:
    print(f'Dezena: {n1[len(n1)-2]}')

if len(n1) > 2:
    print(f'Centena: {n1[len(n1)-3]}')

if len(n1) > 3:
    print(f'Milhar: {n1[len(n1)-4]}')
