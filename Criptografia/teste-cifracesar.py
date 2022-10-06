import os
os.system('cls') or None

abcdario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', ' ', ' ', ' ', ' ']
# A ocupa 0, Z ocupa 25

msg = input(f'Entre com sua mensagem: ').upper()

Cmsg = []
for i in range(len(msg)):
    Cmsg.append(abcdario[abcdario.index(msg[i])+3])

#print(abcdario.index(msg[0])+3, abcdario[abcdario.index(msg[0])+3])


os.system('cls') or None
empty = ''
print(f' A mensagem criptografada é: {empty.join(Cmsg)}')


Dmsg = []
for i in range(len(empty.join(Cmsg))):
    if abcdario[abcdario.index(empty.join(Cmsg[i]))] == ' ':
        Dmsg.append(' ')
    else:
        Dmsg.append(abcdario[abcdario.index(empty.join(Cmsg[i]))-3])
print(f' A mensagem descriptografada é: {empty.join(Dmsg)}')

# Falta colocar: caso seja numero, colocar uma identificação de numero e somar +3.
# Problemas: Só pode usar caracteres normais, se for usar caracteres como !@$%¨¨*%¨#% não tem como usar como usar cifra de cesar, nem se o caracter tiver acento como áôãè
