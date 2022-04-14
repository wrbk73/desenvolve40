# Você irá receber uma lista bi-dimensional com altura e largura não necessáriamente iguais contendo apenas 0's e 1's. 
# Cada 1 representa um pedaço de rio, enquanto os 0's representam terra. 
# Rios são compostos por 1's adjacentes horizontalmente ou verticalmente (mas não diagonalmente). 
# O número de 1's adjacentes representa o tamanho do rio.
# Note que o rio pode fazer curvas, isto é, rios podem ter formato de L ou até mesmo de cruz e são considerados um rio só.
# Crie um algoritmo que receba esta lista bi-dimensional e retorne uma lista com os tamanhos dos rios dentro dessa estrutura, 
# os tamanhos de rios dentro da lista resposta não precisam ter uma ordem específica.

# **Saída esperada:**
# [1, 2, 2, 2, 5] 
# # Note que os números poderiam estar em qualquer ordem dentro da lista
# [1,  ,  , 1,  ]
# [1,  , 1,  ,  ]
# [ ,  , 1,  , 1]
# [1,  , 1,  , 1]
# [1,  , 1, 1,  ]

import os
os.system('clear') or None


def contaRio(posicao_linha, posicao_coluna, lista_rio, visitado, tamanho_do_rio):
    tamanho_atual_do_rio = 0
    conexoes = [[posicao_linha, posicao_coluna]]

    while len(conexoes):
        conexao_atual = conexoes.pop()
        posicao_linha = conexao_atual[0]
        posicao_coluna = conexao_atual[1]

        if visitado[posicao_linha][posicao_coluna]:
            continue

        visitado[posicao_linha][posicao_coluna] = True

        if lista_rio[posicao_linha][posicao_coluna] == 0:
            continue

        tamanho_atual_do_rio += 1
        naovisitados = naoVisitados(posicao_linha, posicao_coluna, lista_rio, visitado)

        for vizinhos in naovisitados:
            conexoes.append(vizinhos)

    if tamanho_atual_do_rio > 0:
        tamanho_do_rio.append(tamanho_atual_do_rio)


def naoVisitados(posicao_linha,posicao_coluna,lista_rio,visitados):
    nao_visitados = []

    if posicao_linha > 0 and not visitados[posicao_linha - 1][posicao_coluna]:
        nao_visitados.append([posicao_linha - 1, posicao_coluna])

    if posicao_linha < len(lista_rio) - 1 and not visitados[posicao_linha + 1][posicao_coluna]:
        nao_visitados.append([posicao_linha + 1, posicao_coluna])

    if posicao_coluna > 0 and not visitados[posicao_linha][posicao_coluna - 1]:
        nao_visitados.append([posicao_linha, posicao_coluna - 1])

    if posicao_coluna < len(lista_rio[0]) - 1 and not visitados[posicao_linha][posicao_coluna + 1]:
        nao_visitados.append([posicao_linha, posicao_coluna + 1])

    return nao_visitados


def encontreRios(lista_rio):    
    visitados = [[False for idx in linha] for linha in lista_rio] 
    rios_encontrados = []
    
    for posicao_da_linha in range(len(lista_rio)):
        linha = lista_rio[posicao_da_linha]

        for posicao_da_coluna in range(len(lista_rio[posicao_da_linha])):

            if linha[posicao_da_coluna] == 1: 
                contaRio(posicao_da_linha,posicao_da_coluna,lista_rio,visitados,rios_encontrados)

    rios_encontrados.sort()

    return rios_encontrados


matriz = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

print(encontreRios(matriz))
