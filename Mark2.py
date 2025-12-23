import os

Restaurantes = [{'nome':'La Boca', 'Categoria': 'Pizza', 'Ativo': False},
{'nome':'Sushi do Rei', 'Categoria': 'Japonesa', 'Ativo': True},
{'nome':'Manos Brazzeiros', 'Categoria': 'Hamburguer', 'Ativo': False}]

def exibir_nome_do_programa():
    print('Sushi Boulevard\n')
    # essa função exibe para o usuario o nome do programa criado

def exibir_opções():
    # essa função exibe as opções que o usuario tem para usar o aplicativo
    print('1. cadastrar restaurante')
    print('2. listar restaurante')
    print('3. alterar estado do restaurante')
    print('4. sair\n')

def finalizar_app():
    #essa função tem como objetivo apresentar uma frase que indica o encerramento do aplicativo
    exibir_subtitulo('Finalizando App')

def opção_invalida():
    # essa função tem como sinalizar ao usuario uma opção invalida caso seja inserida, dando retorno ao menu principal
    print('opção invalida!\n')

    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    #essa função tem como objetivo retornar ao menu principal sem encerrar o programa
    input('\ndigite uma tecla para voltar ao menu ')
    main()

def exibir_subtitulo(texto):
    # tem como objetivo apresentar um texto a cada opção escolhida
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    #Essa função e responsavel por cadastrar um novo restaurante
    # inputs : 
    #- nome do restaurante
    #- categoria
    # outputs: 
    #- adiciona um novo restaurante a lista de restaurantes
    

    exibir_subtitulo('cadastro de novos restaurantes\n')
    nome_do_restaurante = input('nome do restaurante que deseja cadastrar: ')
    categoria = input('digite o nome da categoria do restaurante {}: '.format(nome_do_restaurante))
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
    Restaurantes.append(dados_do_restaurante)   
    print('o restaurante {} foi cadastrado com sucesso!'.format(nome_do_restaurante))

    voltar_ao_menu_principal()

def listar_restaurantes():
    #essa função tem como objetivo exibir ao usuario os restaurantes cadastrados, suas categorias e status
    exibir_subtitulo('Listando os Restaurantes\n')


    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in Restaurantes:
        nome_restaurante = restaurante ['nome']
        categoria = restaurante ['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado' 
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def escolher_opção():
    #essa função apresenta as opções escolhidas pelo usuario, e suas funções no programa
    try:
        opção_escolhida = int(input('escolha uma opção: '))
        match opção_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                print('Finalizar App')
                finalizar_app()
            case _:
                opção_invalida()
    except:
        opção_invalida()

def alternar_estado_restaurante():
    #essa função busca alterar o estado do restaurante escolhido
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in Restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

        if not restaurante_encontrado:
            print('o restaurante não foi encontrado')

    voltar_ao_menu_principal()

def main():
    # essa função tem por objetivo mostrar o menu principal, e suas opções
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opção()

if __name__ == '__main__':
    main()