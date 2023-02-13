import os
from time import sleep
from datetime import datetime

os.system('cls') or None


filename = 'Gratidao.txt'
filepath = os.path.join(os.path.dirname(__file__), filename)

escolha = ''
while escolha != 'add' and escolha != 'read':
    print(f"Boas vindas, este codigo é para fazer um arquivo estilo de 'pote da gratidão'")
    print(f'Você deseja a adicionar alguma gratidão [add] ou ler as gratidões colocadas? [read]')
    escolha = input(f'').lower()

    
    sleep(1)
    os.system('cls') or None


if escolha == 'add':
    gratidao_dia = input(f'Qual é a gratidão do dia?\n\t')

    with open (filepath, 'a',encoding="utf-8") as arquivo:
        arquivo.write(f"\n\n{gratidao_dia}")
        arquivo.write(f"\nData: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")


elif escolha == 'read':
    with open(filepath,'r',encoding="utf-8") as arquivo:
        notepad = arquivo.read()
        print(notepad)