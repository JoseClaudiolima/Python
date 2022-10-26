from os import system
from random import randint
system('cls') or None

dic = {'jogador1' : randint(1,20),'jogador2': randint(1,20),'jogador3':randint(1,20),'jogador4':randint(1,20)}

diccopy = {}
c=0
for chave, valor in dic.items():
    if c==0:
        lugar = [chave,valor]
        c+=1
    else:
        if valor <= lugar[-1]:
            lugar.append(chave)
            lugar.append(valor)
        elif valor >= lugar[1]:
            lugar.insert(0,valor)
            lugar.insert(0,chave)
        else:
            lugar.insert(2,valor)
            lugar.insert(2,chave)
dic.clear()

for i in range (4):
    dic[str(lugar[0])] = lugar[1]
    key = lugar[0]
    del lugar[0]
    del lugar[0]
    print(f'{i+1}° Lugar:',key,'com',dic[str(key)])
