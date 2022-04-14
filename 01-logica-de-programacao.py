import json
import os.path
import sys
from os import system, name 


def limpar_terminal(): 
      
    if name == 'nt': 
        _ = system('cls') 
    
    else: 
        _ = system('clear') 


def seleciona_categoria(todas_categorias):

    limpar_terminal()
    print('9. Selecionar categoria\n')    

    if todas_categorias == []:
        print('ATENÇÃO!!!\nÉ necessário listar todas categorias. Volte ao menu principal e digite a opção 1')
        input(' \nPressione qualquer tecla para continuar >> ')
        return

    for ponteiro in range(len(todas_categorias)):
        #print(f'{ponteiro+1}. {todas_categorias[ponteiro]}')
        print(f'-> {todas_categorias[ponteiro]}')
        
    while True:
        selecionar_categoria = input('\nDigite o nome da categoria desejada: ')
        if selecionar_categoria in todas_categorias:
            print(f'\nVocê selecionou a categoria {selecionar_categoria}')
            input(' \nPressione qualquer tecla para continuar >> ')
            return selecionar_categoria
        
        else:
            print('Categoria não existe! Digite uma categoria relacionada na lista acima')


def obter_dados():
    
    # Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    # NÃO MODIFIQUE essa função.
    
    with open(os.path.join(sys.path[0], '01-dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


def listar_categorias(dados):
    
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    # Cuidado para não retornar categorias repetidas.    
    
    limpar_terminal()
    print('1. Listar categorias\n')

    lista_de_categorias = []

    for ponteiro in range(len(dados)):
        testador = dados[ponteiro]['categoria']
        if testador not in lista_de_categorias:
            lista_de_categorias.append(testador)
    
    lista_de_categorias.sort()

    for ponteiro in range(len(lista_de_categorias)):
        print(f'{ponteiro+1}. {lista_de_categorias[ponteiro]}')

    print(f'\nForam encontradas {len(dados)} produtos em {len(lista_de_categorias)} categorias')
    #print(lista_de_categorias)
    input(' \nPressione qualquer tecla para continuar >> ')

    return lista_de_categorias


def listar_por_categoria(dados, categoria):
    
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    # Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
     
    limpar_terminal()
    print('2. Listar produtos de uma categoria\n')


    if categoria == '' or categoria == None:
        print('ATENÇÃO!!!\nÉ necessário selecionar uma categoria. Volte ao menu principal e digite a opção 9')
        input(' \nPressione qualquer tecla para continuar >> ')
        return

    else:
        print(f'Categoria selecionada foi {categoria}')

    categoria_selecionada = categoria
    lista_produtos_categoria = []

    for ponteiro in range(len(dados)):
        testador_categoria = dados[ponteiro]['categoria']
        testador_produto = dados[ponteiro]['id']
        if categoria_selecionada == testador_categoria:
            lista_produtos_categoria.append(testador_produto)

    print(f'\nForam encontrados {len(lista_produtos_categoria)} produtos na categoria {categoria_selecionada}\n\nVeja a lista dos produtos\n')
    print(lista_produtos_categoria)
    
    input(' \nPressione qualquer tecla para continuar >> ')

    return lista_produtos_categoria


def produto_mais_caro(dados, categoria):
    
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    # Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    
    limpar_terminal()
    print('3. Produto mais caro por categoria')

    if categoria == '':
        print('ATENÇÃO!!!\nÉ necessário selecionar uma categoria. Volte ao menu principal e digite a opção 9')
        input(' \nPressione qualquer tecla para continuar >> ')
        return

    else:
        print(f'Categoria selecionada foi {categoria}')

    categoria_selecionada = categoria
    produto_mais_caro = float(dados[0]['preco'])
    dicionario_produto_mais_caro = {}

    for ponteiro in range(len(dados)):
        testador_categoria = dados[ponteiro]['categoria']

        if categoria_selecionada == testador_categoria:
                testador_valor = float(dados[ponteiro]['preco'])
                if produto_mais_caro < testador_valor:
                    produto_mais_caro = testador_valor
                    dicionario_produto_mais_caro = dados[ponteiro]
            
    print(f'\nO produto mais caro da categoria {categoria_selecionada} \nfoi o produto {dicionario_produto_mais_caro["id"]}\nno valor de {produto_mais_caro}')
    input(' \nPressione qualquer tecla para continuar >> ')

    return dicionario_produto_mais_caro


def produto_mais_barato(dados, categoria):
    
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    # Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    
    limpar_terminal()
    print('4. Produto mais barato por categoria')

    if categoria == '':
        print('ATENÇÃO!!!\nÉ necessário selecionar uma categoria. Volte ao menu principal e digite a opção 9')
        input(' \nPressione qualquer tecla para continuar >> ')
        return

    else:
        print(f'Categoria selecionada foi {categoria}')

    categoria_selecionada = categoria
    produto_mais_barato = float(dados[0]['preco'])
    dicionario_produto_mais_barato = {}

    for ponteiro in range(len(dados)):
        testador_categoria = dados[ponteiro]['categoria']

        if categoria_selecionada == testador_categoria:
                testador_valor = float(dados[ponteiro]['preco'])
                if produto_mais_barato > testador_valor:
                    produto_mais_barato = testador_valor
                    dicionario_produto_mais_barato = dados[ponteiro]
            
    print(f'\nO produto mais barato da categoria {categoria_selecionada} \nfoi o produto {dicionario_produto_mais_barato["id"]}\nno valor de {produto_mais_barato}')
    #print(dicionario_produto_mais_barato)
    input(' \nPressione qualquer tecla para continuar >> ')

    return dicionario_produto_mais_barato


def top_10_caros(dados):
    
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    
    limpar_terminal()
    print('5. Top 10 produtos mais caros\n')

    lista_dicionario_10_produtos_mais_caros = []
    dados_float = dados
    lista_temp_produtos = []

    for ponteiro in range(len(dados_float)):
        valor_float = float(dados_float[ponteiro]['preco'])
        dados_float[ponteiro].update({'preco_float':valor_float})
        grava_valor = valor_float
        lista_temp_produtos.append(grava_valor)

    lista_temp_produtos.sort(reverse=True)

    #pegar os 10 mais caros
    for ponteiro in range(10):
        procura_dados_completos = lista_temp_produtos[ponteiro]
        
        for p_interno in range(len(dados_float)):

            if procura_dados_completos == dados_float[p_interno]['preco_float']:
                print(f'{ponteiro+1}. O produto {dados_float[p_interno]["id"]} custa {dados_float[p_interno]["preco"]} da categoria {dados_float[p_interno]["categoria"]}')
                lista_dicionario_10_produtos_mais_caros.append(dados_float[p_interno])

    #print(lista_dicionario_10_produtos_mais_caros)
    input(' \nPressione qualquer tecla para continuar >> ')

    return lista_dicionario_10_produtos_mais_caros


def top_10_baratos(dados):
    
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    
    limpar_terminal()
    print('6. Top 10 produtos mais baratos\n')

    lista_dicionario_10_produtos_mais_baratos = []
    dados_float = dados
    lista_temp_produtos = []

    for ponteiro in range(len(dados_float)):
        valor_float = float(dados_float[ponteiro]['preco'])
        dados_float[ponteiro].update({'preco_float':valor_float})
        grava_valor = valor_float
        lista_temp_produtos.append(grava_valor)

    lista_temp_produtos.sort()

    for ponteiro in range(10):
        procura_dados_completos = lista_temp_produtos[ponteiro]

        for p_interno in range(len(dados_float)):

            if procura_dados_completos == dados_float[p_interno]['preco_float']:
                print(f'{ponteiro+1}. O produto {dados_float[p_interno]["id"]} custa {dados_float[p_interno]["preco"]} da categoria {dados_float[p_interno]["categoria"]}')
                lista_dicionario_10_produtos_mais_baratos.append(dados_float[p_interno])

    input(' \nPressione qualquer tecla para continuar >> ')

    return lista_dicionario_10_produtos_mais_baratos


def menu(dados):
     
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # Essa função deverá, em loop, realizar as seguintes ações:
    # - Exibir as seguintes opções:
    #     1. Listar categorias
    #     2. Listar produtos de uma categoria
    #     3. Produto mais caro por categoria
    #     4. Produto mais barato por categoria
    #     5. Top 10 produtos mais caros
    #     6. Top 10 produtos mais baratos
    #     0. Sair
    # - Ler a opção do usuário.
    # - No caso de opção inválida, imprima uma mensagem de erro.
    # - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    # - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    # - Imprimir o retorno salvo. 
    # O loop encerra quando a opção do usuário for 0.
    

    # Informar a categoria AQUI
    c = ''
    tc = []

    while True:
        limpar_terminal()

        print('MENU PRINCIPAL\n')
        print('Digite o número da opção desejada!\n')
        print('   1. Listar categorias\n   -> 9. Selecione a categoria desejada para utilizar as opções 2. 3. e 4.\n      2. Listar produtos de uma categoria\n      3. Produto mais caro por categoria\n      4. Produto mais barato por categoria\n   5. Top 10 produtos mais caros\n   6. Top 10 produtos mais baratos\n   0. Sair')

        opcao_digitada = int(input('>> '))

        if opcao_digitada == 1:
            tc = listar_categorias(d) #variavel recebe o retorno da lista de todas as categorias
        elif opcao_digitada == 2:
            listar_por_categoria(d,c)
        elif opcao_digitada == 3:
            produto_mais_caro(d,c)
        elif opcao_digitada == 4:
            produto_mais_barato(d,c)
        elif opcao_digitada == 5:
            top_10_caros(d)
        elif opcao_digitada == 6:
            top_10_baratos(d)
        elif opcao_digitada == 9:
            c = seleciona_categoria(tc) #variavel recebe o retorno da categoria selecionada pelo usuário
        elif opcao_digitada == 0:
            limpar_terminal()
            print('Obrigado por utilizar nosso sistema!\n\n Até a próxima!!! \n\n\n\n   dev_by wrbk.com.br\n           ¯\_(ツ)_/¯ \n\n')
            break
        else:
            limpar_terminal()
            print(f'{opcao_digitada} não é uma opção válida!!!')
            input(' \nPressione qualquer tecla para continuar >> ')

limpar_terminal()

# Programa Principal - não modificar!
d = obter_dados()
menu(d)
