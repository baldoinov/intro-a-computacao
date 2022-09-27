'''
   Dada uma matriz inteira com n linhas e n colunas,
   verificar se ela é simétrica. 
   Exemplo: a matriz a seguir é simétrica.
   
   Matriz com 4 linhas e 4 colunas

     1     2     3     4
     2     0     5     8
     3     5     6     7
     4     8     7     0
 
   Esta matriz será representada como uma lista de listas:
   [ [1, 2, 3, 4], [2, 0, 5, 8], [3, 5, 6, 7], [4, 8, 7, 0] ]
   
'''
#--------------------------------------------------------------------

def main():
    n = int(input("Digite o no. de linhas (= colunas) da matriz: "))

    # ler e criar a lista matrizA (n x n)
    matrizA = []
    print("matrizA = %s\n" %matrizA)   # teste
     
    for i in range(0, n, 1):
        # ler e criar uma lista para a i-ésima linha da matriz
        linha = [] 
        print("linha %d = %s" %(i, linha))  # teste
        for j in range(0, n, 1):
            num = int(input("Digite um inteiro para a posição"
                            " [%d][%d]: " %(i, j)))
            linha.append(num)
            print("linha %d = %s" %(i, linha)) # teste
            
        # inserir a lista linha no final da lista matrizA
        matrizA.append(linha)
        print("\nmatrizA = %s\n" %matrizA)   # teste
  
    # imprimir a lista matrizA
    print("\n\nLista com os elementos da matriz lida:\n", matrizA)
       
    # imprimir os elementos de matrizA no formato bidimensional de matriz
    print("\n\nMatriz com %d linhas e %d colunas:\n" %(n, n))
    for i in range(0, n, 1):
        # imprimir os elementos da i-ésima linha da matriz
        for j in range(0, n, 1):
            print("%6d" %(matrizA[i][j]), end='')
        print()
    print()
    
    # verificar se a matriz matrizA é simétrica
    simetrica = True
    i = 1
    while i < n and simetrica:
        j = 0
        while j < i and simetrica:
            if matrizA[i][j] != matrizA[j][i]:
                simetrica = False
            else:
                j += 1
        i +=1

    if simetrica:
        print("A matriz dada é simétrica.")
    else:
        print("A matriz dada não é simétrica.")

#---------------------------------------------------------------------
main()
