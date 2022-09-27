# -*- coding: utf-8 -*-

'''
   Arquivo: produto_matrizesA.py  (Solucao em que cria antes uma matriz C com zeros)
   
   Dadas duas matrizes inteiras A(mxn) e B(pxq),
   determinar o produto de A por B.
   Ler o valores m, n, os dados da matriz A linha a linha;
   ler os valores p, q, e os dados da matriz B linha a linha.
   
   OBS: Só é possível fazer o produto se n = p.
        Se n!=p, dar uma mensagem de erro.
	
'''


def main():
    print("Leitura da matriz A:")
    dimensaoA = list(map(int, input("Digite o numero de linhas seguido do no. de colunas da matriz A: ").split()))
    m = dimensaoA[0]
    n = dimensaoA[1] 

    print("m = ", m, "n = ", n)
    
    A = le_constroi_matriz(m,n)

    
    ################################

    print("Leitura da matriz B:")
    
    dimensaoB= list(map(int, input("Digite o numero de linhas seguido do no. de colunas da matriz B: ").split()))
    p = dimensaoB[0]
    q = dimensaoB[1] 

    B = le_constroi_matriz(p,q)

    
    print("Matriz A dada:")   
    imprime_matriz(A)

    print("Matriz B dada:")   
    imprime_matriz(B)
    
    C = produto_matrizes(A,B)
    print ("Matriz C= AxB:")
    
    imprime_matriz(C)    
#-----------------------
    
def produto_matrizes(A, B):
   lin_A = len(A)
   col_A = len(A[0])  # lin_A = numero de linhas da matriz A    col_A = numero de colunas da matriz A
   lin_B = len(B)
   col_B = len(B[0])  # lin_B = numero de linhas da matriz B    col_B = numero de colunas da matriz B

   if col_A != lin_B:
      print("Não é possível fazer o produto! No. de colunas de A é diferente do no. de linhas de B!")
   else:
       
     # Construcao da matrix C = A x B que tem dimensao lin_A x col_B
     # Inicializacao da matriz C com zeros
       
     C = []
     for linha in range(lin_A):
        lista = []
        for coluna in range (col_B):
             lista.append(0)
        C.append(lista)
     #------------------ Término da construção da matriz C cujas entradas são todas iguais a zero.
                                                                          
     for i in range(lin_A):                             #                |-------------------------     ----- (coluna j de B) ---
         for j in range(col_B):                         #                |                         |   |       
             soma = 0                                   #                |                         |   |         B[0][j]
             for k in range(col_A):                     # (linha i de A)=| A[i][0] A[i][1] A[i][2] |   |         B[1][j]
                 soma += A[i][k] * B[k][j]              #                |      *       *       *  |   |         B[2][j]
             C[i][j] = soma    #-- OK,  pois C existe.  #                |                         |   |
     return C                                           #
                                                        #               -----------------       ---------          ---------
#-----------------------------------------              #              |  1   1   1    1 |     |  4    5  |        \      |
                                                        #              |  2   2   2    2 |  .  |  4    5  |    =   |      |
def le_constroi_matriz(nlin, ncol):                     #              |  3   3   3    3 |     |  4    5  |        |      |
     """    (int, int) --> matriz                       #              | ----------------      |  4    5  |        --------
     """                                                #                                      ----------
                                                        #                   A (3x4)               B (4x2)            C (3x2)
     matriz = []
     print("De as entradas da matriz, cada linha por vez: ")
     
     for i in range(nlin):
          print("De as entradas da linha", i, "da matriz")
          linha  = list(map(int, input().split()))
          matriz.append(linha) 
     
     return matriz
 
#--------------------------------------------

def imprime_matriz(A):
     """   (matriz) --> 
     """
     nlin =  len(A)  # numero de linhas da matriz A
     ncol =  len(A[0])  # numero de colunas da matriz A

     for i in range(nlin):
        for j in range(ncol):
            print ("%5d" %(A[i][j]), end=' ') 
        print()  
     print()
#-------------------------------------------
main()

                                  
                                  
                                    
                                  
                                  
                              
                              
                

   
