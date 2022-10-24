from os import system
system('cls') or None

array = [[input(f'Nome do aluno : '),[int(input(f'Nota 1: ')),int(input(f'Nota 2: '))]]]
#[input(f'Nome do aluno : '),[int(input(f'Digite a nota 1 do aluno: '))],[int(input(f'Digite a nota 2 do aluno: '))]]
n= c = 0
r='s'
while True:
    r = input(f'Deseja continuar? [S/N] ').lower()
    if r in 'Ss':
        system('cls') or None
        c +=1 
        array.append(list('a'))
        array[c][0] = input(f'Nome do aluno : ')
        array[c].append(list('a'))
        array[c][1][0] = int(input(f'Nota 1: '))
        array[c][1].append(int(input(f'Nota 2: ')))
    if r in 'Nn':
        break
print('-='*30)
print(f'RA.     NOME       MÉDIA')
print('-'*30)
for k in range (len(array)):
    media = str((array[k][1][0]+array[k][1][1])/2)
    print(k,' '*6,array[k][0],media.rjust(12, ' '))
print('-='*30)
while True:
    n = int(input(f'Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    if n > len(array)-1:
        print(f'Conforme a lista acima!')
        print('-'*30)
        continue
    print(f'Notas de {array[n][0]} são {array[n][1]}')
    print('-'*30)