# -*- coding: utf-8 -*-
'''
   Arquivo: matriz_varias_operacoes.py

   Dada uma matriz A (nxm), 
   calcular e imprimir a transposta de A.
   Testar se A é simetrica (verificando se A é igual à sua transposta). 

   Como imprimir as linhas de uma matriz sem se referir aos seus índices.
  
   Tem função para impressao de matriz (no formato de matriz)

  
'''
import numpy as np   #<============= Veja 
import numpy         #<============ Veja 

def main():
  
    A = [[1, 2, 3, 4], [2, 5, 6, 7], [3, 6, 8, 9], [4, 7, 9, 0]]
    
     
    print("\n Matriz dada A:")
    imprime_matriz(A) 

    # Como se referir à uma linha da matriz A:
    
    print("1a.linha da matriz A:")
    print(A[0])

    print("2a.linha da matriz A:")
    print(A[1])

    if(A[0] == A[1]):
        print("A primeira e a segunda linha de A são iguais.")
    else:
        print("A primeira e a segunda linha de A são distintas.")

        
    print("\nOutra forma de imprimir A, sem usar índices:")
    for linha in A:   ## nao precisa chamar de linha!!! veja abaixo
        print(linha) 
        
    print("------")
    for i in A:
        print(i)

    #--------------------------------

    # Como obter a transposta de uma matriz A.

    B = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
         
    # len(B) = 4
    # len(B[0])= 3
         
    B_transp = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))] # veja o significado dessa forma condensada de tomar os elementos de B 

    # Para o exemplo, equivale a:
    # 
    # B_transp = [[B[j][i] for j in range(4)] for i in range(3))]
    # B_transp = [ [B[0][0], B[1][0], B[2][0], B[3][0]],  [B[0][1], B[1][1], B[2][1], B[3][1]],    [B[0][2], B[1][2], B[2][2], b[3][2]] ]
    #              -----------------------------------    ------------------------------------     -----------------------------------
    #                    j=0,1,2,3   e  i = 0                       j=0,1,2,3   e i = 1                     j = 0,1,2,3  e  i = 2
    #
    # B_transp = [[1, 4, 7, 10],[2, 5, 8, 11], [ 3, 6, 9, 12]]
         
         
    print("\nMatriz B_transp:") 
    imprime_matriz(B_transp)

    print("\nOutra forma:")
            
    for linha in B_transp:
        print(linha)

    print("-----------------")
    print("Usando numpy")
   
    matrixB = np.array(B)
    print(matrixB)

    print("Transposta:") 
    print(matrixB.T)

    print()
    print("Outra matriz C=:")

    C = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
    matrixC = np.array(C)
    print(matrixC)

    print("Transposta:") 
    print(matrixC.T)

    
    if Testa_simetrica(matrixC):
        print("A matriz C dada é simetrica")
    else:
        print("A matriz C dada  não é simetrica")

 
    print("---------")

    print("Outra matriz")
    
    matrixB=[[0, 1, 8], [1, 3, 4], [2, 4, 5]]
            
    print("matrixB=", matrixB) 
    print()
    Transp_matrixB = numpy.transpose(matrixB)

    print("Transposta da matrixB =\n", Transp_matrixB)
    
    # print(numpy.transpose(matrix))

    if Testa_simetrica(matrixB):
        print("matrixB é simetrica")
    else:
        print("matrixB não é simetrica")

#-------------------------

def le_matriz(nlin,ncol):
    '''(int, int) --> matriz listas de listas
       Cria e retorna uma matriz (de inteiros) com nlin linhas e ncol colunas. 
       Para criar, ler as entradas de uma matriz (de inteiros) de dimensao nlin x ncol,
       fornecidas linha a linha, um elemento por vez.     
    '''

    matriz = [] # lista vazia
    for i in range(nlin):
        # cria a linha i
        linha = [] # cria lista vazia chamada linha
        print ("Digite os numeros da %da. linha:" %(i)) 
        for j in range(ncol):
            elemento = int(input( )) # se preferir:  int(input("Digite um inteiro para a"
                                     #                 "posicao [%d][%d]: " %(i, j)))
            linha.append(elemento)
        # adiciona a lista linha em matriz 
        matriz.append(linha)
        
    print()

    return matriz          
#-----------------------------

def Testa_simetrica(a):
    '''
     (matri) --> bool
     Recebe uma matriz a e retorna True se a é simétrica; cc, retorna False.
    '''   
  
    Transp_a = numpy.transpose(a)

    comparison = (a == Transp_a)

    tudo_true = comparison.all()


    if tudo_true:
      return True
    else:
        return False
                      
#--------------------------------
          
def imprime_matriz(c):
    '''
     (matriz) --> Nonetype
     Recebe e imprime uma matriz de inteiros.
    ''' 
    nlin = len(c)
    ncol = len(c[0])

    for i in range(nlin):
        for j in range(ncol):
            print ("%5d" %(c[i][j]), end=' ') ## formato para números de poucos dígitos; mudar, se necessario.
        print()           
# -------------------------------
main()        
        
 
'''
sage

'''
