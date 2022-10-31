def destaque(a):
    print('~' * int(len(a))+'~~~~')
    print(a.center(len(a)+4,' '))
    print('~' * int(len(a))+'~~~~')


m1 = input(f'Digite uma mensagem: ')
m2 = input(f'Digite outra mensagem: ')
m3 = input(f'Ultima mensagem: ')
destaque(m1)
destaque(m2)
destaque(m3)