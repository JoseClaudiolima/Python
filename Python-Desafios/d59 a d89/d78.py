from os import system
system('cls') or None

array = [int(input(f'Digite um valor: ')), int(input(f'Digite um valor: ')), int(
    input(f'Digite um valor: ')), int(input(f'Digite um valor: ')), int(input(f'Digite um valor: '))]

for c, v in enumerate(array):
    if c == 0:
        maior = v
        pmaior = '0'
        menor = v
        pmenor = '0'
    else:
        if v > maior:
            maior = v
            pmaior = str(c)
        elif v == maior:
            pmaior += '... ' + str(c)
        if v < menor:
            menor = v
            pmenor = str(c)
        elif v == menor:
            pmenor += '... ' + str(c)

print(
    f'O maior valor foi {maior}, e estava na(s) posição {pmaior}.\nO menor valor foi {menor}, e estava na(s) posição {pmenor}.')
