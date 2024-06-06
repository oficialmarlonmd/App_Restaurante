#Programa simple de cadastro de restaurante

restaurantes = []

def cadastrar_restaurante():
    print('\n')
    print('Cadastrar restaurantes')
    nome_restaurante = input('Nome do restaurante:')
    categoria = input('Categoria: ')
    dados_restaurante = {'nome' : nome_restaurante, 'categoria' : categoria, 'status': False}
    restaurantes.append(dados_restaurante)
    
    main()
    
def listar_restaurantes():
    print('\n')
    print(f'{'Nome'.ljust(10)} | {'Categoria'.ljust(10)} | {'Status'.ljust(10)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['status'] == True else 'Desativado'
        print(f'{nome_restaurante.ljust(15)} | {categoria.ljust(15)} | {ativo.ljust(15)}')

    main()
    
def alternar_status():
    print('\n')
    print('Alternar status')
    nome_restaurante =  input('Diga qual restaurante receberá o status: ')
    
    for restaurante in restaurantes:
        if nome_restaurante ==  restaurante['nome']:
            restaurante['status'] = not restaurante['status']
            
            if restaurante['status'] == False:
                mansagem = f'O restaurante {nome_restaurante} foi altivado com sucesso!'
            else:
                mansagem = f'O restaurante {nome_restaurante} foi desativado com sucesso!'
                
            # mensagem = f'O restaurante {nome_restaurante} foi altivado com sucesso!' if restaurante ['satatus'] == False else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
    main()
    
def finalizar_app():
    print(' Finalizando o APP......')
    
def logo():
    
    print(""" ℂ𝕒𝕕𝕒𝕤𝕥𝕣𝕠 ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖 """)

    
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
            print('ERRO! OPÇÃO INVÁLIDA!!!')
    main()
     
def main():
    logo()
    print_opcao()
    escolher_opcao()
      
main()