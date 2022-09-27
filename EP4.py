# -*- coding: utf-8 -*-

"""
     Nome do aluno: Vitor Domingos Baldoino dos Santos
     Número USP: 11766857
     Curso: Ciências Econômicas
     Disciplina: MAC0110 Introdução à Computação
     Turma 47
     Exercício-Programa EP - 4

     DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
     TODAS AS PARTES ORIGINAIS DESTE EXERCÍCIO-PROGRAMA FORAM
     DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
     DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
     OU PLÁGIO.
     DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
     PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
     ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA
     SERÃO TRATADOS SEGUNDO OS CRITÉRIOS DIVULGADOS NA PÁGINA DA
     DISCIPLINA.
"""

def main():
    """ () -> NoneType
    ...
    """
    print("Esse programa recebe um labirinto, posições de origem e de\n"
          "destino de um arquivo, determina e imprime, se existir, \n"
          "um caminho de comprimento mínimo da origem para o destino.\n"
          "Caso não exista nenhum caminho, ele te informa através de \n"
          "uma mensagem correpondente.\n")
    
    pergunta = str(input("Você quer que a saída seja feita em um arquivo separado (y/n)? ")).lower().strip()
    print()

    labirinto, lin_origem, col_origem, lin_destino, col_destino = le_cria_labirinto()

    if pergunta == "y":
        arquivo = open(input("Digite o nome do arquivo de SAÍDA: "), 'w')
        imprime_arquivo(arquivo, labirinto, lin_origem, col_origem, lin_destino, col_destino)
        arquivo.close()
        print("\nTudo pronto! Agora é só olhar o arquivo de saída")
    elif pergunta == "n":
        imprime_tela(labirinto, lin_origem, col_origem, lin_destino, col_destino)
    else:
        print("Resposta inválida. Reinicie o programa.")
    

def le_cria_labirinto():
    """ () -> matriz, int, int, int int
    Esta função lê todos os dados de um arquivo cujo nome deve ser fornecido
    pelo usuário. Ela cria uma matriz (com moldura) com as informações lidas,
    e retorna essa matriz, os índices de linha e de coluna da posição da 
    origem e os índices de linha e de coluna da posição do destino.
    """
    # lendo o arquivo e as informações iniciais
    dados_in = open(input("Digite o nome do arquivo de ENTRADA: "), 'r')
    dimensoes = list(map(int, dados_in.readline().split()))
    origem = list(map(int, dados_in.readline().split()))
    destino = list(map(int, dados_in.readline().split()))

    nlin = dimensoes[0]
    ncol = dimensoes[1]

    # montando a matriz com moldura
    labirinto = []
    for i in range(nlin + 2):
        linha = [-1]*(ncol+2)
        labirinto.append(linha)

    # montando o labirinto com moldura
    for i in range(1, nlin + 1):
        prox_linha = list(map(int, dados_in.readline().split()))
        for j in range(1, ncol + 1):
            labirinto[i][j] = prox_linha[j-1]

    dados_in.close()

    return labirinto, origem[0], origem[1], destino[0], destino[1]
    

def marca_labirinto(matrizL, lin_destino, col_destino):
    """ (matriz, int, int) -> NoneType
    Recebe uma matriz de inteiros (com moldura) matrizL, representando um labirinto,
    e dois inteiros lin_destino e col_destino que são os índices de linha e de coluna
    da posição do destino nesse labirinto. Efetua a marcação da matrizL, conforme
    o algoritmo que foi descrito.
    """
    p = 0       # indice da fila de marcação
    m = 0       # controle do loop

    pares_linha_coluna = [(lin_destino, col_destino)]       # fila de marcação
    matrizL[lin_destino][col_destino] = 1
    
    fim = len(pares_linha_coluna) - 1   # tamanho da fila

    while m <= fim:
        inicio = pares_linha_coluna[p] # elemento da fila a ser analisado no momento
        i = inicio[0] # primeiro valor da tuple
        j = inicio[1] # segundo valor da tuple
        k = matrizL[i][j] + 1 # valor de k usando a referência do valor já marcado no labirinto
        if matrizL[i-1][j] == 0:
            matrizL[i-1][j] = k
            pares_linha_coluna.append((i-1, j))
        if matrizL[i+1][j] == 0:
            matrizL[i+1][j] = k
            pares_linha_coluna.append((i+1, j))
        if matrizL[i][j-1] == 0:
            matrizL[i][j-1] = k
            pares_linha_coluna.append((i, j-1))
        if matrizL[i][j+1] == 0:
            matrizL[i][j+1] = k
            pares_linha_coluna.append((i, j+1))
        p += 1
        m += 1
        fim = len(pares_linha_coluna) - 1


def determina_um_caminho(matrizL, lin_origem, col_origem):
    """ (matriz, int, int) -> matriz, list
    Recebe uma matriz de inteiros (com moldura) matrizL, representando um labirinto
    já marcado, e dois inteiros lin_origem e col_origem que são os índices de linha
    e de coluna da posição da origem nesse labirinto.
    A função cria uma matriz de caracteres (como mostrada no exemplo), diferenciando
    as posições livres das posições que representam paredes, e indicando nessa matriz
    as posições da origem, do destino e do caminho encontrado.
    Esta função cria também uma lista, onde cada elemento é um par representando
    os índices de linha e de coluna de uma posição do caminho encontrado.
    A função retorna a matriz e a lista criadas.
    """
    caminho = []
    for i in range(len(matrizL)):
        linha = []
        for j in range(len(matrizL[0])):
            if matrizL[i][j] < 0:
                linha.append(matrizL[i][j])
            else:
                linha.append(0)
        caminho.append(linha)

    posicoes = [(lin_origem, col_origem)] # lista das posições do caminho mínimo
    p = 0 # indice da lista posiçoes
    l = matrizL[lin_origem][col_origem] # controle do loop

    while l >= 1:
        prox = posicoes[p]  # próxima posição da lista a ser analisada
        i = prox[0] # linha
        j = prox[1] # coluna
        k = matrizL[i][j]
        if matrizL[i-1][j] == k - 1:
            posicoes.append((i-1, j))
            caminho[i-1][j] = " # "
        elif matrizL[i+1][j] == k-1:
            posicoes.append((i+1, j))
            caminho[i+1][j] = " # "
        elif matrizL[i][j-1] == k-1:
            posicoes.append((i, j-1))
            caminho[i][j-1] = " # "
        elif matrizL[i][j+1] == k-1:
            posicoes.append((i, j+1))
            caminho[i][j+1] = " # "
        p += 1
        l -= 1

    e = len(posicoes) - 1 # ultima posição registrada
    caminho[lin_origem][col_origem] = " O "
    caminho[posicoes[e][0]][posicoes[e][1]] = " D "

    return caminho, posicoes


def imprime_tela(labirinto, lin_origem, col_origem, lin_destino, col_destino):
    """ (list, int, int, int, int) -> NoneType
    Essa função faz a saída do EP na tela do computador.
    """
    # impressão do labirinto antes da marcação
    print("\nO labirinto dado é: ")
    imprime_labirinto_numericamente(labirinto)

    marca_labirinto(labirinto, lin_destino, col_destino)

    # impressão do labirinto depois da marcação
    print("Após a marcação númerica o labirinto é: ")
    imprime_labirinto_numericamente(labirinto)

    destino = labirinto[lin_destino][col_destino]
    origem = labirinto[lin_origem][col_origem]

    if destino and origem > 0: # teste para ver se há um caminho mínimo
        print("O caminho mínimo do destino a origem é: ")
        caminho, posicoes = determina_um_caminho(labirinto, lin_origem, col_origem)
        imprime_labirinto_simbolicamente(caminho)
        print("Os indices do caminho mínimo são: ")
        imprime_caminho(posicoes)
    else:
        print("\nNão há caminho mínimo que leve da origem ao destino.\n")


def imprime_arquivo(output, labirinto, lin_origem, col_origem, lin_destino, col_destino):
    """ (file, list, int, int, int, int) -> NoneType
    Essa função faz a saída do EP em um arquivo fornecido pelo usuário.
    """
    # impressão do labirinto antes da marcação
    output.write("\nO labirinto dado é: \n")
    imprime_numericamente_arquivo(labirinto, output)

    marca_labirinto(labirinto, lin_destino, col_destino)

    # impressão do labirinto depois da marcação
    output.write("Após a marcação númerica o labirinto é: \n")
    imprime_numericamente_arquivo(labirinto, output)

    destino = labirinto[lin_destino][col_destino]
    origem = labirinto[lin_origem][col_origem]

    if destino and origem > 0: # teste para ver se há um caminho mínimo
        output.write("O caminho mínimo do destino a origem é: \n")
        caminho, posicoes = determina_um_caminho(labirinto, lin_origem, col_origem)
        imprime_simbolicamente_arquivo(caminho, output)
        output.write("Os indices do caminho mínimo são: ")
        imprime_caminho_arquivo(posicoes, output)
    else:
        output.write("\nNão há caminho mínimo que leve da origem ao destino.\n")


def imprime_labirinto_numericamente(matrizL):
    """ (matriz) -> NoneType
    Recebe uma matriz de inteiros (com moldura) matrizL, representando
    um labirinto (antes ou depois da marcação).
    Imprime o labirinto (sem a moldura), no formato de matriz e ajustada
    nas colunas (exibindo também os índices das linhas e das colunas).
    """
    nlin = len(matrizL)
    ncol = len(matrizL[0])

    underline = "\033[4m"
    underline_end = "\033[m"
    
    print("\n", "   ", end="", sep="")

    for i in range(1, ncol - 1):
        print(f"{underline}{i:4}{underline_end}", end="")

    print()

    for i in range(1, nlin-1):
        print(f"{i:3}|", end="")
        for j in range(1, ncol-1):
            print(f"{underline}{matrizL[i][j]:^3}{underline_end}", end="|")
        print()
    print("\n")


def imprime_numericamente_arquivo(matrizL, arquivo):
    """ (matriz, file) -> NoneType
    Realiza a mesma tarefa da função impreme_labirinto_numericamente(),
    só que com a saída em um arquivo fornecido pelo usuário.
    """
    nlin = len(matrizL)
    ncol = len(matrizL[0])
    
    arquivo.write("\n   ")

    for i in range(1, ncol - 1):
        arquivo.write(f"{i:4}")

    arquivo.write("\n")

    for i in range(1, nlin-1):
        arquivo.write(f"{i:3}|")
        for j in range(1, ncol-1):
            arquivo.write(f"{matrizL[i][j]:^3}|")
        arquivo.write("\n")
    arquivo.write("\n\n")


def imprime_labirinto_simbolicamente(matrizC):
    """ (matriz) -> NoneType
    Recebe uma matriz de caracteres (com moldura) matrizC, representando
    um labirinto já com um caminho de comprimento mínimo.
    Imprime o labirinto (sem a moldura), no formato de matriz e ajustada
    nas colunas (exibindo também os índices das linhas e das colunas).
    """

    nlin = len(matrizC)
    ncol = len(matrizC[0])

    underline = "\033[4m"
    underline_end = "\033[m"
    
    print("\n", "   ", end="", sep="")

    for i in range(1, ncol - 1):
        print(f"{underline}{i:4}{underline_end}", end="")

    print()

    for i in range(1, nlin-1):
        print(f"{i:3}|", end="")
        for j in range(1, ncol-1):
            print(f"{underline}{matrizC[i][j]:^3}{underline_end}", end="|")
        print()
    print("\n")


def imprime_simbolicamente_arquivo(matrizC, arquivo):
    """ (matriz, file) -> NoneType
    Realiza a mesma tarefa da função impreme_labirinto_simbolicamente(),
    só que com a saída em um arquivo dado pelo usuário.
    """

    nlin = len(matrizC)
    ncol = len(matrizC[0])
    
    arquivo.write("\n   ")

    for i in range(1, ncol - 1):
        arquivo.write(f"{i:4}")

    arquivo.write("\n")

    for i in range(1, nlin-1):
        arquivo.write(f"{i:3}|")
        for j in range(1, ncol-1):
            arquivo.write(f"{matrizC[i][j]:^3}|")
        arquivo.write("\n")
    arquivo.write("\n\n")
    

def imprime_caminho(lin_col_caminho):
    """ (list) -> NoneType
    Recebe uma lista lin_col_caminho, onde cada elemento é um par representando
    os índices de linha e de coluna de uma posição do caminho encontrado.
    Imprime os índices das posições do caminho encontrado (conforme o exemplo dado).
    """
    i = 0
    p = 0
    print("\n")
    while i < len(lin_col_caminho):
        while p < 10 and i < len(lin_col_caminho):
            print(f"{lin_col_caminho[i]!s:10}", end="")
            i += 1
            p += 1
        print("\n")
        p = 0


def imprime_caminho_arquivo(lin_col_caminho, arquivo):
    """ (list, file) -> NoneType
    Realiza a mesma tarefa da função imprime_caminho(),
    só que com a saída em um arquivo dado pelo usuário.
    """
    i = 0
    p = 0
    arquivo.write("\n\n")
    while i < len(lin_col_caminho):
        while p < 10 and i < len(lin_col_caminho):
            arquivo.write(f"{lin_col_caminho[i]!s:10}")
            i += 1
            p += 1
        arquivo.write("\n\n")
        p = 0

main()
