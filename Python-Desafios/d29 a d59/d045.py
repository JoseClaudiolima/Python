from random import choice
import os
from time import sleep
os.system('cls') or None

r = 0
v = 0
jokenpo = ["Tesoura", "Papel", "Pedra"]

while v != 1:
    r += 1
    op1 = input(f'''0 - Tesoura
    1 - Papel
    2 - Pedra
    Faça sua escolha de Jokenpo:\t''')
    op1 = jokenpo[int(op1)]
    op2 = choice(jokenpo)

    if (op1 == "Tesoura" and op2 == "Papel") or (op1 == "Papel" and op2 == "Pedra") or (op1 == "Pedra" and op2 == "Tesoura"):
        print(f'''Você escolheu {op1} e a máquina {op2}.
Você venceu na rodada {r}!''')
        v = 1

    elif (op2 == "Tesoura" and op1 == "Papel") or (op2 == "Tesoura" and op1 == "Papel") or (op2 == "Tesoura" and op1 == "Papel"):
        print(f'''Você escolheu {op1} e a máquina {op2}.
Você perdeu na rodada {r}!''')
        v = 1
    else:
        print(
            f'\nVocê escolheu "{op1}" e a máquina também escolheu "{op2}", nada acontece!\nVamos para a próximo rodada!')
    sleep(5)
    os.system('cls') or None
