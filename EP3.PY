# -*- coding: utf-8 -*-

"""
     Nome do aluno: Vitor Domingos Baldoino dos Santos
     Número USP: 11766857
     Curso: Ciências Econômicas
     Disciplina: MAC0110 Introdução à Computação
     Turma 47
     Exercício-Programa EP - 3

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
    ''' ( ) -> NoneType
    ...
    '''

    print("="*75, "\n", sep="")
    resolverProblema1()
    print("\n", "="*75, "\n", sep="")
    resolverProblema2()
    print("\n", "="*75, "\n", sep="")
    resolverProblema3()
    print("\n", "="*75, "\n", sep="")


def resolverProblema1():
    ''' ( ) -> NoneType
    ...
    '''
    print("PROBLEMA 1\n")
    print("Determinar todos os números primos menores ou iguais a n.\n")

    n = int(input("Digite um inteiro >= 2 para n: "))
    print("\n")

    lista_erasto = criaListaCrivoEratostenes(n)
    lista_primos = criaListaPrimos(lista_erasto)
    print("Existem %d números primos menores ou iguais a %d. São eles:\n" %(len(lista_primos), n))
    imprimeNumerosInteirosLista(lista_primos)


def resolverProblema2():
    ''' ( ) -> NoneType
    ...
    '''
    print("PROBLEMA 2\n")
    print("Determinar dois números primos r e s tais que 2 <= r < s <= n,\n"
          "o valor de s−r é máximo e não existem números primos entre r e s.\n")

    n = int(input("Digite um inteiro > 2 para n: "))
    print()

    r, s = maiorIntervaloSemPrimos(n)
    print("Uma sequência consecutiva mais longa de inteiros menores do que %d,\n"
          "sem nenhum número primo, é formada por %d inteiros que estão entre\n" 
          "o par de números primos %d e %d." %(n, (s-r)-1, r, s))


def resolverProblema3():
    ''' ( ) -> NoneType
    ...
    '''
    print("PROBLEMA 3\n")
    print("Testar a Conjetura de Goldbach para todo inteiro par menor do que k.\n")

    k = int(input("Digite um inteiro > 4 para k: "))
    valores_n = [0,0]
    lista_gold, conjectura = testaConjecturaGoldbach(k)
    for j in range(4, k, 2):
        valores_n.append(j)

    print("\nPara todo n par tal que 2 < n < %d, os pares p e q tais que n = p + q são:\n" %k)
    for i in range(2, len(lista_gold)):
        print("%6d  =%5d  +%5d" %(valores_n[i], lista_gold[i], valores_n[i] - lista_gold[i]))


def criaListaCrivoEratostenes(n):
    ''' (int) -> list
    Recebe um inteiro n >= 2 e cria uma lista crivo[0...n] com zeros e uns
    tal que para cada i, 0 <= i <= n, crivo[i] é 1 se i é primo e crivo[i] é 0
    se i não é primo.
    A lista crivo é criada implementando o algoritmo do Crivo de Eratóstenes.
    Esta função retorna a lista crivo.
    '''

    a = [1] * (n + 1)
    a[0] = a[1] = 0
    raizn = int(n**(1/2))

    for i in range (2, raizn + 1):
        if a[i] == 1:
            for j in range(2, (n//i + 1)):
                a[i * j] = 0
    return a


def criaListaPrimos(crivo):
    ''' (list) -> list
    Recebe uma lista crivo que foi criada utilizando o algoritmo do Crivo de
    Eratostenes. A partir da lista crivo, esta funcao cria e retorna uma lista
    chamada primos, contendo todos os numeros primos, em ordem crescente.
    '''
    n = len(crivo)
    a = []
    for i in range(n):
        if crivo[i] == 1:
            a.append(i)
    return a


def imprimeNumerosInteirosLista(a):
    ''' (list) -> NoneType
    Recebe uma lista a de numeros inteiros e imprime todos os numeros da lista,
    escrevendo no maximo dez numeros em cada linha e de modo que fiquem
    ajustados nas colunas.
    '''
    i = 0
    p = 0
    while i < len(a):
        while p < 10 and i < len(a):
            print("%5d" %a[i], end="")
            i += 1
            p += 1
        print("\n")
        p = 0
    

def maiorIntervaloSemPrimos(n):
    '''(int) -> int, int
    Recebe um inteiro n > 2 e determina um par de numeros primos r e s
    tais que 2 <= r < s <= n, o valor s-r é maximo e para todo i tal que
    r < i < s, tem-se que i nao é primo (ou seja, entre r e s nao há nenhum
    primo).
    Esta funcao retorna os primos r e s.
    '''
    p_erasto = criaListaCrivoEratostenes(n)
    primos = criaListaPrimos(p_erasto)
    i_max = 0   # intervalo máximo sem números primos

    for i in range(len(primos) - 1):
        if primos[i + 1] - primos[i] >= i_max:
            i_max = primos[i + 1] - primos[i]
            r = primos[i]
            s = primos[i+1]
    return r, s


def testaConjecturaGoldbach(k):
    '''(int) -> list, bool
    Recebe um inteiro k > 2 e verifica se a Conjectura de Goldbach é verdadeira
    para todo inteiro n par, 2 < n < k.

    Para isto, para cada tal inteiro n, esta funcao tenta encontrar dois
    numeros primos p e q tais que n = p + q. Se existir mais do que um tal par,
    escolha o par com o menor p (e tal que p <= q).

    Para dar um certificado da validade da conjectura para os numeros pares n
    entre 2 e k, o programa constroi uma lista chamada lista pares_primos que
    tem a seguinte propriedade:

    Como n é par, n >= 4, entao n = 2 * i, onde i >= 2.
    Para cada i, i >= 2, pares_primos[i] armazena o primo p tal que n = p + q,
    onde p <= q e q = n - p é primo. Apenas o valor de p é armazenado já
    que o valor de q é precisamente n - p.

    A funcao testaConjecturaGoldbach retorna a lista pares_primos e retorna
    tambem True ou False dependendo se a conjectura for valida ou nao para
    todo n par, 2 < n < k.
    '''
    valores_n = []
    pares_primos = [0, 0]
    lista_erasto = criaListaCrivoEratostenes(k)
    lista_primos = criaListaPrimos(lista_erasto)
    deu_certo = False
    is_true = 0
    
    for i in range(4, k, 2):
        valores_n.append(i)

    # A lógica utilizada para montar o próximo trecho foi a seguinte:
    # 1) Seleciono um N dentro de valores_n.
    # 2) Começo testando a condição (N == P + Q) para P e Q dentro de lista_primos.
    # 3) Caso a condição não seja atendida, prossigo para o próximo Q da lista, indo até o final da lista.
    # 4) Caso teste todos os Q possíveis e a condição não seja atendida, passo para o próximo P 
    # e repito o teste dos Q's.
    # 5) Repito o processo para todos os N's possíveis.
    
    for n in valores_n:
        deu_certo = False
        for p in lista_primos:
            for q in lista_primos:
                if n == p + q:
                    pares_primos.append(p)
                    is_true += 1
                    deu_certo = True
                    break
            if deu_certo:
                break

    if is_true == len(valores_n):
        return pares_primos, True
    else:
        return pares_primos, False
            
                
main()
