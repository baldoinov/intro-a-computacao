'''
   Construa uma matriz inteira com m linhas e n colunas,
   inicializando-a com zeros. 
   Altere alguma posição dessa matriz e verifique.
    
   Usa funções:  
   cria_matriz e imprime_matriz.    
'''
#--------------------------------------------------------------------

def main():
    
    m = int(input("Digite o número de linhas da matriz: "))
    n = int(input("Digite o número de colunas da matriz: "))

    # criar a 'estrutura' para uma matriz (m x n), com zeros
    matrizA = cria_matriz(m, n, 0)

    # imprimir matrizA como lista de listas
    print("\n\nLista com os elementos da matriz lida:\n", matrizA)
    print()
                              
    imprime_matriz(matrizA)    # imprime os elementos de matrizA (no formato de matriz)
   
    # alterar posição linha 0, coluna n-1 da matrizA:
    matrizA[0][n-1] = -m

    print("\nPosição [0][%d] da matriz foi atualizada com %d."  %(n-1, -m))   

    # imprimir matrizA (como lista de listas) após a alteração 
    print("\nLista com os elementos da matriz após a alteração:\n",  matrizA)


    imprime_matriz(matrizA)  # imprime a matrizA após a alteração (no formato de matriz)

#--------------------------------------------------------------------

def cria_matriz(nlin, ncol, valor):
    ''' (int, int, tipo do valor) -> matriz (ou seja, tipo list) 

    Cria uma matriz com nlin linhas e ncol colunas,
    sendo que cada elemento é igual a valor.
    Retorna a matriz criada.
    '''
 
    # criar uma lista para uma linha da matriz,
    # com todas as posições inicializadas com valor
    linha = []
    for j in range(0, ncol, 1):
        linha.append(valor)
    # as três linhas acima poderiam ser substituídas por 
    #     linha = [valor] * ncol        
    print("\nlista linha =", linha)   
          
    matriz = []
    print("\nmatriz =", matriz)
    for i in range(0, nlin, 1):       
        # inserir a lista linha no final da lista matriz      
        matriz.append(linha)
        print("matriz =", matriz)
   
    return matriz

#--------------------------------------------------------------------

def imprime_matriz(matriz):
    ''' (matriz) -> NoneType

    Recebe uma matriz de inteiros e imprime-a no formato 
    bidimensional de matriz.
    '''

    nlin = len(matriz)
    ncol = len(matriz[0])
    
    print("\nMatriz com %d linhas e %d colunas\n" %(nlin, ncol))
        
    for i in range(0, nlin, 1):
        # imprimir os elementos da i-ésima linha de matriz 
        for j in range(0, ncol, 1):
            print("%6d" %(matriz[i][j]), end='')
        print()
    print()

#--------------------------------------------------------------------
main()

