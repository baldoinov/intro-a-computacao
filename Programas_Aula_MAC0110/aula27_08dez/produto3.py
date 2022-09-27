
# -*- coding: utf-8 -*-
'''
   Arquivo: produto3_matrizes_arquivo.py
   -------------------------------------

   Dada uma matriz inteira A  e uma matriz inteira B
   calcular o produto dessas matrizes.

   Os dados dessas matrizes são dados num arquivo 
   chamado dados1

   (Veja como estão os dados, para entender como deve 
   ser feita a leitura.)

   A resposta A x B deve ser gravada num arquivo - nome de sua escolha)

   Diferença em relacao aos outros programas vistos:
   Vai ter uma funcao adicional.

'''

def main():
    
    nomeArqEntrada = input("Digite o nome de um arquivo de entrada: ")  
    arqEntra = open(nomeArqEntrada, 'r')
    # open:  abre o arquivo nomeArqEntrada para leitura ("r = read"),
    #        retorna um objeto 'arquivo', que tem um método para ler o 
    #        conteúdo do arquivo. (Dá erro se o arquivo não existe.)

    nomeArqSaida = input("Digite o nome de um arquivo para saida: ")
    arqSai =  open(nomeArqSaida, 'w')
    # open:  Abre um arquivo para escrita, cria um  arquivo nomeArqSaida se ele não existe,
    #        

    ## Leitura do arquivo de entrada  dados1_produto.txt (veja como está este arquivo)
    #########################################################################################
    # Leitura dos dados da matriz A (na primeira linha: numero de linhas e de colunas
    ####### cada linha do arquivo deve ter os dados correspondentes a uma linha 
    
    A =  le_matriz_arquivo(arqEntra)
    
    nlin = len(A)
    ncol = len(A[0])
    
    arqSai.write("\nMatriz A tem  %d linhas e %d colunas\n\n" %(nlin, ncol))
    imprime_matriz_arquivo(A, arqSai)
            
   #########################

    # Leitura dos dados da matriz B (dados como no caso da matriz A)
    # OBS: Esses dados devem vir logo após os dados da matriz A (veja o arquivo dados1_produto.txt
    
    B =  le_matriz_arquivo(arqEntra) 
    
    arqEntra.close()  # para fechar o arquivo de entrada dados.txt

    nlin = len(B)
    ncol = len(B[0])
    
    arqSai.write("\nMatriz B tem  %d linhas e %d colunas\n\n" %(nlin, ncol))
    imprime_matriz_arquivo(B, arqSai)

    #####
    
    C = produto_matrizes(A, B)

    
    nlinC = len(C)
    ncolC = len(C[0])

    arqSai.write("\nMatriz C = A x B  tem  %d linhas e %d colunas\n\n" %(nlin, ncol))
    
    imprime_matriz_arquivo(C, arqSai)
    
    arqSai.close()   # para fechar o arquivo de saida saida.txt

#--------------------------------------------------
def le_matriz_arquivo(arqEntra):

    
    linha = arqEntra.readline()  
    lista = linha.split()        
    nlin = int(lista[0])         
    ncol = int(lista[1])         
   
    X = []
    for i in range(nlin):
        linha = arqEntra.readline()  
        lista = linha.split()       

        listaX = []
        for j in range(ncol):
            listaX.append(int(lista[j]))  # aqui cada string em lista[j] é transformada num inteiro e concatenada a listaA
        X.append(listaX)
        
    return X
#############################################

def imprime_matriz_arquivo(X, arqSai):   
        
    nlin = len(X)
    ncol = len(X[0])
    
    for i in range(nlin):
        arqSai.write("\t") 
        for j in range(ncol):
             arqSai.write("%4d   " %(X[i][j]))  ### Veja no arquivo saida.txt o que o formato %4d  produziu 
        arqSai.write("\n")
    

#-----------------------------------------------------
"""
def imprime_matriz(matriz):
    ''' (matriz) ->

    Recebe e imprime (na tela) uma matriz de inteiros.
    '''
    
    nlin = len(matriz)
    ncol = len(matriz[0])
    
    print("\nMatriz com %d linhas e %d colunas\n" %(nlin, ncol))
        
    for i in range(nlin):
        # imprimir os elementos da i-esima linha de matriz 
        for j in range(ncol):
            print("%6d" %(matriz[i][j]), end='')
        print()
    print()
"""
#---------------------------------------------------------------

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
     for i in range(lin_A):   
         for j in range(col_B):
             soma = 0
             for k in range(col_A):
                 soma += A[i][k] * B[k][j]
             C[i][j] = soma    #------ isto pode ser feito, pois C existe.
     return C

#-----------------------------------------
main()
