#Programa simples de cadastro de restaurante

import os

restaurantes = []

def cadastrar_restaurante():
    print('\n')
    print('Cadastrar restaurantes') 
    nome_restaurante = input('Nome do restaurante:').title()
    categoria = input('Categoria: ')
    dados_restaurante = {'nome' : nome_restaurante, 'categoria' : categoria, 'status': False}
    restaurantes.append(dados_restaurante)
    for restaurante in restaurantes:
        if dados_restaurante['nome'] in restaurantes:
             print('Erro!Dados cadastrados já exitem!!!')
        else:
            print('Cadastrado com sucesso!!!')
            
    voltar_ao_menu()
    
def listar_restaurantes():
    print('\n')
    print(f'{'Nome'.ljust(15)} | {'Categoria'.ljust(15)} | {'Status'.ljust(15)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['status'] == True else 'Desativado'
        print(f'{nome_restaurante.ljust(15)} | {categoria.ljust(15)} | {ativo.ljust(15)}')

    main()
    
def alternar_status():
    print('\n')
    print('Alternar status')
    nome_restaurante =  input('Diga qual restaurante receberá o status: ').title()
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante ==  restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            
            if restaurante['status'] == False:
                mansagem = f'O restaurante {nome_restaurante} foi altivado com sucesso!'
            else:
                mansagem = f'O restaurante {nome_restaurante} foi desativado com sucesso!'
                                
            # mensagem = f'O restaurante {nome_restaurante} foi altivado com sucesso!' if restaurante ['satatus'] == False else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            
    if restaurante_encontrado == False:
        print('Restaurante encontrado!')
        
    main()
    
def finalizar_app():
 print('''\n Finalizando o APP......................
 Obrigado pela prefênciaa!!!\n''')
    
def logo():
    
    print("""\n ℂ𝕒𝕕𝕒𝕤𝕥𝕣𝕠 ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖 """)

    
def print_opcao():
    
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar status do Restaurante')
    print('4. Finalizar o Programa')

    
def escolher_opcao():
    
    opçao_escolha = int(input('Escolha umas das opcões numéricas acima: '))

    match opçao_escolha:
        case 1:
            cadastrar_restaurante()
        case 2:
            listar_restaurantes()
        case 3 :
            alternar_status()
        case 4 :
            finalizar_app()
        case _:
            opcao_invalida()


def opcao_invalida():
    print('ERRO! OPÇÃO INVÁLIDA!!!')
    main()

def voltar_ao_menu():     
    input('\n Precione o "ENTER" no teclado para voltar ao menu inicial.')
    main()
    
def main():
    os.system('cls')
    logo()
    print_opcao()
    escolher_opcao()
      
main()
