
'''
  arquivo:  cria_matriz.py 
   
  Construir uma matriz inteira com m linhas e n colunas,
  cujas entradas são dadas linha a linha (em cada linha na ordem das colunas).

  Ler m, n  e os valores da matriz.

  Imprimir a matriz construída.

'''


def main():

    m = int(input("Digite o numero de linhas da matriz:"))
    n = int(input("Digite o numero de colunas da matriz:"))
                   
    
    b = cria_matriz(m, n)

    print(b)

    print("\n\nMatriz com %d linhas e %d colunas:\n" %(m, n))
    for i in range(m):
        # imprimir os elementos da i-ésima linha da matriz
        for j in range(n):
            print("%6d" %(b[i][j]), end='')
        print()
    print()
    
# --------------

def cria_matriz(nlin, ncol):
    '''(int, int) --> matriz listas de listas
       Cria e retorna uma matriz com nlin linhas e ncol colunas,
       com os valores dados pelo usuário.
    '''
    matriz = []  # lista vazia
    for i in range(nlin):
        # cria a linha i
        linha = [] # cria lista vazia chamada linha
        for j in range(ncol):
            num = int(input("Digite um inteiro para a posição"
                            " [%d][%d]: " %(i, j)))
            linha.append(num)
        # adiciona a linha à matriz
        matriz.append(linha)

    return matriz          
#-------------
main()
