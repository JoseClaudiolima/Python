def metade(n,sit=0):
    if sit ==0:
        return n/2
    elif sit ==1:
        r = f'{(n/2):.2f}'
        return r.replace('.',',')



def dobro(n,sit=0):
    if sit ==0:
        return n*2
    elif sit ==1:
        r = f'{(n*2):.2f}'
        return r.replace('.',',')    



def aumentar(p,n,sit=0):
    n *= 0.01
    if sit ==0:
        return (n * p) + p
    elif sit ==1:
        r = f'{((n * p) + p):.2f}'
        return r.replace('.',',')



def reduzir(p,n,sit=0):
    n *=  0.01
    if sit ==0:
        return p - (n * p) 
    elif sit ==1:
        r = f'{(p - (n * p) ):.2f}'
        return r.replace('.',',')


def resumo(p,a,r):

    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    print(f'Preço analisado:{"R$":>12}{pformat(p)}')
    print(f'Metade do preço:{"R$":>12}{metade(p,1)}')
    print(f'Dobro do preço: {"R$":>12}{dobro(p,1)}')
    print(f'10% de aumento: {"R$":>12}{aumentar(p,a,1)}')
    print(f'35% de redução: {"R$":>12}{reduzir(p,r,1)}')


def pformat(p):
    p = f'{p:.2f}'
    p = p.replace('.',',')
    return p