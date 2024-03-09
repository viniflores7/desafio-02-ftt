from time import sleep
import webbrowser #Biblioteca para abrir uma imagem no navegador


def main(): #Função principal para rodar o programa
    while True:
        menu(True, opcoes_menuprincipal(), str="GERENCIADOR DE PERSONAGENS")
        op = str(input('\033[1mOpção =--> \033[m')).strip()
        if op == '1':
            new_character()
        elif op == '2':
            see_character()
        elif op == '3':
            linha(33, 52)
            print('''\033[1mEste é um Gerenciador de Personagem onde:\n
1 - Você pode cadastrar seu personagem, editar as informações antes de confirma-lo
2 - Você pode abrir o link da imagem que anexar e ela irá abrir em seu navegador padrão (Todas as orientações estão no cadastro)
\nDono do projeto e programador: Vinícius Flores Ribeiro
Versão: 1.5 BETA''')
            linha(33, 52)
            con = str(input('Aperte "Enter" para voltar para o Menu Principal: '))
            con = 2
            if con == 2:
                backToMenu()
        elif op == '4':
            linha(33, 52)
            print('Muito obrigado por usar o Gerenciador de Personagens')
            sleep(0.8)
            print('Encerrando o programa', end='')
            for c in range(0,3):
                print('.', end='', flush=True)
                sleep(0.5)
            print('\n\033[1;32m[PROGRAMA ENCERRADO COM SUCESSO]\033[m')
            exit()
        else:
            error(op)


def menu(tit = True, op='',  cor=36, str=''): #Menu principal | Tit = True = Vai ter título | op = Opções | Cor padrão = azul | str= Nome do título | 
    if tit:
        print(f'\033[{cor}m-='*25, end='')
        print('-\033[m')
        print(f'\033[1m{f"{str}":^50}\033[m')
        print(f'\033[{cor}m-='*25, end='')
        print('-\033[m')
        print(op)
        print(f'\033[{cor}m-='*25, end='')
        print('-\033[m')
    else:
        print(f'\033[{cor}m-='*25, end='')
        print('-\033[m')
        print(op)
        print(f'\033[{cor}m-='*25, end='')
        print('-\033[m')


def opcoes_menuprincipal(): #Se o n=True vai retornar com negrito
    return'''\033[1m1 - Cadastrar um novo personagem
2 - Vizualizar todos os personagens cadastrados
3 - Sobre
4 - Sair do programa\033[m'''


def opcoes_newcharacter():
    return'''\033[1m1 - Confirmar todos os dados
2 - Editar algum dado
3 - Cancelar\033[m'''


def opcoes_seecharacter():
    return'''\033[1m1 - Ver a imagem de algum personagem
2 - Voltar para o menu principal\033[m'''


def linha(cor, num): #Criar uma linha onde o primeiro parâmetro é o código da cor, e a segunda é a quantidade
    print(f'\033[1;0{cor}m-\033[m'*num)


def error(var):
    print(f'\033[1;31mERRO: "{var}" não é uma opção válida\033[m')
    print('\n\n')


def backToMenu():
    sleep(0.6)
    print('Voltando para o \033[36mMenu Principal\033[m')
    sleep(0.6)
    print('\n\n\n\n\n\n\n')
    main()


def see_image(link_imagem): # Abra o navegador padrão com o URL da imagem
    webbrowser.open(link_imagem, new=2)


def new_character():
    linha(32,55)
    temp = dict()
    temp["Nome"] = str(input('Digite o nome do personagem: ')).strip().capitalize()
    temp["Descrição"] = str(input('\nDigite a descrição do seu personagem: ')).strip().capitalize()
    print('\n\033[1mOBS: Copie e cole o link da imagem, quando ir na opção "Vizualizar todos os personagens cadastrados" caso o link esteja inválido, ele abrirá no seu navegador padrão e irá mostrar uma mensagem de erro.')
    print('Como pegar o link? Clique com o botão direito do mouse em "Copiar o endereço da imagem" e cole na opção abaixo.')
    temp["Link"] = str(input('Digite o link para imagem: \033[m')).strip()
    temp["Programa"] = str(input('\nPrograma: ')).strip().capitalize()
    temp["Animador"] = (input('\nAnimador: ')).strip().capitalize()
    while True: # Entrando no meu de confirmação de dados
        linha(32,55)
        sleep(0.3)
        print('As informações cadastradas foram:')
        for n, i in temp.items():
            print(f'\033[1m{n}\033[m: {i}')
        menu(False, opcoes_newcharacter(), 32)
        op = str(input('\033[1mOpção =--> \033[m')).strip()
        if op == '1': #Confirmar todos os dados
            lis.append(temp.copy()) #Adicionando na lista principal
            temp.clear() #Limpando o dicionário temporário
            sleep(0.2)
            print('\033[1mTodos os dados foram adicionados com \033[1;32mSUCESSO\033[m')
            sleep(0.4)
            backToMenu()
        elif op == '2': #Alteração de informações
            inf = str(input('Qual o nome da informação que você deseja alterar: ')).capitalize().strip()
            if inf != 'Nome' and inf != 'Descrição' and inf != 'Link' and inf != 'Programa' and inf != 'Animador':
                error(inf)
            else:
                temp[f"{inf}"] = str(input(f'{inf}: ')).strip().capitalize()
        elif op == '3': # Cancelar
            backToMenu()
        else:
            error(op)


def see_character(): #Ver os personagens e a imagem cadastrada
        if len(lis) == 0: #Se não tiver nenhum personagem cadastrado
            linha(34, 50)
            print('Você ainda não tem nenhum personagem cadastrado!')
            linha(34, 50)
            backToMenu()
        else:  #Caso já tenha personagens cadastrados
            linha(34, 50)
            print(f'Personagens cadastrados até o momento: \033[34m{len(lis)}\033[m')
            linha(34, 50)
            sleep(0.5)
            print('Segue a lista de personagens:')
            for c, personagem in enumerate(lis):
                print(f'\nNúmero: {c+1}')
                for chave, valor in personagem.items():
                    if chave == 'Link': #Colocando o link menor para a vizualização
                        print(f'{chave}: {valor[0:40]}...')
                    else:
                        print(f'{chave}: {valor}')
            while True:
                linha(34, 50)
                print(opcoes_seecharacter())
                linha(34,50)
                op = str(input('\033[1mOpção =---> \033[m')).strip()
                if op == '1': #Ver a imagem de algum personagem
                    num = str(input('Digite o número do personagem do qual você gostaria de ver o link: ')).strip()[0]
                    try:
                        num_correct = int(num)
                        if 1 <= num_correct <= len(lis):
                            link = lis[num_correct - 1]['Link']
                            see_image(link)
                        else:
                            error(num_correct)
                    except ValueError:
                        error(num)
                    see_character()
                if op == '2': #Voltar para o menu principal
                    backToMenu()
                else:
                    error(op)


#Programa principal
lis = list()
main()
