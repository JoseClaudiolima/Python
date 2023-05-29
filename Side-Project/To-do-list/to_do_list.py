import os

os.system('cls')


# Métodos
def show_todaylist():
    with open (os.path.join(os.path.dirname(__file__),"today_list.txt"),'r',encoding="utf-8") as arquivo:
        print(arquivo.read()+"\n")

def show_alllist():
    with open (os.path.join(os.path.dirname(__file__),"non_today_list.txt"),'r',encoding="utf-8") as arquivo:
        print(arquivo.read()+"\n")



def main():
    escolha = ''

    while escolha != 'add' and escolha != 'del' and escolha != 'view' and escolha != 'c' and escolha != "add-non":
        print(f'A sua to-do list diária está assim:')
        show_todaylist()
        escolha = input(f"O que deseja fazer?\n[add] adicionar\n[add-non] adicionar em lista não diária\n[view] visualiza a to do list inteira\n[del] deletar\n[c] close\n").lower()


    if escolha == 'add':
        todo = input(f'\nO que deseja acrescentar na lista?\n')
        with open (os.path.join(os.path.dirname(__file__),"today_list.txt"), 'a',encoding="utf-8") as arquivo:
            arquivo.write(f'\n{todo}')

    elif escolha == 'add-non':
        os.system('cls')
        todo = input(f'O que deseja acrescentar na lista não diária?\n')
        with open (os.path.join(os.path.dirname(__file__),"non_today_list.txt"),'a',encoding="utf-8") as arquivo:
            arquivo.write(f'\n{todo}')

    elif escolha == 'view':
        os.system('cls')
        show_alllist()
        main()
       
    elif escolha == 'del':
        os.system('cls')
        quallista = ''

        while quallista != 'today-list' and quallista != 'non-today':
            quallista = input(f'Qual lista você deseja deletar um elemento?\n[today-list]\n[non-today]\n\n')

        if quallista == 'today-list':
            os.system('cls')
            show_todaylist()
            numdel = input('Qual desses deletar? (em numeros)\n')

        if quallista == 'non-today':
            os.system('cls')
            show_alllist()
            numdel = input('Qual desses deletar? (em numeros)\n')


main()