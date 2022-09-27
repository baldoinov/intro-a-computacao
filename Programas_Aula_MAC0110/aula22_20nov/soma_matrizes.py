'''
   Arquivo: soma_matrizes.py
   Dada uma matriz A (nxm) e uma matriz B (nxm), ambos com núemros inteiros,
   calcular e imprimir a matriz C = A+B.
   Inicialmente, ler os valores de n e m, depois ler as entradas de A e depois as de B.
   Fazer uso de funcoes para leitura de matriz, impressao de matriz, e para calcular a soma.
'''

def main():
    n = int(input("Digite o numero de linhas da matriz: "))
    m = int(input("Digite o numero de colunas da matriz: "))

    print("Digite as entradas da matriz A (por ordem de linha, um por vez): ") 
    A = le_matriz(n,m)
        
    print("Digite as entradas da matriz B (por ordem de linha, um por vez): ") 
    B = le_matriz(n,m)

    C = soma_matrizes(A,B)
 
    print("\n Matriz A:")
    imprime_matriz(A)

    print("\n Matriz B:")
    imprime_matriz(B)
    
    print("\n Matriz C = A + B") 
    imprime_matriz(C)
    
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

def soma_matrizes(a,b):
    '''
     (matriz, matriz) --> matriz
     Recebe duas matrizes (de inteiros), calcula a soma dessas matrizes, e retorna a matriz obtida
    '''   
     
    nlin = len(a)   # len(a) é o numero de linhas da matriz a
    ncol = len(a[0]) # len(a[0]) é o comprimento da linha a[0] da matriz a, ou seja, o numero de colunas de a
    
    c = [ ]
    for i in range(nlin):
        linha = [] 
        for j in range(ncol):
            elemento = a[i][j] + b[i][j]
            linha.append(elemento)
        c.append(linha) # equivalente a   c += [linha]  (testar!)
    return c
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
            print ("%5d" %(c[i][j]), end=' ') ## formato para numeros de poucos digitos; mudar, se necessario.
        print()           
# -------------------------------
main()        
        
 

    
