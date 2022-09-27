'''
   Arquivo: matriz_palavras_cruzadas
   ---------------------------------

   Um jogo de palavras cruzadas pode ser representado por uma
   matriz a com m linhas e n colunas, onde cada posição da matriz
   corresponde a um quadrado do jogo, sendo que 0 representa um 
   quadrado branco e -1 representa um quadrado preto.

   Indicar na matriz as posições que são inícios de palavras
   na horizontal ou na vertical (substituindo os zeros),
   considerando que uma palavra deve ter pelo menos duas letras.
   Para isso, numere consecutivamente tais posições.

   Exemplo: Para m=5, n=8 e a matriz dada a seguir,

             0  -1   0  -1  -1   0  -1   0
             0   0   0   0  -1   0   0   0
             0   0  -1  -1   0   0  -1   0
            -1   0   0   0   0  -1   0   0
             0   0  -1   0   0   0  -1  -1

    a saída deverá ser:

             1  -1   2  -1  -1   3  -1   4
             5   6   0   0  -1   7   0   0
             8   0  -1  -1   9   0  -1   0
            -1  10   0  11   0  -1  12   0
            13   0  -1  14   0   0  -1  -1
'''

def main():
    m = int(input("Digite o número de linhas da matriz: "))
    n = int(input("Digite o número de colunas da matriz: "))
    
    a = cria_matriz(m+2, n+2, -1)       # matriz com moldura

    # atualizando os valores da matriz
    for i in range(1, m+1):
        for j in range(1, n+1):
            a[i][j] = int(input(f"Insira o valor do elemento {i}x{j}: "))
    
    print("A matriz com moldura é: ")
    imprime_matriz(a)

    numera_matriz(a)

    print("A matriz numerada com moldura é: ")
    imprime_matriz(a)
    
    print("A matriz numerada sem moldura é: \n")
    
    for k in range(1, len(a)-1):
        for p in range(1, len(a[0])-1):
            print(f"{a[k][p]:6}", end="")
        print()
    print()
    

def cria_matriz(linhas, colunas, valor):
    '''
    (int, int, int) -> list
    '''
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz


def imprime_matriz(matriz):
    '''
    (list) -> NoneType
    '''
    m = len(matriz)
    n = len(matriz[0])
    print()

    for i in range(m):
        for j in range(n):
            print(f"{matriz[i][j]:6}", end="")
        print()
    print()


def numera_matriz(matriz):
    ''' (matriz) -> NoneType

    Recebe uma matriz e numera consecutivamente as posições que
    podem ser início de palavras na horizontal ou na vertical.
    Essas palavras devem ter comprimento pelo menos dois.
    Obs. A função supõe que a matriz têm apenas os inteiros 0 ou -1
    e que ela tem uma moldura com -1.
    '''

    m = len(matriz) - 2
    n = len(matriz[0]) - 2
    num = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matriz[i][j] == 0:
                if matriz[i][j-1] == -1 and matriz[i][j+1] == 0:
                    matriz[i][j] = num
                    num += 1
                elif matriz[i-1][j] == -1 and matriz[i+1][j] == 0:
                    matriz[i][j] = num
                    num += 1


main()
