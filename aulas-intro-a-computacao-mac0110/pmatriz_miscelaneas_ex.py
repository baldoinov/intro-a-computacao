'''
   Arquivo: matriz_varias_operacoes.py

   Dada uma matriz A (nxm), 
   calcular e imprimir a transposta de A.
   Testar se A é simetrica (verificando se A é igual à sua transposta). 

   Como imprimir as linhas de uma matriz sem se referir aos seus índices.
  
   Tem função para impressao de matriz (no formato de matriz)

'''
import numpy as np 

def main():
    print("Esse programa faz a transposta de uma matriz e verifica se ela é simétrica.\n")

    A = cria_matriz()
    print("A matriz dada foi: ")
    imprime_matriz(A)

    B = matriz_transposta(A)
    print("A matriz transposta é: ")
    imprime_matriz(B)

    if A == B:
        print("A matriz dada é simétrica")
    else:
        print("A matriz dada não é simétrica")


def cria_matriz():
    '''
    (NoneType) -> list
    '''
    i = int(input("Insira o número de linhas da matriz: "))
    j = int(input("Insira o número de colunas da matriz: "))
    print()

    matriz = []
    for m in range(1, i + 1):
        linha = []
        for n in range(1, j + 1):
            num = int(input(f"Qual o valor {m}x{n} da matriz: "))
            linha.append(num)
        matriz.append(linha)
    return matriz

def imprime_matriz(matriz):
    '''
    (list) -> NoneType
    '''
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"{matriz[i][j]:3}", end=" ")
        print()
    print()


def matriz_transposta(matriz):
    '''
    (list) -> list    
    '''

    i = len(matriz)
    j = len(matriz[0])
    matriz_t = []

    for n in range(j):
        linha = []
        for m in range(i):
            linha.append(matriz[m][n])
        matriz_t.append(linha)
    return matriz_t

    # OU
    # matriz_t = [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]

def simetrica(matriz):
    '''
    (list) -> bool
    '''
    m = len(matriz)
    n = len(matriz[0])
    
    if m != n:
        return False

    i = 1
    while i < m:
        j = 0
        while j < i:
            if matriz[i][j] != matriz[j][i]:
                return False
            else:
                j += 1
        i += 1    
    return True
            

main()
