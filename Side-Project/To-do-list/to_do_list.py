import os

# Métodos
def show_todaylist():
    with open (os.path.join(os.path.dirname(__file__),"today_list.txt"),'r',encoding="utf-8") as arquivo:
        print(arquivo.read()+"\n")

def show_alllist():
    with open (os.path.join(os.path.dirname(__file__),"non_today_list.txt"),'r',encoding="utf-8") as arquivo:
        print(arquivo.read()+"\n")


def del_line(filepath,n_line):
    with open (filepath,'r',encoding="utf-8") as arquivo:
        text = arquivo.readlines()

    if n_line < 1 or n_line > len(text) + 1 :
        print("Número de linha inválido!") 
    else:
        del text[n_line - 1]
        with open (filepath,'w',encoding="utf-8") as arquivo:
            arquivo.writelines(text)
    print("Linha removida com sucesso")


def edit_line(filepath,conteudo,n_line):
    with open(filepath, 'r', encoding="utf-8") as arquivo:
        text = arquivo.readlines()

    if n_line < 1 or n_line > len(text) + 1:
        print("Número de linha inválido!")
    else:
        text[n_line - 1] = conteudo
        with open (filepath,'w',encoding="utf-8") as arquivo:
            arquivo.writelines(text)
        print("Linha editada com sucesso!")


def main():
    os.system('cls')
    escolha = ''

    while escolha != 'add' and escolha != 'del' and escolha != 'view' and escolha != 'edit' and escolha != 'c' and escolha != "add-non":
        print(f'A sua to-do list diária está assim:')
        show_todaylist()
        escolha = input(f"O que deseja fazer?\n[add] adicionar\n[add-non] adicionar em lista não diária\n[edit] Edita uma linha\n\n[view] visualiza a to do list inteira\n[del] deletar\n[c] close\n").lower()


    if escolha == 'add':
        os.system('cls')
        show_todaylist()
        todo = input(f'\nO que deseja acrescentar na lista?\n')
        with open (os.path.join(os.path.dirname(__file__),"today_list.txt"), 'a',encoding="utf-8") as arquivo:
            arquivo.write(f'\n{todo}')
        main()

    elif escolha == 'add-non':
        os.system('cls')
        show_alllist()
        todo = input(f'O que deseja acrescentar na lista não diária?\n')
        with open (os.path.join(os.path.dirname(__file__),"non_today_list.txt"),'a',encoding="utf-8") as arquivo:
            arquivo.write(f'\n{todo}')
        main()

    elif escolha == 'edit':
        os.system('cls')
        quallista = ''

        while quallista != 'today-list' and quallista != 'non-today':
            quallista = input(f'Qual lista você deseja deletar um elemento?\n[today-list]\n[non-today]\n\n')
        
        if quallista == 'today-list':
            os.system('cls')
            show_todaylist()
            n_line = int(input(f'Digite a linha em que deseje fazer a mudança:\n'))
            conteudo = input(f'Digite o conteúdo que irá colocar na linha escolhida:\n')+ "\n"
            edit_line(os.path.join(os.path.dirname(__file__),"today_list.txt"),conteudo,n_line)
            main()
        elif quallista == 'non-today':
            os.system('cls')            
            show_alllist()
            n_line = int(input(f'Digite a linha em que deseje fazer a mudança:\n'))
            conteudo = input(f'Digite o conteúdo que irá colocar na linha escolhida:\n') + "\n"
            edit_line(os.path.join(os.path.dirname(__file__),"non_today_list.txt"),conteudo,n_line)
            main()

    elif escolha == 'view':
        os.system('cls')
        show_alllist()
        show_todaylist()
        input(f'\n\nWaiting... ... ... ..')
        main()
       
    elif escolha == 'del':
        os.system('cls')
        quallista = ''

        while quallista != 'today-list' and quallista != 'non-today':
            quallista = input(f'Qual lista você deseja deletar um elemento?\n[today-list]\n[non-today]\n\n')

        if quallista == 'today-list':
            os.system('cls')
            show_todaylist()
            del_line(os.path.join(os.path.dirname(__file__),"today_list.txt"),int(input('Qual desses deletar? (em numeros)\n')))
            main()

        elif quallista == 'non-today':
            os.system('cls')
            show_alllist()
            del_line(os.path.join(os.path.dirname(__file__),"non_today_list.txt"),int(input('Qual desses deletar? (em numeros)\n')))
            main()

os.system('cls')
main()
