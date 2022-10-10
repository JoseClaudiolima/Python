from os import system
system('cls') or None

d = 'S'
s = 0
maior = 0
contagem = 0
while d != "N":
    n = int(input(f'Entre com um valor: '))
    d = input(f'Deseja continuar? [S/N]\t').upper()

    if n > maior:
        maior = n
    if s == 0:
        menor = n
    elif menor > n:
        menor = n
    s += n
    contagem += 1
print(
    f'A média dos valores digitados é {s/contagem}, o maior valor foi {maior} e o menor foi {menor}.')
