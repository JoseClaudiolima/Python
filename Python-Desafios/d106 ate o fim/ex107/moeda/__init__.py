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


    