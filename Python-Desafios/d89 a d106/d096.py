def area(a,b):
    return f' A área de um terreno {a} e {b} é de {a*b}m².'

print(' Controle de Terrenos')
print('-'*20)
larg = float(input(f'LARGURA (m): '))
comp = float(input(f'COMPRIMENTO (m): '))
print(area(larg,comp))