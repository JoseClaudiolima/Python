from os import system
system('cls') or None

print('=' * 30)
print(' ' * 10, 'Banco JJ')
print('=' * 30)
n = int(input(f'Digite o valor que deseja sacar: '))
nini = n
a = n50 = n20 = n10 = n2 = n1 = 0
while n > 0:
    if n / 50 >= 1:
        a = n // 50
        n -= a*50
        n50 += a

    if n / 20 >= 1:
        a = n // 20
        n -= a*20
        n20 += a

    if n / 10 >= 1:
        a = n // 10
        n -= a*10
        n10 += a

    if n / 2 >= 1:
        a = n // 2
        n -= a*2
        n2 += a

    if n - 1 == 0:
        n = 0
        n1 += a

print(f'''Para sacar {nini}, você receberá:
{n50} nota(s) de 50,00\t({n50*50})
{n20} nota(s) de 20,00\t({n20*20})
{n10} nota(s) de 10,00\t({n10*10})
{n2} nota(s) de 2,00\t({n2*2})
{n1} nota(s) de 1,00\t({n1*1})''')
